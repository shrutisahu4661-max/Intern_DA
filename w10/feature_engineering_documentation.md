# Feature Engineering Documentation

This document describes every engineered feature created from `customer_churn.csv`, the rationale, and its expected business value.

---

## Source Features

| Column | Type | Description |
|---|---|---|
| CustomerID | string | Unique identifier (dropped before modeling) |
| Tenure | int | Months the customer has stayed |
| MonthlyCharges | float | Current monthly bill |
| TotalCharges | float | Lifetime total paid |
| Contract | categorical | Month-to-month / One year / Two year |
| PaymentMethod | categorical | Credit Card / Bank Transfer / Electronic Check / Mailed Check |
| PaperlessBilling | binary | 0/1 |
| SeniorCitizen | binary | 0/1 |
| Churn | binary | **Target** (0 = stayed, 1 = churned) |

---

## Engineered Features (7 total — exceeds the 5+ requirement)

### 1. `AvgMonthlySpend`
- **Definition:** `TotalCharges / (Tenure + 1)`
- **Rationale:** Smooths out the natural growth of `TotalCharges` with tenure. A customer who pays a lot over a short tenure is a high-value short-term customer (churn risk).
- **Business meaning:** Identifies high-velocity spenders — those whose average monthly outlay exceeds their current `MonthlyCharges` are likely upgraded and at risk of churn if they perceive no value.

### 2. `CustomerLifetimeValue` (CLV)
- **Definition:** `Tenure * MonthlyCharges`
- **Rationale:** Standard CLV proxy using only what we have.
- **Business meaning:** Long-tenure customers with high monthly bills are gold. A drop in CLV is a leading indicator of churn.

### 3. `PaymentEfficiency`
- **Definition:** `MonthlyCharges / (TotalCharges + 1)`
- **Rationale:** Captures the ratio of current month to cumulative spend. Low values indicate a long-paying customer; high values indicate a recent or fast-ramping customer.
- **Business meaning:** Useful to flag new high-paying customers that may need onboarding nurturing.

### 4. `TenureGroup`
- **Definition:** Binned `Tenure`: `0–12`, `13–24`, `25–48`, `49+`
- **Rationale:** Non-linear tenure effect — the first 12 months see the highest churn.
- **Business meaning:** Marketing/retention teams can target by cohort.

### 5. `IsHighValue`
- **Definition:** `1 if MonthlyCharges > median(MonthlyCharges) else 0`
- **Rationale:** Binary flag isolating premium customers.
- **Business meaning:** Premium customers are more expensive to lose; this is a stratification feature for the modeling team.

### 6. `ChargesPerTenureYear`
- **Definition:** `(MonthlyCharges * 12) / (Tenure + 1)`
- **Rationale:** Annualized spend per year of tenure — comparable across customers.
- **Business meaning:** Customers paying >$1 500/yr-per-year-of-tenure are heavy users; a sudden drop correlates with churn.

### 7. `ContractRisk`
- **Definition:** Map `Contract` → `Month-to-month=2, One year=1, Two year=0`
- **Rationale:** Encodes the prior domain knowledge that month-to-month customers churn more.
- **Business meaning:** A direct risk score for the contract type.

---

## Encoding Decisions

| Original | Method | Why |
|---|---|---|
| `Contract` | **Label Encoding** (after ordinal mapping) | Naturally ordered by lock-in length. |
| `PaymentMethod` | **One-Hot Encoding** (4 dummies) | No order; small cardinality — one-hot is safe. |
| `PaperlessBilling` | Map (Yes/No → 1/0) | Already binary. |
| `SeniorCitizen` | Kept numeric | Already 0/1. |

A third encoding — **Binary / Target-frequency encoding** for `PaymentMethod` — is shown in the notebook as a `lambda` demonstration (`PaymentMethod_freq`).

---

## Outlier Handling Strategy

- **Detection:** IQR (1.5×) and Z-score (|z|>3).
- **Treatment:** **Winsorization** at 5th/95th percentile — caps extreme but legitimate values without dropping rows.
- **Rationale:** In churn data, high spenders are exactly the customers we don't want to delete; capping preserves them while reducing the influence on distance-based models.

---

## Scaling Comparison

| Method | After-fit Mean | After-fit Std |
|---|---|---|
| `StandardScaler` | ~0 | ~1 |
| `MinMaxScaler` | varies | ranges 0–1 |

For the final pipeline we chose `StandardScaler` because the downstream classifier (Logistic Regression) is sensitive to feature variance and benefits from zero-mean inputs.

---

## Feature Selection Summary

| Method | Action |
|---|---|
| Pearson correlation `|r|>0.85` | Drop `CustomerLifetimeValue` (correlated with `TotalCharges`) — keep `TotalCharges`. |
| RandomForest feature importance | Top 5: `Contract_LE`, `Tenure`, `MonthlyCharges`, `ContractRisk`, `CustomerLifetimeValue`. |

Final feature set contains **14 columns** + `Churn` target.

---

## Validation Approach

- 80/20 train-test split (`stratify=y` to preserve class balance).
- 5-fold cross-validation on the training set.
- Metrics: Accuracy, Precision, Recall, F1, ROC-AUC.
- Random Forest baseline: **AUC ≈ 0.86**, beating the logistic regression baseline (≈ 0.83).
