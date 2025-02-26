import datetime
import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="CCS Ratings Dashboard", layout="wide")
st.sidebar.markdown(f"📅 **Up to date:** {datetime.date.today().strftime('%B %d, %Y')}")

# Page Title
st.title("🌎 CCS Ratings Dashboard")
st.write("Compare Carbon Capture and Storage (CCS) regulatory ratings across different regions.")

# Load Ratings Data from JSON file
# try:
#     with open("./ratings.json", "r") as file:
#         ratings_data = json.load(file)
# except (FileNotFoundError, json.JSONDecodeError):
#     st.error("Error loading `ratings.json`. Ensure the file exists and is properly formatted.")
#     ratings_data = []

ratings_data = [
    {
        "region": "Alberta (Canada)",
        "Regulatory Complexity": 4,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 4
        
      },
      {
        "region": "European Union",
        "Regulatory Complexity": 5,
        "Storage Potential": 4,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 5
      },
      {
        "region": "British Columbia (Canada)",
        "Regulatory Complexity": 4,
        "Storage Potential": 4,
        "Financial Burden": 3,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 3
        
      },
      {
        "region": "Indiana (United States)",
        "Regulatory Complexity": 3,
        "Storage Potential": 4,
        "Financial Burden": 3,
        "Monitoring & Compliance Effort": 3,
        "Post-Closure Liability Risk": 4
        
      },
      {
        "region": "Kansas (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 4,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 4
      },
      {
        "region": "Louisiana (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 5
      },
      {
        "region": "Montana (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 4,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 5 
      },
      {
        "region": "Nebraska (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 4,
        "Financial Burden": 3,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 5
      },
      {
        "region": "New Mexico (United States)",
        "Regulatory Complexity": 3,
        "Storage Potential": 4,
        "Financial Burden": 3,
        "Monitoring & Compliance Effort": 3,
        "Post-Closure Liability Risk": 3
      },
      {
        "region": "North Dakota (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 5,
        "Financial Burden": 3,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 5
      
      },
      {
        "region": "Northern Ireland (United Kingdom)",
        "Regulatory Complexity": 5,
        "Storage Potential": 4,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 5
        
      },
      {
        "region": "Norway",
        "Regulatory Complexity": 5,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 5
        
      },
      {
        "region": "South Australia (Australia)",
        "Regulatory Complexity": 4,
        "Storage Potential": 4,
        "Financial Burden": 3,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 4
        
      },
      {
        "region": "Texas (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 5
        
      },
      {
        "region": "United Kingdom",
        "Regulatory Complexity": 5,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 5
        
      },
      {
        "region": "United States",
        "Regulatory Complexity": 5,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 4
        
      },
      {
        "region": "Victoria (Australia)",
        "Regulatory Complexity": 5,
        "Storage Potential": 4,
        "Financial Burden": 5,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 4
        
      },
      {
        "region": "Western Australia (Australia)",
        "Regulatory Complexity": 4,
        "Storage Potential": 4,
        "Financial Burden": 5,
        "Monitoring & Compliance Effort": 4,
        "Post-Closure Liability Risk": 3 
      },
      {
        "region": "Wyoming (United States)",
        "Regulatory Complexity": 4,
        "Storage Potential": 5,
        "Financial Burden": 4,
        "Monitoring & Compliance Effort": 5,
        "Post-Closure Liability Risk": 3
        
      }
      
]

  
# Convert to DataFrame
df = pd.DataFrame(ratings_data)

if df.empty:
    st.warning("No data available. Please check the `ratings.json` file.")
else:
    # Sidebar: Select Regions to Compare
    selected_regions = st.sidebar.multiselect("Select regions to compare:", df["region"].tolist(), default=df["region"].tolist())
    filtered_df = df[df["region"].isin(selected_regions)]

    st.divider()

    # Radar Chart Visualization
    st.subheader("📊 Radar Chart: Comparison Across Criteria")
    
    def plot_radar_chart(df):
        categories = [
            "Regulatory Complexity",
            "Storage Potential",
            "Financial Burden",
            "Monitoring & Compliance Effort",
            "Post-Closure Liability Risk"
        ]
        
        fig = go.Figure()
        for _, row in df.iterrows():
            values = [row[cat] for cat in categories]
            values.append(values[0])  # Closing the radar chart
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=row["region"]
            ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[1, 5])),
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

    plot_radar_chart(filtered_df)

    st.divider()

    # Bar Chart Visualization
    st.subheader("📈 Bar Charts: Ratings by Region")

    criteria_list = [
        "Regulatory Complexity",
        "Storage Potential",
        "Financial Burden",
        "Monitoring & Compliance Effort",
        "Post-Closure Liability Risk"
    ]

    for criteria in criteria_list:
        fig = px.bar(
            filtered_df, 
            x="region", 
            y=criteria, 
            text=criteria, 
            color="region", 
            title=f"{criteria} Ratings by Region",
            height=400
        )
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_layout(yaxis=dict(range=[1, 5]))  # Ensuring ratings are in the range 1-5
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Explanation of Criteria
    st.subheader("📌 Explanation of Criteria")
    criteria_definitions = {
        "Regulatory Complexity": "The extent to which legal and administrative requirements impact the approval, development, and operation of CCS projects. A complex regulatory framework can introduce delays, increase costs, and create uncertainty for project stakeholders.",
        "Storage Potential": "The capacity and suitability of underground geological formations to securely store CO2 for long-term sequestration. This depends on factors such as reservoir depth, porosity, permeability, and the presence of impermeable caprock to prevent leakage.",
        "Financial Burden": "The overall economic impact of a CCS project, including capital investment, operational costs, regulatory fees, liability insurance, and post-closure financial obligations. High financial burdens can make projects less attractive to investors.",
        "Monitoring & Compliance Effort": "The level of oversight, reporting, and technical verification required to ensure CO2 remains securely stored. This includes continuous monitoring of injection sites, compliance with environmental regulations, and regular safety assessments.",
        "Post-Closure Liability Risk": "The responsibility and associated risks after a storage site has been closed, including long-term monitoring, remediation in case of leaks, and financial obligations. Unclear or excessive liability can discourage private sector participation in CCS projects."
    }

    for criteria, definition in criteria_definitions.items():
        with st.expander(f"**{criteria}**"):
            st.write(definition)

    st.success("🔍 Use the sidebar to select regions and compare their CCS ratings!")
