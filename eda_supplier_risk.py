import pandas as pd
# pyrefly: ignore [missing-import]
import numpy as np
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Loading the dataset
    # Reads the CSV file from the current directory.
    file_path = 'supplier_risk.csv'
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path}\n")
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}. Please make sure the file is in the same directory.")
        return

    # 2. Showing dataset shape
    # Prints the number of rows and columns.
    print("--- 2. Dataset Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

    # 3. Showing column names and data types
    # df.info() provides a concise summary including names, non-null counts, and data types.
    print("--- 3. Column Names and Data Types ---")
    print(df.info())
    print("\n")

    # 4. Checking missing values
    # Sums the null values for each column and displays only those with missing data.
    print("--- 4. Missing Values ---")
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print(missing_values[missing_values > 0])
    else:
        print("No missing values found.")
    print("\n")

    # 5. Checking duplicate rows
    # Counts the total number of exact duplicate rows.
    print("--- 5. Duplicate Rows ---")
    duplicate_count = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicate_count}\n")

    # 6. Showing descriptive statistics
    # Provides mean, std, min, max, and quartiles for numerical columns.
    print("--- 6. Descriptive Statistics ---")
    print(df.describe())
    print("\n")

    # 7. Showing the distribution of Risk_Category
    # Counts the occurrences of each category in the Risk_Category column.
    print("--- 7. Distribution of Risk_Category ---")
    if 'Risk_Category' in df.columns:
        print(df['Risk_Category'].value_counts())
    else:
        print("'Risk_Category' column not found.")
    print("\n")

    # 8. Showing the distribution of Year
    # Counts the number of records for each year and sorts them chronologically.
    print("--- 8. Distribution of Year ---")
    if 'Year' in df.columns:
        print(df['Year'].value_counts().sort_index())
    else:
        print("'Year' column not found.")
    print("\n")

    # 9. Showing the number of unique suppliers
    # Uses nunique() on the Supplier_ID column to find distinct supplier count.
    print("--- 9. Number of Unique Suppliers ---")
    if 'Supplier_ID' in df.columns:
        print(f"Number of unique suppliers (Supplier_ID): {df['Supplier_ID'].nunique()}")
    else:
        print("'Supplier_ID' column not found.")
    print("\n")

    # 10. Comparing numerical variables by Risk_Category using group means
    # Groups by Risk_Category and calculates the mean for all numerical columns.
    print("--- 10. Group Means of Numerical Variables by Risk_Category ---")
    if 'Risk_Category' in df.columns:
        # Select only numerical columns to avoid errors when calculating means
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_cols:
            group_means = df.groupby('Risk_Category')[numeric_cols].mean()
            print(group_means)
        else:
            print("No numerical columns found for grouping.")
    else:
        print("'Risk_Category' column not found.")
    print("\n")

    # 11. Creating correlation matrix for numerical variables
    # Computes pairwise correlation of numerical columns using Pearson standard correlation coefficient.
    print("--- 11. Correlation Matrix ---")
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        print(corr_matrix)
    else:
        print("No numerical variables to compute correlation.")
        corr_matrix = None
    print("\n")

    # 12. Visualizing
    print("--- 12. Generating Visualizations ---")
    sns.set_theme(style="whitegrid") # Set a clean visual theme
    
    # 12a. Risk_Category distribution
    if 'Risk_Category' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.countplot(
            data=df, 
            x='Risk_Category', 
            order=df['Risk_Category'].value_counts().index, 
            hue='Risk_Category', 
            palette='viridis', 
            legend=False
        )
        plt.title('Distribution of Risk_Category')
        plt.xlabel('Risk Category')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('risk_category_distribution.png')
        print("Görsel kaydedildi: risk_category_distribution.png")
        plt.close()

    # 12b. Year distribution
    if 'Year' in df.columns:
        plt.figure(figsize=(8, 5))
        # discrete=True ensures bins align with integer years
        sns.histplot(data=df, x='Year', discrete=True, color='skyblue')
        plt.title('Distribution of Year')
        plt.xlabel('Year')
        plt.ylabel('Frequency')
        # Ensure only integer years are shown on the x-axis
        plt.xticks(sorted(df['Year'].unique()))
        plt.tight_layout()
        plt.savefig('year_distribution.png')
        print("Görsel kaydedildi: year_distribution.png")
        plt.close()

    # 12c. Boxplots of key numerical variables by Risk_Category
    if 'Risk_Category' in df.columns and not numeric_df.empty:
        # Select a few key numerical variables for boxplots (excluding IDs and Year)
        potential_key_vars = [
            'Financial_Stability_Score', 
            'Delivery_Performance_Score', 
            'Quality_Compliance_Score', 
            'MCDM_Score'
        ]
        key_vars = [var for var in potential_key_vars if var in df.columns]
        
        # Fallback if specific expected variables are not in the dataset
        if not key_vars:
            key_vars = [col for col in numeric_df.columns if col not in ['Supplier_ID', 'Year']][:4]

        # Generate a boxplot for each key variable
        for var in key_vars:
            plt.figure(figsize=(8, 5))
            sns.boxplot(
                data=df, 
                x='Risk_Category', 
                y=var, 
                hue='Risk_Category', 
                palette='Set2', 
                legend=False
            )
            plt.title(f'Boxplot of {var} by Risk_Category')
            plt.xlabel('Risk Category')
            plt.ylabel(var)
            plt.tight_layout()
            plt.savefig(f'boxplot_{var}.png')
            print(f"Görsel kaydedildi: boxplot_{var}.png")
            plt.close()

    # 12d. Correlation heatmap
    if not numeric_df.empty:
        plt.figure(figsize=(12, 10))
        # Exclude IDs like 'Supplier_ID' from the correlation heatmap as they aren't meaningful features
        corr_cols = [col for col in numeric_df.columns if col != 'Supplier_ID']
        corr_matrix_viz = df[corr_cols].corr()
        
        # Draw the heatmap with annotations
        sns.heatmap(
            corr_matrix_viz, 
            annot=True, 
            cmap='coolwarm', 
            fmt=".2f", 
            linewidths=0.5
        )
        plt.title('Correlation Heatmap of Numerical Variables')
        plt.tight_layout()
        plt.savefig('correlation_heatmap.png')
        print("Görsel kaydedildi: correlation_heatmap.png")
        plt.close()

if __name__ == "__main__":
    main()
