import requests
import time

URL = "http://127.0.0.1:8000/generate"

prompts = [
    "Explain machine learning in one sentence.",
    "What is model monitoring?",
    "Define data drift.",
    "Why is caching useful for LLM inference?",
    "Explain batching in simple terms."
]

for i in range(30):
    prompt = prompts[i % len(prompts)]

    response = requests.post(
        URL,
        json={
            "prompt": prompt,
            "max_tokens": 10,
            "temperature": 0.0
        }
    )

    print(i + 1, response.status_code, response.json()["latency_ms"])
    time.sleep(0.5)
