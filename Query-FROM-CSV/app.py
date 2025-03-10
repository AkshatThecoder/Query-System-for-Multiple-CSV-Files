import streamlit as st
import pandas as pd
import os
from utils.process_csv import load_csv, list_available_csv, get_csv_summary
from utils.query_engine import process_query

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing. Set it in the .env file.")


st.title("📊 Query Multiple CSV Files with LangChain & Groq")

# File Upload Section
uploaded_files = st.file_uploader("📂 Upload CSV files", type=["csv"], accept_multiple_files=True)

# Save uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join("data/", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("✅ CSV files uploaded successfully!")

# List available CSVs
available_csvs = list_available_csv()
selected_csv = st.selectbox("📂 Choose a CSV file", available_csvs)

if selected_csv:
    df = load_csv(f"data/{selected_csv}")
    st.write("📄 **CSV Summary**", get_csv_summary(df))

    # Query Input
    query = st.text_input("🔍 Ask a question about the data:")

    if st.button("Get Answer"):
        if query:
            response = process_query(df, query)
            st.write("🤖 **Answer:**", response)
        else:
            st.error("❌ Please enter a question!")
