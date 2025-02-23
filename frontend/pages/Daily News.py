import streamlit as st
import requests
from datetime import datetime
# Set your API key
API_KEY = "pub_71477894cb8a9ebadfb55e3e26bbcbceae124"
st.sidebar.markdown(f"📅 **Up to date:** {datetime.today().strftime('%B %d, %Y')}")

QUERY = "Carbon Capture and Storage"
URL = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={QUERY}&language=en"

@st.cache_data(ttl=86400)  # Cache for 24 hours
def fetch_news():
    response = requests.get(URL)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("results", [])
        
        # Remove duplicates based on title
        unique_titles = set()
        filtered_articles = []
        for article in articles:
            title = article.get("title", "").strip()
            if title and title not in unique_titles:
                unique_titles.add(title)
                filtered_articles.append(article)
        
        return filtered_articles
    return None

# Streamlit UI
st.markdown("<h1 style='text-align: center; color: #28a745;'>📰 Carbon Capture & Storage News</h1>", unsafe_allow_html=True)

# st.title("")
st.write("Fetching the latest news articles about Carbon Capture and Storage (CCS).")

# Fetch and display cached news
news_articles = fetch_news()

if news_articles:
    for article in news_articles:  # Display up to 5 unique articles
        st.subheader(article.get("title"))
        st.write(f"**Source:** {article.get('source_id')}")
        
        # Convert and display the publication date
        pub_date = article.get("pubDate", "")
        if pub_date:
            try:
                formatted_date = datetime.strptime(pub_date, "%Y-%m-%d %H:%M:%S").strftime("%B %d, %Y")
                st.write(f"**Published:** {formatted_date}")
            except ValueError:
                st.write(f"**Published:** {pub_date}")  # Fallback if format is different
        
        # Display image if available
        image_url = article.get("image_url")
        if image_url:
            st.image(image_url, caption="News Image")

        st.markdown(f"[Read more]({article.get('link')})")
        st.markdown("---")  # Separator line
else:
    st.error("Failed to fetch news. Please check your API key or try again later.")