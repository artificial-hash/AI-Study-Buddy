from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1
)

def generate_exam_questions(text):
    prompt = f"""
Create exam-oriented questions strictly from the given content.

FORMAT EXACTLY AS:
1–2 Marks:
3–5 Marks:
8–15 Marks:

CONTENT:
{text}
"""

    result = generator(prompt, max_new_tokens=400)[0]["generated_text"]

    sections = {
        "1–2 Marks": [],
        "3–5 Marks": [],
        "8–15 Marks": []
    }

    current = None
    for line in result.split("\n"):
        line = line.strip()
        if "1–2" in line:
            current = "1–2 Marks"
        elif "3–5" in line:
            current = "3–5 Marks"
        elif "8–15" in line:
            current = "8–15 Marks"
        elif current and line:
            sections[current].append(line)

    return sections
