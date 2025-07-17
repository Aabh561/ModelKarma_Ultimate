import streamlit as st
import pandas as pd
from dashboard.components import ranking_table
from dashboard.components import model_cards
from dashboard.utils.fetch_scores import fetch_latest_scores
from dashboard.components import trend_graphs


st.set_page_config(page_title="ModelKarma Dashboard", layout="wide")

st.title("📊 ModelKarma Scoreboard")

data = fetch_latest_scores()
col1, col2 = st.columns([2, 3])

with col1:
    model_cards.display(data)

with col2:
    trend_graphs.display(data)


trend_graphs.display(data)


st.markdown("### 🔍 Raw Karma Data")
st.dataframe(data)
st.markdown("## 📈 Model Karma Rankings")
ranking_table.display(data)


