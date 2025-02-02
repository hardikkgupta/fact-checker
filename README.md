# fact-checker
RAG system that lets you ask questions about Tim Walz and receive concise fact-checking answers with sources. It leverages a FAISS index to retrieve relevant context from pre-collected statements and a locally saved language model (using Hugging Face Transformers) to generate responses. The user interface is built with Streamlit.

[![Watch the video](https://img.youtube.com/vi/T2Sik5N8M1E/0.jpg)](https://www.youtube.com/watch?v=T2Sik5N8M1E)


## Features
- FAISS Retrieval: Efficiently retrieves the most relevant context statements using vector similarity search.
- LLM: Uses a language model to generate fact-checking answers.
- Streamlit Chat Interface: Provides an interactive, chat-style UI for asking questions and viewing responses.
- Concise Output: Processes the generated answer to display only the final YES/NO decision along with one key supporting statement.

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/fact-checker.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run `build_index.py` script for creating and saving an efficient similarity search index using FAISS.
```bash
python build_index.py
```
4. Downloads a model and tokenizer from Hugging Face, then stores them in a local directory
```bash
python save_model.py
```
## Running Locally
Launces app.py and `fact_checker.py`
```bash
streamlit run /Users/hardikgupta/Documents/Projects/model/app.py
```

## Troubleshooting
Confirm that the directory contains the necessary files (`faiss_index.bin`, `statements.pkl`, `my_local_model/`). If not, follow the instructions again provided in the project documentation to generate or download these files.

Contributions are welcome!