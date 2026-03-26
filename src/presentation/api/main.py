from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Request
from src.application.use_cases import TestGraphConnectionUseCase
from src.infrastructure.factories import get_test_graph_connection_use_case


@asynccontextmanager
async def lifespan(app: FastAPI):
    test_graph_connection_use_case: TestGraphConnectionUseCase = get_test_graph_connection_use_case()
    app.state.test_graph_connection_use_case = test_graph_connection_use_case

    try:
        await test_graph_connection_use_case.verify_connectivity()
        print("Successfully connected to Neo4j")
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}")

    try:
        yield
    finally:
        await test_graph_connection_use_case.close()


app = FastAPI(title="GraphRAG API", lifespan=lifespan)


def get_test_graph_connection_use_case_dependency(request: Request) -> TestGraphConnectionUseCase:
    return request.app.state.test_graph_connection_use_case

@app.get("/health")
async def health_check():
    return {
        "status": "online", 
        "project": "Microsserviços + RAG + Knowledge Graph", 
        "institution": "COPIS/STI/UFS" 
    }

@app.post("/test-graph")
async def test_graph(
    test_graph_connection_use_case: TestGraphConnectionUseCase = Depends(
        get_test_graph_connection_use_case_dependency
    ),
):
    try:
        await test_graph_connection_use_case.create_test_node()
        return {"message": "Nó criado com sucesso no Neo4j!"}
    except Exception as e:
        return {"error": str(e)}