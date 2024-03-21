import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['win_rate'] = df['win_rate'].str.replace('%', '')
    df['pick_rate'] = df['pick_rate'].str.replace('%', '')
    df['total_base_attribute'] = pd.to_numeric(df['total_base_attribute'])
    df['movement_speed'] = pd.to_numeric(df['movement_speed'])
    df['complexity'] = pd.to_numeric(df['complexity'])
    df['win_rate'] = pd.to_numeric(df['win_rate'])
    df['pick_rate'] = pd.to_numeric(df['pick_rate'])
    df['Balanced']= ((df['total_base_attribute']+ df['movement_speed'])/df['complexity']) * ((df['win_rate']+ df['pick_rate']) / 2)
    hero_df = df[['hero', 'primary_role', 'Balanced']]

    safe = df[df['primary_role'] == 'safelane']
    mid = df[df['primary_role'] == 'midlane']
    off = df[df['primary_role'] == 'offlane']
    softsupp = df[df['primary_role'] == 'soft support']
    hardsupp = df[df['primary_role'] == 'hard support']

    # Create a list of dataframes for each role
    roles = [safe, mid, off, softsupp, hardsupp]

    # Calculate the sum of balanced team composition for each role
    max_balanced_sums = [role.groupby('primary_role').apply(lambda x: (x['Balanced']).max()).sum() for role in roles]

    # Create a DataFrame to display the results
    result_df = pd.DataFrame({
        'Role': ['safelane', 'midlane', 'offlane', 'soft support', 'hard support'],
        'max_balanced_sums': max_balanced_sums
    })

    # Calculate the total sum of max balanced team composition
    total_balance = result_df['max_balanced_sums'].sum()
    return df, hero_df, total_balance

#file_path = 'dataset\dota2_heroes.csv'

#df, hero_df, total_balance = preprocess_data(file_path)