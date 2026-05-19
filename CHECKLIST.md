# 🎬 Catálogo de Filmes API - Checklist de Desenvolvimento

Este checklist detalha as etapas de construção do servidor e cliente para o mini projeto de consumo de APIs, focando na implementação de uma API REST com FastAPI e um cliente Python que a consome, conforme os requisitos da disciplina.

## 🟢 1. Configuração e Infraestrutura

- [x] Inicializar repositório Git e configurar `.gitignore`.
- [x] Criar o arquivo `requirements.txt` na raiz com as dependências do servidor.
- [x] **Estrutura de Pastas:** Criar diretórios `server/app/`, `server/data/` e `client/`.
- [x] Criar arquivos `server/.env.example` e `client/.env.example`.
- [x] Criar arquivo `server/app/__init__.py` vazio.

## 🔵 2. Dados e Modelagem (Pessoa A — Servidor)

- [x] **CSV de Filmes:** Criar `server/data/movies.csv` com colunas `id`, `title`, `genre`, `year`, `rating`, `description` e ao menos 15 filmes.
- [x] **Leitura do CSV:** Carregar o CSV com `pandas` na inicialização da aplicação como variável global.
- [x] **Modelo Pydantic `MovieIn`:** Implementar modelo de entrada com campos `title`, `genre`, `year`, `rating` e `description` para validação do POST.

## 🟡 3. Implementação do Servidor — Rotas (Pessoa A)

- [x] **`GET /movies`:** Retornar todos os filmes como lista de dicts.
  - [x] Suportar query param opcional `?genre=` para filtrar por gênero.
  - [x] Retornar lista vazia quando nenhum resultado for encontrado.
- [x] **`GET /movies/{id}`:** Retornar um filme pelo ID.
  - [x] Lançar `HTTPException 404` com mensagem amigável se não encontrado.
- [x] **`POST /movies`:** Receber body `MovieIn`, gerar novo ID automático e adicionar ao DataFrame.
  - [x] Persistir a alteração salvando o CSV atualizado em disco.
  - [x] Retornar o filme criado com status HTTP 201.
- [x] **`GET /genres`:** Retornar lista de gêneros únicos presentes no CSV.

## 🟠 4. Implementação do Cliente (Pessoa B)

- [x] **Configuração:** Ler `API_BASE_URL` do `.env` com fallback para `http://localhost:8000`.
- [x] **`listar_generos()`:** Chamar `GET /genres` e imprimir os gêneros disponíveis.
- [x] **`listar_filmes(genre=None)`:** Chamar `GET /movies` (com ou sem filtro) e imprimir filmes formatados com título, ano, gênero, nota e descrição.
- [x] **`buscar_filme(id)`:** Chamar `GET /movies/{id}` e imprimir detalhes completos.
  - [x] Tratar erro 404 com mensagem amigável ao usuário.
- [x] **`adicionar_filme()`:** Chamar `POST /movies` com dados de um novo filme e confirmar criação com o ID gerado.
- [x] **Bloco `main`:** Executar todas as funções em sequência, demonstrando todas as rotas.

## ⚪ 5. Robustez e Boas Práticas

- [x] **Tratamento de erros no cliente:** Envolver chamadas HTTP em `try/except` para tratar falhas de conexão.
- [x] **Tratamento de erros no servidor:** Garantir que IDs inválidos (não numéricos) retornem 422 automaticamente via FastAPI.
- [x] **Variáveis de ambiente:** Garantir que nenhuma URL ou configuração esteja hardcoded — tudo via `.env`.

## 🔴 6. Finalização e Entrega

- [x] **Colaboração Git:** Pessoa B deve contribuir via Pull Request da branch `client` → `main`.
- [x] **Histórico de PR:** Garantir que o Pull Request esteja visível no repositório antes da entrega.
- [x] **README.md:** Escrever instruções claras de como rodar servidor e cliente, listar as rotas disponíveis e identificar os integrantes.
- [x] **Commits regulares:** Realizar entregas incrementais para evidenciar o desenvolvimento ao longo do tempo.
- [x] **Link do repositório:** Confirmar que o repositório está público e o link funciona antes de entregar.

---

*Status Atual: 🚧 Finalizado*