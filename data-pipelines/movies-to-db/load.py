import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

def load_to_postgres(df, table_name='watchlist', env_path=None):
    if env_path is None:
        env_path = Path(__file__).resolve().parent.parent / 'env' / 'watchlist.env'
    else:
        env_path = Path(env_path).resolve()

    if not env_path.exists():
        raise FileNotFoundError(f"Could not find environment file at: {env_path}")

    load_dotenv(dotenv_path=env_path)

    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    if None in (username, password, host, port, database):
        raise ValueError("One or more environment variables are missing in the .env file!")

    port = int(port)

    connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)

    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)

    print(f"Data loaded to PostgreSQL table: {table_name}")