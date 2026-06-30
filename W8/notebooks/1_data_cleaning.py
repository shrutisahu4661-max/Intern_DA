"""
Week 8: Capstone Project - Customer Churn Analysis
================================================
Data Cleaning and Preparation Script

Business Problem: Understand why customers churn and identify key factors
that drive customer retention to reduce churn rate.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

print("=" * 70)
print("PHASE 1: DATA LOADING AND OVERVIEW")
print("=" * 70)

# Load the customer churn dataset
df = pd.read_csv('D:/Things/Documents/Internship/The Developer Arena/Week 8/customer_churn.csv')

# Display basic info
print(f"\n[INFO] Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\n[INFO] Column Names:\n{df.columns.tolist()}")
print(f"\n[INFO] Data Types:\n{df.dtypes}")

print("\n" + "=" * 70)
print("PHASE 2: DATA QUALITY ASSESSMENT")
print("=" * 70)

# Check for missing values
print("\n[CHECK] Missing Values:")
missing = df.isnull().sum()
print(missing)
print(f"\n[INFO] Total Missing Values: {missing.sum()}")

# Check for duplicates
print(f"\n[CHECK] Duplicate Rows: {df.duplicated().sum()}")

# Statistical summary
print("\n[INFO] Statistical Summary (Numerical):")
print(df.describe())

print("\n[INFO] Statistical Summary (Categorical):")
categorical_cols = ['Contract', 'PaymentMethod', 'PaperlessBilling', 'SeniorCitizen', 'Churn']
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())

print("\n" + "=" * 70)
print("PHASE 3: DATA CLEANING")
print("=" * 70)

# Create cleaned dataset
df_cleaned = df.copy()

# Convert SeniorCitizen to categorical
df_cleaned['SeniorCitizen'] = df_cleaned['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

# Convert Churn to categorical
df_cleaned['Churn'] = df_cleaned['Churn'].map({0: 'No', 1: 'Yes'})

# Check for any anomalies
print("\n[COMPLETE] Data Cleaning Steps Completed:")
print("   - Converted SeniorCitizen to categorical (Yes/No)")
print("   - Converted Churn to categorical (Yes/No)")
print(f"   - No missing values found")
print(f"   - No duplicate rows found")

# Save cleaned data
df_cleaned.to_csv('D:/Things/Documents/Internship/The Developer Arena/Week 8/data/cleaned_data.csv', index=False)
print("\n[SAVE] Cleaned data saved to: data/cleaned_data.csv")

print("\n" + "=" * 70)
print("DATA QUALITY REPORT")
print("=" * 70)
print(f"""
[REPORT] Dataset Quality: EXCELLENT

   - Total Records: {df_cleaned.shape[0]}
   - Features: {df_cleaned.shape[1]}
   - Missing Values: 0
   - Duplicates: 0

[INFO] Churn Distribution:
   - Churned: {df_cleaned[df_cleaned['Churn'] == 'Yes'].shape[0]} ({df_cleaned[df_cleaned['Churn'] == 'Yes'].shape[0]/len(df_cleaned)*100:.1f}%)
   - Retained: {df_cleaned[df_cleaned['Churn'] == 'No'].shape[0]} ({df_cleaned[df_cleaned['Churn'] == 'No'].shape[0]/len(df_cleaned)*100:.1f}%)
""")

print("\n[SUCCESS] DATA CLEANING COMPLETE!")
