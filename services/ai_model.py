from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import logging

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def get_movie_name(prompt: str) -> str:
    try:
        input_text = f"Suggest a popular movie for the context: {prompt}. Only return the movie title."
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=20)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result.strip()
    except Exception as e:
        logging.error("❌ Local model inference error: %s", e)
        return None
