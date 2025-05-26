import pandas as pd

def transform_watchlist(watchlist_path):

    file = pd.read_csv(watchlist_path)

    file_transformed = file[['Title', 'Original Title', 'URL', 'IMDb Rating', 'Runtime (mins)', 'Year', 'Genres', 'Directors']].copy()
    file_transformed.columns = ['title', 'original_title', 'url', 'imdb_rating', 'runtime_mins', 'year', 'genres', 'directors']

    file_transformed = file_transformed.where(pd.notnull(file_transformed), None)

    file_transformed['imdb_rating'] = file_transformed['imdb_rating'].astype(float)
    file_transformed['runtime_mins'] = file_transformed['runtime_mins'].astype('Int64')

    return file_transformed