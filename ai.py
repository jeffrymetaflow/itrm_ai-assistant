import streamlit as st
import openai
from intent_classifier import classify_intent

st.set_page_config(page_title="ITRM AI Assistant", layout="wide")
st.title("\U0001F916 ITRM Conversational AI Assistant")

# --- Placeholder Simulated State (would be tied to real modules later) ---
session_state = {
    "Hardware": 320000,
    "Software": 280000,
    "Personnel": 500000,
    "Maintenance": 160000,
    "Telecom": 120000,
    "Cybersecurity": 220000,
    "BC/DR": 140000,
    "Revenue": 100_000_000
}

# --- Simple Prompt-to-Action Map ---
intent_map = {
    "adjust": "adjust_category_forecast",
    "increase": "adjust_category_forecast",
    "decrease": "adjust_category_forecast",
    "what": "report_summary",
    "show": "report_summary",
    "recommend": "recommend_action",
    "risk": "show_risk_insight",
    "margin": "optimize_margin"
}

def classify_intent(prompt):
    for keyword in intent_map:
        if keyword in prompt.lower():
            return intent_map[keyword]
    return "unknown"

# --- Sample Simulated Actions ---
def adjust_category_forecast(prompt):
    for cat in session_state:
        if cat.lower() in prompt.lower():
            if "increase" in prompt:
                session_state[cat] *= 1.10
                return f"Increased {cat} budget by 10%. New value: ${session_state[cat]:,.0f}"
            elif "decrease" in prompt:
                session_state[cat] *= 0.90
                return f"Decreased {cat} budget by 10%. New value: ${session_state[cat]:,.0f}"
    return "Which category would you like to adjust?"

def report_summary(prompt):
    total_spend = sum([v for k, v in session_state.items() if k != "Revenue"])
    ratio = total_spend / session_state["Revenue"] * 100
    return f"Total IT Spend: ${total_spend:,.0f}\nIT-to-Revenue Ratio: {ratio:.2f}%"

def recommend_action(prompt):
    return "You could reduce Telecom and Maintenance by 15% to save money without significantly increasing risk."

def show_risk_insight(prompt):
    return "Cybersecurity and BC/DR protect 43% of revenue with a combined ROPR of 5.3x."

def optimize_margin(prompt):
    return "To improve margin by 2%, consider reducing Personnel and Maintenance by 5% each."

# --- Prompt Input ---
st.subheader("\U0001F4AC Ask me anything about your IT strategy")
user_prompt = st.text_input("Type your question or command:", "What is my current IT spend?")

if st.button("Submit"):
    action = classify_intent(user_prompt)
    if action == "adjust_category_forecast":
        response = adjust_category_forecast(user_prompt)
    elif action == "report_summary":
        response = report_summary(user_prompt)
    elif action == "recommend_action":
        response = recommend_action(user_prompt)
    elif action == "show_risk_insight":
        response = show_risk_insight(user_prompt)
    elif action == "optimize_margin":
        response = optimize_margin(user_prompt)
    else:
        response = "I'm not sure how to help with that yet, but I'm learning!"

    st.success(response)



# --- Debug Info (optional) ---
with st.expander("\U0001F527 Simulated Data State"):
    st.write(session_state)
