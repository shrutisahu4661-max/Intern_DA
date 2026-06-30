# Customer Churn Analysis - Capstone Project

## Week 8: End-to-End Business Analysis

This project demonstrates a complete data analysis workflow for understanding and reducing customer churn.

---

## Project Overview

**Business Problem:** Identify why customers churn and develop data-driven retention strategies to reduce the 10.6% churn rate.

**Dataset:** 500 customers with 9 features including tenure, charges, contract type, and payment methods.

---

## Project Structure

```
Week 8/
├── data/
│   ├── customer_churn.csv        # Raw data
│   └── cleaned_data.csv         # Cleaned data
├── notebooks/
│   ├── 1_data_cleaning.py       # Data cleaning script
│   ├── 2_eda.py                 # Exploratory Data Analysis
│   └── 3_analysis.py            # Advanced statistical analysis
├── reports/
│   ├── executive_summary.txt     # 1-page business summary
│   ├── technical_report.txt     # Detailed technical report
│   ├── 1_churn_distribution.png
│   ├── 2_churn_by_contract.png
│   ├── 3_churn_by_payment.png
│   ├── 4_tenure_distribution.png
│   ├── 5_monthly_charges.png
│   ├── 6_correlation_heatmap.png
│   ├── 7_churn_by_senior.png
│   ├── 8_churn_by_paperless.png
│   ├── 9_feature_importance.png
│   └── 10_statistical_tests.png
├── presentation/
│   └── business_presentation.md # 10-slide presentation
└── README.md                    # This file
```

---

## Key Findings

### 1. Contract Type (Most Important)
- **Month-to-month:** 20.6% churn rate
- **One year:** 4.3% churn rate  
- **Two year:** 6.9% churn rate
- Statistical significance: p < 0.001

### 2. Customer Tenure
- **Churned customers:** Average 6 months tenure
- **Retained customers:** Average 40 months tenure
- Statistical significance: p < 0.001

### 3. Monthly Charges
- **Churned:** $129.77/month average
- **Retained:** $111.72/month average
- Statistical significance: p < 0.05

---

## Statistical Methods Used

1. **Chi-Square Tests** - For categorical variables
2. **Independent T-Tests** - For numerical variables
3. **Mann-Whitney U Tests** - Non-parametric validation
4. **Logistic Regression** - Coefficient estimation
5. **Correlation Analysis** - Feature importance ranking

---

## Deliverables

| Deliverable | File | Status |
|-------------|------|--------|
| Data Cleaning | notebooks/1_data_cleaning.py | Complete |
| EDA | notebooks/2_eda.py | Complete |
| Statistical Analysis | notebooks/3_analysis.py | Complete |
| Executive Summary | reports/executive_summary.txt | Complete |
| Technical Report | reports/technical_report.txt | Complete |
| Business Presentation | presentation/business_presentation.md | Complete |
| Visualizations | reports/*.png (10 charts) | Complete |

---

## Recommendations

### Immediate Actions (0-3 months)
1. Launch "Contract Upgrade" campaign for 170 month-to-month customers
2. Offer 10-15% discount for annual contracts

### Short-Term Actions (3-6 months)
3. Create "First Year Success" onboarding program
4. Build early warning system for at-risk customers

### Long-Term Actions (6-12 months)
5. Deploy predictive machine learning model
6. Develop customer segmentation strategy

---

## Expected Business Impact

- **Churn reduction:** From 10.6% to 8% (25% improvement)
- **Customers retained:** ~13 additional customers/year
- **Revenue saved:** $50,000 - $75,000 annually

---

## How to Run

1. **Data Cleaning:**
   ```bash
   python notebooks/1_data_cleaning.py
   ```

2. **Exploratory Data Analysis:**
   ```bash
   python notebooks/2_eda.py
   ```

3. **Advanced Analysis:**
   ```bash
   python notebooks/3_analysis.py
   ```

---

## Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- scikit-learn

---

## Conclusion

This analysis demonstrates the complete data science workflow from business problem definition through actionable insights. The key finding is that **contract type and tenure** are the strongest predictors of customer churn, providing clear direction for retention strategies.

---

*Project completed as part of The Developer Arena - Data Analysis Internship*
*Date: June 2026*
