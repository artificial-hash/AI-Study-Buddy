print("test_core.py started")

from core.chunker import chunk_text
from core.generator import generate_summary, generate_quiz, generate_flashcards

sample_text = """
Machine Learning is a subset of Artificial Intelligence.
It allows systems to learn from data.
Deep Learning uses neural networks with many layers.
Machine learning is widely used in healthcare, finance, and education.
"""

chunks = chunk_text(sample_text)

print("\n--- SUMMARY ---")
summary = generate_summary(chunks)
print(summary)

print("\n--- QUIZ ---")
quiz = generate_quiz(summary)
for q in quiz:
    print("-", q)

print("\n--- FLASHCARDS ---")
cards = generate_flashcards(summary)
for c in cards:
    print("-", c)
