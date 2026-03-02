# Estrutura do Projeto - Onion Architecture

Este projeto segue os princípios da **Onion Architecture**, onde as dependências apontam sempre para dentro, garantindo que o núcleo da aplicação (Domain) seja independente de frameworks, bancos de dados e outras ferramentas externas.

## 📁 Estrutura de Camadas

### Domain (Núcleo)
O coração da aplicação, contendo as regras de negócio puras. **Não possui dependências externas**.

- **`entities/`**: Modelos de negócio ricos em comportamento. Classes bem detalhadas, evitando entidades anêmicas.
- **`exceptions/`**: Exceções de domínio específicas que expressam erros de negócio.
- **`interfaces/`**: Classes abstratas (ABCs) que definem contratos para repositórios e serviços externos.

### Application (Casos de Uso)
Orquestra a lógica de negócio sem conhecer detalhes de infraestrutura.

- **`use_cases/`**: Cada caso de uso representa uma ação específica da aplicação (ex: `CreateUserUseCase`).
- **`dtos/`**: Data Transfer Objects para entrada e saída de dados. Use Pydantic aqui.
- **`services/`**: Lógica que envolve múltiplas entidades, mas ainda agnóstica à infraestrutura.

### Infrastructure (Detalhes)
Implementações concretas que interagem com o mundo externo.

- **`repositories/`**: Implementações das interfaces de repositório definidas no Domain (SQLAlchemy, MongoDB, etc.).
- **`external_services/`**: Clientes HTTP, integração com APIs externas, envio de e-mails, etc.
- **`persistence/`**: Configurações de banco de dados, modelos ORM e mappers.

### Presentation (Interface)
Camada de entrada da aplicação.

- **`api/`**: Rotas, controllers e schemas de requisição/resposta (FastAPI, Flask, etc.).

## 🎯 Regra de Dependência

- **Domain** não conhece ninguém
- **Application** conhece apenas Domain
- **Infrastructure** conhece Domain (implementa suas interfaces)
- **Presentation** conhece Application e Domain

## 📝 Exemplo de Fluxo

1. **API** recebe requisição → valida com schema
2. **Use Case** orquestra o fluxo → chama repositório via interface
3. **Repository** acessa banco → retorna Entity
4. **Use Case** processa → retorna DTO
5. **API** serializa DTO → retorna resposta
