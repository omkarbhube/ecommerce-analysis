import pandas as pd

# LOAD DATA
df = pd.read_csv("online_retail.csv")

#FEATURE ENGINEERING 
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

#REVENUE OVERVIEW
print("\n----- REVENUE OVERVIEW -----")

# Total Revenue
print("Total Revenue Generated:", df["Revenue"].sum())

# Total Orders
print("Total Number of Orders Placed:", df["InvoiceNo"].nunique())

#COUNTRY ANALYSIS 
print("\n----- COUNTRY ANALYSIS -----")

print("Top 5 Countries by Revenue:")
print(df.groupby("Country")["Revenue"].sum().nlargest(5))

# PRODUCT ANALYSIS
print("\n----- PRODUCT ANALYSIS -----")

# Remove non-product entries
df_products = df[~df["Description"].str.contains("POSTAGE", case=False, na=False)]

print("Top 5 Products by Revenue:")
top_products = df_products.groupby("Description")["Revenue"].sum().nlargest(5)
print(top_products)

print("\nInsight:")
print("Revenue appears to be distributed across multiple products rather than dominated by a single item.")

# TIME ANALYSIS 
print("\n----- TIME ANALYSIS -----")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = df.groupby("Month")["Revenue"].sum().sort_index()
print(monthly_revenue)

print("\nInsight:")
print("Revenue shows an increase towards the later months of the year, suggesting possible seasonal demand.")

#CUSTOMER ANALYSIS 
print("\n----- CUSTOMER ANALYSIS -----")

# Dropping Null Customer IDs
df_customers = df.dropna(subset=["CustomerID"])

print("Top 5 Customers by Revenue:")
print(df_customers.groupby("CustomerID")["Revenue"].sum().nlargest(5))