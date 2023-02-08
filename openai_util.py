import openai
import config
import numpy as np
from numpy.linalg import norm
import re

openai.api_key = config.OPENAI_API_KEY

def gpt3_embedding(content, engine='text-embedding-ada-002'):
    content = content.encode(encoding='utf-8', errors='ignore').decode()
    response = openai.Embedding.create(input=content, engine=engine)
    v = response['data'][0]['embedding']
    return v

def similarity(v1, v2):
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

def gpt3_completion(prompt, engine='text-davinci-003', temp=0.0, top_p=1.0,
                    tokens=500, freq_pen=0.0, pres_pen=0.0, stop=['USER:', 'JARVIS:']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='utf-8', errors='ignore').decode()

    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
