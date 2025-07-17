import requests

def generate_commentary(old_score, new_score, model_name, trigger_reason):
    prompt = f"""
You are an ML Ops analyst.

A model named '{model_name}' had a karma score change from {old_score} to {new_score}.
This was due to: {trigger_reason}.

Generate a short professional, insightful commentary (2–3 lines) explaining what this change implies and how to address it.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=10
        )
        content = response.json()
        return content.get("response", "🤖 Commentary unavailable.")
    except Exception as e:
        return f"❌ LLM failed: {str(e)}"
