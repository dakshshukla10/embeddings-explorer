# Embeddings Explorer

> A visual playground and analysis tool for high-dimensional vector embeddings and semantic search.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)

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
