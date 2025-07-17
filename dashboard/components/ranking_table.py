import streamlit as st
import pandas as pd

def display(df: pd.DataFrame):
    latest = df.sort_values("timestamp").groupby("model_name").tail(1)
    sorted_df = latest.sort_values("karma_score", ascending=False).reset_index(drop=True)
    st.dataframe(sorted_df[["model_name", "karma_score", "timestamp"]], use_container_width=True)
