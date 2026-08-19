from typing import List
from llama_index.core.schema import Document, TextNode
from llama_index.core.node_parser import SentenceSplitter

def chunk_documents(documents: List[Document]) -> List[TextNode]:
    """Chunk documents into smaller text nodes."""
    splitter = SentenceSplitter(
        chunk_size=512,
        chunk_overlap=64,
        paragraph_separator="\n\n",
    )

    nodes = splitter.split_documents(documents)
    #attach chunk index per source file for context enrichment
    file_chunk_counter:dict = {}
    for node in nodes:
        source = node.metadata.get("file_name", "unknown")
        file_chunk_counter[source] = file_chunk_counter.get(source, 0) + 1
        node.metadata["chunk_index"] = file_chunk_counter[source]

    return nodes