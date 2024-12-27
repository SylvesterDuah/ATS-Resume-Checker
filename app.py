from dotenv import load_dotenv

load_dotenv()

import streamlit as st

import os
import io

import base64
from PIL import Image
import PyPDF2 as pdf
# import pdf2image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text=""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text




input_prompt= """
Hey Act like a skilled or very experience ATS(Application Tracking System) with a deep understanding
of tech field, Artificial Intelligence, Machine Learning, Software Engineer, Data Science, Data Analyst and Cyber Security. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide best assistance for improving the resume. Assign the percentage Matching based on the Jd and the missing keywords with high accuracy
resume: {text}
decription: {jd}

I want the response in one single string having the structure
{{"JD Match":"%", "MissingKeywords:[]", "Profile Summary":""}}
"""

# Streamlit App

st.title("Sly's AI")
st.text("Let's see your chance of getting the job")
jd=st.text_area("Tell Sly.AI the job's description: ")
uploaded_file=st.file_uploader("Upload your reseme(PDF)...", type="pdf", help="Please upload the pdf")

submit = st.button("submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)
       