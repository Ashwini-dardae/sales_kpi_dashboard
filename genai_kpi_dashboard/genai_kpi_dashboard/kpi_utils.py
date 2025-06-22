
import pandas as pd

def get_kpis(df):
    revenue = df["revenue"].sum()
    orders = df["orders"].sum()
    customers = df["customers"].sum()
    ad_spend = df["ad_spend"].sum()
    cac = ad_spend / customers if customers else 0
    aov = revenue / orders if orders else 0
    return {
        "revenue": int(revenue),
        "orders": int(orders),
        "cac": cac,
        "aov": aov,
    }
