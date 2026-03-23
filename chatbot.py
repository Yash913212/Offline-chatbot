#!/usr/bin/env python3
"""
Offline Customer Support Chatbot
Evaluates Zero-Shot vs One-Shot Prompting with Llama 3.2 3B
"""

import requests
import json
import time
from datetime import datetime

# Configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:latest"
RESULTS_FILE = "eval/results.md"
ZERO_SHOT_TEMPLATE_PATH = "prompts/zero_shot_template.txt"
ONE_SHOT_TEMPLATE_PATH = "prompts/one_shot_template.txt"

# 20 Adapted E-commerce Queries (from Ubuntu Dialogue Corpus context)
CUSTOMER_QUERIES = [
    "How do I track the shipping status of my recent order?",
    "My discount code is not working at checkout. What should I do?",
    "Can I change my delivery address after placing the order?",
    "What is your return policy for items purchased online?",
    "How long does standard shipping usually take?",
    "I received a damaged item. How do I file a claim?",
    "Is the product available in size XL?",
    "Do you offer international shipping to Canada?",
    "My account password isn't working. How can I reset it?",
    "Can I cancel my order after it's been placed?",
    "Are there any ongoing sales or promotions this month?",
    "How do I apply a gift card to my purchase?",
    "What payment methods do you accept?",
    "Can I combine multiple discount codes on one order?",
    "How do I check my order history?",
    "What's the warranty policy on electronics?",
    "Is customer support available on weekends?",
    "Can I request gift wrapping at checkout?",
    "How do I update my billing address?",
    "What's your policy on price matching with competitors?",
]


def load_template(template_path):
    """Load a prompt template from file."""
    try:
        with open(template_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {template_path}")
        return None


def query_ollama(prompt):
    """
    Send a prompt to the Ollama API and retrieve the model's response.
    
    Args:
        prompt (str): The prompt to send to the model.
    
    Returns:
        str: The model's response text, or an error message if the request fails.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False  # We want the full response at once
    }
    
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=300)
        response.raise_for_status()
        result = json.loads(response.text).get("response", "").strip()
        return result
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama server. Is it running at http://localhost:11434?"
    except requests.exceptions.Timeout:
        return "Error: Request to Ollama server timed out. The model may be taking too long to generate a response."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


def initialize_results_file():
    """Create and initialize the results markdown file with headers and table structure."""
    header = """# Customer Support Chatbot Evaluation Results

## Date: {date}

### Scoring Rubric

- **Relevance (1-5)**: How well does the response address the customer's query? (1 = Irrelevant, 5 = Perfectly relevant)
- **Coherence (1-5)**: Is the response grammatically correct and easy to understand? (1 = Incoherent, 5 = Flawless)
- **Helpfulness (1-5)**: Does the response provide a useful, actionable answer? (1 = Not helpful, 5 = Very helpful)

### Results Table

| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |
|---------|---|---|---|---|---|---|
""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    with open(RESULTS_FILE, 'w') as f:
        f.write(header)


def log_result(query_num, customer_query, method, response):
    """Log a single query result to the results file."""
    # Clean response text for markdown table (remove newlines, limit length)
    clean_response = response.replace('\n', ' ').replace('|', '\\|')
    if len(clean_response) > 150:
        clean_response = clean_response[:147] + "..."
    
    row = f"| {query_num} | {customer_query} | {method} | {clean_response} | | | |\n"
    
    with open(RESULTS_FILE, 'a') as f:
        f.write(row)


def main():
    """Main execution function."""
    print("\n" + "="*70)
    print("OFFLINE CUSTOMER SUPPORT CHATBOT EVALUATION")
    print("="*70)
    print(f"Model: {MODEL_NAME}")
    print(f"Ollama Endpoint: {OLLAMA_ENDPOINT}")
    print(f"Number of Queries: {len(CUSTOMER_QUERIES)}")
    print(f"Results File: {RESULTS_FILE}")
    print("="*70 + "\n")
    
    # Load templates
    print("Loading prompt templates...")
    zero_shot_template = load_template(ZERO_SHOT_TEMPLATE_PATH)
    one_shot_template = load_template(ONE_SHOT_TEMPLATE_PATH)
    
    if not zero_shot_template or not one_shot_template:
        print("Error: Failed to load prompt templates. Exiting.")
        return
    
    print("Templates loaded successfully.\n")
    
    # Initialize results file
    print("Initializing results file...")
    initialize_results_file()
    print(f"Results file created at {RESULTS_FILE}\n")
    
    # Process queries
    print("Starting chatbot evaluation...")
    print("This may take several minutes depending on your hardware.\n")
    
    for idx, query in enumerate(CUSTOMER_QUERIES, 1):
        print(f"Processing Query {idx}/{len(CUSTOMER_QUERIES)}: {query[:60]}...")
        
        # Zero-shot prompting
        print("  - Generating zero-shot response...", end="", flush=True)
        zero_shot_prompt = zero_shot_template.format(query=query)
        zero_shot_response = query_ollama(zero_shot_prompt)
        print(" Done")
        log_result(idx, query, "Zero-Shot", zero_shot_response)
        
        # One-shot prompting
        print("  - Generating one-shot response...", end="", flush=True)
        one_shot_prompt = one_shot_template.format(query=query)
        one_shot_response = query_ollama(one_shot_prompt)
        print(" Done")
        log_result(idx, query, "One-Shot", one_shot_response)
        
        print()
    
    print("="*70)
    print("Evaluation Complete!")
    print(f"Results have been saved to {RESULTS_FILE}")
    print("Next Step: Manually score each response using the rubric provided.")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
