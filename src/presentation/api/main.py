from fastapi import FastAPI
from src.infrastructure.graph import Neo4jRepository


app = FastAPI(title="GraphRAG API")

graph_repo = Neo4jRepository()

@app.get("/health")
async def health_check():
  return {"status": "online", "project": "IA-STI-UFS"}

@app.on_event("shutdown")
async def shutdown():
  await graph_repo.close()