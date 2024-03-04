import openai
import lyzr
import os
import streamlit as st
import openpyxl
import pandas as pd
import numpy as np
from lyzr import DataConnector, DataAnalyzr

# Load OpenAI API key from Streamlit Secrets
api_key = st.secrets["OPENAI_API_KEY"]

st.title("Excel Data Analyzer")

uploaded_file = st.file_uploader("Upload your Excel file", type="xlsx")
sheet_name = None

if uploaded_file:
    sheet_name = st.text_input("Enter the sheet name")

    if sheet_name:
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
        data_analyzr = DataAnalyzr(df=df, api_key=api_key)

        # Button layout in a vertical stack
        with st.expander("Choose an action"):
            with st.form(key="form_analysis"):
                st.subheader("Analysis")
                user_input_analysis = st.text_input("Enter your analysis query", key="analysis_input")
                submitted_analysis = st.form_submit_button("Submit Analysis")
                if submitted_analysis:
                    analysis = data_analyzr.analysis_insights(user_input=user_input_analysis)
                    st.write(analysis)

            with st.form(key="form_visualization"):
                st.subheader("Visualization")
                user_input_visualization = st.text_input("Enter your visualization query", key="visualization_input")
                submitted_visualization = st.form_submit_button("Submit Visualization")
                if submitted_visualization:
                    visualization = data_analyzr.visualizations(user_input=user_input_visualization)
                    st.write(visualization)

            with st.form(key="form_description"):
                st.subheader("Dataset Description")
                submitted_description = st.form_submit_button("Submit Description")
                if submitted_description:
                    description = data_analyzr.dataset_description()
                    st.write(description)

            with st.form(key="form_queries"):
                st.subheader("Queries for Analysis")
                submitted_queries = st.form_submit_button("Submit Queries")
                if submitted_queries:
                    queries = data_analyzr.ai_queries_df()
                    st.write(queries)

            with st.form(key="form_recommendations_analysis"):
                st.subheader("Recommendations for Analysis")
                submitted_recommendations_analysis = st.form_submit_button("Submit Recommendations for Analysis")
                if submitted_recommendations_analysis:
                    analysis_recommendation = data_analyzr.analysis_recommendation()
                    st.write(analysis_recommendation)

            with st.form(key="form_recommendations"):
                st.subheader("Recommendations")
                user_input_recommendations = st.text_input("Enter your initial query", key="recommendations_input")
                submitted_recommendations = st.form_submit_button("Submit Recommendations")
                if submitted_recommendations:
                    recommendations = data_analyzr.recommendations(user_input=user_input_recommendations)
                    st.write(recommendations)

            with st.form(key="form_tasks"):
                st.subheader("Tasks for Analysis")
                user_input_tasks = st.text_input("Enter your analysis query", key="tasks_input")
                submitted_tasks = st.form_submit_button("Submit Tasks")
                if submitted_tasks:
                    tasks = data_analyzr.tasks(user_input=user_input_tasks)
                    st.write(tasks)
