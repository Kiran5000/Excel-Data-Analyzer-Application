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
            # Display audio for playback
            st.audio(audio_bytes, format='audio/wav')
            st.success("Text converted to speech successfully.")
            # Provide download link to the user for MP3 format
            st.markdown(get_binary_file_downloader_html(audio_bytes, "output_audio.mp3"), unsafe_allow_html=True)

# Function to generate a download link for files
def get_binary_file_downloader_html(data, file_name, file_label='File'):
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">{file_label}</a>'
    return href

if __name__ == "__main__":
    main()
