import streamlit as st
import plotly.express as px
import pandas as pd
import uuid

def display(df: pd.DataFrame):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    models = df["model_name"].unique()

    for model in models:
        model_df = df[df["model_name"] == model]
        fig = px.line(
            model_df,
            x="timestamp",
            y="karma_score",
            title=f"{model} Karma Trend",
            markers=True,
        )
        unique_key = f"trend_{model}_{uuid.uuid4()}"  # 🎯 Unique key using uuid
        st.plotly_chart(fig, use_container_width=True, key=unique_key)

