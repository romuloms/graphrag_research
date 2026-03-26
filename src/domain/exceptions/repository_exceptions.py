class DatabaseOperationError(Exception):
    """Exceção genérica para falhas em operações de repositório/banco de dados, mantendo o domínio agnóstico à infraestrutura."""
    def __init__(self, message: str):
        super().__init__(message)
