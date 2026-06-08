# Sales Data Analysis - Report

## 1. Objective
i wan to create somwthing that can do my work multiple times without manually reprocessing the dataset and generate clear insights using simple data analysis and visualization steps, So i have create different functions to load data, clean data, analyze data, visualize results, and save a report. This way i can easily run the script multiple times with different datasets or after updating the data without needing to redo all the steps manually.

## 2. Dataset
- Source file: data/sales_data.csv
- Fields used:
  - Date
  - Product
  - Region`
  - Total_Sales

## 3. Data Cleaning Steps
1. Convert Date to datetime format.
2. Convert Total_Sales to numeric values.
3. Fill missing Product and Region` with Unknown.
4. Remove rows with invalid date or sales value.
5. Remove negative sales rows.
6. Remove duplicate rows.

## 4. Analysis Metrics
The script calculates:
- Total orders
- Total sales
- Average sale per order
- Highest order sale
- Lowest order sale
- Sales by product
- Sales by region
- Monthly total sales
- Best-selling product

## 5. Visualizations Created
Saved in visualizations/:
1. product_bar_chart.png (Bar chart)
2. region_pie_chart.png (Pie chart)
3. monthly_sales_line_chart.png (Line chart)

## 6. Insights
- Product bar chart shows which product generates the most revenue.
- Region pie chart shows how total sales are distributed across regions.
- Monthly line chart shows sales trend over time.

## 7. Output Files
- Text summary: report/sales_summary.txt
- Charts: visualizations/

## 8. Outputs
=== Sales Data Analysis ===
Total Orders: 100
Total Sales: INR 12365048.00
Average Sale per Order: INR 123650.48
Highest Order Sale: INR 373932.00
Lowest Order Sale: INR 6540.00
Best Selling Product: Laptop (INR 3889210.00)
Charts saved to: visualizations
Text summary saved to: report\sales_summary.txt
