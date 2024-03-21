import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path, nrows=124)  # Membaca 125 baris pertama dari file CSV
    df['win_rate'] = df['win_rate'].str.replace('%', '')
    df['pick_rate'] = df['pick_rate'].str.replace('%', '')
    df['total_base_attribute'] = pd.to_numeric(df['total_base_attribute'])
    df['movement_speed'] = pd.to_numeric(df['movement_speed'])
    df['complexity'] = pd.to_numeric(df['complexity'])
    df['win_rate'] = pd.to_numeric(df['win_rate'])
    df['pick_rate'] = pd.to_numeric(df['pick_rate'])
    df['Balanced'] = ((df['total_base_attribute'] + df['movement_speed']) / df['complexity']) * ((df['win_rate'] + df['pick_rate']) / 2)
    hero_df = df[['hero', 'primary_role', 'Balanced']]
    safe = df[df['primary_role'] == 'safelane']
    mid = df[df['primary_role'] == 'midlane']
    off = df[df['primary_role'] == 'offlane']
    supp = df[df['primary_role'] == 'support']
    roles = [safe, mid, off, supp]
    max_balanced_sums = [role.groupby('primary_role').apply(lambda x: (x['Balanced']).max()).sum() for role in roles]
    result_df = pd.DataFrame({
        'Role': ['safelane', 'midlane', 'offlane', 'support'],
        'max_balanced_sums': max_balanced_sums,
    })
    total_balance = result_df['max_balanced_sums'].sum()
    return df, hero_df, total_balance

file_path = 'dataset\dota2_heroes.csv'
df, hero_df, total_balance = preprocess_data(file_path)
print(df)
print(hero_df)
print(total_balance)
Safe = df[df['primary_role'] == 'safelane'].max()
Mid = df[df['primary_role'] == 'midlane'].max()
Off = df[df['primary_role'] == 'offlane'].max()
Supp = df[df['primary_role'] == 'support'].max()


print(Safe+Mid+Off+Supp)
