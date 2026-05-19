import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


def listar_generos():
    try:
        resp = requests.get(f"{BASE_URL}/genres")
        resp.raise_for_status()
        generos = resp.json()
        print("Gêneros disponíveis:")
        for g in generos:
            print(f"  - {g}")
    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao servidor.")


def listar_filmes(genre=None):
    try:
        url = f"{BASE_URL}/movies"
        if genre:
            url += f"?genre={genre}"
        resp = requests.get(url)
        resp.raise_for_status()
        filmes = resp.json()
        if not filmes:
            print("Nenhum filme encontrado.")
            return
        for f in filmes:
            print(f"[{f['id']}] {f['title']} ({f['year']}) — {f['genre']} | Nota: {f['rating']}")
            print(f"   {f['description']}")
    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao servidor.")


def buscar_filme(id):
    try:
        resp = requests.get(f"{BASE_URL}/movies/{id}")
        if resp.status_code == 404:
            print(f"Filme com ID {id} não encontrado.")
            return
        resp.raise_for_status()
        f = resp.json()
        print(f"ID: {f['id']}")
        print(f"Título: {f['title']}")
        print(f"Gênero: {f['genre']}")
        print(f"Ano: {f['year']}")
        print(f"Nota: {f['rating']}")
        print(f"Descrição: {f['description']}")
    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao servidor.")


def adicionar_filme():
    novo = {
        "title": "Blade Runner 2049",
        "genre": "Sci-Fi",
        "year": 2017,
        "rating": 8.0,
        "description": "Um caçador de replicantes descobre um segredo que pode mudar a humanidade."
    }
    try:
        resp = requests.post(f"{BASE_URL}/movies", json=novo)
        resp.raise_for_status()
        criado = resp.json()
        print(f"Filme adicionado com sucesso! ID gerado: {criado['id']}")
    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao servidor.")
