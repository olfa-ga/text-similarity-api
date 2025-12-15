# Text Similarity API

---

## Description

**Text Similarity API** is a RESTful API built with **FastAPI** that leverages **Natural Language Processing (NLP)** techniques using **Sentence Transformers** to compute semantic similarity between two texts by converting them into embeddings and measuring their semantic closeness.

**Key features:**
- Compute semantic similarity with `all-MiniLM-L6-v2`.
- Simple REST API with FastAPI.
- Dockerized for easy deployment and development.

---

## Installation 

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
---
