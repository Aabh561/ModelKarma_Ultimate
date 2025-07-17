import streamlit as st
import pandas as pd
from llm_commentator.karma_commentary_generator import generate_commentary
from recovery_engine.auto_retrain_suggester import AutoRetrainSuggester
from notifiers.telegram_notifier import send_telegram_alert

def display(df: pd.DataFrame):
    latest = df.sort_values("timestamp").groupby("model_name").tail(1)

    for _, row in latest.iterrows():
        karma = row["karma_score"]
        model = row["model_name"]

        # 🎯 Determine status
        if karma > 0.9:
            status, color = "🔥 Excellent", "green"
        elif karma > 0.75:
            status, color = "🟡 Moderate", "orange"
        else:
            status, color = "❗ Needs Attention", "red"
            send_telegram_alert(f"⚠️ Model '{model}' has low Karma Score: {karma}")

        # 🧠 LLM Commentary
        commentary = generate_commentary(karma - 0.05, karma, model, "recent metric shifts")

        # 🔁 Auto-Retrain Suggestion
        suggester = AutoRetrainSuggester()
        scores = df[df["model_name"] == model]["karma_score"].tolist()
        retrain_needed, advice = suggester.should_retrain(scores, days_since_retrain=18)

        if retrain_needed:
            send_telegram_alert(f"🔁 Retraining triggered for '{model}': {advice}")
        else:
            advice = "No retraining needed at this time."

        # 🧱 UI Container
        with st.container():
            st.markdown(
                f"""
                <div style="border-left: 6px solid {color}; padding: 10px 16px; margin-bottom: 14px; background-color: #fdfdfd; border-radius: 10px;">
                    <h4 style="margin: 0;">🧠 {model}</h4>
                    <p style="margin: 0;">Karma Score: <b>{karma}</b></p>
                    <p style="margin: 0;">Status: <span style="color: {color}; font-weight: bold;">{status}</span></p>
                    <p style="margin: 4px 0 0; font-style: italic; color: #333;">💬 <b>LLM Insight:</b> {commentary}</p>
                    <p style="margin: 4px 0 0; color: #333;">🔁 <b>Recovery Suggestion:</b> {advice}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

