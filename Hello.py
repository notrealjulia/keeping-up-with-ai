import streamlit as st
from transformers import pipeline
import requests
import PyPDF2
from io import BytesIO

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

    # Create a text input in Streamlit for the PDF URL
    pdf_url = st.text_input('Enter the URL of your PDF')

    # When the 'Extract & Summarize' button is pressed, extract the text from the PDF and summarize it
    if st.button('Extract & Summarize'):
        # Send a GET request to the PDF URL
        response = requests.get(pdf_url)

        # Create a BytesIO object from the content of the response
        pdf_file = BytesIO(response.content)

        # Create a PDF file reader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to hold the text
        text = ""

        # Loop through each page in the PDF and extract the text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        st.write(summary[0]['summary_text'])

if __name__ == "__main__":
    run()