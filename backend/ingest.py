from backend.utils.file_loader import load_file
from backend.utils.text_splitter import chunk_text
from backend.utils.embedding_utils import create_embeddings, insert_to_vector_db

async def ingest_files(file):
    content = load_file(file)
    chunks = chunk_text(content)
    embeddings = create_embeddings(chunks)
    insert_to_vector_db(embeddings)
    return {"chunks_added": len(chunks)}
