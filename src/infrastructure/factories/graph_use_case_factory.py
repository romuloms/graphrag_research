from src.application.use_cases import TestGraphConnectionUseCase
from src.infrastructure.graph import Neo4jRepository


def get_test_graph_connection_use_case() -> TestGraphConnectionUseCase:
    graph_repository = Neo4jRepository()
    return TestGraphConnectionUseCase(graph_repository=graph_repository)