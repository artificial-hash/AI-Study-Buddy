# models/model_loader.py

from transformers import pipeline

_model = None

def get_text_generator():
    global _model

    if _model is None:
        _model = pipeline(
            task="text2text-generation",
            model="google/flan-t5-base",
            device=-1  # CPU
        )

    return _model
