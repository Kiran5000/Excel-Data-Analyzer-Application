import streamlit as st
from lyzr import VoiceBot
import tempfile
import os
import io
from pydub import AudioSegment

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
            # Convert audio to MP3 format
            audio = AudioSegment.from_wav(io.BytesIO(audio_bytes))
            with io.BytesIO() as output_buffer:
                audio.export(output_buffer, format="mp3")
                mp3_audio_bytes = output_buffer.getvalue()
            # Provide download link to the user
            st.audio(mp3_audio_bytes, format='audio/mp3')
            st.success("Text converted to speech successfully.")

if __name__ == "__main__":
    main()
