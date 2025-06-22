
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def forecast_revenue(df):
    df["date"] = pd.to_datetime(df["date"])
    df = df.groupby("date")["revenue"].sum().reset_index()
    df["days"] = (df["date"] - df["date"].min()).dt.days
    X = df[["days"]]
    y = df["revenue"]
    model = LinearRegression().fit(X, y)
    future_day = df["days"].max() + 30
    return model.predict([[future_day]])[0]
