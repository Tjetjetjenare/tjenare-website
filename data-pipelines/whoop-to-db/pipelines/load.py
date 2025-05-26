import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

def load_to_postgres(df, table_name='daily_summary'):
    env_path = Path(__file__).resolve().parent.parent / 'env' / 'whoop.env'
    load_dotenv(dotenv_path=env_path)

    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)

    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)
    print(f"Data loaded to PostgreSQL table: {table_name}")