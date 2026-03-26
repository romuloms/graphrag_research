from neo4j import AsyncGraphDatabase
from src.domain.interfaces import IGraphRepository
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
    async with self.driver.session() as session:
      query = f"MERGE (n:{label} {{id: $id}}) SET n+= $props RETURN n"
      await session.run(query, id=properties.get("id"), props=properties)
