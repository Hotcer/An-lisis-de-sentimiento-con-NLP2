import pandas as pd
from fastapi import FastAPI, Path
from funciones import sentiment_analysis
import ast

app = FastAPI()


games = pd.read_csv('clean_games.csv')
revisiones = pd.read_csv('revision.csv')

# Endpoints 

@app.get('/userdata/{user_id}')

  
  except Exception as e:
    return {'error': str(e)}



@app.get('/genre/{genre}')
def genre(genre: str):

  playtime_by_genre = games.groupby('genres')['PlayTimeForever'].sum().reset_index()
  
  sorted_genres = playtime_by_genre.sort_values('PlayTimeForever', ascending=False)
  
  rank = sorted_genres[sorted_genres['genres'] == genre].index[0] + 1

  return {
    'rank': rank
  }


@app.get('/userforgenre/{genre}')
def userforgenre(genre: str):

  top_users = games[games['genres'] == genre].groupby('user_id')['PlayTimeForever'].sum().reset_index().sort_values('PlayTimeForever', ascending=False).head(5)

  top_users['url'] = 'https://steamcommunity.com/id/' + top_users['user_id']

  return top_users[['url', 'user_id']].to_dict(orient='records')


@app.get('/developer/{developer}')
def developer(developer: str):

  developer_data = games[games['developer'] == developer]
  
  result = []

  for year in developer_data['release_date'].dt.year.unique():
  
    data = developer_data[developer_data['release_date'].dt.year == year]
  
    total_items = len(data)
  
    free_items = len(data[data['price'] == 0])
  
    pct_free = (free_items / total_items) * 100
    
    result.append(f"{developer} {year} Total Items: {total_items} Contenido Gratis: {pct_free:.2f}%")

  return result


@app.get('/sentiment_analysis/{developer}')
def sentiment_analysis(developer: str):

  developer_reviews = reviews[reviews['developer'] == developer]  

  sentiment_counts = developer_reviews.groupby('sentiment_analysis').size().to_dict()

  return sentiment_counts