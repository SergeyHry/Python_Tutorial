from transformers import pipeline

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
print(generator("Song", max_length=30))

