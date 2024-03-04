import streamlit as st
from lyzr import VoiceBot
import os
import tempfile
import shutil

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

# Directory to save audio files
AUDIO_DIR = "audio_files"

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
            temp_audio_file_path = os.path.join(tempfile.gettempdir(), "output.wav")
            with open(temp_audio_file_path, "wb") as temp_audio_file:
                shutil.copyfileobj(io.BytesIO(audio_bytes), temp_audio_file)
            # Provide download link to the user
            st.audio(audio_bytes, format='audio/wav')
            st.success("Text converted to speech successfully.")
            # Save audio file to specified directory
            save_audio_to_directory(temp_audio_file_path, AUDIO_DIR)
            st.markdown(f"Audio file saved to directory: `{AUDIO_DIR}`")

# Function to save audio file to a specified directory
def save_audio_to_directory(audio_file_path, directory):
    os.makedirs(directory, exist_ok=True)
    shutil.move(audio_file_path, os.path.join(directory, os.path.basename(audio_file_path)))

if __name__ == "__main__":
    main()
