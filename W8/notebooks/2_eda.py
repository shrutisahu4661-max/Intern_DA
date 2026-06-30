"""
Week 8: Capstone Project - Customer Churn Analysis
================================================
Exploratory Data Analysis (EDA)

This script performs comprehensive EDA with visualizations to understand
the patterns and relationships in customer churn data.
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

# Output directory
OUTPUT_DIR = 'D:/Things/Documents/Internship/The Developer Arena/Week 8/'

print("=" * 70)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 70)

# Load cleaned data
df = pd.read_csv(OUTPUT_DIR + 'data/cleaned_data.csv')

# Convert numeric columns for analysis
df['Churn_numeric'] = df['Churn'].map({'No': 0, 'Yes': 1})
df['SeniorCitizen_numeric'] = df['SeniorCitizen'].map({'No': 0, 'Yes': 1})

# ============================================================
# VISUALIZATION 1: Churn Distribution
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pie chart
churn_counts = df['Churn'].value_counts()
colors = ['#2ecc71', '#e74c3c']
axes[0].pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%',
            colors=colors, explode=(0, 0.1), shadow=True, startangle=90)
axes[0].set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')

# Bar chart
churn_counts.plot(kind='bar', ax=axes[1], color=colors, edgecolor='black')
axes[1].set_title('Churn Count by Status', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Churn Status')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=0)
for i, v in enumerate(churn_counts):
    axes[1].text(i, v + 5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/1_churn_distribution.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 1: Churn Distribution saved")

# ============================================================
# VISUALIZATION 2: Churn by Contract Type
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stacked bar chart
contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
contract_churn.plot(kind='bar', stacked=True, ax=axes[0], color=colors, edgecolor='black')
axes[0].set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Contract Type')
axes[0].set_ylabel('Percentage (%)')
axes[0].legend(title='Churn', loc='upper right')
axes[0].tick_params(axis='x', rotation=45)

# Count plot
contract_order = ['Month-to-month', 'One year', 'Two year']
sns.countplot(data=df, x='Contract', hue='Churn', ax=axes[1], palette=colors, order=contract_order)
axes[1].set_title('Churn Count by Contract Type', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Contract Type')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=45)
axes[1].legend(title='Churn')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/2_churn_by_contract.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 2: Churn by Contract Type saved")

# ============================================================
# VISUALIZATION 3: Churn by Payment Method
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stacked bar chart
payment_churn = pd.crosstab(df['PaymentMethod'], df['Churn'], normalize='index') * 100
payment_churn.plot(kind='bar', stacked=True, ax=axes[0], color=colors, edgecolor='black')
axes[0].set_title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Payment Method')
axes[0].set_ylabel('Percentage (%)')
axes[0].legend(title='Churn', loc='upper right')
axes[0].tick_params(axis='x', rotation=45)

# Count plot
sns.countplot(data=df, x='PaymentMethod', hue='Churn', ax=axes[1], palette=colors)
axes[1].set_title('Churn Count by Payment Method', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Payment Method')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=45)
axes[1].legend(title='Churn')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/3_churn_by_payment.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 3: Churn by Payment Method saved")

# ============================================================
# VISUALIZATION 4: Tenure Distribution
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram by Churn status
for churn_status, color in zip(['No', 'Yes'], colors):
    subset = df[df['Churn'] == churn_status]
    axes[0].hist(subset['Tenure'], bins=20, alpha=0.6, label=f'Churn: {churn_status}', color=color, edgecolor='black')

axes[0].set_title('Tenure Distribution by Churn Status', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Tenure (months)')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# Box plot
sns.boxplot(data=df, x='Churn', y='Tenure', ax=axes[1], palette=colors)
axes[1].set_title('Tenure Distribution by Churn Status', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Churn Status')
axes[1].set_ylabel('Tenure (months)')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/4_tenure_distribution.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 4: Tenure Distribution saved")

# ============================================================
# VISUALIZATION 5: Monthly Charges Distribution
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram by Churn status
for churn_status, color in zip(['No', 'Yes'], colors):
    subset = df[df['Churn'] == churn_status]
    axes[0].hist(subset['MonthlyCharges'], bins=20, alpha=0.6, label=f'Churn: {churn_status}', color=color, edgecolor='black')

axes[0].set_title('Monthly Charges Distribution by Churn Status', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Monthly Charges ($)')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# Box plot
sns.boxplot(data=df, x='Churn', y='MonthlyCharges', ax=axes[1], palette=colors)
axes[1].set_title('Monthly Charges by Churn Status', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Churn Status')
axes[1].set_ylabel('Monthly Charges ($)')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/5_monthly_charges.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 5: Monthly Charges Distribution saved")

# ============================================================
# VISUALIZATION 6: Correlation Heatmap
# ============================================================
fig, ax = plt.subplots(figsize=(10, 8))

# Select numeric columns
numeric_cols = ['Tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen_numeric', 'Churn_numeric']
correlation_matrix = df[numeric_cols].corr()

# Create heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', center=0,
            fmt='.3f', linewidths=0.5, ax=ax, vmin=-1, vmax=1)
ax.set_title('Correlation Matrix of Numerical Features', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/6_correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 6: Correlation Heatmap saved")

# ============================================================
# VISUALIZATION 7: Churn by Senior Citizen
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stacked bar chart
senior_churn = pd.crosstab(df['SeniorCitizen'], df['Churn'], normalize='index') * 100
senior_churn.plot(kind='bar', stacked=True, ax=axes[0], color=colors, edgecolor='black')
axes[0].set_title('Churn Rate by Senior Citizen Status', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Senior Citizen')
axes[0].set_ylabel('Percentage (%)')
axes[0].legend(title='Churn', loc='upper right')
axes[0].tick_params(axis='x', rotation=0)

# Count plot
sns.countplot(data=df, x='SeniorCitizen', hue='Churn', ax=axes[1], palette=colors)
axes[1].set_title('Churn Count by Senior Citizen Status', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Senior Citizen')
axes[1].set_ylabel('Count')
axes[1].legend(title='Churn')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/7_churn_by_senior.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 7: Churn by Senior Citizen saved")

# ============================================================
# VISUALIZATION 8: Churn by Paperless Billing
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stacked bar chart
paper_churn = pd.crosstab(df['PaperlessBilling'], df['Churn'], normalize='index') * 100
paper_churn.plot(kind='bar', stacked=True, ax=axes[0], color=colors, edgecolor='black')
axes[0].set_title('Churn Rate by Paperless Billing', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Paperless Billing')
axes[0].set_ylabel('Percentage (%)')
axes[0].legend(title='Churn', loc='upper right')
axes[0].tick_params(axis='x', rotation=0)

# Count plot
sns.countplot(data=df, x='PaperlessBilling', hue='Churn', ax=axes[1], palette=colors)
axes[1].set_title('Churn Count by Paperless Billing', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Paperless Billing')
axes[1].set_ylabel('Count')
axes[1].legend(title='Churn')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/8_churn_by_paperless.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization 8: Churn by Paperless Billing saved")

print("\n" + "=" * 70)
print("EDA SUMMARY STATISTICS")
print("=" * 70)

# Calculate key insights
print("\n[KEY INSIGHTS]")
print("-" * 50)

# Churn by Contract
print("\n1. Churn Rate by Contract Type:")
contract_churn_rate = df.groupby('Contract')['Churn_numeric'].mean() * 100
for contract, rate in contract_churn_rate.items():
    print(f"   - {contract}: {rate:.1f}%")

# Churn by Payment Method
print("\n2. Churn Rate by Payment Method:")
payment_churn_rate = df.groupby('PaymentMethod')['Churn_numeric'].mean() * 100
for payment, rate in payment_churn_rate.items():
    print(f"   - {payment}: {rate:.1f}%")

# Tenure statistics
print("\n3. Tenure Statistics by Churn Status:")
tenure_stats = df.groupby('Churn')['Tenure'].agg(['mean', 'median', 'std'])
print(tenure_stats.round(2))

# Monthly Charges statistics
print("\n4. Monthly Charges Statistics by Churn Status:")
charges_stats = df.groupby('Churn')['MonthlyCharges'].agg(['mean', 'median', 'std'])
print(charges_stats.round(2))

print("\n[SUCCESS] EDA COMPLETE - All visualizations saved to reports folder!")
print("=" * 70)
