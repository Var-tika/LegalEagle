⚖️ LegalEagle

«An AI-powered legal document assistant designed to make complex legal documents easier to understand.»

""Open App" (https://img.shields.io/badge/Live%20App-Streamlit-red?logo=streamlit)" (https://legaleaglee.streamlit.app/)

🌐 Live Demo

🚀 Try LegalEagle here: https://legaleaglee.streamlit.app/

📌 About

LegalEagle is an AI-powered legal document assistant that helps users interact with and understand legal documents. It leverages Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and provide context-based responses to user queries.

The application combines document processing, semantic search, and language models to make legal information easier to access and understand.

✨ Features

- 📄 PDF Document Processing – Extract and process text from legal documents.
- 🔍 Semantic Search – Retrieve relevant information based on the meaning of user queries.
- 🧠 Retrieval-Augmented Generation (RAG) – Generate responses grounded in retrieved document context.
- 💬 Interactive Question Answering – Ask questions about the uploaded legal documents.
- ⚡ Efficient Retrieval – FAISS-based vector search for retrieving relevant document chunks.
- 🖥️ Interactive UI – Built with Streamlit for a simple user experience.

🛠️ Tech Stack

Technology| Purpose
Python| Core development
Streamlit| User interface
LangChain| RAG pipeline orchestration
FAISS| Vector similarity search
Sentence Transformers| Text embeddings
PyPDF| PDF text extraction

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/LegalEagle.git
cd LegalEagle

2. Create a virtual environment

python -m venv venv

3. Activate the environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Run the application

streamlit run app.py

The application will open in your browser.

📂 Project Structure

LegalEagle/
│
├── app.py
├── backend.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

🔄 How It Works

1. Upload a legal document.
2. Extract text from the uploaded PDF.
3. Split the extracted text into smaller chunks.
4. Generate embeddings for document chunks.
5. Store embeddings in FAISS for efficient retrieval.
6. Retrieve relevant chunks based on the user's query.
7. Generate a contextual response using the RAG pipeline.

⚠️ Disclaimer

LegalEagle is an AI-powered tool intended for informational and educational purposes only. Its responses should not be considered a substitute for professional legal advice. Always consult a qualified legal professional for advice regarding legal matters.

🌟 Support

If you find this project useful, consider giving the repository a star!

---

Built with Python, LangChain, FAISS and Streamlit. ⚖️
