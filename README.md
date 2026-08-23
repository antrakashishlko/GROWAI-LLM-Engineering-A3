# GROWAI LLM Engineering - Assignment 3

## Local LLM Benchmarker

This project demonstrates how to benchmark and compare multiple open-source Large Language Models running locally through Ollama. The same set of five prompts is given to three different models, and their response time and output quality are evaluated.

## Description

This project implements a local Large Language Model (LLM) benchmarking system using Python and Ollama.The benchmark evaluates three different open-source Ollama models using the same set of five prompts. The prompts test different capabilities, including factual knowledge, sentiment classification, mathematical reasoning, Python code generation, and creative writing.For each model-prompt combination, the system records the generated response and response time. The results are saved in a CSV file, where the responses can be manually evaluated using a quality rating from 1 to 5.

## Features

- Benchmarks three local Ollama LLMs:
  - Qwen3 0.6B
  - TinyLlama
  - Phi3 Mini
    
- Uses the same five prompts for every model
- Tests different LLM capabilities
- Sends requests to the local Ollama `/api/generate` endpoint
- Measures model response time
- Captures the generated response
- Handles API request errors and timeouts
- Stores benchmark results in CSV format
- Supports manual quality ratings from 1 to 5
- Enables comparison of model speed and response quality

## Technologies Used

- Python
- Ollama
- Requests Library
- CSV File Handling
- Local Open-Source LLMs
  
## Requirements

- Python 3.x
- Ollama
- `requests`

The required Python dependency can be installed using:
```text
pip install -r requirements.txt
```

The following Ollama models are required:
ollama pull qwen3:0.6b
ollama pull tinyllama
ollama pull phi3:mini

## Setup/Installation

1. Install Python
Install Python 3.x and verify the installation:
```text
python --version 
```

3. Install Ollama
Install Ollama and ensure that the Ollama service is running locally.
The API used by this project is:
```text
http://localhost:11434/api/generate 
```

5. Download the Models
Pull the three benchmark models:
ollama pull qwen3:0.6b
ollama pull tinyllama
ollama pull phi3:mini

7. Install Python Dependencies
Open the project directory in a terminal and run:
```text
pip install -r requirements.txt
```

## How to Run

Execute the benchmark script:
```text
python benchmark.py
```

The program runs five prompts against each of the three models, resulting in a total of 15 model-prompt evaluations.

For every evaluation, the program records:
- Model name
- Prompt
- Generated response
- Response latency in milliseconds

After execution, the complete results are saved to:
```text
benchmark_results.csv
```

The quality_rating field is manually evaluated after reviewing each generated response. Ratings range from 1 to 5, where a higher score represents better correctness, relevance, and overall response quality.

## Project Files

- `benchmark.py`– Main benchmarking script that communicates with the Ollama API, runs the prompts, measures latency, and collects results.
- `benchmark_results.csv`– Complete benchmark dataset containing model responses, response times, and manual quality ratings.
- `requirements.txt`– Python dependency required to run the benchmarking script.

## Benchmark Results

The benchmark uses five prompts representing different task categories:
- Factual Question – Tests general knowledge.
- Sentiment Classification – Tests basic text classification.
- Mathematical Reasoning – Tests logical and arithmetic reasoning.
- Code Generation – Tests Python code-generation capability.
- Creative Writing – Tests creative language generation.

The benchmark produced the following observations:
- `Qwen3 0.6B`generated consistently accurate and detailed responses and received high quality ratings, although its response latency was comparatively higher.
- `TinyLlama`demonstrated significantly lower latency on several prompts but produced an incorrect answer for the mathematical reasoning task, showing that faster inference does not always result in better output quality.
- `Phi3 Mini`performed well on factual, reasoning, and creative tasks. However, its generated Python code contained an incorrect function call, reducing its quality for the coding task.

These results demonstrate the practical trade-off between latency and response quality when selecting an LLM for a specific application.

## Real-World Relevance

LLM benchmarking is useful when selecting a model for production applications.For example, a customer-support system may prioritize low latency to provide fast responses, while a coding assistant or analytical application may prioritize accuracy and response quality.This project demonstrates a simplified version of the evaluation process used by engineers to select an appropriate model based on application requirements, performance constraints, and output quality.

## Edge Case

A potential failure point is the unavailability of the Ollama server, an incorrectly installed model, or a request that exceeds the configured timeout.The implementation handles HTTP request failures using exception handling and records the failure in the benchmark results instead of terminating the entire benchmarking process.

## Assignment
GROWAI LLM Engineering & Generative AI – Assignment 3
