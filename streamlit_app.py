import streamlit as st
from lyzr import VoiceBot

# Set page configuration
st.set_page_config(
    page_title="Voice Bot",
    page_icon=":microphone:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.title("🎙️ Voice Bot 🤖")

    vb = VoiceBot(api_key="OPENAI_API_KEY")

    option = st.sidebar.selectbox("Select Functionality", ("Text-to-Notes", "Text-to-Speech", "Transcription"))

    if option == "Text-to-Notes":
        text = st.text_area("Enter text for summarization:")
        if st.button("Summarize"):
            notes = vb.text_to_notes(text)
            st.write("Summarized Notes:")
            st.write(notes)

    elif option == "Text-to-Speech":
        text = st.text_area("Enter text for speech conversion:")
        if st.button("Convert to Speech"):
            vb.text_to_speech(text)
            st.success("Text converted to speech. Check the output file.")

    elif option == "Transcription":
        audio_file = st.file_uploader("Upload audio file for transcription", type=["mp3", "wav"])
        if audio_file is not None:
            transcript = vb.transcribe(audio_file)
            st.write("Transcription:")
            st.write(transcript)

if __name__ == "__main__":
    main()
