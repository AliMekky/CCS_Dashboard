import streamlit as st
import json
import plotly.express as px
import geopandas as gpd
from streamlit_card import card
import openai 
import os 
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Compare by Parameter Summaries - CCS Dashboard", layout="wide")
current_date = datetime.today().strftime("%B %d, %Y")  # Format: "Month Day, Year"
st.sidebar.markdown(f"📅 **Up to date:** {datetime.today().strftime('%B %d, %Y')}")

# Display Title and Date
st.markdown("<h1 style='text-align: center; color: #28a745;'>📊 Compare CCS by Parameter</h1>", unsafe_allow_html=True)

# st.title("📊 Compare CCS by Parameter")
# st.write(f"Analyze how different regions perform across various parameters as per  📅 **Date:** {current_date}")
st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Learn how to interpret the output from the comparative analysis of CCS regulations.</p>", unsafe_allow_html=True)


# Section 1 - Comparative Analysis
with st.expander("🔍 **1️⃣ Comparative Analysis - How Different Regions Regulate CCS**"):
    st.markdown("""
    This section compares **CCS action points and compliance challenges** across different regions.  
    - **What you’ll see:**  
        - ✅ **Similarities** in policies across multiple countries.  
        - 🔄 **Differences** in compliance strategies and policy enforcement.  
        - ⚠️ **Challenges** faced by different regions.  

    💡 **Example Output:**  
    > **Region A vs. Region B:** Both enforce mandatory CO₂ reporting, but **Region A** has stricter penalties for non-compliance.  
    > **Region C vs. Region D:** **Region C** provides **financial incentives**, whereas **Region D** relies on **carbon pricing mechanisms**.

    ✅ **How to use it?**  
    - Identify **best practices** and gaps in CCS policies across regions.  
    - Learn what regulations **work well in specific economic or environmental conditions**.  
    """)


# Section 2 - Clustering Analysis
with st.expander("🔗 **2️⃣ Clustering Analysis - Grouping Regions with Shared Policies**"):
    st.markdown("""
    This section **groups regions** based on **common regulatory characteristics**, such as:  
    - 🌍 **Economic status** (developed vs. developing countries).  
    - 🏛 **Policy structure** (strict vs. flexible enforcement).  
    - ⚡ **CCS strategies** (government-driven vs. private-sector-led).  

    💡 **Example Output:**  
    > **Cluster 1 (Developed Nations):** Countries with **advanced monitoring systems, strong incentives, and clear carbon storage policies**.  
    > **Cluster 2 (Emerging Markets):** Countries **heavily reliant on international funding, with evolving regulatory structures**.

    ✅ **How to use it?**  
    - Compare how **similar countries regulate CCS differently**.  
    - Identify **trends in CCS adoption** within each group.  
    """)


# Section 3 - Regulatory Compliance Rating
with st.expander("📊 **3️⃣ Regulatory Compliance Rating - How Easy It Is to Follow Regulations**"):
    st.markdown("""
    This section assigns a **rating (1-10) for each region**, measuring how easy it is to comply with CCS regulations.  
    It also provides a **match ratio (%)** showing alignment with **international CCS standards**.  

    💡 **Example Output:**  
    | Region        | Compliance Rating (1-10) | Match Ratio (%) |  
    |--------------|-------------------------|----------------|  
    | Region A     | 9/10                     | 95%            |  
    | Region B     | 6/10                     | 70%            |  
    | Region C     | 4/10                     | 50%            |  

    ✅ **How to use it?**  
    - Compare regions based on **how well their policies align with global standards**.  
    - Identify which regions **offer a favorable regulatory environment** for CCS projects.  
    """)


# Section 4 - Regulatory Recommendations
with st.expander("📌 **4️⃣ Regulatory Recommendations - Key Takeaways for Future Policy Design**"):
    st.markdown("""
    This section provides **clear, actionable insights** on how to shape **effective CCS policies** based on global best practices.  
    - **What you’ll see:**  
        - 📌 **The most effective CCS regulations** from different regions.  
        - 🛠 **Key policy recommendations** based on comparative data.  
        - 🔗 **Actionable next steps** for developing your own CCS regulations.  

    💡 **Example Output:**  
    > **Storage & Infrastructure:** Develop a **centralized carbon storage registry** for better transparency.  
    > **Incentives & Carbon Pricing:** Implement **tax credits** for early adopters of CCS technology.  
    > **Monitoring & Compliance:** Require **annual CO₂ reporting** with **third-party verification**.  
    > **Cross-Border Collaboration:** Align regulations with **global carbon markets** to facilitate CCS trade.  

    ✅ **How to use it?**  
    - Use these insights to **enhance your own CCS regulations**.  
    - Align new policies with **proven international best practices**.  
    """)
# Data processing function to structure the table with transposed rows and columns
    def create_table(data):
        countries = []
        issues = set()
        issue_presence = {}
        
        for entry in data:
            country = entry["region"]
            countries.append(country)
            issue_presence[country] = {}
            
            for issue in entry["issues"]:
                issue_name = issue["issue"]
                issues.add(issue_name)
                issue_presence[country][issue_name] = "✅"
        
        issues = sorted(issues)
        table_data = {"Issue": issues}
        
        for country in countries:
            table_data[country] = [issue_presence[country].get(issue, "") for issue in issues]
        
        df = pd.DataFrame(table_data).set_index("Issue")
        
        # Sort countries by the number of issues they have in descending order
        sorted_countries = df.apply(lambda col: col.eq("✅").sum(), axis=0).sort_values(ascending=False).index.tolist()
        
        return df[sorted_countries]

with st.expander("📊 **Available Data**"):
    
    # Load JSON data
    with open("./10_PARAMS_BY_REGION_LINKS.json", "r") as file:
        data = json.load(file)

    # Create a DataFrame for the table
    df = create_table(data)

    # Streamlit UI
    st.markdown("""
        <style>
            .main {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # st.title("Global Regulation Tracker: Issues Acrosss Countries")

    # Center table
    st.markdown("<div style='display: flex; justify-content: center; width: 100%;'>", unsafe_allow_html=True)
    st.dataframe(df.style.set_table_styles(
        [{'selector': 'th', 'props': [('max-width', '250px')]},
        {'selector': 'td', 'props': [('max-width', '250px')]}]
    ), width=1500)
    st.markdown("</div>", unsafe_allow_html=True)

with open("./10_PARAMS_BY_REGION_LINKS.json", "r") as file:
    data = json.load(file)

cache_file = "responses_cache.json"
if os.path.exists(cache_file):
    with open(cache_file, "r") as file:
        try:
            cached_responses = json.load(file)
        except json.JSONDecodeError:
            cached_responses = {}
else:
    cached_responses = {}

unique_issues = {issue["issue"] for entry in data for issue in entry["issues"]}
options = list(unique_issues)

# Issue selection
st.sidebar.subheader("📌 Select Issues")
selected_options = st.sidebar.multiselect("Choose issues to display:", options)

# st.divider()
# # User Question Section
# st.subheader("💬 Ask AI About CCS Regulations")
# user_query = st.text_input("Enter your question:")
# if st.button("Ask AI"):
#     if user_query:
#         question_prompt = f"""
#         Using the provided CCS policy data and analysis, answer the following user question:
#         **{user_query}**
#         Provide a **concise and accurate response** backed by data found in {data}
#         Back your responses with sources. Do not reply if you're not sure. Be straight to the point and provide high quality answers.
#         When you are providing sources, give the links.
#         """

#         with st.spinner("Generating response..."):
#             response = client.chat.completions.create(
#                 model="gpt-4o",
#                 messages=[
#                     {"role": "system", "content": "You are an expert in CCS regulations."},
#                     {"role": "user", "content": question_prompt}
#                 ],
#                 temperature=0.2
#             )

#         user_response = response.choices[0].message.content.strip()
#         st.markdown(f"**AI Response:** {user_response}")
# st.divider()


# Display Selected Issues with Cards
if selected_options:
    st.subheader("📝 Selected Issues & Action Points")

    grouped_cards = {option: [] for option in selected_options}
    for option in selected_options:
        for entry in data:
            for issue in entry["issues"]:
                if issue["issue"] == option:
                    grouped_cards[option].append((entry["region"], issue["action_point"], issue['summary'], issue["link"]))

        combined_text = "\n\n".join([f"**Region: {region}**\n\nAction Point: {action_point}\n\nSummary: {text}\n\n[Link]({link})" for region, action_point, text, link in grouped_cards[option]])
        # Render as a big card
        # st.markdown(
        #     f"""
        #     <div style="
        #         padding: 15px; 
        #         background-color: #2c3e50; 
        #         color: white; 
        #         border-radius: 12px; 
        #         box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        #         font-size: 14px;">
        #         {option}\n
        #         {combined_text}
        #     </div>
        #     """, unsafe_allow_html=True
        # )
        
        if option in cached_responses:
            # st.subheader("📢 Cached AI-Generated Insights")
            st.subheader(f"**{option}**")
            st.markdown(cached_responses[option])
        else:
            st.header(f"**{option}**")
            prompt = f"""
                You are an expert in Carbon Capture and Storage (CCS) regulations. Analyze the provided regional data to identify key trends, compare policies, and assess compliance challenges. Since we are developing our **own CCS regulations**, provide insights on what we should consider.  

                    ### **🎯 Tasks:**  
                    1️⃣ **Comparative Analysis**  
                    - Compare CCS action points and issues across regions.  
                    - Highlight **similarities, differences, and major challenges**.  

                    2️⃣ **Clustering Analysis**  
                    - Group regions with **shared characteristics** (e.g., economic status, policies, CCS strategies).  
                    - Explain the **key factors** defining each cluster.  

                    3️⃣ **Regulatory Compliance Rating**  
                    - **Rate each region (1-10)** on how easy it is to comply with CCS regulations.  
                    - Provide a **match ratio (%)** indicating alignment with international CCS standards.  

                    4️⃣ **Regulatory Recommendations**  
                    - **Analyze the biggest cluster** and identify what works best.  
                    - Provide **clear, actionable recommendations** on what we should consider when designing our own CCS regulations.  

                    ---

                    ### **📌 Text Data Input:**  
                    {combined_text}  

                    ---

                    ### **📊 Output Format:**  

                    #### **🔍 Comparative Analysis**  
                    - **Region A vs. Region B** → (Key similarities & differences)  
                    - **Region C vs. Region D** → (Key similarities & differences)  

                    #### **🔗 Clustered Regions**  
                    - **Cluster 1:** [Region Names] → (Common characteristics)  
                    - **Cluster 2:** [Region Names] → (Common characteristics)  

                    #### **📊 Compliance Ratings**  
                    | Region        | Rating (1-10) | Match Ratio (%) |  
                    |--------------|--------------|----------------|  
                    | Region A     | X/10         | XX%            |  
                    | Region B     | X/10         | XX%            |  

                    #### **📌 Regulatory Recommendations**  
                    - Based on global best practices and identified trends, suggest key policies we should consider:  
                    - **Storage & Infrastructure**: [Best approaches]  
                    - **Incentives & Carbon Pricing**: [Policy options]  
                    - **Monitoring & Compliance**: [Effective strategies]  
                    - **Technology & Innovation**: [Research & development priorities]  
                    - **Cross-Border Collaboration**: [How to align with international frameworks]  

                    🔹 **Provide clear, structured, and actionable insights to help shape new CCS regulations.**  

                    """
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a legal compliance assistant for CCS regulations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            # Extracting the response
            res = response.choices[0].message.content.strip()
            st.header(res)
            cached_responses[option] = res
            with open(cache_file, "w") as file:
                json.dump(cached_responses, file, indent=4)

        if st.button("🔎 See More", key = option):
            st.subheader("🌍 All Country Information")
            st.markdown(combined_text)  # Display full country data when button is clicked
else:
    st.info("No issues selected. Please choose from the sidebar.")
