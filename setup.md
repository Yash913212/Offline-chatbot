# Setup Guide (Simple)

Follow these steps to run the offline chatbot project.

## What you need first

- Python 3.8+
- Ollama installed
- Internet once, to download the model

## 1. Install Ollama

Download and install from `https://ollama.ai`.

Check installation:

```bash
ollama --version
```

## 2. Download the model

```bash
ollama pull llama3.2:3b
```

Optional test:

```bash
ollama run llama3.2:3b
```

Type a message to test, then use `/bye` to exit.

## 3. Create Python environment

Linux/macOS:

```bash
cd /path/to/Offline-chatbot
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
cd C:\path\to\Offline-chatbot
python -m venv venv
venv\Scripts\activate
```

## 4. Install dependency

```bash
pip install requests
```

## 5. Make sure Ollama is running

Linux check:

```bash
systemctl --user status ollama
```

Start if needed:

```bash
systemctl --user start ollama
```

If `systemctl` is not available, start Ollama manually.

## 6. Run the script

```bash
python3 chatbot.py
```

What happens:

1. The script checks Ollama connection.
2. It loads prompt templates.
3. It runs 20 queries with zero-shot and one-shot prompts.
4. It saves output to `eval/results.md`.

Runtime can be 15 to 60 minutes depending on your machine.

## 7. Score the results

Open `eval/results.md` and fill scores (1 to 5):

- Relevance
- Coherence
- Helpfulness

## 8. Write report

Use your scores to update `report.md`.

Include:

- average scores
- zero-shot vs one-shot comparison
- strengths and weak points
- final recommendation

## Troubleshooting

Issue: Cannot connect to Ollama

- Check server: `curl http://localhost:11434/api/tags`
- Ensure Ollama is running

Issue: Model not found

- Run: `ollama pull llama3.2:3b`
- Verify: `ollama list`

Issue: Too slow

- CPU inference is usually slow
- Close heavy apps
- Use GPU if possible

Issue: Out of memory

- Llama 3.2 3B usually needs about 2 to 4 GB RAM
- Close apps or try a smaller model

## Useful links

- https://github.com/ollama/ollama
- https://huggingface.co/meta-llama/Llama-3.2-3B
- https://www.promptingguide.ai/
