import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os


st.set_page_config(page_title="Language Translator", page_icon="🌎", layout="centered")

st.title("🌎 AI Language Translation Tool")
st.markdown("Translate text instantly between languages using Google Translate.")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Select Source Language",
        options=['auto', 'en', 'es', 'fr', 'de', 'hi', 'ja', 'ko', 'zh-CN'],
        format_func=lambda x: "Detect Automatically" if x == 'auto' else x.upper(),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "Select Target Language",
        options=['en', 'es', 'fr', 'de', 'hi', 'ja', 'ko', 'zh-CN'],
        format_func=lambda x: x.upper(),
        index=4 
    )

text_input = st.text_area("Enter text to translate:", height=150, placeholder="Type something here...")

if st.button("Translate 🚀", type="primary"):
    if text_input:
        try:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translation = translator.translate(text_input)

            st.success("Translation:")
            st.markdown(f"### {translation}")

            try:
                tts = gTTS(text=translation, lang=target_lang, slow=False)
                tts.save("audio.mp3")
                
                st.audio("audio.mp3")
            except Exception as e:
                st.warning("Audio playback not supported for this language or text.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to translate.")

with st.sidebar:
    st.header("About")
    st.info("This tool uses the Deep Translator library to access Google Translate APIs.")
    st.markdown("Created for **Task 1: Language Translation Tool**")