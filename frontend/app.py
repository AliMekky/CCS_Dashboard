import openai
import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import json
from streamlit_card import card

# Set page configuration
st.set_page_config(page_title="Carbon Capture Dashboard", layout="wide", page_icon="🌍")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "Compare by Parameter", "Compare by Country"])

# Title
st.title("🌍 Carbon Capture and Storage Dashboard")
st.markdown("#### Track and visualize carbon capture initiatives worldwide.")

# Load JSON data
with open("../10_PARAMS_BY_REGION_LINKS.json", "r") as file:
    data = json.load(file)


if page == "Compare by Parameter":
    
    # Unique issues extraction
    unique_issues = {issue["issue"] for entry in data for issue in entry["issues"]}
    options = list(unique_issues)
    # Issue selection
    st.sidebar.subheader("📌 Select Issues")
    selected_options = st.sidebar.multiselect("Choose issues to display:", options)

    st.divider()  # Adds a visual separator

    # Geospatial Visualization Section
    st.subheader("🗺️ Geospatial Visualization")

    # Define geospatial data
    map_data = {
        "City A": (-74.006, 40.7128, "red"),
        "City B": (2.3522, 48.8566, "blue"),
        "City C": (139.6917, 35.6895, "green")
    }

    geo_df = gpd.GeoDataFrame(
        {"name": list(map_data.keys()), "lon": [x[0] for x in map_data.values()], "lat": [x[1] for x in map_data.values()]},
        geometry=gpd.points_from_xy([x[0] for x in map_data.values()], [x[1] for x in map_data.values()]),
        crs="EPSG:4326"
    )

    # Create a map
    fig_map = px.scatter_mapbox(
        geo_df,
        lat="lat",
        lon="lon",
        hover_name="name",
        zoom=1,
        color_discrete_sequence=["red", "blue", "green"]
    )

    fig_map.update_layout(mapbox_style="carto-positron", margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st.plotly_chart(fig_map, use_container_width=True)

    st.divider()

    # Display Selected Issues with Cards
    if selected_options:
        st.subheader("📝 Selected Issues & Action Points")
        
        grouped_cards = {option: [] for option in selected_options}
        
        for option in selected_options:
            for entry in data:
                for issue in entry["issues"]:
                    if issue["issue"] == option:
                        grouped_cards[option].append((entry["region"], issue["action_point"], issue["link"]))

        for issue_name, cards in grouped_cards.items():
            st.markdown(f"### {issue_name}")  # Display issue name as a heading
            
            # Dynamically set number of columns
            num_cols = min(len(cards), 3)
            cols = st.columns(num_cols)

            for idx, (region, action_name, link) in enumerate(cards):
                with cols[idx % num_cols]:  
                    card(
                        title=region,
                        text=action_name,
                        url="",
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
        st.info("No issues selected. Please choose from the sidebar.")

if page == "Compare by Country":
    # Unique issues extraction
    unique_issues = {entry['region'] for entry in data}
    options = list(unique_issues)

    # Country selection
    st.sidebar.subheader("📌 Select Country")
    selected_options = st.sidebar.multiselect("Choose countries to display:", options)

    st.divider()
    # Display Selected Issues with Cards
    if selected_options:
        st.subheader("📝 Selected Issues & Action Points")
        
        grouped_cards = {option: [] for option in selected_options}
        
        for option in selected_options:
            for entry in data:
                if entry["region"] == option:
                    for issue in entry["issues"]:
                        grouped_cards[option].append((issue["issue"], issue["action_point"], issue["link"]))

        for issue_name, cards in grouped_cards.items():
            st.markdown(f"### {issue_name}")  # Display issue name as a heading
            
            # Dynamically set number of columns
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
        st.info("No issues selected. Please choose from the sidebar.")