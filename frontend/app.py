import streamlit as st

def main():
    st.sidebar.title("Navigation")
    options = ["Home", "Data Overview", "Regulatory Compliance", "Chatbot"]
    selection = st.sidebar.radio("Choose a page:", options)

    if selection == "Home":
        home()
    elif selection == "Data Overview":
        data_overview()
    elif selection == "Regulatory Compliance":
        regulatory_compliance()
    elif selection == "Chatbot":
        chatbot()

def home():
    st.title("Welcome to the CCS Regulatory Dashboard")
    st.text("Explore various regulatory categories for Carbon Capture and Storage across regions.")

def data_overview():
    st.title("Data Overview")
    st.write("Here you can see a summary of all the data collected from various regions.")

def regulatory_compliance():
    st.title("Regulatory Compliance")
    st.write("This page will help you compare regulatory compliance requirements across different regions.")

def chatbot():
    st.title("Chatbot Assistance")
    st.write("Use this chatbot to navigate through the regulatory data or ask questions about the CCS regulations.")

if __name__ == "__main__":
    main()
