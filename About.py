import datetime
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="About the CCS Regulatory Dashboard",
    layout="wide",
    page_icon="🌍",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown(f"📅 **Up to date:** {datetime.date.today().strftime('%B %d, %Y')}")


# Main Page Title
st.markdown("""
    <h1 style='text-align: center; color: #28a745;'>🌍 CCS Regulatory Compliance System  </h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>Your go-to platform for tracking, analyzing, and comparing CCS regulations globally.</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Why This Tool?
st.markdown("## 🎯 Why This Tool?")
st.info("CCS regulations are constantly evolving, making it crucial to stay updated. However, navigating complex regulatory frameworks daily can be overwhelming. That's why we built this tool—providing you with **comparative analysis across multiple parameters and regions** while also offering **insights and guidance** to support your next CCS project.")

st.markdown("---")

# 2️⃣ Key Features
st.markdown("## 🚀 Key Features")
col1, col2 = st.columns(2)

with col1:
    st.success("📌 **Regulatory Database** – Browse CCS policies worldwide.")
    st.success("📊 **Comparison Tool** – Analyze differences in CCS regulations.")
    st.success("📑 **Policy Summaries** – Understand key compliance requirements.")

with col2:
    st.success("🤖 **AI Chatbot** – Get instant answers to regulatory queries.")
    st.success("📈 **Analytics & Insights** – Track CCS policy trends.")
    st.success("📰 **Daily News Scraping** – Stay updated with the latest regulatory changes.")

st.markdown("---")

# 3️⃣ Daily News Scraping
st.markdown("## 📰 Stay Informed with Daily News Updates")
st.markdown("""
Our **automated news scraping system** collects and organizes the latest news on:
- 🌍 **Global CCS regulations and policies**  
- 🔬 **Scientific advancements in carbon capture**  
- 💰 **Investments, funding, and market trends**  
- 🌱 **Sustainability & climate-related policies**  

📢 **Check our News & Updates section** for real-time regulatory developments!
""")

st.markdown("---")

# 4️⃣ How It Works
st.markdown("## ⚙️ How It Works")
st.markdown("""
Our dashboard provides **clear, data-driven insights** into CCS regulations using the following tools:

1️⃣ **Explore** regional policies in our **Regulatory Database**.  
2️⃣ **Compare** regulations using our **Comparison Tool**.  
3️⃣ **Ask** the **AI Chatbot** for instant compliance answers.  
4️⃣ **Analyze** trends with our **Analytics & Insights Dashboard**.  
5️⃣ **Stay Updated** with daily news scraping on CCS & climate regulations.  
""")



# Footer
st.markdown("---")
