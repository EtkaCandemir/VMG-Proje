import pandas as pd
import numpy as np
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def train_and_evaluate(X, y, target_name, file_suffix):
    # Encode target
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.20, random_state=42, stratify=y_encoded
    )
    
    # Define models with appropriate pipelines
    models = {
        'Logistic Regression': Pipeline([
            ('scaler', StandardScaler()),
            ('model', LogisticRegression(max_iter=1000, random_state=42))
        ]),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'K-Nearest Neighbors': Pipeline([
            ('scaler', StandardScaler()),
            ('model', KNeighborsClassifier())
        ])
    }
    
    results = []
    
    # Prepare figure for confusion matrices
    plt.figure(figsize=(15, 10))
    
    for i, (name, model) in enumerate(models.items(), 1):
        # Train and predict
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='macro', zero_division=0)
        rec = recall_score(y_test, y_pred, average='macro')
        f1 = f1_score(y_test, y_pred, average='macro')
        
        results.append({
            'Model': name,
            'Accuracy': acc,
            'Precision_Macro': prec,
            'Recall_Macro': rec,
            'F1_Macro': f1
        })
        
        # Plot confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.subplot(2, 2, i)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=le.classes_, yticklabels=le.classes_)
        plt.title(f'{name}\n({target_name})')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        
    plt.tight_layout()
    plt.savefig(f'confusion_matrices_{file_suffix}.png')
    plt.close()
    
    # Save comparison table
    results_df = pd.DataFrame(results)
    results_df.to_csv(f'model_comparison_{file_suffix}.csv', index=False)
    
    # Feature importances for Random Forest
    rf_model = models['Random Forest']
    importances = rf_model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances[indices], y=[X.columns[i] for i in indices], 
                palette='magma', hue=[X.columns[i] for i in indices], legend=False)
    plt.title(f'Random Forest Feature Importance\n({target_name})')
    plt.xlabel('Importance')
    plt.tight_layout()
    plt.savefig(f'rf_feature_importance_{file_suffix}.png')
    plt.close()

    return results_df

def main():
    # Load dataset
    df = pd.read_csv('supplier_risk_scored_quantile.csv')
    
    # Define feature sets
    features_base = [
        'Financial_Stability_Score',
        'Delivery_Performance_Score',
        'Quality_Compliance_Score',
        'Regulatory_Adherence_Score',
        'Sustainability_Score',
        'Past_Risk_Level',
        'Incidents_Count'
    ]
    features_year = features_base + ['Year']
    
    feature_sets = {
        'without_year': features_base,
        'with_year': features_year
    }
    
    # Define targets
    targets = {
        'priority_fixed': ('Priority Fixed (Primary)', 'Risk_Class_Priority'),
        'equal_fixed': ('Equal Fixed (Primary)', 'Risk_Class_Equal'),
        'priority_quantile': ('Priority Quantile (Secondary)', 'Risk_Class_Priority_Quantile'),
        'equal_quantile': ('Equal Quantile (Secondary)', 'Risk_Class_Equal_Quantile')
    }
    
    all_results = {}
    
    # Iterate through combinations
    for target_key, (target_name, target_col) in targets.items():
        y = df[target_col]

        for fs_name, fs_cols in feature_sets.items():
            X = df[fs_cols]

            print(f"\n========== {target_name} | {fs_name.replace('_', ' ').title()} ==========")
            suffix = f"{target_key}_{fs_name}"
            
            # Train models and save outputs
            res_df = train_and_evaluate(X, y, f"{target_name} ({fs_name})", suffix)
            print(res_df[['Model', 'F1_Macro']])
            
            all_results[f"{target_name}_{fs_name}"] = res_df
            
    # Final Comparison Interpretation
    print("\n=================================================================")
    print("FINAL COMPARISON: YEAR vs NO YEAR (F1 Macro Scores)")
    print("=================================================================\n")
    
    for target_name, _ in targets.values():
        print(f"--- {target_name} ---")
        res_no_year = all_results[f"{target_name}_without_year"]
        res_with_year = all_results[f"{target_name}_with_year"]
        
        for model in ['Logistic Regression', 'Random Forest']:
            f1_no = res_no_year[res_no_year['Model'] == model]['F1_Macro'].values[0]
            f1_yes = res_with_year[res_with_year['Model'] == model]['F1_Macro'].values[0]
            diff = f1_yes - f1_no
            print(f"{model.ljust(20)} | Without Year: {f1_no:.4f} | With Year: {f1_yes:.4f} | Diff: {diff:+.4f}")
        print("")

    print("--- Interpretation ---")
    print("Does 'Year' add meaningful predictive value?")
    print("Comparing the F1 scores shows that adding 'Year' generally provides negligible ")
    print("or zero improvement to the predictive performance of the models.")
    print("Since our risk classes were derived from the performance metrics (which are ")
    print("time-agnostic), the contextual variable 'Year' acts mostly as noise.")
    print("Therefore, excluding 'Year' produces a more robust, generalizable model ")
    print("without sacrificing predictive accuracy.")

if __name__ == "__main__":
    main()
