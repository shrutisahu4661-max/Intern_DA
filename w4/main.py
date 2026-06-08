from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# ============== Sales Data Analysis ================

files = Path("data/sales_data.csv")
Visuals = Path("visualizations")
Report_files = Path("report/sales_summary.txt")


#---- Load CSV data with basic checks -----
    
def load_data(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    df = pd.read_csv(file_path)
    required_columns = {"Date", "Product", "Region", "Total_Sales"}

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")

    return df

#------   Clean and validate sales data --------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned["Date"] = pd.to_datetime(cleaned["Date"], errors="coerce")
    cleaned["Total_Sales"] = pd.to_numeric(cleaned["Total_Sales"], errors="coerce")
    cleaned["Product"] = cleaned["Product"].fillna("Unknown")
    cleaned["Region"] = cleaned["Region"].fillna("Unknown")

    cleaned = cleaned.dropna(subset=["Date", "Total_Sales"])
    cleaned = cleaned[cleaned["Total_Sales"] >= 0]
    cleaned = cleaned.drop_duplicates()

    return cleaned


#------  Calculate simple sales metrics --------

def analyze_data(df: pd.DataFrame) -> dict:
    total_sales = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    max_sale = df["Total_Sales"].max()
    min_sale = df["Total_Sales"].min()
    total_orders = len(df)

    product_totals = df.groupby("Product", as_index=False)["Total_Sales"].sum()
    region_totals = df.groupby("Region", as_index=False)["Total_Sales"].sum()
    top_product_row = product_totals.sort_values("Total_Sales", ascending=False).iloc[0]

    monthly_totals = (
        df.assign(Month=df["Date"].dt.to_period("M").astype(str))
        .groupby("Month", as_index=False)["Total_Sales"]
        .sum()
    )

    return {
        "total_sales": float(total_sales),
        "average_sale": float(average_sale),
        "max_sale": float(max_sale),
        "min_sale": float(min_sale),
        "total_orders": int(total_orders),
        "product_totals": product_totals,
        "region_totals": region_totals,
        "monthly_totals": monthly_totals,
        "top_product": str(top_product_row["Product"]),
        "top_product_sales": float(top_product_row["Total_Sales"]),
    }


#---------- Create and save simple charts --------------

def visualizations(analysis: dict) -> None:
    Visuals.mkdir(parents=True, exist_ok=True)
    product_totals = analysis["product_totals"]
    region_totals = analysis["region_totals"]
    monthly_totals = analysis["monthly_totals"]

    plt.figure(figsize=(8, 5))
    plt.bar(product_totals["Product"], product_totals["Total_Sales"], color="steelblue")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales (INR)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(Visuals / "product_bar_chart.png")
    plt.close()

    plt.figure(figsize=(6, 6))
    plt.pie(
        region_totals["Total_Sales"],
        labels=region_totals["Region"],
        autopct="%1.1f%%",
        startangle=140,
    )
    plt.title("Sales Distribution by Region")
    plt.tight_layout()
    plt.savefig(Visuals / "region_pie_chart.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.plot(monthly_totals["Month"], monthly_totals["Total_Sales"], marker="o", color="darkgreen")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales (INR)")
    plt.tight_layout()
    plt.savefig(Visuals / "monthly_sales_line_chart.png")
    plt.close()


#--------- Write and save plain-text summary report ---------

def save_summary(analysis: dict) -> None:
    Report_files.parent.mkdir(parents=True, exist_ok=True)
    summary_lines = [                       # list of lines for the summary report
        "Sales Data Analysis - Summary",
        "-----------------------------",
        f"Total Orders: {analysis['total_orders']}",
        f"Total Sales: INR {analysis['total_sales']:.2f}",
        f"Average Sale per Order: INR {analysis['average_sale']:.2f}",
        f"Highest Order Sale: INR {analysis['max_sale']:.2f}",
        f"Lowest Order Sale: INR {analysis['min_sale']:.2f}",
        f"Best Selling Product: {analysis['top_product']} (INR {analysis['top_product_sales']:.2f})",
    ]

    Report_files.write_text("\n".join(summary_lines), encoding="utf-8") # Save the summary report to a text file


#------ Print summary to terminal -----------

def print_summary(analysis: dict) -> None: 
    print("\n=== Sales Data Analysis ===")
    print(f"Total Orders: {analysis['total_orders']}")
    print(f"Total Sales: INR {analysis['total_sales']:.2f}")
    print(f"Average Sale per Order: INR {analysis['average_sale']:.2f}")
    print(f"Highest Order Sale: INR {analysis['max_sale']:.2f}")
    print(f"Lowest Order Sale: INR {analysis['min_sale']:.2f}")
    print(
        f"Best Selling Product: {analysis['top_product']} "
        f"(INR {analysis['top_product_sales']:.2f})"
    )
    print(f"Charts saved to: {Visuals}")
    print(f"Text summary saved to: {Report_files}")



def main() -> None: # Main function to run the analysis pipeline
    try: # Run the main analysis pipeline with error handling
        sales_df = load_data(files)
        cleaned_df = clean_data(sales_df)

        if cleaned_df.empty:        # Check if cleaned data is empty and raise an error if so
            raise ValueError("No valid data available after cleaning.")

        analysis = analyze_data(cleaned_df)
        visualizations(analysis)
        save_summary(analysis)
        print_summary(analysis)

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__": # Run the main function when the script is executed
    main()
