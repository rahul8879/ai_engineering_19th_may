import os
from pathlib import Path
from typing import List, Optional

from llama_index.core import SimpleDirectoryReader
from llama_index.core.schema import Document



def load_single_resume(file_path: str) -> List[Document]:
    """Load a single resume from a PDF file."""
    path = Path(file_path)
    print(f"Loading resume from: {path}")
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Invalid file type: {file_path}. Only PDF files are supported.")
    reader = SimpleDirectoryReader(input_files=str(path))
    documents = reader.load_data()
    return documents

def load_data(file_path: str) -> List[Document]:
    resume_path = Path(file_path)
    if not resume_path.exists():
        raise FileNotFoundError(f"Resume file not found: {resume_path}")
    pdf_files = list(resume_path.glob("*.pdf"))
    if not pdf_files:
        raise ValueError(f"No PDF files found in {resume_path}")
    reader = SimpleDirectoryReader(
        input_dir = str(resume_path),
        required_exts = [".pdf"],
    )

    document = reader.load_data()
    return document
