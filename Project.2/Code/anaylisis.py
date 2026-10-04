import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Project.2/Data/ecommerce_customer_analysis.csv")

most_order_product = df.groupby("Product")["Quantity"].sum()


'''most_order_product.plot(kind='bar',color='red')
plt.xlabel("Product Name")
plt.ylabel('PRoduct sales quantity')
plt.title('Product sales quntity by product')
plt.savefig("Product sales quntity by product")
plt.show()'''

most_order_bycity = df.groupby('City')["Order_ID"].count()

most_order_customer_type  = df.groupby('Customer_Type')["Order_ID"].count()

most_order_payment_type  = df.groupby('Payment')["Order_ID"].count()

high_avrage_quantity_producs  = df.groupby('Product')["Quantity"].mean()

highest_unitprice_pruducts = df.groupby("Product")['Unit_Price'].mean()


df["Gros_sales"]= df['Quantity'] * df['Unit_Price']

df["Discount_Values"] = df["Gros_sales"] * df["Discount"] / 100

df["Final_sales"] = df['Gros_sales'] - df["Discount_Values"]


Total_product_sales = df.groupby('Product')['Final_sales'].sum()

Total_sales_by_city = df.groupby('City')['Final_sales'].sum()

Total_sales_by_payment = df.groupby('Payment')['Final_sales'].sum()

Total_sales_by_category = df.groupby('Category')['Final_sales'].sum()

Total_sales_by_customer_type = df.groupby('Customer_Type')['Final_sales'].sum()


'''print(Total_product_sales.sort_values(ascending=False))
print(Total_sales_by_city.sort_values(ascending=False))
print(Total_sales_by_payment .sort_values(ascending=False))
print(Total_sales_by_category.sort_values(ascending=False))
print(Total_sales_by_customer_type.sort_values(ascending=False))'''


pivot_city_product = pd.pivot_table(
    df,
    values="Final_sales",
    index="City",
    columns="Product",
    aggfunc="sum"
)

sales_by_discount = df.groupby("Discount")["Final_sales"].sum()

orders_by_discount = df.groupby("Discount").size()

avg_sales_by_discount = df.groupby("Discount")["Final_sales"].mean()



product_sales = Total_product_sales.sort_values(ascending=False)

payment_sales = Total_sales_by_payment.sort_values(ascending=False)

city_sales = Total_sales_by_city.sort_values(ascending=False)

customer_type_sales = Total_sales_by_customer_type.sort_values(ascending=False)

category_sales = Total_sales_by_category.sort_values(ascending=False)


print(df["Quantity"].sum())