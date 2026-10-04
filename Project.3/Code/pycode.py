import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Project.3/Data/sales_project3.csv")

df["Quantity"] = df["Quantity"].replace("three", 3)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean().round())


df["Product"] = df["Product"].str.title().str.strip()

df.loc[df["Discount"] > 100, "Discount"] = 10

df["Discount"] = df["Discount"].fillna(10)

df.loc[df["Unit_Price"] < 0,'Unit_Price'] = pd.NA
df["Unit_Price"] = df["Unit_Price"].round()


df["Payment"] = df["Payment"].str.upper().str.strip()

df["City"] = df["City"].str.title().str.strip()
df["City"] = df["City"].fillna("Unknown")
df["Payment"] = df["Payment"].fillna("Unknown")


df = df.drop_duplicates()

#print(df["Payment"].unique())

df["Gros_sales"]= df['Quantity'] * df['Unit_Price']

df["Discount_Values"] = df["Gros_sales"] * df["Discount"] / 100

df["Final_sales"] = df['Gros_sales'] - df["Discount_Values"]



Total_product_sales = df.groupby('Product')['Final_sales'].sum()

Total_sales_by_city = df.groupby('City')['Final_sales'].sum()

Total_sales_by_payment = df.groupby('Payment')['Final_sales'].sum()

Total_sales_by_customer_type = df.groupby('Customer_Type')['Final_sales'].sum()

most_order_bycity = df.groupby('City')["Order_ID"].count()

most_order_customer_type  = df.groupby('Customer_Type')["Order_ID"].count()

most_order_payment_type  = df.groupby('Payment')["Order_ID"].count()

sales_by_discount = df.groupby("Discount")["Final_sales"].sum()

orders_by_discount = df.groupby("Discount").size()

avg_sales_by_discount = df.groupby("Discount")["Final_sales"].mean()



product_sales = Total_product_sales.sort_values(ascending=False)

payment_sales = Total_sales_by_payment.sort_values(ascending=False)

city_sales = Total_sales_by_city.sort_values(ascending=False)

customer_type_sales = Total_sales_by_customer_type.sort_values(ascending=False)




'''plt.bar(
Total_sales_by_city.index,Total_sales_by_city.values)

plt.xlabel("City")
plt.ylabel("Final Sales (₹)")
plt.title("City Type Sales Bar")
plt.xticks(rotation=45)
plt.ticklabel_format(style="plain", axis="y")
#plt.savefig("Product Total Sales barchart")
plt.tight_layout()
plt.savefig("City total sales barchart")
plt.show()'''


print(Total_product_sales.idxmax())
print(Total_sales_by_city.idxmax())
print(Total_sales_by_customer_type.idxmax())
print(Total_sales_by_payment.idxmax())
print("-" * 25)
print(df.isna().sum())
print(df["Gros_sales"].sum())

print(df["Discount_Values"] .sum())

print(df["Final_sales"].sum()) 
print(df["Final_sales"].mean()) 
print(df['Quantity'].sum())
