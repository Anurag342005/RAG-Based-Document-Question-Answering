from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


class PDFParser:
    """
    PDF Parser using PyPDFLoader.
    Returns LangChain Document objects with metadata.
    """

    def __init__(self):
        pass

    def load_pdf(self, pdf_path: str) -> List[Document]:

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

        loader = PyPDFLoader(str(pdf_path))

        documents = loader.load()

        return documents