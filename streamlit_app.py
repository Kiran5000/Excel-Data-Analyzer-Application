import os
import openai
import lyzr
import streamlit as st
from lyzr import ChatBot

# Function to initialize the ChatBot with a text file
def initialize_chatbot(text_file_path, api_key):
    # Define parameters for the Weaviate vector store
    # You can choose either an external Weaviate cluster or local Embedded Weaviate vector store
    # Replace the placeholders with actual values if using an external Weaviate cluster
    vector_store_params = {
        "vector_store_type": "WeaviateVectorStore",
        "url": "https://sample..weaviate.network",
        "api_key": "DB_API_KEY",
        "index_name": "IndexName"  # first letter should be capital
    }
    
    # Initialize the ChatBot with the text file
    chatbot = ChatBot.txt_chat(input_files=[text_file_path], vector_store_params=vector_store_params)
    return chatbot

# Function to query the ChatBot with a given question
def query_chatbot(chatbot, question):
    # Ask a question related to the text content
    response = chatbot.chat(question)
    return response.response

def main():
    st.title("Docx ChatBot")

    # Retrieve the API key from Streamlit secrets
    api_key = st.secrets["OPENAI_API_KEY"]

    # Get the path to the text file from user input
    text_file_path = st.text_input("Enter the path to your text file (e.g., /path/to/your/file.txt):")
    
    # Initialize the ChatBot
    if text_file_path:
        chatbot = initialize_chatbot(text_file_path, api_key)

        # Get the question from user input
        question = st.text_input("Enter your question:")

        # Query the ChatBot with the question
        if st.button("Ask"):
            if question:
                response = query_chatbot(chatbot, question)
                st.write("ChatBot's Response:")
                st.write(response)
            else:
                st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
