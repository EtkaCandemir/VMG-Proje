import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load the scored dataset
    df = pd.read_csv('supplier_risk_scored.csv')
    
    # 1. Calculate quantile thresholds
    quantiles_equal = df['Risk_Score_Equal'].quantile([0.33, 0.66])
    quantiles_priority = df['Risk_Score_Priority'].quantile([0.33, 0.66])
    
    print("--- 1. Quantile Threshold Values ---")
    print(f"Risk_Score_Equal thresholds: 33% = {quantiles_equal[0.33]:.4f}, 66% = {quantiles_equal[0.66]:.4f}")
    print(f"Risk_Score_Priority thresholds: 33% = {quantiles_priority[0.33]:.4f}, 66% = {quantiles_priority[0.66]:.4f}")
    print("\n")
    
    # Save thresholds to CSV
    thresholds_df = pd.DataFrame({
        'Scoring_Method': ['Risk_Score_Equal', 'Risk_Score_Priority'],
        'Low_Medium_Threshold': [quantiles_equal[0.33], quantiles_priority[0.33]],
        'Medium_High_Threshold': [quantiles_equal[0.66], quantiles_priority[0.66]]
    })
    thresholds_df.to_csv('quantile_thresholds.csv', index=False)
    print("--- Saved 'quantile_thresholds.csv' ---\n")

    # 2. Assign quantile-based classes
    def classify_quantile(score, q33, q66):
        if score <= q33:
            return 'Low Risk'
        elif score <= q66:
            return 'Medium Risk'
        else:
            return 'High Risk'
            
    df['Risk_Class_Equal_Quantile'] = df['Risk_Score_Equal'].apply(
        lambda x: classify_quantile(x, quantiles_equal[0.33], quantiles_equal[0.66])
    )
    df['Risk_Class_Priority_Quantile'] = df['Risk_Score_Priority'].apply(
        lambda x: classify_quantile(x, quantiles_priority[0.33], quantiles_priority[0.66])
    )
    
    # Set categorical order
    risk_order = ['Low Risk', 'Medium Risk', 'High Risk']
    df['Risk_Class_Equal_Quantile'] = pd.Categorical(df['Risk_Class_Equal_Quantile'], categories=risk_order, ordered=True)
    df['Risk_Class_Priority_Quantile'] = pd.Categorical(df['Risk_Class_Priority_Quantile'], categories=risk_order, ordered=True)
    
    # Also ensure old ones are ordered
    df['Risk_Class_Equal'] = pd.Categorical(df['Risk_Class_Equal'], categories=risk_order, ordered=True)
    df['Risk_Class_Priority'] = pd.Categorical(df['Risk_Class_Priority'], categories=risk_order, ordered=True)
    
    # 2. Class distributions
    print("--- 2. Class Distributions ---")
    print("Equal-weighted (Fixed vs Quantile):")
    print("Fixed:")
    print(df['Risk_Class_Equal'].value_counts().sort_index())
    print("\nQuantile:")
    print(df['Risk_Class_Equal_Quantile'].value_counts().sort_index())
    
    print("\nPriority-weighted (Fixed vs Quantile):")
    print("Fixed:")
    print(df['Risk_Class_Priority'].value_counts().sort_index())
    print("\nQuantile:")
    print(df['Risk_Class_Priority_Quantile'].value_counts().sort_index())
    print("\n")
    
    # 3. Bar charts comparing both thresholding approaches
    plt.figure(figsize=(14, 10))
    sns.set_theme(style="whitegrid")
    
    palette = ['#1a9850', '#fee08b', '#d73027']
    
    plt.subplot(2, 2, 1)
    sns.countplot(data=df, x='Risk_Class_Equal', palette=palette, order=risk_order, legend=False, hue='Risk_Class_Equal')
    plt.title('Equal-Weighted (Fixed Threshold)')
    plt.xlabel('')
    plt.ylabel('Count')
    
    plt.subplot(2, 2, 2)
    sns.countplot(data=df, x='Risk_Class_Equal_Quantile', palette=palette, order=risk_order, legend=False, hue='Risk_Class_Equal_Quantile')
    plt.title('Equal-Weighted (Quantile Threshold)')
    plt.xlabel('')
    plt.ylabel('Count')
    
    plt.subplot(2, 2, 3)
    sns.countplot(data=df, x='Risk_Class_Priority', palette=palette, order=risk_order, legend=False, hue='Risk_Class_Priority')
    plt.title('Priority-Weighted (Fixed Threshold)')
    plt.xlabel('Risk Class')
    plt.ylabel('Count')
    
    plt.subplot(2, 2, 4)
    sns.countplot(data=df, x='Risk_Class_Priority_Quantile', palette=palette, order=risk_order, legend=False, hue='Risk_Class_Priority_Quantile')
    plt.title('Priority-Weighted (Quantile Threshold)')
    plt.xlabel('Risk Class')
    plt.ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('threshold_comparison.png')
    print("--- 3. Saved 'threshold_comparison.png' ---")
    plt.close()
    
    # 4. Cross-tabulation between fixed-threshold and quantile-threshold classes
    print("\n--- 4. Cross-tabulation (Fixed vs Quantile) ---")
    print("\nEqual-Weighted:")
    print(pd.crosstab(df['Risk_Class_Equal'], df['Risk_Class_Equal_Quantile'], rownames=['Fixed'], colnames=['Quantile']))
    
    print("\nPriority-Weighted:")
    print(pd.crosstab(df['Risk_Class_Priority'], df['Risk_Class_Priority_Quantile'], rownames=['Fixed'], colnames=['Quantile']))
    print("\n")
    
    # 5. Save the updated dataset
    output_file = 'supplier_risk_scored_quantile.csv'
    df.to_csv(output_file, index=False)
    print(f"--- 5. Saved updated dataset to '{output_file}' ---")

if __name__ == "__main__":
    main()
