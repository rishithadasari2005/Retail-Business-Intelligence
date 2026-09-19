import pandas as pd

df = pd.read_csv("data/raw/retail_sales.csv", parse_dates=["order_date"])

df["profit_margin"] = df["profit"] / df["revenue"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

print("\n=== Overall KPIs ===")
print("Revenue:", round(df["revenue"].sum(), 2))
print("Profit:", round(df["profit"].sum(), 2))
print("Margin:", round(df["profit"].sum()/df["revenue"].sum()*100, 2), "%")
print("Orders:", df["order_id"].nunique())
print("Units:", df["quantity"].sum())

print("\n=== Regional Performance ===")
print(df.groupby("region")[["revenue","profit","quantity"]].sum()
      .sort_values("profit", ascending=False))

print("\n=== Category Performance ===")
print(df.groupby("category")[["revenue","profit","quantity"]].sum()
      .sort_values("profit", ascending=False))

print("\n=== Monthly Performance ===")
print(df.groupby("month")[["revenue","profit"]].sum())

print("\n=== Discount Analysis ===")
print(df.groupby("discount")[["revenue","profit"]].mean()
      .sort_index())
