def generate_answer(query, chunks):
    """
    Stub: Integrate with OpenAI GPT / LLaMA
    """
    context = " ".join(chunks)
    return f"Answer for: {query} based on context: {context[:200]}..."
