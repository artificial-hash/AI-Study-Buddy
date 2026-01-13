import streamlit as st
from pypdf import PdfReader
from core.generator import (
    generate_theory,
    generate_quiz,
    generate_flashcards
)

st.set_page_config(page_title="AI Study Buddy", layout="wide")
st.title("📘 AI Study Buddy – Exam Preparation Tool")

st.markdown("""
Paste your notes or upload a PDF.  
Generate **exam-ready content**, **quizzes**, and **flashcards**.
""")

input_mode = st.radio("Choose input type:", ["Paste Text", "Upload PDF"])
text = ""

if input_mode == "Paste Text":
    text = st.text_area("Paste your content here:", height=250)
else:
    pdf = st.file_uploader("Upload PDF", type=["pdf"])
    if pdf:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text() + "\n"

option = st.selectbox(
    "Choose what to generate:",
    ["Exam Theory", "Quiz", "Flashcards"]
)

if st.button("Generate"):
    if not text.strip():
        st.warning("Please provide input text.")
    else:
        with st.spinner("Generating..."):
            if option == "Exam Theory":
                st.write(generate_theory(text))
            elif option == "Quiz":
                st.write(generate_quiz(text))
            elif option == "Flashcards":
                st.write(generate_flashcards(text))
