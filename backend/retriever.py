from backend.rag.vector_db.faiss_db import search_similar
from backend.llm import generate_answer

def retrieve_answer(query: str):
    relevant_chunks = search_similar(query, top_k=5)
    return generate_answer(query, relevant_chunks)
