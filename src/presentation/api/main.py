from fastapi import FastAPI
from src.application.use_cases import TestGraphConnectionUseCase
from src.infrastructure.factories import get_test_graph_connection_use_case


app = FastAPI(title="GraphRAG API")

test_graph_connection_use_case: TestGraphConnectionUseCase = get_test_graph_connection_use_case()

@app.on_event("startup")
async def startup():
    try:
        await test_graph_connection_use_case.verify_connectivity()
        print("Successfully connected to Neo4j")
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}")

@app.on_event("shutdown")
async def shutdown():
    await test_graph_connection_use_case.close()

@app.get("/health")
async def health_check():
    return {
        "status": "online", 
        "project": "Microsserviços + RAG + Knowledge Graph", 
        "institution": "COPIS/STI/UFS" 
    }

@app.post("/test-graph")
async def test_graph():
    try:
        await test_graph_connection_use_case.create_test_node()
        return {"message": "Nó criado com sucesso no Neo4j!"}
    except Exception as e:
        return {"error": str(e)}