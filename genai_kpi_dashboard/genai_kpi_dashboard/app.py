
import streamlit as st
import pandas as pd
from kpi_utils import get_kpis
from forecast_utils import forecast_revenue
from genai_utils import ask_question, get_summary

st.title("📊pdf Smart KPI + GenAI Business Dashboard")
data = pd.read_csv("data/sales_data.csv")

# Filters
product = st.selectbox("Select Product", ["All"] + list(data["product"].unique()))

if product != "All":
    data = data[data["product"] == product]

# KPI Display
kpis = get_kpis(data)
st.metric("Revenue", f"₹{kpis['revenue']}")
st.metric("Orders", kpis['orders'])
st.metric("CAC", f"₹{kpis['cac']:.2f}")
st.metric("AOV", f"₹{kpis['aov']:.2f}")

# Forecasting
if st.button("📈 Forecast Revenue"):
    pred = forecast_revenue(data)
    st.success(f"Next month's projected revenue: ₹{pred:.2f}")

# GenAI Section
st.subheader("🤖 Ask your Data")
query = st.text_input("Your question")
if st.button("Ask") and query:
    response = ask_question(data, query)
    st.write(response)

# Summary
if st.button("📝 Get Summary"):
    summary = get_summary(data)
    st.info(summary)
