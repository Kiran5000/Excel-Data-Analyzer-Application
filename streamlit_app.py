import openai
import lyzr
import os

import streamlit as st
from lyzr import QABot

def initialize_qabot(video_url, api_key):
    # Define parameters for the Weaviate vector store
    vector_store_params = {
        "vector_store_type": "WeaviateVectorStore",
        "url": "https://sample..weaviate.network",
        "api_key": api_key,
        "index_name": "IndexName"  # first letter should be capital
    }
    
    # Initialize the QABot with YouTube videos
    qa_bot = QABot.youtube_qa(urls=[video_url], vector_store_params=vector_store_params)
    return qa_bot

def query_qabot(qa_bot, question):
    response = qa_bot.query(question)
    return response.response

def main():
    st.title("YouTube Question-Answering with QABot")

    # Retrieve the API key from Streamlit secrets
    api_key = st.secrets["OPENAI_API_KEY"]

    # Get the YouTube video URL from user input
    video_url = st.text_input("Enter the YouTube video URL:")
    
    # Get the question from user input
    question = st.text_input("Enter your question:")
    
    # Initialize the QABot
    if video_url:
        qa_bot = initialize_qabot(video_url, api_key)

        # Query the QABot with the question
        if st.button("Ask"):
            if question:
                response = query_qabot(qa_bot, question)
                st.write("QABot's Response:")
                st.write(response)
            else:
                st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
