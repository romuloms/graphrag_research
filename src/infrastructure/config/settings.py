from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  OPENAI_API_KEY: str
  NEO4J_URI: str = "bolt://localhost:7687"
  NEO4J_USER: str = "neo4j"
  NEO4J_PASSWORD: str

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()