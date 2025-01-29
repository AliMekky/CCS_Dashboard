# CCS Regulatory Dashboard

## Project Overview

This dashboard aims to develop a user-friendly interface that compares various regulatory categories for Carbon Capture and Storage (CCS) across regions. It includes a chatbot feature to enhance user interaction, aggregates, and analyzes regulatory information from different countries, and provides insights into compliance requirements.

## Features

- **Comparative Dashboard**: Visualize and compare CCS regulations across different regions.
- **Chatbot Assistance**: Interact with the chatbot for guided navigation and data interpretation.
- **Data Automation**: Automated scraping and analysis of regulatory data.
- **Scalable Architecture**: Designed to be scalable and maintainable with a clean codebase.

## Technology Stack

- **Frontend & Backend**: Streamlit (Python)
- **Data Scraping**: Python libraries
- **AI/ML**: LangChain, OpenAI API
- **Version Control**: GitHub
- **Hosting**: Streamlit Cloud

## Files Structure:
- frontend: for the streamlit app (created)
- backend: for the scraper and regulatory docs (not created yet)
- chatbot: for the chatbot code (not created yet)
- scripts: for any additional scripts that may be useful. (not created yet)

## Getting Started

### Prerequisites

Ensure you have Conda installed on your system to manage Python versions and dependencies efficiently. If you do not have Conda installed, follow the installation instructions on the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual) websites.

### Installation Steps

#### Create and Activate a Conda Environment

1. **Open your terminal.**
2. **Create a new Conda environment** by running:
   ```bash
   conda create --name ccs_dashboard_env python=3.10
3. **Activate the environment**:
   ```bash
   conda activate ccs_dashboard_env
4. **Install the requirements**:
    ```bash
    pip install -r requirements.txt
5. **Run the Application inside frontend folder**:
    ```bash
    streamlit run app.py
