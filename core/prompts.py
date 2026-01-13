# core/prompts.py

SUMMARY_PROMPT = """
You are a university professor.

Task:
Create a detailed, exam-oriented summary.

Rules:
- Use bullet points
- Explain concepts clearly
- Include examples if relevant
- Length: minimum 8 bullet points

Content:
{text}
"""

QUIZ_PROMPT = """
You are an examiner.

Task:
Generate exactly 5 conceptual exam questions.

Rules:
- Questions must be theory-based
- No answers
- Suitable for 5-mark questions

Content:
{text}
"""

FLASHCARD_PROMPT = """
Create exactly 5 flashcards.

Rules:
- Format strictly as:
Q: question
A: answer
- Clear and concise
- Exam-focused

Content:
{text}
"""
