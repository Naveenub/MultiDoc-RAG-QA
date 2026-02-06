from fastapi import FastAPI, UploadFile, File
from backend.ingest import ingest_files
from backend.retriever import retrieve_answer

app = FastAPI(title="Multi-Document RAG QA System")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    result = await ingest_files(file)
    return {"message": "File ingested", "details": result}

@app.post("/query")
async def query(question: str):
    answer = retrieve_answer(question)
    return {"question": question, "answer": answer}
