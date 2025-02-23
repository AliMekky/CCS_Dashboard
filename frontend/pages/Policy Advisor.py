from datetime import datetime
import streamlit as st
import json

# Load compliance advice from a JSON file
file_path = "./advice.json"
st.sidebar.markdown(f"📅 **Up to date:** {datetime.today().strftime('%B %d, %Y')}")

try:
    with open(file_path, "r") as file:
        model_advice_data = json.load(file)
except Exception as e:
    st.error(f"Error loading compliance advice file: {e}")
    model_advice_data = []

# Streamlit UI
st.markdown("<h1 style='text-align: center; color: #28a745;'>🔍 Policy Advisor</h1>", unsafe_allow_html=True)
st.image("./image.png")

# st.title("🔍 Compliance Advisor")
st.write("Select an LLM model to view compliance recommendations.")

# Dropdown to select LLM
selected_model = st.selectbox(
    "Choose the LLM Model:",
    [model["model_name"] for model in model_advice_data] if model_advice_data else []
)

# Retrieve and display compliance advice for the selected model
if selected_model:
    advice_text = next(
        (model["advice"] for model in model_advice_data if model["model_name"] == selected_model),
        "No advice available for this model."
    )

    # Display advice in a styled box
    st.markdown(
        f"""
        <div style="border: 2px solid #4CAF50; padding: 15px; border-radius: 10px; background-color: white;">
            {advice_text}
        </div>
        """,
        unsafe_allow_html=True
    )
