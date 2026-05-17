from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import pandas as pd
import uvicorn

app = FastAPI() # inicializa a aplicação FastAPI

CSV_PATH = Path(__file__).parent.parent / 'data' / 'movies.csv' # define o caminho do arquivo CSV

def load_df(): # carregar o dataframe do pandas a partir do arquivo CSV
    return pd.read_csv(CSV_PATH)

class MovieIn(BaseModel): # modelo de dados para validar as requisições post
    title: str
    genre: str
    year: int
    rating: float
    description: str


@app.get('/movies') # rota get para listar todos os filmes
def get_movies(genre: str = None): # genero é opcional
    df = load_df()
    if genre:
        df = df[df["genre"].str.lower() == genre.lower()] # filtra o dataframe, .lower() padroniza para minúscula
    return df.to_dict(orient='records') # retorna os dados convertidos em uma lista de dicionários


@app.get('/genres') # rota get para retornar todos os gêneros únicos cadastrados na base de dados
def get_genres():
    df = load_df()
    return df['genre'].unique().tolist() # remove duplicatas e converte em uma lista nativa


@app.get('/movies/{id}') # rota get para buscar e retornar os detalhes de um filme pelo id
def get_movie(id: int):
    df = load_df()
    result = df[df['id'] == id] # realiza a busca filtrando pela coluna id
    if result.empty: # se resultado estiver vazio, retorna o erro 404
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    return result.iloc[0].to_dict() # retorna o primeiro registro encontrado convertido em dicionário


@app.post('/movies', status_code=201) # rota post para cadastrar um novo filme com status de sucesso 201
def create_movie(movie: MovieIn):
    df = load_df()
    new_id = int(df['id'].max()) + 1 # autoincremento do id: pega o maior id atual e soma 1
    new_movie = {'id': new_id, **movie.model_dump()} # cria novo dicionário juntando o novo id com os dados validados
    df = pd.concat([df, pd.DataFrame([new_movie])], ignore_index=True) # ddiciona novo filme ao final do dataframe existente
    df.to_csv(CSV_PATH, index=False) # salva as alterações de volta no arquivo csv
    return new_movie # retorna o objeto do filme criado para confirmação


if __name__ == '__main__': # ponto de entrada para execução local do servidor com recarga automática
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)