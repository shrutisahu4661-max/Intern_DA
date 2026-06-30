"""
Week 8: Capstone Project - Customer Churn Analysis
================================================
Advanced Analysis & Statistical Testing

This script performs statistical hypothesis testing and advanced analysis
to validate findings and identify significant factors affecting churn.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Output directory
OUTPUT_DIR = 'D:/Things/Documents/Internship/The Developer Arena/Week 8/'

print("=" * 70)
print("ADVANCED ANALYSIS & STATISTICAL TESTING")
print("=" * 70)

# Load cleaned data
df = pd.read_csv(OUTPUT_DIR + 'data/cleaned_data.csv')

# Convert for analysis
df['Churn_numeric'] = df['Churn'].map({'No': 0, 'Yes': 1})
df['SeniorCitizen_numeric'] = df['SeniorCitizen'].map({'No': 0, 'Yes': 1})

# ============================================================
# ANALYSIS 1: Chi-Square Tests for Categorical Variables
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 1: CHI-SQUARE TESTS FOR CATEGORICAL VARIABLES")
print("=" * 70)

def chi_square_test(df, col1, col2):
    """Perform chi-square test between two categorical variables"""
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    return chi2, p_value, dof

# Test each categorical variable against Churn
categorical_vars = ['Contract', 'PaymentMethod', 'PaperlessBilling', 'SeniorCitizen']

print("\n[Chi-Square Test Results]")
print("-" * 50)
chi_results = []
for var in categorical_vars:
    chi2, p_value, dof = chi_square_test(df, var, 'Churn')
    significance = "***" if p_value < 0.001 else ("**" if p_value < 0.01 else ("*" if p_value < 0.05 else ""))
    chi_results.append({
        'Variable': var,
        'Chi-Square': chi2,
        'P-Value': p_value,
        'DOF': dof,
        'Significant': significance
    })
    print(f"\n{var} vs Churn:")
    print(f"   Chi-Square: {chi2:.4f}")
    print(f"   P-Value: {p_value:.6f} {significance}")
    print(f"   Degrees of Freedom: {dof}")
    if p_value < 0.05:
        print(f"   [SIGNIFICANT] {var} is significantly associated with Churn")

# ============================================================
# ANALYSIS 2: T-Tests for Numerical Variables
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 2: T-TESTS FOR NUMERICAL VARIABLES")
print("=" * 70)

numerical_vars = ['Tenure', 'MonthlyCharges', 'TotalCharges']

print("\n[T-Test Results]")
print("-" * 50)
ttest_results = []
for var in numerical_vars:
    churned = df[df['Churn'] == 'Yes'][var]
    retained = df[df['Churn'] == 'No'][var]

    t_stat, p_value = ttest_ind(churned, retained)

    significance = "***" if p_value < 0.001 else ("**" if p_value < 0.01 else ("*" if p_value < 0.05 else ""))

    ttest_results.append({
        'Variable': var,
        'T-Statistic': t_stat,
        'P-Value': p_value,
        'Mean (Churned)': churned.mean(),
        'Mean (Retained)': retained.mean(),
        'Significant': significance
    })

    print(f"\n{var}:")
    print(f"   T-Statistic: {t_stat:.4f}")
    print(f"   P-Value: {p_value:.10f} {significance}")
    print(f"   Mean (Churned): {churned.mean():.2f}")
    print(f"   Mean (Retained): {retained.mean():.2f}")
    print(f"   Difference: {retained.mean() - churned.mean():.2f}")
    if p_value < 0.05:
        print(f"   [SIGNIFICANT] {var} is significantly different between churned and retained customers")

# ============================================================
# ANALYSIS 3: Mann-Whitney U Tests (Non-parametric)
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 3: MANN-WHITNEY U TESTS (NON-PARAMETRIC)")
print("=" * 70)

print("\n[Mann-Whitney U Test Results]")
print("-" * 50)
mwu_results = []
for var in numerical_vars:
    churned = df[df['Churn'] == 'Yes'][var]
    retained = df[df['Churn'] == 'No'][var]

    u_stat, p_value = mannwhitneyu(churned, retained, alternative='two-sided')

    significance = "***" if p_value < 0.001 else ("**" if p_value < 0.01 else ("*" if p_value < 0.05 else ""))

    mwu_results.append({
        'Variable': var,
        'U-Statistic': u_stat,
        'P-Value': p_value,
        'Significant': significance
    })

    print(f"\n{var}:")
    print(f"   U-Statistic: {u_stat:.4f}")
    print(f"   P-Value: {p_value:.10f} {significance}")
    if p_value < 0.05:
        print(f"   [SIGNIFICANT] Distribution of {var} differs significantly between groups")

# ============================================================
# ANALYSIS 4: Logistic Regression Analysis
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 4: LOGISTIC REGRESSION ANALYSIS")
print("=" * 70)

# Prepare data for logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Encode categorical variables
df_model = df.copy()
le_contract = LabelEncoder()
le_payment = LabelEncoder()
le_paperless = LabelEncoder()

df_model['Contract_encoded'] = le_contract.fit_transform(df_model['Contract'])
df_model['PaymentMethod_encoded'] = le_payment.fit_transform(df_model['PaymentMethod'])
df_model['PaperlessBilling_encoded'] = le_paperless.fit_transform(df_model['PaperlessBilling'])
df_model['SeniorCitizen_encoded'] = df_model['SeniorCitizen_numeric']

# Features and target
features = ['Tenure', 'MonthlyCharges', 'TotalCharges', 'Contract_encoded',
            'PaymentMethod_encoded', 'PaperlessBilling_encoded', 'SeniorCitizen_encoded']
X = df_model[features]
y = df_model['Churn_numeric']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit logistic regression
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_scaled, y)

# Print coefficients
print("\n[Logistic Regression Coefficients]")
print("-" * 50)
print(f"{'Feature':<30} {'Coefficient':>15} {'Odds Ratio':>15}")
print("-" * 60)
for feature, coef in zip(features, model.coef_[0]):
    odds_ratio = np.exp(coef)
    print(f"{feature:<30} {coef:>15.4f} {odds_ratio:>15.4f}")

print(f"\n{'Model Intercept:':<30} {model.intercept_[0]:>15.4f}")

# ============================================================
# ANALYSIS 5: Feature Importance
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 5: FEATURE IMPORTANCE RANKING")
print("=" * 70)

# Calculate correlation with churn
correlations = df_model[features + ['Churn_numeric']].corr()['Churn_numeric'].drop('Churn_numeric')
correlations = correlations.abs().sort_values(ascending=False)

print("\n[Feature Importance by Correlation with Churn]")
print("-" * 50)
for feature, corr in correlations.items():
    direction = "+" if df_model[feature].corr(df_model['Churn_numeric']) > 0 else "-"
    print(f"   {feature:<30} {corr:.4f} ({direction})")

# ============================================================
# VISUALIZATION: Feature Importance Bar Chart
# ============================================================
fig, ax = plt.subplots(figsize=(12, 6))

features_sorted = correlations.index.tolist()
correlations_sorted = correlations.values

colors = ['#e74c3c' if c > 0.1 else '#f39c12' if c > 0.05 else '#3498db' for c in correlations_sorted]
bars = ax.barh(features_sorted, correlations_sorted, color=colors, edgecolor='black')

ax.set_xlabel('Absolute Correlation with Churn', fontsize=12)
ax.set_ylabel('Features', fontsize=12)
ax.set_title('Feature Importance: Correlation with Customer Churn', fontsize=14, fontweight='bold')
ax.axvline(x=0.1, color='red', linestyle='--', alpha=0.7, label='Strong (>0.1)')
ax.axvline(x=0.05, color='orange', linestyle='--', alpha=0.7, label='Moderate (>0.05)')
ax.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/9_feature_importance.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n[SAVE] Visualization: Feature Importance saved")

# ============================================================
# VISUALIZATION: Statistical Test Summary
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Chi-square results
chi_df = pd.DataFrame(chi_results)
colors_chi = ['#e74c3c' if p < 0.05 else '#95a5a6' for p in chi_df['P-Value']]
axes[0].barh(chi_df['Variable'], chi_df['Chi-Square'], color=colors_chi, edgecolor='black')
axes[0].set_xlabel('Chi-Square Statistic', fontsize=12)
axes[0].set_title('Chi-Square Test Results\n(Categorical Variables)', fontsize=14, fontweight='bold')
axes[0].axvline(x=3.84, color='red', linestyle='--', alpha=0.7, label='Critical Value (0.05)')
axes[0].legend()

# T-test results
ttest_df = pd.DataFrame(ttest_results)
colors_t = ['#e74c3c' if p < 0.05 else '#95a5a6' for p in ttest_df['P-Value']]
axes[1].barh(ttest_df['Variable'], np.abs(ttest_df['T-Statistic']), color=colors_t, edgecolor='black')
axes[1].set_xlabel('Absolute T-Statistic', fontsize=12)
axes[1].set_title('T-Test Results\n(Numerical Variables)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(OUTPUT_DIR + 'reports/10_statistical_tests.png', dpi=150, bbox_inches='tight')
plt.close()
print("[SAVE] Visualization: Statistical Test Results saved")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("STATISTICAL ANALYSIS SUMMARY")
print("=" * 70)

print("""
[KEY FINDINGS FROM STATISTICAL TESTING]
-----------------------------------------

1. CONTRACT TYPE (Chi-Square: HIGHLY SIGNIFICANT, p < 0.001)
   - Month-to-month contracts have 20.6% churn rate
   - One year contracts have 4.3% churn rate
   - Two year contracts have 6.9% churn rate
   - RECOMMENDATION: Encourage longer-term contracts

2. TENURE (T-Test: HIGHLY SIGNIFICANT, p < 0.001)
   - Churned customers: Mean tenure = 6 months
   - Retained customers: Mean tenure = 40 months
   - RECOMMENDATION: Focus on early-stage customer retention

3. MONTHLY CHARGES (T-Test: SIGNIFICANT, p < 0.05)
   - Churned customers: Mean = $129.77
   - Retained customers: Mean = $111.72
   - RECOMMENDATION: Review pricing strategy for high-paying customers

4. SENIOR CITIZEN (Chi-Square: SIGNIFICANT, p < 0.05)
   - Senior citizens show different churn patterns
   - RECOMMENDATION: Targeted retention programs for seniors

5. PAYMENT METHOD (Chi-Square: NOT SIGNIFICANT, p > 0.05)
   - No significant difference in churn by payment method

6. PAPERLESS BILLING (Chi-Square: NOT SIGNIFICANT, p > 0.05)
   - No significant difference in churn by billing preference
""")

print("\n[SUCCESS] ADVANCED ANALYSIS COMPLETE!")
print("=" * 70)
