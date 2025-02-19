import streamlit as st
import json
from streamlit_card import card

st.set_page_config(page_title="Compare by Country - CCS Dashboard", layout="wide")

st.title("🌎 Compare Carbon Capture by Country")
st.write("View country-wise trends in carbon capture and storage.")

# Load JSON data
with open("../10_PARAMS_BY_REGION_LINKS.json", "r") as file:
    data = json.load(file)

# Unique issues extraction
unique_countries = {entry['region'] for entry in data}
options = list(unique_countries)

# Country selection
st.sidebar.subheader("📌 Select Country")
selected_options = st.sidebar.multiselect("Choose countries to display:", options)

st.divider()

if selected_options:
    st.subheader("📝 Selected Issues & Action Points")

    grouped_cards = {option: [] for option in selected_options}

    for option in selected_options:
        for entry in data:
            if entry["region"] == option:
                for issue in entry["issues"]:
                    grouped_cards[option].append((issue["issue"], issue["action_point"], issue["link"]))

    for issue_name, cards in grouped_cards.items():
        st.markdown(f"### {issue_name}")

        num_cols = min(len(cards), 3)
        cols = st.columns(num_cols)

        for idx, (region, action_name, link) in enumerate(cards):
            with cols[idx % num_cols]:
                card(
                    title=region,
                    text=action_name,
                    url=link,
                    styles={
                        "card": {
                            "width": "350px",
                            "height": "200px",
                            "border-radius": "10px",
                            "background-color": "#2c3e50",
                            "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.2)",
                        },
                        "title": {"font-size": "16px", "color": "white"},
                        "text": {"font-size": "12px", "color": "white"},
                    }
                )
else:
    st.info("No countries selected. Please choose from the sidebar.")
