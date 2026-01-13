from pypdf import PdfReader

def load_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def load_text_from_string(text):
    return text.strip()
