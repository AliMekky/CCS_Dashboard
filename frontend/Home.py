# import openai
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import geopandas as gpd
# import json
# from streamlit.components.v1 import html
# from streamlit_card import card

# # Set page configuration
# st.set_page_config(page_title="Carbon Capture Dashboard", layout="wide", page_icon="🌍", initial_sidebar_state="expanded")

# # Function to apply custom CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("styles.css")

# # Function for JavaScript-based page navigation
# def nav_page(page_name, timeout_secs=3):
#     page_name_url = page_name.lower().replace(' ', '_').capitalize()  # Ensure proper formatting
#     nav_script = f"""
#         <script type="text/javascript">
#             function attempt_nav_page(page_name, start_time, timeout_secs) {{
#                 var links = window.parent.document.getElementsByTagName("a");
#                 for (var i = 0; i < links.length; i++) {{
#                     if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {{
#                         links[i].click();
#                         return;
#                     }}
#                 }}
#                 var elapsed = new Date() - start_time;
#                 if (elapsed < timeout_secs * 1000) {{
#                     setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
#                 }} else {{
#                     alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
#                 }}
#             }}
#             window.addEventListener("load", function() {{
#                 attempt_nav_page("{page_name_url}", new Date(), {timeout_secs});
#             }});
#         </script>
#     """
#     html(nav_script)

# # Sidebar Navigation
# st.sidebar.title("🔍 Navigation")
# page = st.sidebar.radio("Go to:", ["Home", "About", "Compare by Parameter", "Compare by Country"])

# # 📌 **Page Logic**
# if page == "Home":
#     st.title("🌍 Carbon Capture and Storage Dashboard")
#     st.markdown("#### Track and visualize carbon capture initiatives worldwide.")

#     # About Navigation Button
#     col1 = st.columns(1)[0]
#     with col1:
#         if st.button("About CCS"):
#             nav_page("about")  # Navigates to About Page

# elif page == "About":
#     st.title("📖 About This Dashboard")
#     st.markdown("""
#         This dashboard is designed to track and visualize global carbon capture initiatives.
#         It provides insights into the progress, challenges, and actions taken across different regions.
#     """)

# elif page == "Compare by Parameter":
#     # Load JSON data
#     with open("../10_PARAMS_BY_REGION_LINKS.json", "r") as file:
#         data = json.load(file)

#     # Unique issues extraction
#     unique_issues = {issue["issue"] for entry in data for issue in entry["issues"]}
#     options = list(unique_issues)

#     # Issue selection
#     st.sidebar.subheader("📌 Select Issues")
#     selected_options = st.sidebar.multiselect("Choose issues to display:", options)

#     st.divider()
#     st.subheader("🗺️ Geospatial Visualization")

#     # Define geospatial data
#     map_data = {
#         "City A": (-74.006, 40.7128, "red"),
#         "City B": (2.3522, 48.8566, "blue"),
#         "City C": (139.6917, 35.6895, "green")
#     }

#     geo_df = gpd.GeoDataFrame(
#         {"name": list(map_data.keys()), "lon": [x[0] for x in map_data.values()], "lat": [x[1] for x in map_data.values()]},
#         geometry=gpd.points_from_xy([x[0] for x in map_data.values()], [x[1] for x in map_data.values()]),
#         crs="EPSG:4326"
#     )

#     # Create a map
#     fig_map = px.scatter_mapbox(
#         geo_df,
#         lat="lat",
#         lon="lon",
#         hover_name="name",
#         zoom=1,
#         color_discrete_sequence=["red", "blue", "green"]
#     )

#     fig_map.update_layout(mapbox_style="carto-positron", margin={"r": 0, "t": 0, "l": 0, "b": 0})
#     st.plotly_chart(fig_map, use_container_width=True)

#     st.divider()

#     # Display Selected Issues with Cards
#     if selected_options:
#         st.subheader("📝 Selected Issues & Action Points")

#         grouped_cards = {option: [] for option in selected_options}

#         for option in selected_options:
#             for entry in data:
#                 for issue in entry["issues"]:
#                     if issue["issue"] == option:
#                         grouped_cards[option].append((entry["region"], issue["action_point"], issue["link"]))

#         for issue_name, cards in grouped_cards.items():
#             st.markdown(f"### {issue_name}")

#             num_cols = min(len(cards), 3)
#             cols = st.columns(num_cols)

#             for idx, (region, action_name, link) in enumerate(cards):
#                 with cols[idx % num_cols]:
#                     card(
#                         title=region,
#                         text=action_name,
#                         url=link,
#                         styles={
#                             "card": {
#                                 "width": "350px",
#                                 "height": "200px",
#                                 "border-radius": "10px",
#                                 "background-color": "#2c3e50",
#                                 "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.2)",
#                             },
#                             "title": {"font-size": "16px", "color": "white"},
#                             "text": {"font-size": "12px", "color": "white"},
#                         }
#                     )
#     else:
#         st.info("No issues selected. Please choose from the sidebar.")

# elif page == "Compare by Country":
#     # Load JSON data
#     with open("../10_PARAMS_BY_REGION_LINKS.json", "r") as file:
#         data = json.load(file)

#     # Unique issues extraction
#     unique_countries = {entry['region'] for entry in data}
#     options = list(unique_countries)

#     # Country selection
#     st.sidebar.subheader("📌 Select Country")
#     selected_options = st.sidebar.multiselect("Choose countries to display:", options)

#     st.divider()
#     if selected_options:
#         st.subheader("📝 Selected Issues & Action Points")

#         grouped_cards = {option: [] for option in selected_options}

#         for option in selected_options:
#             for entry in data:
#                 if entry["region"] == option:
#                     for issue in entry["issues"]:
#                         grouped_cards[option].append((issue["issue"], issue["action_point"], issue["link"]))

#         for issue_name, cards in grouped_cards.items():
#             st.markdown(f"### {issue_name}")

#             num_cols = min(len(cards), 3)
#             cols = st.columns(num_cols)

#             for idx, (region, action_name, link) in enumerate(cards):
#                 with cols[idx % num_cols]:
#                     card(
#                         title=region,
#                         text=action_name,
#                         url=link,
#                         styles={
#                             "card": {
#                                 "width": "350px",
#                                 "height": "200px",
#                                 "border-radius": "10px",
#                                 "background-color": "#2c3e50",
#                                 "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.2)",
#                             },
#                             "title": {"font-size": "16px", "color": "white"},
#                             "text": {"font-size": "12px", "color": "white"},
#                         }
#                     )
#     else:
#         st.info("No countries selected. Please choose from the sidebar.")
import streamlit as st
from streamlit.components.v1 import html

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.set_page_config(page_title="Carbon Capture Dashboard", layout="wide", page_icon="🌍", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: green; margin-top: 100px;'>CCS Dashboard</h1>", unsafe_allow_html=True)

def nav_page(page_name, timeout_secs=3):
    page_name_url = page_name.replace(' ', '_').capitalize()
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

local_css("styles.css")

# First row with a single button in one column
col1 = st.columns(1)[0]  # Correctly access the first column

with col1:
    if st.button("About"):
        nav_page("About")


