import streamlit as st
from lyzr import VoiceBot
import tempfile
import os

# Load the API key from secrets.toml
api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the VoiceBot with your OpenAI API key
vb = VoiceBot(api_key=api_key)

# Set page configuration
st.set_page_config(
    page_title="Voice Bot",
    page_icon=":microphone:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.title("🎙️ Voice Bot 🤖")

    # Sidebar options
    option = st.sidebar.selectbox("Select Option", ["Text to Notes", "Text to Speech"])

    if option == "Text to Notes":
        # Text input for text-to-notes functionality
        text = st.text_area("Enter Text")
        if st.button("Convert"):
            # Convert text to notes
            notes = vb.text_to_notes(text)
            st.write("Notes:")
            st.write(notes)
            st.success("Text converted to notes successfully.")

    elif option == "Text to Speech":
        # Text input for text-to-speech functionality
        text = st.text_area("Enter Text")
        if st.button("Convert"):
            # Convert text to speech
            audio_bytes = vb.text_to_speech(text)
            # Save audio to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
                temp_audio_file.write(audio_bytes)
                audio_file_path = temp_audio_file.name
            # Automatically download the audio file to the default location
            st.audio(audio_bytes, format='audio/wav', filename="output_audio.wav")
            st.success("Text converted to speech successfully.")

# Function to download files to the default location
def download_file(file_path):
    with open(file_path, "rb") as file:
        file_bytes = file.read()
    st.download_button(label="Click here to download the audio file", data=file_bytes, file_name="output_audio.wav")

if __name__ == "__main__":
    main()
