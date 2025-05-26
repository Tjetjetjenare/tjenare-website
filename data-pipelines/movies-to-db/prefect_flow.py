from prefect import flow, task
from transform import transform_watchlist
from load import load_to_postgres

@task
def transform_task(path):
    df = transform_watchlist(path)
    return df

@task
def load_task(df, table_name, env_path):
    load_to_postgres(df, table_name=table_name, env_path=env_path)

@flow(name="Watchlist Dataflow")
def watchlist_flow():
    watchlist_path = '../data/watchlist.csv'
    env_path = 'watchlist.env'
    table_name = 'watchlist'

    df = transform_task(watchlist_path)
    load_task(df, table_name, env_path)

if __name__ == "__main__":
    watchlist_flow.serve(
        name="watchlist-deployment",
        cron="0 8 * * 1",  # Every monday at 8 AM
    )