# Week 4 Project: Sales Data Analysis

## Project Overview
i want to create somwthing that can do my work multiple times without manually reprocessing the dataset and generate clear insights using simple data analysis and visualization steps, So i have create different functions to load data, clean data, analyze data, visualize results, and save a report. This way i can easily run the script multiple times with different datasets or after updating the data without needing to redo all the steps manually.


Project goals:
- Calculate total and average sales.
- Find highest and lowest order sales.
- Identify the best-selling product.
- Visualize product-wise, region-wise, and monthly sales.

## Setup Instructions
1. Open terminal in this project folder.

2. Install dependencies:
   pip install -r requirements.txt

3. Run the project:
    python main.py

## Code Structure
```text
Week 4/
|-- README.md
|-- main.py
|-- requirements.txt
|-- data/
|   |-- sales_data.csv
|-- visualizations/
|   |-- product_bar_chart.png
|   |-- region_pie_chart.png
|   |-- monthly_sales_line_chart.png
|-- report/
|   |-- analysis_report.md
|   |-- sales_summary.txt
```

## Visual Documentation
After running main.py , charts are automatically saved in visualizations folder.

- demo output after terminal successful run.

visualizations/product_bar_chart.png
visualizations/region_pie_chart.png
visualizations/monthly_sales_line_chart.png

## Technical Details
- Language: Python 3
- Libraries: pandas, matplotlib
- Workflow:
  - Load CSV file
  - Validate required columns
  - Clean missing/invalid values
  - Compute metrics
  - Build charts and save outputs
- Error handling:
  - Missing file check
  - Missing required columns check
  - Empty cleaned data check

## Testing Evidence
Basic validation included in code:
- File-not-found scenario handled in load_data.
- Missing columns scenario handled in load_data.
- Empty dataset after cleaning handled in main.

Quick manual test cases:
1. Run with data/sales_data.csv and confirm chart files are generated.
2. Rename the CSV file and run again to verify error handling.
3. Remove one required column from CSV and run to verify validation message.
