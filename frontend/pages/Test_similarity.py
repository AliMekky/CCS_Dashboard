import streamlit as st
import json
import numpy as np
import faiss
import pandas as pd
import plotly.express as px
from sentence_transformers import SentenceTransformer


# --- 🏗️ Page Configuration ---
st.set_page_config(page_title="Similarity Testing - CCS Dashboard", layout="wide")

# st.title("🔍 LLM Similarity Testing")
st.write("Compare your query with **Carbon Capture and Storage (CCS) regulatory issues**.")

# --- 📂 Load JSON Data ---
@st.cache_data
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

json_file = "../10_PARAMS_BY_REGION_LINKS.json"
json_data = load_json(json_file)

# --- ⚡ Initialize Sentence Transformer Model ---
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')  # Efficient & lightweight

model = load_model()

# --- 📑 Extract issue-level text and metadata ---
issue_texts = []
issue_regions = []
issue_titles = []

for region in json_data:
    region_name = region["region"]
    for issue in region["issues"]:
        issue_texts.append(issue["text"])  # Store issue text
        issue_regions.append(region_name)  # Store corresponding region
        issue_titles.append(issue["issue"])  # Store issue title

# --- 🔢 Encode all issues into embeddings ---
@st.cache_resource
def compute_embeddings(texts):
    embeddings = model.encode(texts, convert_to_numpy=True).astype('float32')
    faiss.normalize_L2(embeddings)  # Normalize for cosine similarity
    return embeddings

issue_embeddings = compute_embeddings(issue_texts)

# --- 🏗️ Initialize FAISS Index ---
dimension = issue_embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)  # Inner Product Index (Cosine Similarity)
index.add(issue_embeddings)

# --- 🔍 Function to Search Similar Issues ---
def search_similar_issues(input_text, top_k=10):
    query_embedding = model.encode([input_text], convert_to_numpy=True).astype('float32')
    faiss.normalize_L2(query_embedding)  # Normalize Query
    D, I = index.search(query_embedding, top_k)  # Retrieve Top-K matches

    similarity_scores = [
        (issue_regions[i], issue_titles[i], round(d * 100, 2)) for i, d in zip(I[0], D[0])
    ]

    return pd.DataFrame(similarity_scores, columns=["Region", "Issue", "Similarity (%)"])


# --- 🎯 User Input Query ---
st.subheader("📝 Input Query for Similarity Search")
user_query = st.text_area(
    "Enter a regulatory issue description:", 
    "Prepare, submit, and update a post-operation plan for approval, ensuring compliance with monitoring, reporting, corrective measures, sealing, and removal obligations until the storage location responsibility is transferred to the State."
)

top_k = st.slider("Select Top-K Similar Issues", min_value=3, max_value=15, value=10)

# --- 🔍 Search & Display Results ---
if st.button("Find Similar Issues"):
    with st.spinner("Searching..."):
        similarity_df = search_similar_issues(user_query, top_k)

    # 🎯 **Show Similarity Results**
    st.subheader("📊 Similarity Results")
    st.dataframe(similarity_df, use_container_width=True)

    # 📊 **Bar Chart Visualization**
    st.subheader("📈 Similarity Score Distribution")
    fig = px.bar(similarity_df, x="Similarity (%)", y="Issue", color="Region", 
                 orientation="h", text="Similarity (%)", 
                 color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_layout(yaxis_title="Issue", xaxis_title="Similarity (%)", margin={"l": 0, "r": 0, "t": 10, "b": 10})
    st.plotly_chart(fig, use_container_width=True)
