# import streamlit as st
# from streamlit.components.v1 import html
# import datetime

# # Set page config
# st.set_page_config(
#     page_title="CCS Regulatory Compliance Across the Globe", 
#     layout="wide", 
#     page_icon="🌍", 
#     initial_sidebar_state="expanded"
# )

# # Sidebar - Date and Navigation
# st.sidebar.markdown(f"📅 **Up to date:** {datetime.date.today().strftime('%B %d, %Y')}")
# st.sidebar.title("🔍 Explore More")
# st.sidebar.markdown("📌 **Navigate to:**")
# st.sidebar.button("📜 About")
# st.sidebar.button("📊 Dashboard")
# st.sidebar.button("🤖 AI Chatbot")
# st.sidebar.button("📰 News & Updates")
# # Main Page Title
# st.markdown("""
#     <h1 style='text-align: center; color: #28a745;'>🌍 CCS Regulatory Compliance System </h1>
#     <p style='text-align: center; font-size: 18px; color: #555;'>Your go-to platform for tracking, analyzing, and comparing CCS regulations globally.</p>
# """, unsafe_allow_html=True)
# # Custom CSS for Background and Styling

# st.markdown("---")

# # Why This Tool?
# st.markdown("## 🎯 Why This Tool?")
# st.info("CCS regulations are constantly evolving, making it crucial to stay updated. However, navigating complex regulatory frameworks daily can be overwhelming. That's why we built this tool—providing you with **comparative analysis across multiple parameters and regions** while also offering **insights and guidance** to support your next CCS project.")

# st.markdown("---")

# # Key Features Section
# st.markdown("## 🚀 Key Features")
# col1, col2 = st.columns(2)

# with col1:
#     st.success("📌 **Regulatory Database** – Browse CCS policies worldwide.")
#     st.success("📊 **Comparison Tool** – Analyze differences in CCS regulations.")
#     st.success("📑 **Policy Summaries** – Understand key compliance requirements.")

# with col2:
#     st.success("🤖 **AI Chatbot** – Get instant answers to regulatory queries.")
#     st.success("📈 **Analytics & Insights** – Track CCS policy trends.")
#     st.success("📰 **Daily News Scraping** – Stay updated with the latest regulatory changes.")

# st.markdown("---")
import datetime
import streamlit as st
from streamlit.components.v1 import html

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

def nav_page(page_name, timeout_secs=3):
    page_name_url = page_name.replace(' ', '_')
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elapsed = new Date() - start_time;
                if (elapsed < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name_url, timeout_secs)
    html(nav_script)

# 2️⃣ Key Features Section
st.markdown("## 🚀 Key Features")
col1, col2 = st.columns(2)

with col1:
    st.button("📌 **Regulatory Database** – Browse CCS policies worldwide.")
    if st.button("📊 **Comparison Tool** – Analyze differences in CCS regulations."):
        nav_page("Comparison_Tool")
    if st.button("📰 **Daily News** – Stay updated with the latest regulatory changes."):
        nav_page("Daily_News")

with col2:
    if st.button("🤖 **AI Chatbot** – Get instant answers to regulatory queries."):
        nav_page("AI_Chatbot")
    if st.button("📈 **Compliance Score** – Track CCS policy compliance measures."):
        nav_page("Compliance_Score")
    if st.button("📑 **Policy Advisor** – Understand key compliance requirements."):
        nav_page("Policy_Advisor")


st.markdown("---")

# 3️⃣ Daily News Scraping
st.markdown("## 📰 Stay Informed with Daily News Updates")
st.markdown("""
Our **automated news system** collects and organizes the latest news on:
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
5️⃣ **Stay Updated** with daily news on CCS & climate regulations.  
""")



# Footer
st.markdown("---")
