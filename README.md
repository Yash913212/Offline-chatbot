# Offline Customer Support Chatbot

This project shows how to run a customer support chatbot fully offline.
It uses Llama 3.2 3B through Ollama, so customer data stays on your machine.

## Why this project

Many companies must protect customer data under laws like GDPR, CCPA, and DPDP.
Cloud APIs can be risky for sensitive data.
This project explores a local setup as a privacy-friendly option.

## What this project does

- Runs a local LLM using Ollama
- Tests two prompting styles: zero-shot and one-shot
- Saves model responses to `eval/results.md`
- Lets you score responses manually and write analysis in `report.md`

## Project structure

```text
Offline-chatbot/
├── chatbot.py
├── setup.md
├── report.md
├── README.md
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
└── eval/
    └── results.md
```

## Quick start

1. Install Ollama and pull the model:

```bash
ollama pull llama3.2:3b
```

2. Set up Python:

```bash
cd /path/to/Offline-chatbot
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install requests
```

3. Run the evaluation:

```bash
python chatbot.py
```

4. Open `eval/results.md`, score each response (1-5), then update `report.md`.

For full setup help, see `setup.md`.

## How data flows

```text
chatbot.py
  -> http://localhost:11434/api/generate
  -> Ollama (local)
  -> Llama 3.2 3B
  -> response
  -> eval/results.md
```

All processing is local.

## Evaluation method

Two prompting styles are compared:

- `Zero-Shot`: instruction only
- `One-Shot`: instruction + one example

Each response is scored on:

- `Relevance` (does it answer the question?)
- `Coherence` (is it clear and correct language?)
- `Helpfulness` (is it useful and actionable?)

Score each from 1 to 5.

## Expected behavior

- One-shot often gives better formatting and tone consistency.
- Zero-shot can still perform well and sometimes be more direct.
- The model may struggle with real-time facts (current promotions, stock, etc.).

## Limits to keep in mind

1. No real-time access to your order system or inventory
2. Possible hallucinations for unknown policy details
3. Slower responses on CPU
4. Knowledge is limited to training data cutoff

## Ideas to improve

1. Try few-shot prompting (3-5 examples)
2. Add a knowledge base (RAG)
3. Test other models (Mistral, Phi, etc.)
4. Add automated quality checks

## FAQ

Q: Do I need a GPU?
A: No. CPU works, but slower.

Q: Ollama is not responding. What should I check?
A: Confirm Ollama is running and test `curl http://localhost:11434/api/tags`.

Q: Can I switch models?
A: Yes. Update `MODEL_NAME` in `chatbot.py` and pull that model first.

## References

- https://ollama.ai
- https://www.meta.com/ai/llama/
- https://www.promptingguide.ai/
- https://github.com/rkadlec/ubuntu-ranking-dataset

## License

Educational use.
