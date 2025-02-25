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
import base64

# Page Configuration
st.set_page_config(
    page_title="About the CCS Regulatory Dashboard",
    layout="wide",
    page_icon="🌍",
    initial_sidebar_state="expanded"
)

# Get the current date
current_date = datetime.date.today().strftime('%B %d, %Y')

# Use HTML to simulate adding the date next to the top-right "Deploy" button
st.markdown(
    f"""
    <style>
        .top-bar-date {{
            position: absolute;
            top: 10px; /* Adjust for proper vertical alignment */
            right: 50px; /* Reduce spacing for smaller screens */
            font-size: 14px; /* Slightly smaller font for better fit */
            color: #666; /* Subtle gray color */
            z-index: 1000; /* Ensure it appears above other elements */
        }}
        /* Compatibility for Streamlit's top navigation bar */
        .css-1v3fvcr {{
            display: flex;
            justify-content: flex-end;
            align-items: center;
        }}
    </style>
    <div class="top-bar-date">📅 {current_date}</div>
    """,
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.markdown(f"📅 **Up to date:** {current_date}")

# Main Page Title
st.markdown("""
    <h1 style='text-align: center; color: #28a745;'>🌍 Carbon Compass  </h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>Navigate the world of CCS regulations with ease.</p>
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

def feature_button(image_path, title, description, page_name=None):
    """
    Displays a feature button with a local image, title, description, and optional navigation functionality.

    :param image_path: Path to the local image.
    :param title: Title of the feature.
    :param description: Description of the feature.
    :param page_name: Name of the page to navigate to (optional). If None, no navigation occurs.
    """
    # Convert the image to a base64 string
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    # Create the button with navigation if `page_name` is provided
    onclick_action = f"window.location.href='/{page_name.replace(' ', '_')}'" if page_name else ""

    # Render the button
    st.markdown(
        f"""
        <div onclick="{onclick_action}" 
             style="cursor: pointer; background-color: #f8f9fa; border: none; text-align: left; 
                    display: flex; align-items: center; padding: 10px; border-radius: 8px; 
                    width: 100%; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <img src="data:image/png;base64,{encoded_image}" alt="{title}" 
                 style="width: 40px; height: 40px; margin-right: 10px;">
            <div>
                <span style="font-size: 16px; color: #333;"><b>{title}</b></span><br>
                <span style="font-size: 14px; color: #666;">{description}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add navigation only if page_name is provided
    if page_name:
        if st.button(f"Go to {title}"):
            nav_page(page_name)


# Column 1 Buttons
with col1:
    # Regulatory Database button without navigation
    feature_button(
        "/Users/nikhil/Desktop/CCS_Dashboard/frontend/images/regulatory_database.jpg",
        "📌 Regulatory Database",
        "Browse CCS policies worldwide.",
        "Regulatory_Database"
    )
    # Other buttons with navigation
    feature_button(
        "/Users/nikhil/Desktop/CCS_Dashboard/frontend/images/comparison_tool.jpg",
        "📊 Comparison Tool",
        "Analyze differences in CCS regulations.",
        "Comparison_Tool"
    )
    feature_button(
        "/Users/nikhil/Desktop/CCS_Dashboard/frontend/images/daily_news.jpg",
        "📰 Daily News",
        "Stay updated with the latest regulatory changes.",
        "Daily_News"
    )

# Column 2 Buttons
with col2:
    feature_button(
        "/Users/nikhil/Desktop/CCS_Dashboard/frontend/images/ai_chatbot.jpg",
        "🤖 AI Chatbot",
        "Get instant answers to regulatory queries.",
        "AI_Chatbot"
    )
    feature_button(
        "/Users/nikhil/Desktop/CCS_Dashboard/frontend/images/compliance_score.jpg",
        "📈 Compliance Score",
        "Track CCS policy compliance measures.",
        "Compliance_Score"
    )
    feature_button(
        "/Users/nikhil/Desktop/CCS_Dashboard/frontend/images/policy_advisor.jpg",
        "📑 Policy Advisor",
        "Understand key compliance requirements.",
        "Policy_Advisor"
    )

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
