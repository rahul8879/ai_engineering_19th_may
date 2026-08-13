from dotenv import load_dotenv
load_dotenv()
import json
from datetime import datetime
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

PDF_FOLDER ='./bajaj_pdfs'
CHROMA_DIR = './bfl_db'
COLLECTION_NAME = 'bfl_policy'
LOG_FILE = './data_pipeline.log'

CHUNK_SIZE = 500
CHUNK_OVERLAP = 0



def load_and_chunk(filepath):
    loader = PyPDFLoader(filepath)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(docs)
    for chunk in chunks:
        chunk.metadata['source'] = Path(filepath).name
        chunk.metadata['ingested_on'] = datetime.now().isoformat()
    return chunks



def run_pipeline(file_path):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma(collection_name=COLLECTION_NAME,
                         embedding_function=embeddings,
                         persist_directory=CHROMA_DIR)

    print("Chroma DB loaded", vectorstore._collection.count())
    chunks = load_and_chunk(file_path)
    vectorstore.add_documents(chunks)
    print("Documents added to Chroma DB")


run_pipeline('bajaj_finance_policy_prose_v1.pdf')