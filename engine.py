import re
from pypdf import PdfReader


# -------------------------
# LOAD PDF
# -------------------------
def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + " "
    return text.strip()


# -------------------------
# CLEAN TEXT
# -------------------------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# -------------------------
# SUMMARY (EXAM NOTES)
# -------------------------
def generate_summary(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    points = []

    for s in sentences:
        if len(s.split()) > 6:
            points.append(s.strip())

    points = points[:10]

    return "\n".join([f"- {p}" for p in points])


# -------------------------
# QUIZ
# -------------------------
def generate_quiz(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    questions = []

    for s in sentences:
        if " is " in s:
            concept = s.split(" is ")[0]
            questions.append(f"Explain {concept}.")
        elif " are " in s:
            concept = s.split(" are ")[0]
            questions.append(f"Describe {concept}.")
        elif len(s.split()) > 8:
            questions.append(f"Write a note on: {s[:40]}...")

    return questions[:5]


# -------------------------
# FLASHCARDS
# -------------------------
def generate_flashcards(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    cards = []

    for s in sentences:
        if " is " in s:
            q, a = s.split(" is ", 1)
            cards.append((f"What is {q}?", a))

    return cards[:5]
