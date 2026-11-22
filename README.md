<div align="center">

# LegalEagle — AI Contract Assistant

### Making Legal Documents Understandable, Searchable, and Actionable

</div>

---

## Overview

**LegalEagle** is an AI-powered legal assistant designed to analyze contracts, agreements, and legal documents with speed and precision.

By integrating **FAISS vector search, Hugging Face embeddings, and Groq’s high-performance LLM API**, the system enables users to extract insights, ask contextual questions, and understand complex legal content in seconds.

The goal is to reduce the friction of legal comprehension and make **contract intelligence accessible to everyone**.

---

## Key Features

* 📄 **Contract Upload** → Upload legal PDFs (agreements, policies, contracts)
* 🔎 **AI-Powered Q&A** → Ask questions in natural language and receive contextual answers
* 📚 **Source Attribution** → View exact references from the document
* ⚡ **High-Performance Stack** → Fast embeddings + ultra-low latency inference
* 🔐 **Secure API Usage** → User-provided Groq API key at runtime
* 🎯 **User-Friendly Interface** → Simple and intuitive experience

---

## System Architecture

```
PDF Upload → Text Extraction → Embeddings (HuggingFace)
        ↓
     FAISS Vector Store
        ↓
User Query → LangChain Pipeline → Groq LLM → Contextual Answer
```

---

## Tech Stack

* **Frontend**: Streamlit (Python-based UI)
* **Backend**: LangChain + FAISS (vector search)
* **Embeddings**: SentenceTransformers (Hugging Face)
* **LLM**: Groq API (high-speed inference)
* **Storage**: FAISS index + local document storage

---

## Deployment

This project uses Streamlit and should be deployed on a platform that runs a
persistent Streamlit server, such as [Streamlit Community Cloud](https://share.streamlit.io/).
Vercel's Python runtime expects an HTTP function export (`app`, `application`,
or `handler`) and does not run this Streamlit application directly.

To deploy on Streamlit Community Cloud:

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, create an app from the repository's `main`
   branch and set the app file to `app.py`.
3. Deploy. The platform installs the dependencies from `requirements.txt`.
4. Enter a Groq API key in the app when prompted.

You can also configure `GROQ_API_KEY` as an environment variable on a hosting
platform that supports it; the app will use it as the initial key field value.
Uploaded contracts and the generated FAISS index are stored on the app's local
filesystem, so they may not persist across redeployments or restarts. Do not
upload documents unless you are comfortable with the hosting provider handling
them.

---

## Use Cases

### 🏛️ Legal Professionals

* Rapid contract review
* Identification of clauses, risks, and obligations
* Reduced manual workload

### 📑 Businesses & Startups

* Faster due diligence for agreements
* Improved compliance checks
* Risk minimization in contracts

### 👨‍💼 General Users

* Understand legal documents in simple language
* Analyze employment, rental, or policy documents
* Access legal insights without specialized knowledge

---

## Engineering Approach

### Retrieval-Augmented Generation (RAG)

LegalEagle uses a RAG-based pipeline to ensure responses are:

* Contextually grounded
* Factually aligned with uploaded documents
* Traceable via source references

### Modular Design

* Document ingestion and processing
* Embedding and indexing
* Query handling and response generation

### Performance Optimization

* FAISS for efficient similarity search
* Groq for low-latency inference

---

## What This Project Demonstrates

* End-to-end LLM application development
* Implementation of RAG pipelines
* Integration of vector databases (FAISS)
* Real-world AI system for document intelligence
* Focus on usability + performance

---

## Future Scope

* Multi-document querying and comparison
* Advanced clause detection and summarization
* Integration with legal databases and APIs
* Voice-based legal assistant
* Deployment as SaaS platform

---

## Vision

LegalEagle aims to democratize legal understanding:

* Make contracts transparent and accessible
* Reduce dependency on expensive legal reviews
* Enable faster, smarter decision-making

In the long term, it can evolve into a **universal legal intelligence system** integrated across businesses, startups, and public platforms.

---

<div align="center">

### "Transforming legal complexity into clarity with AI."

</div>

