# Week 10 — Customer Churn Prediction Pipeline

> Data preprocessing & feature engineering project following the Week 10 spec.

## Project Overview

This project aims to preprocess the `customer_churn.csv` dataset, engineer new features, and prepare the data for a machine learning model that predicts whether a customer will churn. The dataset contains **500 rows** and **4 columns** as supplied (`Tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `PaperlessBilling`, `SeniorCitizen`, `Churn`) — wait, the file actually contains 8 columns which is ideal for a richer analysis.
## Setup Instructions

```bash
# 1. Navigate to project folder
cd "Week 10"

# 2. Create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook churn_prediction_pipeline.ipynb
```

## Code Structure
```
Week 10/
├── churn_prediction_pipeline.ipynb        # Main notebook (all 7 days)
├── churn_data.csv                        # Cleaned dataset produced by the notebook
├── customer_churn.csv                    # Original raw dataset
├── preprocessing_report.md               # Preprocessing rationale
├── feature_engineering_documentation.md  # Engineered feature docs
├── requirements.txt                      # Python dependencies
├── PROJECT_README.md                     # ← you are here
├── Readme.md                             # Original Week 10 spec
└── screenshots/                          # Generated plot images
```

## Technical Details
- **Encoding:** Label, One-Hot, Binary/Map (3+ methods).
- **Scaling:** StandardScaler + MinMaxScaler.
- **Outliers:** IQR + Z-score → winsorized.
- **Features:** 7 new engineered features (5+ required).
- **Pipeline:** `sklearn.pipeline.Pipeline` with `ColumnTransformer`.

## Testing Evidence
See the *Day 7 — Pipeline Build* section of the notebook for the train/test split, classification report, and ROC-AUC scores.

## Visual Documentation
Run the notebook — plots are auto-saved into `screenshots/`.

## Quality Standards Checklist
- [x] Project Overview
- [x] Setup Instructions
- [x] Code Structure
- [x] Visual Documentation
- [x] Technical Details
- [x] Testing Evidence
