import pandas as pd
from fastapi import FastAPI, Path
#from funciones import sentiment_analysis
from datetime import datetime
from typing import Tuple

app = FastAPI()




df_games = pd.read_pickle('games.pkl')
df_items = pd.read_pickle('playtime.pkl')
df_reviews = pd.read_pickle('reviews.pkl')

# Endpoints 

@app.get("/count_reviews")
async def count_reviews(start_date: str, end_date: str) -> Tuple[int, float]:
    def count_reviews_between_dates(df, start_date, end_date):
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        filtered_reviews = df[(df['posted'] >= start_date) & (df['posted'] <= end_date)]
        total_users = len(filtered_reviews['user_id'].unique())
        recommend_percentage = (filtered_reviews['recommend'].astype(int).sum() / len(filtered_reviews)) * 100

        return total_users, recommend_percentage

    total_users, recommend_percentage = count_reviews_between_dates(df_reviews, start_date, end_date)
    return total_users, round(recommend_percentage, 2)