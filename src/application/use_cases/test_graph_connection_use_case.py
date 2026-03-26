from src.domain.interfaces import IGraphRepository


class TestGraphConnectionUseCase:

    def __init__(self, graph_repository: IGraphRepository) -> None:
        self._graph_repository = graph_repository

    async def verify_connectivity(self) -> None:
        await self._graph_repository.verify_connectivity()

    async def create_test_node(self) -> None:
        test_properties = {
            "id": "teste-001",
            "nome": "Nó de Teste STI",
            "descricao": "Validando a conexão do protótipo",
        }
        await self._graph_repository.create_node("Teste", test_properties)

    async def close(self) -> None:
        await self._graph_repository.close()