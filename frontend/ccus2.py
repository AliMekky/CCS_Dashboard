import streamlit as st
import pandas as pd
import plotly.express as px

# Carbon capture data (2024)
data = {
    "Country": [
        "Europe", "USA", "Canada", "Brazil", "Australia", "China", "Qatar", "Saudi Arabia", "Algeria", "Russia"
    ],
    "Carbon Captured (MtCO2)": [
        250, 220, 180, 150, 120, 100, 80, 60, 50, 30
    ],
    "Region": [
        "Europe", "North America", "North America", "South America", "Oceania", "Asia", "Middle East", "Middle East", "Africa", "Eurasia"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.set_page_config(page_title="Carbon Capture Dashboard", layout="wide", page_icon="🌍")
st.title("🌍 Carbon Control Regulations")

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stMarkdown h3 {
        color: #007bff;
    }
    .stProgress > div > div > div {
        background-color: #007bff;
    }
    .chatbot-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        background: #007bff;
        color: white;
        border: none;
        border-radius: 50%;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 30px;
        cursor: pointer;
        z-index: 1000;
    }
    .chatbot-container {
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 300px;
        max-height: 400px;
        background: white;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        padding: 10px;
        display: none;
        z-index: 1000;
        overflow-y: auto;
    }
    .chatbot-container.open {
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dashboard layout with dynamic country tiles
st.subheader("Country Performance 🌱")

# Dynamic tiles for countries with drop-down menus
cols = st.columns(4)  # 4 columns for the tiles
for idx, row in df.iterrows():
    with cols[idx % 4]:  # Distribute tiles across columns
        st.markdown(
            f"""
            <div style='text-align: center; border: 2px solid #007bff; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>
                <h3>{row['Country']}</h3>
                <p style='font-size: 24px;'>{row['Carbon Captured (MtCO2)']} MtCO2</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Drop-down menu for each country
        with st.expander(f"Parameters for {row['Country']}"):
            # Legal Framework Parameters
            st.markdown("**Legal Framework Parameters**")
            legal_framework = st.selectbox(
                "Select Legal Framework Parameter",
                ["Parameter 1", "Parameter 2", "Parameter 3"],
                key=f"legal_{row['Country']}"
            )

            # Regulatory Parameters
            st.markdown("**Regulatory Parameters**")
            regulatory = st.selectbox(
                "Select Regulatory Parameter",
                ["Parameter A", "Parameter B", "Parameter C"],
                key=f"regulatory_{row['Country']}"
            )

            # Health, Safety, and Environment (HSE) Parameters
            st.markdown("**Health, Safety, and Environment (HSE) Parameters**")
            hse = st.selectbox(
                "Select HSE Parameter",
                ["Parameter X", "Parameter Y", "Parameter Z"],
                key=f"hse_{row['Country']}"
            )

# Progress bar and match percentage
st.subheader("Progress 📊")
progress = st.progress(0.7)  # 70% match
st.markdown("<h4 style='text-align: center;'>70% match</h4>", unsafe_allow_html=True)

# Interactive Visualizations
st.subheader("Carbon Capture Insights 📈")

# Bar chart by region
st.markdown("**Carbon Capture by Region**")
fig = px.bar(df, x="Region", y="Carbon Captured (MtCO2)", color="Region", text="Carbon Captured (MtCO2)")
st.plotly_chart(fig, use_container_width=True)

# Pie chart for distribution
st.markdown("**Carbon Capture Distribution**")
fig = px.pie(df, values="Carbon Captured (MtCO2)", names="Region", hole=0.3)
st.plotly_chart(fig, use_container_width=True)

# Chatbot integration
st.subheader("Chatbot Assistant 🤖")

# Initialize session state for chatbot
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if 'chat_open' not in st.session_state:
    st.session_state['chat_open'] = False

# Toggle chat visibility
if st.button("💬 Open Chatbot", key="chat_toggle"):
    st.session_state['chat_open'] = not st.session_state['chat_open']

# Chatbot container
chat_container_class = "chatbot-container open" if st.session_state['chat_open'] else "chatbot-container"
st.markdown(f'<div class="{chat_container_class}">', unsafe_allow_html=True)

if st.session_state['chat_open']:
    st.markdown('<h4>Chatbot</h4>', unsafe_allow_html=True)
    user_input = st.text_input("Ask the chatbot:", key="chatbot_input")
    if user_input:
        if "highest" in user_input.lower():
            response = "Europe captures the most carbon in 2024, with 250 MtCO2."
        elif "lowest" in user_input.lower():
            response = "Russia captures the least carbon in 2024, with 30 MtCO2."
        elif "total" in user_input.lower():
            total_capture = df["Carbon Captured (MtCO2)"].sum()
            response = f"The total carbon captured in 2024 is {total_capture} MtCO2."
        elif any(region.lower() in user_input.lower() for region in df["Region"].unique()):
            region_query = [region for region in df["Region"].unique() if region.lower() in user_input.lower()]
            region_data = df[df["Region"].str.lower().isin([r.lower() for r in region_query])]
            response = f"In {region_query[0]}, the total carbon captured is {region_data['Carbon Captured (MtCO2)'].sum()} MtCO2."
        else:
            response = "I'm sorry, I couldn't understand your query. Please try asking about the highest, lowest, or total carbon capture."

        st.session_state['messages'].append({"user": user_input, "bot": response})

    for message_data in st.session_state['messages']:
        st.markdown(f"**You:** {message_data['user']}")
        st.markdown(f"**Bot:** {message_data['bot']}")
        st.markdown("---")

st.markdown('</div>', unsafe_allow_html=True)

# Floating chatbot button
st.markdown('<button class="chatbot-button">💬</button>', unsafe_allow_html=True)