"""
Run this script to regenerate the screenshots in the screenshots/ folder
without launching Jupyter. Equivalent to running the notebook cells.

Usage:
    python generate_screenshots.py
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

SCREEN_DIR = 'screenshots'
os.makedirs(SCREEN_DIR, exist_ok=True)
sns.set_style('whitegrid')

df = pd.read_csv('customer_churn.csv')

# 1. Churn distribution
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
df['Churn'].value_counts().plot(kind='bar', ax=axes[0], color=['steelblue', 'salmon'])
axes[0].set_title('Churn Count')
df['Churn'].value_counts(normalize=True).plot(kind='pie', ax=axes[1],
                                              autopct='%1.1f%%',
                                              colors=['steelblue', 'salmon'])
axes[1].set_title('Churn %')
plt.tight_layout()
plt.savefig(f'{SCREEN_DIR}/day1_churn_dist.png', dpi=120)
plt.close()

# 2. Numeric distributions
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, ['Tenure', 'MonthlyCharges', 'TotalCharges']):
    sns.histplot(df[col], kde=True, ax=ax, color='teal')
plt.tight_layout()
plt.savefig(f'{SCREEN_DIR}/day1_numeric_dist.png', dpi=120)
plt.close()

# 3. Boxplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, ['Tenure', 'MonthlyCharges', 'TotalCharges']):
    sns.boxplot(x=df[col], ax=ax, color='lightblue')
plt.tight_layout()
plt.savefig(f'{SCREEN_DIR}/day4_boxplots.png', dpi=120)
plt.close()

# 4. Correlation
df_feat = df.copy().drop(columns=['CustomerID'])
contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
df_feat['Contract_LE'] = df_feat['Contract'].map(contract_map)
df_feat = pd.get_dummies(df_feat, columns=['PaymentMethod'], prefix='Payment')
df_feat['PaperlessBilling'] = df_feat['PaperlessBilling'].map({'Yes': 1, 'No': 0})
df_feat = df_feat.drop(columns=['Contract'])

df_feat['AvgMonthlySpend'] = df_feat['TotalCharges'] / (df_feat['Tenure'] + 1)
df_feat['CustomerLifetimeValue'] = df_feat['Tenure'] * df_feat['MonthlyCharges']
df_feat['PaymentEfficiency'] = df_feat['MonthlyCharges'] / (df_feat['TotalCharges'] + 1)
df_feat['TenureGroup'] = pd.cut(df_feat['Tenure'], bins=[-1, 12, 24, 48, 100],
                                labels=[0, 1, 2, 3]).astype(int)
df_feat['IsHighValue'] = (df_feat['MonthlyCharges'] > df_feat['MonthlyCharges'].median()).astype(int)
df_feat['ChargesPerTenureYear'] = (df_feat['MonthlyCharges'] * 12) / (df_feat['Tenure'] + 1)
df_feat['ContractRisk'] = (2 - df_feat['Contract_LE']).clip(0, 2)

plt.figure(figsize=(12, 8))
sns.heatmap(df_feat.corr(numeric_only=True), annot=True, fmt='.2f',
            cmap='coolwarm', center=0)
plt.title('Pearson Correlation Matrix')
plt.tight_layout()
plt.savefig(f'{SCREEN_DIR}/day6_corr_matrix.png', dpi=120)
plt.close()

# 5. Churn by engineered feature
fig, axes = plt.subplots(1, 3, figsize=(16, 4))
sns.barplot(x='TenureGroup', y='Churn', data=df_feat, ax=axes[0], palette='viridis')
sns.barplot(x='IsHighValue', y='Churn', data=df_feat, ax=axes[1], palette='magma')
sns.barplot(x='ContractRisk', y='Churn', data=df_feat, ax=axes[2], palette='coolwarm')
plt.tight_layout()
plt.savefig(f'{SCREEN_DIR}/day5_engineered_churn.png', dpi=120)
plt.close()

print(f'Generated screenshots in {SCREEN_DIR}/')
print(os.listdir(SCREEN_DIR))
