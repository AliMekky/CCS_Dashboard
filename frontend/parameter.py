# import openai
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_card import card
import json

st.set_page_config(
    page_title="Construction Graduation Project",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# By default the json file is usually in the directory before the frontend directory, change accordingly if needed
with open("../10_PARAMS_BY_REGION_LINKS.json", "r") as file:
    data = json.load(file)

# This set dynamcally gets all the unique issues from the json file, so whenever we add issues they get added to the dropdown
unique_issues = set()

for entry in data:
    for issue in entry["issues"]:
        unique_issues.add(issue["issue"]) 
options = list(unique_issues)

# Dropdown box to select issues
selected_options = st.multiselect("Choose one or more options:", options)
if selected_options:
    st.write("### Selected Issues:")
    
    # Group cards by issue name
    grouped_cards = {option: [] for option in selected_options}
    
    for option in selected_options:
        for entry in data:
            for issue in entry["issues"]:
                if issue["issue"] == option:

                    # Added the entries to the grouped cards to be displayed, if we need anything else just add it here to be able to display it the card
                    grouped_cards[option].append((entry["region"], issue["issue"], issue["action_point"]))

    # Display grouped cards
    for issue_name, cards in grouped_cards.items():
        st.write(f"**{issue_name}**")  # Display issue name as a heading
        
        # Define number of columns (max 3 per row) for the sake of good UI
        num_cols = min(len(cards), 3)
        cols = st.columns(num_cols)

        for idx, (region, issue, action_name) in enumerate(cards):

            # This places the card in the appropriate column
            with cols[idx % num_cols]:  
                card(
                    title=region,
                    text= action_name,
                    url="",
                    styles={
                        "card": {
                            "width": "375px",  # Set width
                            "height": "375px",  # Set height,
                            "background-color": "#808080",  # Dark background
                        },
                        "title": {
                            "font-size": "18px",  # Smaller title text
                            "color": "white"
                        },
                        "text": {
                            "font-size": "10px",  # Customize text size
                            "color": "white"
                        }
                    }
                )
else:
    st.write("No options selected.")