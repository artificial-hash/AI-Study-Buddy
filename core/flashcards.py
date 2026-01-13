from transformers import pipeline

MODEL_NAME = "google/flan-t5-small"

generator = pipeline(
    "text2text-generation",
    model=MODEL_NAME
)

def generate_summary(chunks):
    results = []

    for chunk in chunks:
        prompt = (
            "Explain the following content in exam-ready theory "
            "with headings and simple language:\n\n"
            + chunk
        )

        output = generator(
            prompt,
            max_new_tokens=120,
            do_sample=False
        )[0]["generated_text"]

        results.append(output)

    return "\n\n".join(results)
