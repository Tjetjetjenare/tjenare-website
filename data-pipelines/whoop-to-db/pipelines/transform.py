import pandas as pd

def transform_data(sleep_path, workout_path, phys_path):

    phys_data = pd.read_csv(phys_path)
    sleep_data = pd.read_csv(sleep_path)
    workout_data = pd.read_csv(workout_path)

    phys_data['Cycle start time'] = pd.to_datetime(phys_data['Cycle start time']).dt.date
    sleep_data['Cycle start time'] = pd.to_datetime(sleep_data['Cycle start time']).dt.date
    workout_data['Workout start time'] = pd.to_datetime(workout_data['Workout start time']).dt.date

    phys_summary = phys_data.groupby('Cycle start time').agg({
        'Recovery score %': 'mean',
        'Resting heart rate (bpm)': 'mean',
        'Heart rate variability (ms)': 'mean',
        'Day Strain': 'mean'
    }).reset_index().rename(columns={
        'Cycle start time': 'date',
        'Recovery score %': 'recovery_score',
        'Resting heart rate (bpm)': 'resting_hr',
        'Heart rate variability (ms)': 'hrv',
        'Day Strain': 'day_strain'
    })

    sleep_summary = sleep_data.groupby('Cycle start time').agg({
        'Sleep performance %': 'mean',
        'Sleep debt (min)': 'mean',
        'Asleep duration (min)': 'mean'
    }).reset_index().rename(columns={
        'Cycle start time': 'date',
        'Sleep performance %': 'sleep_performance',
        'Sleep debt (min)': 'sleep_debt',
        'Asleep duration (min)': 'asleep_duration'
    })

    workout_summary = workout_data.groupby('Workout start time').agg({
        'Duration (min)': 'sum',
        'Energy burned (cal)': 'sum',
        'Activity Strain': 'sum',
        'Max HR (bpm)': 'max',
        'Activity name': 'count'
    }).reset_index().rename(columns={
        'Workout start time': 'date',
        'Duration (min)': 'workout_duration',
        'Energy burned (cal)': 'workout_calories',
        'Activity Strain': 'workout_strain',
        'Max HR (bpm)': 'max_hr',
        'Activity name': 'workout_count'
    })

    daily_summary = phys_summary.merge(sleep_summary, on='date', how='outer')
    daily_summary = daily_summary.merge(workout_summary, on='date', how='outer')
    return daily_summary.sort_values('date')