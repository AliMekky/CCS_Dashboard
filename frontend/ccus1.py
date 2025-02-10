import openai
import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize the OpenAI API (replace 'your-api-key' with an actual key)
openai.api_key = "your-api-key"

def get_chatbot_response(user_input):
    """Get a response from the OpenAI chatbot."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Carbon capture data
data = {
    "Country": [
        "Western Australia", "Norway", "United Kingdom", "Indiana (United States)", "Texas (United States)",
        "Louisiana (United States)", "North Dakota (United States)", "Nebraska (United States)", "European Union",
        "Northern Ireland (United Kingdom)", "New Mexico (United States)", "Queensland (Australia)",
        "British Columbia (Canada)", "Alberta (Canada)"
    ],
    "Carbon Captured (MtCO2)": [50, 75, 100, 60, 80, 70, 40, 30, 120, 25, 35, 45, 55, 65],
    "Region": [
        "Oceania", "Europe", "Europe", "North America", "North America",
        "North America", "North America", "North America", "Europe",
        "Europe", "North America", "Oceania", "North America", "North America"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

region_issues = {
    "Western Australia": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Norway": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "United Kingdom": [
       {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Indiana (United States)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Texas (United States)": [
       {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Louisiana (United States)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "North Dakota (United States)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Nebraska (United States)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "European Union": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Northern Ireland (United Kingdom)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "New Mexico (United States)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Queensland (Australia)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "British Columbia (Canada)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    "Alberta (Canada)": [
        {"Parameter": "Long-term liability post-site closure", "regulation": "", "text": ""},
        {"Parameter": "Permitting and authorisation", "regulation": "Petroleum and Natural Gas Act", "text": ""},
        {"Parameter": "Financial assurances of long-term site stewardship", "regulation": "", "text": ""},
        {"Parameter": "Ownership of pore space", "regulation": "", "text": ""},
        {"Parameter": "Measurement, monitoring and verification (MMV) plans", "regulation": "", "text": ""},
        {"Parameter": "Environmental impact assessments", "regulation": "", "text": ""},
        {"Parameter": "Public engagement and consultation", "regulation": "", "text": ""},
        {"Parameter": "Operational liabilities and financial security", "regulation": "", "text": ""},
        {"Parameter": "Storage resource assessment", "regulation": "", "text": ""},
        {"Parameter": "Site closure process", "regulation": "", "text": ""}
    ],
    # Add other regions with their parameters as needed
}

# Streamlit app
st.set_page_config(page_title="Carbon Capture Dashboard", layout="wide", page_icon="🌍")
st.title("🌍 Carbon Control Dashboard with Chatbot")

# Sidebar chatbot section
st.sidebar.title("🤖 Chat with AI")
user_input = st.sidebar.text_area("Ask a question about carbon capture, policies, or regulations:")

if st.sidebar.button("Get Response") and user_input:
    with st.sidebar.spinner("Thinking..."):
        chatbot_response = get_chatbot_response(user_input)
    st.sidebar.markdown(f"**Chatbot Response:** {chatbot_response}")

# Dashboard Main Section
st.subheader("Country Performance 🌱")
cols = st.columns(4, gap="medium")
selected_country = None

for idx, row in df.iterrows():
    with cols[idx % 4]:  # Distribute tiles across columns
        if st.button(row["Country"]):  # Clicking a button selects a country
            selected_country = row["Country"]

# Check if a country is selected
if selected_country:
    st.markdown(f"### Details for {selected_country}")
    if selected_country in region_issues:
        issues_df = pd.DataFrame(region_issues[selected_country])
        st.dataframe(issues_df)
    else:
        st.write(f"No specific data available for {selected_country}.")

# Carbon capture visualization
st.subheader("📊 Carbon Capture Data Visualization")
fig = px.bar(df, x="Country", y="Carbon Captured (MtCO2)", color="Region",
             title="Carbon Captured by Country", labels={"Carbon Captured (MtCO2)": "Carbon Captured (MtCO2)"})
st.plotly_chart(fig, use_container_width=True)
