# Sales Data Analysis Report

# The final Output

Setup & Load Data - Install pandas, create file, load CSV
          Date     Product  Quantity  Price Customer_ID Region  Total_Sales
0   2024-01-01       Phone         7  37300     CUST001   East       261100
1   2024-01-02  Headphones         4  15406     CUST002  North        61624
2   2024-01-03       Phone         2  21746     CUST003   West        43492
3   2024-01-04  Headphones         1  30895     CUST004   East        30895
4   2024-01-05      Laptop         8  39835     CUST005  North       318680
..         ...         ...       ...    ...         ...    ...          ...
95  2024-04-05      Tablet         8  20770     CUST096  North       166160
96  2024-04-06  Headphones         1   7647     CUST097   West         7647
97  2024-04-07      Tablet         5  27196     CUST098   East       135980
98  2024-04-08     Monitor         1  30717     CUST099  North        30717
99  2024-04-09  Headphones         5  23376     CUST100  South       116880

[100 rows x 7 columns]

Explore Data - Check shape, columns, data types

Number of rows: 100
Number of columns: 7

Column names: ['Date', 'Product', 'Quantity', 'Price', 'Customer_ID', 'Region', 'Total_Sales']

Data Types:
Date             str
Product          str
Quantity       int64
Price          int64
Customer_ID      str
Region           str
Total_Sales    int64
dtype: object

shape:
(100, 7)

Dataset Info:
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         100 non-null    str  
 1   Product      100 non-null    str  
 2   Quantity     100 non-null    int64
 3   Price        100 non-null    int64
 4   Customer_ID  100 non-null    str  
 5   Region       100 non-null    str  
 6   Total_Sales  100 non-null    int64
dtypes: int64(3), str(4)
memory usage: 5.6 KB
None

Summary Statistics:
         Quantity         Price    Total_Sales
count  100.000000    100.000000     100.000000
mean     4.780000  25808.510000  123650.480000
std      2.588163  13917.630242  100161.085275
min      1.000000   1308.000000    6540.000000
25%      2.750000  14965.250000   39517.500000
50%      5.000000  24192.000000   97955.500000
75%      7.000000  38682.250000  175792.500000
max      9.000000  49930.000000  373932.000000

Clean Data - Handle missing values, remove duplicates
Date           0
Product        0
Quantity       0
Price          0
Customer_ID    0
Region         0
Total_Sales    0
dtype: int64

Analyze Sales - Calculate revenue, find best product
Product
Headphones    1384033
Laptop        3889210
Monitor       1348071
Phone         2859394
Tablet        2884340
Name: Revenue, dtype: int64
Best-selling product: Laptop
Total Revenue: 12365048
Average Revenue per Order: 123650.48
Total Quantity Sold: 478

Sales Analysis Report
Total Revenue: $12,365,048.00
Average Revenue per Order: $123,650.48
Total Quantity Sold: 478
Best-selling product: Laptop

## 1. Dataset Overview

Number of rows: 100
Number of columns: 7
Date Range 2024-01-01 to 2024-04-09 |
Missing Values 0

### Columns
'Date', 'Product', 'Quantity', 'Price', 'Customer_ID', 'Region','Total_Sales

## 2. Data Quality

**Status:** No missing values found. Dataset is complete.

### Data Types

Date           object
Product        object
Quantity        int64
Price           int64
Customer_ID    object
Region         object
Total_Sales     int64
dtype: object

---

## 3. Statistical Summary

### Quantity Statistics

Average - 4.78 
 Median - 5.00 
 Highest - 9 
 Lowest -  1 
 Std Deviation - 2.59 

### Price Statistics

 Average  $25,808.51 
 Median  $24,192.00 
 Highest  $49,930.00 
 Lowest  $1,308.00 
 Std Deviation  $13,917.63 

### Total Sales Statistics

 Average  $123,650.48 
 Median  $97,955.50 
 Highest  $373,932.00 
 Lowest  $6,540.00 
 Std Deviation  $100,161.09 |

## 4. Key Findings

### Total Sales Revenue
**$12,365,048.00**

### Best-Selling Product

 Product - Laptop
 Units Sold  136 
 Revenue  $3,889,210.00 

### Product Performance Summary
| Product | Quantity Sold | Total Revenue | Avg Price | Transactions | Avg Sale/Transaction |

 Laptop  136  $3,889,210    $27,651.50   24   $162,050.42 
 Tablet  127  $2,884,340    $24,177.23   26   $110,936.15 
 Phone   101  $2,859,394    $27,379.00   20   $142,969.70 
 Monitor  66  $1,348,071    $20,709.67   15   $89,871.40 
 Headphones  48  $1,384,033 $28,692.13   15   $92,268.87 

### Regional Analysis

 North  147  $3,983,635     28  $142,272.68 
 South  143  $3,737,852     27  $138,438.96 
 East   94    $2,519,639    19    $132,612.58 
 West   94    $2,123,922    26    $81,689.31 

**Best Performing Region:** North $3,983,635.00

### Monthly Sales Trends
 Month    Revenue   Transactions 

 2024-01  $4,120,524  31 
 2024-02  $2,656,050  29 
 2024-03  $4,485,006  31 
 2024-04  $1,103,468  9 

**Best Month:** March 2024 $4,485,006.00

## 5. Summary

### Key Insights

1. **Total Revenue:** $12,365,048.00 across 100 transactions
2. **Best-Selling Product:** Laptop (136 units sold, $3.89M revenue)
3. **Top Region:** North region generates highest revenue
4. **Average Transaction:** $123,650.48
5. **Data Quality:** Clean dataset with no missing values

### Recommendations

1. **Focus on Laptop sales** - Highest revenue generator
2. **Investigate West region** - Lowest average sale per transaction
3. **Analyze February dip** - Lower sales compared to Jan/Mar
4. **Expand North region presence** - Best performing market

---

## 6. How to Run


pip install -r requirements.txt

# Run the analysis
run --- sales_analysis.py

