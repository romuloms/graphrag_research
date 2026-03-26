from neo4j import AsyncGraphDatabase
from src.domain.interfaces import IGraphRepository
from src.domain.exceptions.repository_exceptions import DatabaseOperationError
from src.infrastructure.config import settings


class Neo4jRepository(IGraphRepository):

  def __init__(self):
    self.driver = AsyncGraphDatabase.driver(
      settings.NEO4J_URI,
      auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
    )


  async def close(self):
    await self.driver.close()


  async def create_node(self, label: str, properties: dict):
    node_id = properties.get("id") if properties is not None else None
    if not node_id:
      raise DatabaseOperationError(
        f"Falha ao criar o nó '{label}' no Neo4j: propriedade 'id' ausente ou inválida."
      )
    try:
      async with self.driver.session() as session:
        query = f"MERGE (n:{label} {{id: $id}}) SET n += $props RETURN n"
        await session.run(query, id=node_id, props=properties)
    except Exception as e:
      raise DatabaseOperationError(f"Falha ao criar o nó '{label}' no Neo4j: {str(e)}") from e


  async def create_relationship(self, start_node_id: str, end_node_id: str, rel_type: str):
    try:
      async with self.driver.session() as session:
        query = f"MATCH (a {{id: $start_id}}), (b {{id: $end_id}}) MERGE (a)-[r:{rel_type}]->(b) RETURN r"
        await session.run(query, start_id=start_node_id, end_id=end_node_id)
    except Exception as e:
      raise DatabaseOperationError(f"Falha ao criar relacionamento '{rel_type}' no Neo4j: {str(e)}") from e


  async def execute_query(self, query: str, parameters: dict = None):
    try:
      async with self.driver.session() as session:
        result = await session.run(query, parameters or {})
        # Extrai os registros do AsyncResult para que a camada de domínio receba dados primitivos
        return [record.data() async for record in result]
    except Exception as e:
      raise DatabaseOperationError(f"Falha ao executar query customizada no Neo4j: {str(e)}") from e


  async def verify_connectivity(self):
    await self.driver.verify_connectivity()

