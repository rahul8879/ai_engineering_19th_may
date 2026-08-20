from pathlib import Path
from .loader import load_data,load_single_resume
from .chunker import chunk_documents
from .metadata import build_candidate_id
from .embedder import embed_texts
from .vector_store import upsert_chunks
def ingest_resume(file_path: str) -> dict:
    """
      Steps:
    1. Load PDF → LlamaIndex Documents
    2. Chunk documents → TextNodes
    3. Extract email → candidate_id
    4. Embed chunks → dense vectors
    5. Upsert to Pinecone
    
    """

    file_name = Path(file_path).name
    print(f"\nProcessing: {file_name}")
    # step 1: load data
    documents = load_single_resume(file_path)
    # step 2: split into chunks
    nodes = chunk_documents(documents)

    # step 3 : Extract candidate id from full text
    full_text = " ".join([doc.text for doc in documents])
    candidate_id = build_candidate_id(full_text,file_name)

    print(f"  candidate_id: {candidate_id}")
    # Step 4 — Deduplication
    # was_existing = handle_deduplication(candidate_id)
    chunk_texts = [node.text for node in nodes]
    embeddings = embed_texts(chunk_texts)
    metadata_list= [node.metadata for node in nodes]

    # Step 5 — Embed all chunks
    upsert_chunks(
        candidate_id=candidate_id,
        chunks=chunk_texts,
        embeddings=embeddings,
        metadata_list=metadata_list,
    )
    result = {
        "candidate_id": candidate_id,
        "file_name": file_name,
        "chunks": len(nodes),
        "status": "success"
    }
    print(f"  Result: {result}")

    return result

  # Result: {'candidate_id': 'andrew.green@email.com',
  #          'file_name': 'Andrew_Green_Resume_27.pdf',
  #          'chunks': 2, 'status': 'success'}


if __name__ == "__main__":
    #python -m ingestions.pipeline   (from the HireFlow/ directory)
    ingest_resume("resume/Angela_Lewis_Resume_09.pdf")