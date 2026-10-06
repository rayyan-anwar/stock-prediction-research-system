import streamlit as st
import pandas as pd
from backend.app.model import forecast
st.set_page_config(page_title="Rayyan Anwar | Stock Research",layout="wide")
st.title("Stock Prediction Research System")
st.caption("Research project by Rayyan Anwar — AI/ML Research · Engineering · Technology Management")
f=st.file_uploader("Upload CSV containing close and volume",type=["csv"])
if f:
    df=pd.read_csv(f); st.dataframe(df.tail(20),use_container_width=True)
    if {"close","volume"}.issubset(df.columns):
        try:
            pred,d=forecast(df[["close","volume"]].dropna().values.tolist())
            a,b=st.columns(2); a.metric("Next-price estimate",f"{pred:.4f}"); b.metric("Direction",d)
            st.info("Research estimate only — not financial advice.")
        except ValueError as e: st.error(str(e))
    else: st.error("CSV must contain close and volume columns.")
