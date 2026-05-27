import pandas as pd
import numpy as np
# pyrefly: ignore [missing-import]
from statsmodels.stats.outliers_influence import variance_inflation_factor
# pyrefly: ignore [missing-import]
from statsmodels.tools.tools import add_constant
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def main():
    # Load dataset
    df = pd.read_csv('supplier_risk_scored_quantile.csv')
    
    # Define features
    features = [
        'Financial_Stability_Score',
        'Delivery_Performance_Score',
        'Quality_Compliance_Score',
        'Regulatory_Adherence_Score',
        'Sustainability_Score',
        'Past_Risk_Level',
        'Incidents_Count'
    ]
    X = df[features]
    
    # --- 1. Calculate VIF (Variance Inflation Factor) ---
    print("========== VIF Analysis ==========")
    X_vif = add_constant(X)
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X_vif.columns
    vif_data["VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]
    vif_data = vif_data[vif_data["Feature"] != "const"].reset_index(drop=True)
    
    print(vif_data.to_string(index=False))
    vif_data.to_csv("vif_results.csv", index=False)
    
    # --- 2. Calculate R2 Score ---
    print("\n========== R2 Score Analysis ==========")
    # For Equal Weighted Score
    y_equal = df['Risk_Score_Equal']
    lr_equal = LinearRegression()
    lr_equal.fit(X, y_equal)
    y_pred_equal = lr_equal.predict(X)
    r2_equal = r2_score(y_equal, y_pred_equal)
    
    # For Priority Weighted Score
    y_priority = df['Risk_Score_Priority']
    lr_priority = LinearRegression()
    lr_priority.fit(X, y_priority)
    y_pred_priority = lr_priority.predict(X)
    r2_priority = r2_score(y_priority, y_pred_priority)
    
    print(f"R2 Score for predicting Risk_Score_Equal: {r2_equal:.4f}")
    print(f"R2 Score for predicting Risk_Score_Priority: {r2_priority:.4f}")
    
    with open("r2_results.txt", "w") as f:
        f.write(f"R2 Score for predicting Risk_Score_Equal: {r2_equal:.4f}\n")
        f.write(f"R2 Score for predicting Risk_Score_Priority: {r2_priority:.4f}\n")

if __name__ == "__main__":
    main()
