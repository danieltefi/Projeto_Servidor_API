# Terceiro Projeto: Catálogo de Filmes API
 
## Sobre o Projeto
 
Este projeto consiste no desenvolvimento de uma API REST para gerenciamento de um catálogo de filmes e de um cliente Python que a consome. O sistema permite listar, filtrar, buscar e cadastrar filmes a partir de uma base de dados em CSV.
 
O foco principal é a comunicação entre sistemas distintos por meio de **APIs (Application Programming Interfaces)**, explorando a construção de um servidor com **FastAPI** e o consumo das rotas via **Requests**.

## 🛠️ Tecnologias e Conceitos
 
- **Linguagem:** Python 3.
- **Servidor:** FastAPI + Uvicorn.
- **Cliente:** Requests.
- **Dados:** Pandas para leitura e escrita do CSV.
- **Validação:** Pydantic para validação automática dos dados de entrada.
- **Configuração:** python-dotenv para gerenciamento de variáveis de ambiente.

## ⚙️ Execução
O projeto utiliza **ambiente virtual (venv)** para isolamento de dependências.
 
1. Tenha o Python 3 instalado.
2. Faça o clone do projeto.
   ```bash
   git clone <URL do repositório>
   ```
3. **Criar o Ambiente Virtual:**
   O ambiente virtual isola as bibliotecas do projeto:
   ```bash
   python -m venv .venv
4. **Ative o ambiente:**
   - Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
   - Windows (CMD): `.\.venv\Scripts\activate.bat`
   - Linux/macOS: `source .venv/bin/activate`
5. Instale as dependências.
   ```bash
   pip install -r requirements.txt
   ```
6. Inicie o servidor.
   ```bash
   cd server
   uvicorn app.main:app --reload --port 8000
   # acesse http://localhost:8000/docs no navegador para testar as rotas
   ```
7. Em outro terminal, execute o cliente.
   ```bash
   cd client
   cp .env.example .env
   python main.py
   ```
 
## 📂 Estrutura de Arquivos
 
```text
Projeto_Servidor_API/
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py        # Ponto de entrada da API (FastAPI)
│   ├── data/
│   │   └── movies.csv     # Base de dados dos filmes
│   └── .env.example       # Variáveis de ambiente do servidor
├── client/
│   ├── main.py            # Script de consumo da API
│   └── .env.example       # Variáveis de ambiente do cliente
├── .gitignore
├── README.md
├── CHECKLIST.md
└── requirements.txt
```

## 🌐 Rotas da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `/movies` | Lista todos os filmes |
| GET | `/movies?genre=Action` | Filtra filmes por gênero |
| GET | `/movies/{id}` | Retorna um filme pelo ID |
| POST | `/movies` | Cadastra um novo filme |
| GET | `/genres` | Lista os géneros disponíveis |

## 👥 Integrantes
 
- **Pessoa A** — Servidor (FastAPI)
- **Pessoa B** — Cliente (Requests)

## 🚧 Status do Projeto
 
**Finalizado**