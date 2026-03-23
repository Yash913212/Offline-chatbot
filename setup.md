# Setup Instructions

This document explains how to set up and run the Offline Customer Support Chatbot project.

## Prerequisites

- Python 3.8 or higher
- Ollama installed on your machine
- Internet connection (for initial setup only; chatbot runs offline)

## Step 1: Install Ollama

1. Visit the official [Ollama website](https://ollama.ai)
2. Download the installer for your operating system (macOS, Windows, or Linux)
3. Follow the installation instructions for your platform

### Verify Installation

Open your terminal/command prompt and run:
```bash
ollama --version
```

You should see the version number printed.

## Step 2: Download the Llama 3.2 3B Model

Once Ollama is installed, download the Llama 3.2 3B model. This is approximately 2GB in size and may take several minutes depending on your internet connection.

```bash
ollama pull llama3.2:3b
```

### Test the Model (Optional)

To verify the model works, you can test it interactively:

```bash
ollama run llama3.2:3b
```

You should see a prompt where you can type a message. Type a test query and press Enter. Type `/bye` to exit.

## Step 3: Set Up Python Environment

Navigate to your project directory and create a virtual environment:

### On Linux/macOS:
```bash
cd /path/to/Offline-chatbot
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
cd C:\path\to\Offline-chatbot
python -m venv venv
venv\Scripts\activate
```

## Step 4: Install Python Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install requests
```

The `requests` library is needed to communicate with the Ollama API.

## Step 5: Ensure Ollama is Running

Before running the chatbot, make sure the Ollama server is running:

### On macOS and Windows:
- Open the Ollama application. It should appear as an icon in your menu bar (macOS) or system tray (Windows).

### On Linux:
Check the status of the Ollama service:
```bash
systemctl --user status ollama
```

If it's not running, start it with:
```bash
systemctl --user start ollama
```

If you don't have systemctl (e.g., on a system without systemd), you can start Ollama manually by running the Ollama executable.

## Step 6: Run the Chatbot

With Ollama running and dependencies installed, execute the chatbot script:

```bash
python3 chatbot.py
```

### What to Expect

1. The script will verify the connection to the Ollama server
2. It will load the prompt templates from the `prompts/` directory
3. For each of the 20 customer queries, it will:
   - Generate a zero-shot response (using instructions only)
   - Generate a one-shot response (using instructions + an example)
4. All responses will be logged to `eval/results.md`
5. The script will display progress as it runs

**Note:** Depending on your hardware, this process may take 15-60 minutes. The time depends on:
- CPU speed (running on CPU is slower than GPU)
- RAM available
- System load

## Step 7: Evaluate Results

After the script completes:

1. Open `eval/results.md` in a text editor or Markdown viewer
2. For each response, assign scores (1-5) in the following columns:
   - **Relevance**: How well does the response address the query?
   - **Coherence**: Is the response grammatically correct and clear?
   - **Helpfulness**: Does the response provide useful, actionable information?
3. Save the file

## Step 8: Generate the Report

Based on your manual scoring, create a comprehensive analysis in `report.md`:

- Summarize the quantitative results
- Compare zero-shot and one-shot performance
- Discuss specific examples
- Analyze the suitability of Llama 3.2 3B for customer support
- Document limitations and next steps

## Troubleshooting

### Issue: "Could not connect to Ollama server"

**Solution:** Ensure Ollama is running. Verify that it's accessible at `http://localhost:11434`. You can test this in your browser or with:
```bash
curl http://localhost:11434/api/tags
```

### Issue: "Model not found" error

**Solution:** Ensure you've pulled the model with:
```bash
ollama pull llama3.2:3b
```

Verify it's installed by checking:
```bash
ollama list
```

### Issue: Very slow responses

**Solution:** This is normal when running on CPU. Llama 3.2 3B may take 30-120 seconds per response depending on your hardware. To speed up:
- Close other applications to free up RAM
- Ensure your system is not running other heavy processes
- Consider using a machine with a GPU for faster inference

### Issue: Out of memory errors

**Solution:** The Llama 3.2 3B quantized model requires approximately 2-4GB of RAM. If you're running out of memory:
- Close other applications
- Consider using a smaller model like Phi-3 Mini
- Check available RAM on your system

## Next Steps

After completing the evaluation and scoring:

1. Analyze patterns in model performance
2. Compare zero-shot vs. one-shot results
3. Document findings in `report.md`
4. Consider extensions:
   - Testing different models (e.g., Mistral 7B, Phi-3)
   - Adding few-shot prompting (multiple examples)
   - Integrating with a knowledge base for business-specific information
   - Evaluating response time and resource usage

## Additional Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Llama 3.2 Model Card](https://huggingface.co/meta-llama/Llama-3.2-3B)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

For questions or issues, refer to the README.md or troubleshooting section above.
