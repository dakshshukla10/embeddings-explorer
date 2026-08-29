# Embeddings Explorer

A small Python project for exploring word embeddings and semantic similarity with Gensim.

## Requirements

Use Python 3.12 or 3.13. This project does not currently work on Python 3.14 because Gensim fails to build there.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/explore_embeddings.py
```

If you already created `.venv` with Python 3.14, delete it and recreate the environment with a supported interpreter before installing dependencies.

The script loads a pre-trained Twitter GloVe model and prints the vector details and nearest words for `king`.
