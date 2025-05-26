
from transform import transform_data
from load import load_to_postgres

sleep_path = '../data/sleeps.csv'
workout_path = '../data/workouts.csv'
phys_path = '../data/physiological_cycles.csv'

df = transform_data(sleep_path, workout_path, phys_path)

load_to_postgres(df)