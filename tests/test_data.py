import pandas as pd

def test_required_columns():
    df = pd.read_csv("data/raw/retail_sales.csv")
    required = {
        "order_id","order_date","customer_id","region","customer_segment",
        "product_id","product_name","category","quantity","discount",
        "revenue","cost","profit"
    }
    assert required.issubset(df.columns)

def test_profit_logic():
    df = pd.read_csv("data/raw/retail_sales.csv")
    assert ((df["revenue"] - df["cost"] - df["profit"]).abs() < 0.01).all()
