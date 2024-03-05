import streamlit as st
from lyzr import VoiceBot
import base64
import openai

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
                st.error(f"Error: {e}")

    elif option == "Text to Speech":
        # Text input for text-to-speech functionality
        text = st.text_area("Enter Text")
        if st.button("Convert"):
            try:
                # Convert text to speech
                audio_bytes = vb.text_to_speech(text)
                
                # Provide download link to the user for MP3 format
                st.audio(audio_bytes, format='audio/mp3')
                st.success("Text converted to speech successfully.")

                # Provide download link for the generated audio
                href = f'<a href="data:audio/mp3;base64,{base64.b64encode(audio_bytes).decode()}" download="output_audio.mp3">Download Audio</a>'
                st.markdown(href, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

    elif option == "Transcription":
        # Audio file upload for transcription functionality
        audio_file = st.file_uploader("Upload audio file for transcription", type=["mp3", "wav"])
        if audio_file is not None:
            try:
                # Save the uploaded audio file to a temporary location
                with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
                    temp_audio.write(audio_file.read())
                    temp_audio_path = temp_audio.name
                
                # Transcribe audio file
                transcript = vb.transcribe(temp_audio_path)
                st.write("Transcription:")
                st.write(transcript)
                st.success("Audio file transcribed successfully.")
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
