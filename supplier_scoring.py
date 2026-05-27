import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def main():
    # 1. Load the dataset
    df = pd.read_csv('supplier_risk.csv')
    
    # Define variables to be used
    vars_to_invert = [
        'Financial_Stability_Score',
        'Delivery_Performance_Score',
        'Quality_Compliance_Score',
        'Regulatory_Adherence_Score',
        'Sustainability_Score'
    ]
    vars_direct = [
        'Past_Risk_Level',
        'Incidents_Count'
    ]
    all_vars = vars_to_invert + vars_direct
    
    # 2. Normalize all selected variables to 0-1 range using MinMaxScaler
    scaler = MinMaxScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df[all_vars]), columns=all_vars)
    
    # 3. Convert to risk components
    # For performance scores (higher is better), invert them to make them risk components
    for col in vars_to_invert:
        df_normalized[col] = 1.0 - df_normalized[col]
        
    # vars_direct are already such that higher means higher risk, so we use them directly
    
    # 4. Create Equal-weighted risk score
    # Average of all seven risk components
    df['Risk_Score_Equal'] = df_normalized.mean(axis=1)
    
    # 5. Create Priority-weighted risk score
    df['Risk_Score_Priority'] = (
        0.27 * df_normalized['Financial_Stability_Score'] +
        0.21 * df_normalized['Delivery_Performance_Score'] +
        0.13 * df_normalized['Quality_Compliance_Score'] +
        0.08 * df_normalized['Regulatory_Adherence_Score'] +
        0.11 * df_normalized['Sustainability_Score'] +
        0.10 * df_normalized['Past_Risk_Level'] +
        0.10 * df_normalized['Incidents_Count']
    )
    
    # 6. Classify scores
    def classify_risk(score):
        if score <= 0.33:
            return 'Low Risk'
        elif score <= 0.66:
            return 'Medium Risk'
        else:
            return 'High Risk'
            
    df['Risk_Class_Equal'] = df['Risk_Score_Equal'].apply(classify_risk)
    df['Risk_Class_Priority'] = df['Risk_Score_Priority'].apply(classify_risk)
    
    # Set categorical order for meaningful plots and crosstabs
    risk_order = ['Low Risk', 'Medium Risk', 'High Risk']
    df['Risk_Class_Equal'] = pd.Categorical(df['Risk_Class_Equal'], categories=risk_order, ordered=True)
    df['Risk_Class_Priority'] = pd.Categorical(df['Risk_Class_Priority'], categories=risk_order, ordered=True)
    
    # --- Generate Outputs ---
    
    # 1. Descriptive statistics of both risk scores
    print("--- 1. Descriptive Statistics of Risk Scores ---")
    print(df[['Risk_Score_Equal', 'Risk_Score_Priority']].describe())
    print("\n")
    
    # 2. Class distributions for both methods
    print("--- 2. Class Distributions ---")
    print("Equal-weighted:")
    print(df['Risk_Class_Equal'].value_counts().sort_index())
    print("\nPriority-weighted:")
    print(df['Risk_Class_Priority'].value_counts().sort_index())
    print("\n")
    
    # 3. Bar charts comparing Low / Medium / High distributions
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.countplot(data=df, x='Risk_Class_Equal', palette=['#1a9850', '#fee08b', '#d73027'], order=risk_order, legend=False, hue='Risk_Class_Equal')
    plt.title('Equal-Weighted Risk Classes')
    plt.xlabel('Risk Class')
    plt.ylabel('Count')
    
    plt.subplot(1, 2, 2)
    sns.countplot(data=df, x='Risk_Class_Priority', palette=['#1a9850', '#fee08b', '#d73027'], order=risk_order, legend=False, hue='Risk_Class_Priority')
    plt.title('Priority-Weighted Risk Classes')
    plt.xlabel('Risk Class')
    plt.ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('risk_class_comparison.png')
    print("--- 3. Saved 'risk_class_comparison.png' ---")
    plt.close()
    
    # 4. Cross-tabulation between Risk_Class_Equal and Risk_Class_Priority
    print("\n--- 4. Cross-tabulation (Equal vs Priority) ---")
    crosstab = pd.crosstab(df['Risk_Class_Equal'], df['Risk_Class_Priority'], rownames=['Equal Weight'], colnames=['Priority Weight'])
    print(crosstab)
    print("\n")
    
    # 6. Save the new dataset
    output_file = 'supplier_risk_scored.csv'
    df.to_csv(output_file, index=False)
    print(f"--- 6. Saved new dataset to '{output_file}' ---")

if __name__ == "__main__":
    main()
