import pandas as pd

df = pd.read_csv("Superstore_Sales_Cleaned.csv")

# df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
# df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
# print(df.head())
# print("Total rows:", len(df))
# print(df.columns.tolist())
# print(df.isnull().sum()[df.isnull().sum() > 0])
# print(df.isnull().sum())
# print("Duplicate rows:", df.duplicated().sum())
# print(df.describe())
# print(df["Category"].value_counts())
# print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
# print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
# print(df.groupby("Order Year")["Sales"].sum())
# print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))
# print(
#     df.groupby(["Customer ID", "Customer Name"])["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print(df.groupby("Category")["Sales"].mean().sort_values(ascending=False))
# print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))
# print(df.groupby("Segment")["Order ID"].nunique().sort_values(ascending=False))
# print(
#     df.groupby("Segment")
#     .agg(
#         Total_Sales=("Sales", "sum"),
#         Total_Orders=("Order ID", "nunique")
#     )
#     .assign(
#         Average_Order_Value=lambda x: x["Total_Sales"] / x["Total_Orders"]
#     )
# )
# print(
#     df.groupby("Order Month")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
# )
# print("Average shipping days:", df["Shipping days"].mean())
# print("Minimum shipping days:", df["Shipping days"].min())
# print("Maximum shipping days:", df["Shipping days"].max())
# df["Shipping Category"] = pd.cut(
#     df["Shipping days"],
#     bins=[-1, 2, 5, 7],
#     labels=["Fast", "Standard", "Slow"]
# )

# print(df["Shipping Category"].value_counts())
# order_shipping = df.groupby("Order ID")["Shipping days"].first()

# shipping_category = pd.cut(
#     order_shipping,
#     bins=[-1, 2, 5, 7],
#     labels=["Fast", "Standard", "Slow"]
# )

# print(shipping_category.value_counts())
# print(
#     df.groupby("City")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print(
#     df.groupby(["Product ID", "Product Name"])["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print("Total unique customers:", df["Customer ID"].nunique())
# print("Average orders per customer:", df["Order ID"].nunique() / df["Customer ID"].nunique())
import matplotlib.pyplot as plt

# category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

# category_sales.plot(kind="bar")

# plt.title("Sales by Category")
# plt.xlabel("Category")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()
# yearly_sales = df.groupby("Order Year")["Sales"].sum()

# yearly_sales.plot(kind="line", marker="o")

# plt.title("Sales Trend by Year")
# plt.xlabel("Year")
# plt.ylabel("Total Sales")
# plt.xticks(yearly_sales.index)
# plt.grid(True)
# plt.tight_layout()
# plt.show()
# region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

# region_sales.plot(kind="bar")

# plt.title("Sales by Region")
# plt.xlabel("Region")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()
# segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

# segment_sales.plot(kind="bar")

# plt.title("Sales by Customer Segment")
# plt.xlabel("Segment")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()
# top_cities = (
#     df.groupby("City")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# top_cities.plot(kind="bar")

# plt.title("Top 10 Cities by Sales")
# plt.xlabel("City")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()
# subcategory_sales = (
#     df.groupby("Sub-Category")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# subcategory_sales.plot(kind="bar")

# plt.title("Sales by Sub-Category")
# plt.xlabel("Sub-Category")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()
df["Shipping Category"] = pd.cut(
    df["Shipping days"],
    bins=[-1, 2, 5, 7],
    labels=["Fast", "Standard", "Slow"]
)

shipping_sales = (
    df.groupby("Shipping Category", observed=True)["Sales"]
    .sum()
    .sort_values(ascending=False)
)

shipping_sales.plot(kind="bar")

plt.title("Sales by Shipping Category")
plt.xlabel("Shipping Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# print(df.dtypes)