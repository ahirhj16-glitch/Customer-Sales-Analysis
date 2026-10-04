import pandas as pd
import matplotlib.pyplot as plt


# =========================
# 1. Load Data
# =========================
df = pd.read_csv("project.1 biggener/Data/s.csv")


# =========================
# 2. Create Sales Columns
# =========================

df["Sales"] = df["Quantity"] * df["Unit_Price"]

df["Discount_Amount"] = df["Sales"] * df["Discount"] / 100

df["Final_Sales"] = df["Sales"] - df["Discount_Amount"]


# =========================
# 3. Basic Analysis
# =========================


# =========================
# 4. Product Analysis
# =========================

product_sales = df.groupby("Product")["Sales"].sum()


# =========================
# 5. City Analysis
# =========================

city_sales = df.groupby("City")["Final_Sales"].sum()


# =========================
# 6. Payment Analysis
# =========================

Payment_Sales = df.groupby("Payment")["Final_Sales"].sum()

discount_impact = (df["Discount_Amount"].sum() / df["Sales"].sum()) * 100

PKL = df.groupby("Product")["Quantity"].sum()



print("Grose sales",df["Sales"].sum())

print("final sales",df["Sales"].sum())

print("Grose sales",df["Sales"].sum())

print("Grose sales",df["Sales"].sum())





