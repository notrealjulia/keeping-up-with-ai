import streamlit as st
from transformers import pipeline

# Create a text summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

def run():
    st.set_page_config(
        page_title="Text Summarization",
        page_icon="📝",
    )

    st.write("# Welcome to the Text Summarization App! 📝")

    # Create a text input in Streamlit
    text = st.text_input('Enter your text')

    # When the 'Summarize' button is pressed, summarize the input text
    if st.button('Summarize'):
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        st.write(summary[0]['summary_text'])

if __name__ == "__main__":
    run()