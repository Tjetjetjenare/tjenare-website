from transform import transform_watchlist
from load import load_to_postgres

watchlist_path = '../data/watchlist.csv'

df_transformed = transform_watchlist(watchlist_path)

load_to_postgres(df_transformed, table_name='watchlist', env_path='watchlist.env')