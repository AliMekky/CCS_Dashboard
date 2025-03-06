import streamlit as st
import json
import openai
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# Load API Key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set Page Configuration
st.set_page_config(
    page_title="AI Chatbot - CCS Regulatory Compliance",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Sidebar - Date and Navigation
st.sidebar.markdown(f"📅 **Up to date:** {datetime.today().strftime('%B %d, %Y')}")

# Page Title & Introduction
st.markdown("<h1 style='text-align: center; color: #28a745;'>🤖 AI Chatbot - CCS Regulatory Compliance</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Analyze how different regions perform across various regulatory parameters.</p>", unsafe_allow_html=True)

st.markdown("---")

# Load JSON Data
try:
    with open("./10_PARAMS_BY_REGION_LINKS.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    st.error("Error: Data file not found. Please check the file path.")
    st.stop()




# 💬 AI Chat Section
st.markdown("## 💬 Ask AI About CCS Regulations")
user_query = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if user_query:
        question_prompt = f"""
        Using the provided CCS policy data and analysis, answer the following user question:
        **{user_query}**
        Provide a **concise and accurate response** backed by data found in {data}
        Back your responses with sources. Do not reply if you're not sure. Be straight to the point and provide high quality answers.
        When you are providing sources, give the links. Do not reply with irrelevant information, and be straight to the point while providing
        details.
        """

        with st.spinner("Generating response..."):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert in CCS regulations and compliance policies."},
                    {"role": "user", "content": question_prompt}
                ],
                temperature=0.2
            )

        user_response = response.choices[0].message.content.strip()
        st.markdown(f"### 🤖 AI Response")
        st.success(user_response)

st.markdown("---")


