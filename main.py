import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("charts"):
    os.makedirs("charts")

df = pd.read_csv("sales_data_clean.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color='skyblue', title="Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("charts/Sales_by_Region.png")
plt.show(block=False)
plt.pause(1)
plt.close()

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTop Products by Sales:")
print(product_sales)

plt.figure(figsize=(10,5))
product_sales.plot(kind="bar", color='orange', title="Top Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/Top_Products.png")
plt.show(block=False)
plt.pause(1)
plt.close()

monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

plt.figure(figsize=(10,5))
monthly_sales.plot(marker='o', color='green', title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/Monthly_Sales_Trend.png")
plt.show(block=False)
plt.pause(1)
plt.close()

print("\nInsights:")
print("- North and South regions have the highest sales.")
print("- Laptop and Camera are the top-selling products.")
print("- March shows the peak monthly sales month.")
