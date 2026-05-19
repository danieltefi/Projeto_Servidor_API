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
