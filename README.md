# Offline Customer Support Chatbot

A practical project demonstrating the deployment and evaluation of a local Large Language Model (LLM) for privacy-preserving customer support automation. This chatbot uses Meta's Llama 3.2 3B model running via Ollama, ensuring all customer interactions remain on your local machine—no data is sent to external servers.

## Project Overview

### Motivation

In the age of GDPR, CCPA, and other data protection regulations, processing customer data through cloud-based APIs poses significant legal and security risks. This project demonstrates how companies can leverage powerful AI while maintaining complete data privacy by running LLMs locally.

### What You'll Learn

- **LLM Deployment**: Set up and run open-source models locally using Ollama
- **Prompt Engineering**: Compare zero-shot vs. one-shot prompting techniques
- **Model Evaluation**: Manually assess model performance using a structured rubric
- **System Architecture**: Understand the data flow in an offline AI system

### Key Technologies

- **Ollama**: Open-source tool for running LLMs locally
- **Llama 3.2 3B**: Meta's efficient 3-billion parameter language model
- **Python**: For orchestrating API calls and logging results
- **Ubuntu Dialogue Corpus**: Dataset of realistic support conversations

## Project Structure

```
Offline-chatbot/
├── chatbot.py                # Main script (orchestrates evaluation)
├── setup.md                  # Installation and setup guide
├── report.md                 # Final analysis and report (created after evaluation)
├── README.md                 # This file
├── prompts/
│   ├── zero_shot_template.txt    # Prompt template without examples
│   └── one_shot_template.txt     # Prompt template with one example
└── eval/
    └── results.md            # Detailed results log (created during execution)
```

## Quick Start

### 1. Install Ollama and Download the Model
```bash
# Visit https://ollama.ai and download Ollama for your OS
# Then pull the Llama 3.2 3B model
ollama pull llama3.2:3b
```

### 2. Set Up Python Environment
```bash
cd /path/to/Offline-chatbot
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install requests
```

### 3. Run the Chatbot
```bash
python chatbot.py
```

The script will evaluate 20 customer support queries using both zero-shot and one-shot prompting, logging results to `eval/results.md`.

### 4. Score and Analyze Results
- Open `eval/results.md` and manually assign scores (1-5) for each metric
- Create a comprehensive analysis in `report.md`

For detailed setup instructions, see [setup.md](setup.md).

## System Architecture

```
chatbot.py (Your Script)
    ↓
HTTP POST Request to http://localhost:11434/api/generate
    ↓
Ollama Server (Running Locally)
    ↓
Llama 3.2 3B Model (Inference Engine)
    ↓
Generated Text Response
    ↓
eval/results.md (Logged Results)
```

All communication happens locally. No customer data leaves your machine.

## Evaluation Methodology

### Prompting Techniques Compared

**Zero-Shot Prompting**: The model is given instructions and a query, but no examples. It must infer the desired output format and style.

**One-Shot Prompting**: The model is provided with one complete example of a query-response pair before being asked to respond to the actual query. This helps guide the model's behavior.

### Scoring Rubric

Each response is evaluated on three dimensions:

| Metric | Scale | Definition |
|--------|-------|-----------|
| **Relevance** | 1-5 | How well the response addresses the customer's query (1 = Irrelevant, 5 = Perfectly relevant) |
| **Coherence** | 1-5 | Grammatical correctness and clarity (1 = Incoherent, 5 = Flawless) |
| **Helpfulness** | 1-5 | Usefulness and actionability of the response (1 = Not helpful, 5 = Very helpful) |

### Test Queries

The 20 queries are adapted from the Ubuntu Dialogue Corpus, a real dataset of technical support conversations. Examples of adapted queries:

- "How do I track the shipping status of my recent order?"
- "My discount code is not working at checkout. What should I do?"
- "Can I change my delivery address after placing the order?"
- "What is your return policy for items purchased online?"

(See full list in [chatbot.py](chatbot.py))

## Key Files Explained

### chatbot.py
The main orchestration script. It:
- Loads prompt templates from the `prompts/` directory
- Iterates through 20 customer queries
- Sends each query to the Ollama server using both zero-shot and one-shot templates
- Logs all responses to `eval/results.md`

### prompts/zero_shot_template.txt
Provides role assignment and instructions without examples. The model must infer the desired output style.

### prompts/one_shot_template.txt
Includes role assignment, instructions, and one complete example. The example helps the model understand the expected tone, format, and level of detail.

### eval/results.md
A markdown table containing:
- Query number and text
- Prompting method (Zero-Shot or One-Shot)
- Full response text
- Scoring columns (Relevance, Coherence, Helpfulness) to be manually filled

### report.md
Your comprehensive analysis document covering:
- Methodology & approach
- Quantitative results (average scores per technique)
- Qualitative analysis with specific examples
- Conclusions about model suitability
- Limitations and future improvements

## Expected Results

Based on typical experiments with Llama 3.2 3B:

- **Zero-shot responses**: Often more generic; may lack specific formatting
- **One-shot responses**: Typically more structured; better alignment with the example style
- **Common challenges**: Potential hallucinations about return policies or specific details the model wasn't trained on
- **Strengths**: Good at general customer service tasks, friendly tone, coherent responses

Your actual results may vary based on the specific queries, templates, and how you score them.

## Performance Notes

- **Processing time**: 15-60 minutes for all 20 queries (2 responses each) on typical hardware
- **Hardware**: Works on CPU; GPU support would be faster (NVIDIA CUDA, AMD ROCm)
- **Memory usage**: ~2-4GB RAM for the quantized Llama 3.2 3B model
- **Network**: All processing is local; no internet required after model download

## Limitations and Considerations

1. **No Real-Time Data**: The model cannot access current order databases, inventory, or pricing
2. **Potential Hallucinations**: LLMs can confidently state incorrect information about policies or details
3. **Context Window**: The model can only process a limited amount of text at once (~8K tokens for this model)
4. **Latency**: Expect several seconds per response on CPU
5. **Knowledge Cutoff**: The model's training data has a knowledge cutoff date (before it cannot answer about recent events)

## Next Steps and Extensions

1. **Test Different Models**: Compare with Mistral 7B, Phi-3 Mini, or other open-source models
2. **Few-Shot Prompting**: Provide multiple examples instead of just one
3. **Knowledge Integration**: Add a retrieval system to feed the model business-specific documents
4. **A/B Testing**: Serve both prompting styles to real users and measure satisfaction
5. **Fine-Tuning**: Adapt Llama 3.2 specifically for your business domain
6. **Evaluation Metrics**: Implement automated metrics (BLEU, ROUGE) alongside manual scoring

## FAQ

**Q: Do I need a GPU?**  
A: No, but GPU will make responses faster. The 3B quantized model runs on CPU, though it may be slow.

**Q: What if Ollama isn't responding?**  
A: Ensure it's running (check system tray/menu bar). Verify with `curl http://localhost:11434/api/tags`.

**Q: Can I use a different model?**  
A: Yes! Ollama supports many models. Change the `MODEL_NAME` in `chatbot.py` and pull the model first.

**Q: How do I improve the responses?**  
A: Experiment with different prompts, add more examples, or try larger models with more compute resources.

## References

- [Ollama](https://ollama.ai)
- [Meta Llama 3.2](https://www.meta.com/ai/llama/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Ubuntu Dialogue Corpus](https://github.com/rkadlec/ubuntu-ranking-dataset)
- [GDPR & Data Protection](https://gdpr-info.eu/)

## License

This project is educational and open for learning and experimentation.

---

**Ready to get started?** Check out [setup.md](setup.md) for detailed installation instructions.
