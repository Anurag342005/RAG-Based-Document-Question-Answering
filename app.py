import os
import time
import streamlit as st

from utils.parser import PDFParser
from utils.chunker import TextChunker
from utils.vectorstore import VectorStore
from utils.retriever import Retriever
from utils.reranker import Reranker
from utils.llm import LLM

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="RAG Document QA",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.stChatMessage{
    border-radius:10px;
    padding:12px;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------------
# Session State
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.title("📄 Document QA")

    uploaded_files = st.file_uploader(
        "Upload PDF(s)",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.success("Chat Cleared")

    if st.button("🗑 Clear Database"):

        import shutil

        if os.path.exists("chroma_db"):
            shutil.rmtree("chroma_db")

        os.makedirs("chroma_db", exist_ok=True)

        st.success("Vector Database Cleared")

    # ============================
    # Statistics (Button ke bahar)
    # ============================

    st.markdown("---")
    st.subheader("⚙️ Configuration")

    st.write("**Embedding Model**")
    st.code("nomic-ai/nomic-embed-text-v1.5")

    st.write("**Reranker**")
    st.code("cross-encoder/ms-marco-MiniLM-L-6-v2")

    st.write("**LLM**")
    st.code("openai/gpt-oss-120b")
    
    st.subheader("📊 Statistics")

    pdf_count = len(uploaded_files) if uploaded_files else 0

    st.metric("📄 PDFs", pdf_count)

    if os.path.exists("chroma_db"):
        st.success("✅ Database Ready")
    else:
        st.warning("⚠️ Database Empty")

# -----------------------------------
# Title
# -----------------------------------

st.title("🤖 RAG Based Document Question Answering")

st.markdown("---")

# -----------------------------------
# Upload + Index
# -----------------------------------

if uploaded_files:

    all_chunks = []

    parser = PDFParser()
    chunker = TextChunker()

    progress = st.progress(0)

    for i, pdf in enumerate(uploaded_files):

        pdf_path = os.path.join(
            "data",
            pdf.name
        )

        with open(pdf_path, "wb") as f:
            f.write(pdf.getbuffer())

        docs = parser.load_pdf(pdf_path)

        chunks = chunker.split_documents(docs)

        all_chunks.extend(chunks)

        progress.progress((i + 1) / len(uploaded_files))

    VectorStore().create_vectorstore(all_chunks)

    st.success(f"✅ Indexed {len(uploaded_files)} PDF(s)")

# -----------------------------------
# Chat UI
# -----------------------------------

st.markdown("---")

# Previous chat show karo
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask a question from the document...")

if question:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            start = time.time()

            retriever = Retriever()
            retrieved_docs = retriever.retrieve(question)

            reranker = Reranker()
            top_docs = reranker.rerank(question, retrieved_docs)

            llm = LLM()
            answer = llm.generate(question, top_docs)

            end = time.time()

        st.markdown(answer)

        st.caption(f"⏱ Response Time : {end-start:.2f} sec")

        st.markdown("### 📄 Sources")

        shown = set()

        for doc in top_docs:

            key = (
                doc.metadata["source"],
                doc.metadata["page"]
            )

            if key not in shown:

                shown.add(key)

                with st.expander(
                    f"📄 {os.path.basename(doc.metadata['source'])} | Page {doc.metadata['page']+1}"
                ):

                    st.write(doc.page_content)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.info(f"Retrieved Documents : {len(retrieved_docs)}")

    st.info(f"Reranked Documents : {len(top_docs)}")