from transformers import pipeline
from core.chunker import chunk_text

MODEL = "google/flan-t5-small"

pipe = pipeline(
    "text2text-generation",
    model=MODEL
)

def generate_theory(text):
    chunks = chunk_text(text)
    output = []

    for ch in chunks[:5]:  # HARD LIMIT
        prompt = "Explain this for exam preparation:\n" + ch
        res = pipe(prompt, max_new_tokens=120, do_sample=False)
        output.append(res[0]["generated_text"])

    return "\n\n".join(output)

def generate_quiz(text):
    prompt = "Create 5 exam MCQs from this:\n" + text[:800]
    res = pipe(prompt, max_new_tokens=120, do_sample=False)
    return res[0]["generated_text"]

def generate_flashcards(text):
    prompt = "Create 5 Q&A flashcards from this:\n" + text[:800]
    res = pipe(prompt, max_new_tokens=120, do_sample=False)
    return res[0]["generated_text"]
