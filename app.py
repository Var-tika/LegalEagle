import os
import streamlit as st
from backend import ingest_pdf, load_vectordb, build_qa_chain


st.set_page_config(page_title="LegalEagle", layout="wide")
st.title("🦅 LegalEagle — AI Contract Assistant")

st.markdown(
    """
    **LegalEagle** is an AI-powered assistant for legal documents... Upload contracts, agreements, or policies and ask questions in plain English...The app retrieves the most relevant clauses and explains them clearly with citations.     
    """
)


os.makedirs("contracts", exist_ok=True)


groq_api_key = st.text_input(
    "🔑 Enter your Groq API Key",
    value=os.getenv("GROQ_API_KEY", ""),
    type="password",
)
if not groq_api_key:
    st.warning("Please enter your Groq API key to continue.")
elif not groq_api_key.isascii():
    st.error(
        "The Groq API key contains non-ASCII characters. "
        "Please paste the key exactly as shown in your Groq account."
    )


uploaded = st.file_uploader("📂 Upload a contract / legal document", type=["pdf"])
if uploaded:
    file_path = f"contracts/{uploaded.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded.getbuffer())
    try:
        vectordb = ingest_pdf(file_path)
        st.success(f"✅ {uploaded.name} uploaded & indexed.")
    except Exception as exc:
        vectordb = None
        st.error(f"Could not process {uploaded.name}: {exc}")
else:
    try:
        vectordb = load_vectordb()
    except Exception:
        vectordb = None
        st.warning("⚠️ No documents indexed yet. Please upload a PDF.")


if vectordb and groq_api_key and groq_api_key.isascii():
    qa = build_qa_chain(vectordb, groq_api_key)  # pass API key
    query = st.text_input("💬 Ask a question about your contract")
    if query:
        try:
            result = qa(query)
        except Exception as exc:
            st.error(f"Could not get an answer from Groq: {exc}")
        else:
            st.subheader("📖 Answer")
            st.write(result["result"])

            st.subheader("📑 Sources")
            for doc in result["source_documents"]:
                st.markdown(
                    f"📄 **Page {doc.metadata.get('page', '?')}**\n\n"
                    f"{doc.page_content[:500]}..."
                )
