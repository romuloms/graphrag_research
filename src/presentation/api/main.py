from fastapi import FastAPI
from src.infrastructure.graph import Neo4jRepository


app = FastAPI(title="GraphRAG API")

graph_repo = Neo4jRepository()

@app.on_event("startup")
async def startup():
    # Isso ajuda a validar a Tarefa 1.2 automaticamente
    try:
        await graph_repo.verify_connectivity()
        print("Successfully connected to Neo4j")
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}")

@app.on_event("shutdown")
async def shutdown():
    await graph_repo.close()

@app.get("/health")
async def health_check():
    return {
        "status": "online", 
        "project": "Microsserviços + RAG + Knowledge Graph", 
        "institution": "COPIS/STI/UFS" # 
    }

@app.post("/test-graph")
async def test_graph():
    test_properties = {
        "id": "teste-001",
        "nome": "Nó de Teste STI",
        "descricao": "Validando a conexão do protótipo"
    }
    try:
        await graph_repo.create_node("Teste", test_properties)
        return {"message": "Nó criado com sucesso no Neo4j!"}
    except Exception as e:
        return {"error": str(e)}