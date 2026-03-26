from abc import ABC, abstractmethod


class IGraphRepository(ABC):
  
  @abstractmethod
  async def close(self):
    pass

  @abstractmethod
  async def create_node(self, label: str, properties: dict):
    pass

  @abstractmethod
  async def create_relationship(self, start_node_id: str, end_node_id: str, rel_type: str):
    pass

  @abstractmethod
  async def execute_query(self, query: str, parameters: dict = None):
    pass

  @abstractmethod
  async def verify_connectivity(self):
    pass