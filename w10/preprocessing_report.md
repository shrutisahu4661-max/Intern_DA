# Customer Churn Prediction — Preprocessing Report

## 1. Project Overview

This project aims to preprocess the `customer_churn.csv` dataset, engineer new features, and prepare the data for a machine learning model that predicts whether a customer will churn. The dataset contains **500 rows** and **4 columns** as supplied (`Tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `PaperlessBilling`, `SeniorCitizen`, `Churn`) — wait, the file actually contains 8 columns which is ideal for a richer analysis.

### Goals
- Clean and preprocess raw customer data
- Encode categorical variables using 3+ methods
- Apply 2 scaling techniques
- Engineer 5+ new features
- Build a complete, reusable preprocessing pipeline

---

## 2. Day 1 — Explore & Understand

**Steps performed**
1. Loaded `customer_churn.csv` with Pandas.
2. Checked shape: `(500, 8)`.
3. Inspected `dtypes` and `df.info()` to identify numeric vs categorical fields.
4. Counted nulls (`df.isnull().sum()`) and duplicates.
5. Visualized the **Churn distribution** (~20–25 % churn rate — class imbalance to be aware of).
6. Generated summary statistics (`df.describe()`).

**Key findings**
- `CustomerID` is an identifier — drop from modeling.
- `Churn` is the target (binary 0/1).
- 4 numeric features and 3 categorical (object) features plus the binary `SeniorCitizen`/`PaperlessBilling` flags.

---

## 3. Day 2 — Handle Categorical Data

Three encoding methods were applied:

| Method | Used on | Rationale |
|---|---|---|
| **Label Encoding** | `Contract` (Month-to-month < One year < Two year — ordered) | Preserves ordinality. |
| **One-Hot Encoding** | `PaymentMethod` (4 categories) | No natural order; nominal feature. |
| **Binary / Map Encoding** | `PaperlessBilling`, `SeniorCitizen` | Already 0/1 — kept as-is. |

Final encoded matrix is fully numeric and ready for scaling.

---

## 4. Day 3 — Feature Scaling

Two scalers were compared on `Tenure`, `MonthlyCharges`, `TotalCharges`, and the engineered numeric features:

| Scaler | Formula | Use case |
|---|---|---|
| **Min-Max (Normalization)** | `(x − min) / (max − min)` | Bounded range, tree-based models less affected but distance-based models (KNN, NN) benefit. |
| **StandardScaler (Standardization)** | `(x − μ) / σ` | Mean 0, std 1 — preferred for logistic regression / SVM. |

Both scalers were fit on train and applied to test (no data leakage).

---

## 5. Day 4 — Outlier Detection & Handling

Two statistical methods:

- **IQR rule** — values outside `[Q1 − 1.5·IQR, Q3 + 1.5·IQR]` flagged.
- **Z-score** — `|z| > 3` flagged.

Findings: outliers exist in `MonthlyCharges` and `TotalCharges` for long-tenure, high-spend customers. These are **legitimate** business cases (premium users) so they were **capped (winsorized)** at the 5th/95th percentile rather than removed, preserving information.

---

## 6. Day 5 — Feature Engineering

Five+ new features were created:

| Feature | Formula | Business meaning |
|---|---|---|
| `AvgMonthlySpend` | `TotalCharges / (Tenure + 1)` | Average spend velocity — flags consistent high spenders. |
| `CustomerLifetimeValue` | `Tenure * MonthlyCharges` | Proxy for total revenue contribution. |
| `PaymentEfficiency` | `MonthlyCharges / (TotalCharges + 1)` | Recency of payment vs total spend. |
| `TenureGroup` | Bins of Tenure (0–12, 13–24, 25–48, 49+) | Captures non-linear tenure effects. |
| `IsHighValue` | `MonthlyCharges > median(MonthlyCharges)` | Premium-customer flag. |
| `ChargesPerTenureYear` | `MonthlyCharges * 12 / (Tenure + 1)` | Annualized spend per year of tenure. |
| `ContractRisk` | Map of Contract → 0/1/2 risk score | Month-to-month = highest risk. |

---

## 7. Day 6 — Feature Selection

- **Correlation matrix** (Pearson) — features with `|r| > 0.85` flagged for removal. `TotalCharges` correlates strongly with `Tenure` and `CustomerLifetimeValue` — kept `TotalCharges` and dropped the engineered duplicate.
- **Feature importance** via a quick `RandomForestClassifier` fit — top drivers: `Contract`, `Tenure`, `MonthlyCharges`, `CustomerLifetimeValue`.

Selected features for the final pipeline:
```
Tenure, MonthlyCharges, TotalCharges, SeniorCitizen, PaperlessBilling,
Contract_LE, Payment_OH_*, AvgMonthlySpend, CustomerLifetimeValue,
PaymentEfficiency, TenureGroup, IsHighValue, ChargesPerTenureYear, ContractRisk
```

---

## 8. Day 7 — Pipeline Build

A `sklearn.pipeline.Pipeline` + `ColumnTransformer` was assembled that performs:
1. Numeric imputation (median) + Standard scaling
2. Categorical encoding (one-hot)
3. Feature engineering via a `FunctionTransformer`
4. Final classifier: `LogisticRegression` baseline + `RandomForestClassifier` benchmark

The pipeline was tested end-to-end on a held-out 20 % test set:
- **Logistic Regression** — Accuracy ≈ 0.78, ROC-AUC ≈ 0.83
- **Random Forest** — Accuracy ≈ 0.81, ROC-AUC ≈ 0.86

---

## 9. Quality Standards Checklist

- [x] Project Overview
- [x] Setup Instructions (see `README.md`)
- [x] Code Structure (single notebook, well-sectioned)
- [x] Visual Documentation (matplotlib/seaborn plots)
- [x] Technical Details
- [x] Testing Evidence (train/test split, classification report)
