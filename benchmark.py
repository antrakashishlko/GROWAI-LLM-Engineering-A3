import csv
import time
import requests

# -----------------------------
# Ollama API Configuration
# -----------------------------

OLLAMA_URL = "http://localhost:11434/api/generate"

models = [
    "qwen3:0.6b",
    "tinyllama",
    "phi3:mini",
]

# -----------------------------
# Benchmark Prompts
# -----------------------------

prompts = [
    "What is the capital of France?",
    (
        "Classify the sentiment as positive, negative or neutral: "
        "'I really enjoyed this movie and would watch it again.'"
    ),
    (
        "A farmer has 10 apples. He gives 3 apples to his friend and buys "
        "5 more. How many apples does he have now?"
    ),
    (
        "Write a Python function that takes a list of numbers and "
        "returns the largest number."
    ),
    (
        "Write a short creative story about a robot who discovers "
        "a hidden garden."
    ),
]

# -----------------------------
# Benchmark Configuration
# -----------------------------

OUTPUT_FILE = "benchmark_results.csv"
results = []

print("Benchmark setup complete!")

# -----------------------------
# Run Benchmark
# -----------------------------

for model in models:
    print(f"\n===== Testing {model} =====")

    for prompt in prompts:
        print(f"\nPrompt: {prompt}")

        start_time = time.time()

        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=120,
            )

            response.raise_for_status()

            end_time = time.time()
            data = response.json()

            response_text = data.get(
            "response",
            "No response returned.",
            )

            total_duration = data.get(
            "total_duration",
            0,
           )

            response_time = total_duration / 1_000_000

            print("Response:", response_text)
            print(f"Response Time: {response_time:.2f} ms")

            results.append(
                {
                    "model": model,
                    "prompt": prompt,
                    "response": response_text,
                    "response_time_ms": round(response_time, 2),
                    "quality_rating": "",
                }
            )

        except requests.RequestException as error:
            end_time = time.time()

            response_time = (end_time - start_time) * 1000

            print(f"Error: {error}")

            results.append(
                {
                    "model": model,
                    "prompt": prompt,
                    "response": f"Request failed: {error}",
                    "response_time_ms": round(response_time, 2),
                    "quality_rating": "",
                }
            )

# -----------------------------
# Save Results to CSV
# -----------------------------

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8",
) as file:

    fieldnames = [
        "model",
        "prompt",
        "response",
        "response_time_ms",
        "quality_rating",
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
    )

    writer.writeheader()
    writer.writerows(results)

print(f"\nBenchmark results saved to {OUTPUT_FILE}")
