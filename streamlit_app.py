import openai
import lyzr
import os
import openpyxl
import pandas as pd
import numpy as np

import streamlit as st
from lyzr import DataConnector, DataAnalyzr

def main():
    st.title("Excel Data Analyzer")

    # File Upload
    uploaded_file = st.file_uploader("Upload your Excel file", type="xlsx")
    if uploaded_file:
        sheet_name = st.text_input("Enter the sheet name")

        if sheet_name:
            df = DataConnector().fetch_dataframe_from_excel(file_path=uploaded_file, sheet_name=sheet_name)
            api_key = st.secrets["OPENAI_API_KEY"]  # Load OpenAI API key from Streamlit Secrets

            # Initialize DataAnalyzr with the obtained DataFrame and API key
            data_analyzr = DataAnalyzr(df=df, api_key=api_key)

            # Choose an action
            action = st.selectbox("Choose an action", ["Analysis", "Visualization", "Dataset Description", 
                                                       "Queries for Analysis", "Recommendations for Analysis", 
                                                       "Recommendations", "Tasks for Analysis"])

            if action == "Analysis":
                user_input = st.text_input("Enter your analysis query")
                if st.button("Submit Analysis"):
                    analysis = data_analyzr.analysis_insights(user_input=user_input)
                    st.write(analysis)

            elif action == "Visualization":
                user_input = st.text_input("Enter your visualization query")
                if st.button("Submit Visualization"):
                    visualization = data_analyzr.visualizations(user_input=user_input)
                    st.write(visualization)

            elif action == "Dataset Description":
                if st.button("Submit Description"):
                    description = data_analyzr.dataset_description()
                    st.write(description)

            elif action == "Queries for Analysis":
                if st.button("Submit Queries"):
                    queries = data_analyzr.ai_queries_df()
                    st.write(queries)

            elif action == "Recommendations for Analysis":
                if st.button("Submit Recommendations for Analysis"):
                    analysis_recommendation = data_analyzr.analysis_recommendation()
                    st.write(analysis_recommendation)

            elif action == "Recommendations":
                user_input = st.text_input("Enter your initial query")
                if st.button("Submit Recommendations"):
                    recommendations = data_analyzr.recommendations(user_input=user_input)
                    st.write(recommendations)

            elif action == "Tasks for Analysis":
                user_input = st.text_input("Enter your analysis query")
                if st.button("Submit Tasks"):
                    tasks = data_analyzr.tasks(user_input=user_input)
                    st.write(tasks)

if __name__ == "__main__":
    main()
