import openai
import streamlit as st
from lyzr import VoiceBot
import base64


# Load the API key from secrets.toml
api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the VoiceBot with your OpenAI API key
try:
    vb = VoiceBot(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing VoiceBot: {e}")

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
    option = st.sidebar.selectbox("Select Option", ["Text to Notes", "Text to Speech", "Transcription"])

    if option == "Text to Notes":
        # Text input for text-to-notes functionality
        text = st.text_area("Enter Text")
        if st.button("Convert"):
            try:
                # Convert text to notes
                notes = vb.text_to_notes(text)
                st.write("Notes:")
                st.write(notes)
                st.success("Text converted to notes successfully.")
            except Exception as e:
                st.error(f"Error converting text to notes: {e}")

    elif option == "Text to Speech":
        # Text input for text-to-speech functionality
        text = st.text_area("Enter Text")
        if st.button("Convert"):
            try:
                # Convert text to speech
                audio_bytes = vb.text_to_speech(text)
                if audio_bytes:
                    # Provide audio player for playback
                    st.audio(audio_bytes, format='audio/mp3')
                    
                    # Provide download link for the generated audio
                    st.markdown(get_binary_file_downloader_html(audio_bytes, "output_audio.mp3"), unsafe_allow_html=True)
                    
                    st.success("Text converted to speech successfully.")
                else:
                    st.error("Text conversion to speech failed.")
            except Exception as e:
                st.error(f"Error converting text to speech: {e}")

    elif option == "Transcription":
        # Audio file upload for transcription functionality
        audio_file = st.file_uploader("Upload audio file for transcription", type=["flac", "m4a", "mp3", "mp4", "mpeg", "mpga", "oga", "ogg", "wav", "webm"])
        if audio_file is not None:
            try:
                # Transcribe audio file
                transcript = vb.transcribe(audio_file)
                st.write("Transcription:")
                st.write(transcript)
                st.success("Audio file transcribed successfully.")
            except Exception as e:
                st.error(f"Error transcribing audio file: {e}")

# Function to generate a download link for files
def get_binary_file_downloader_html(data, file_name, file_label='Download Audio'):
    href = f'<a href="data:audio/mp3;base64,{base64.b64encode(data).decode()}" download="{file_name}">{file_label}</a>'
    return href

if __name__ == "__main__":
    main()
