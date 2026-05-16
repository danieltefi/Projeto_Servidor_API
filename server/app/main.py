from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import pandas as pd

app = FastAPI()

CSV_PATH = Path(__file__).parent.parent / 'data' / 'movies.csv'

def load_df():
    return pd.read_csv(CSV_PATH)

class MovieIn(BaseModel):
    title: str
    genre: str
    year: int
    rating: float
    description: str


@app.get('/movies')
def get_movies(genre: str = None):
    df = load_df()
    if genre:
        df = df[df['genre'] == genre]
    return df.to_dict(orient='records')


@app.get('/genres')
def get_genres():
    df = load_df()
    return df['genre'].unique().tolist()


@app.get('/movies/{id}')
def get_movie(id: int):
    df = load_df()
    result = df[df['id'] == id]
    if result.empty:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    return result.iloc[0].to_dict()


@app.post('/movies', status_code=201)
def create_movie(movie: MovieIn):
    df = load_df()
    new_id = int(df['id'].max()) + 1
    new_movie = {'id': new_id, **movie.model_dump()}
    df = pd.concat([df, pd.DataFrame([new_movie])], ignore_index=True)
    df.to_csv(CSV_PATH, index=False)
    return new_movie


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)