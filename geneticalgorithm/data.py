import pandas as pd
from nama_modul import df


def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['win_rate'] = df['win_rate'].str.replace('%', '')
    df['pick_rate'] = df['pick_rate'].str.replace('%', '')
    # df['Hero_Defense'] = df['Mag_Defence'] + df['Phy_Defence']
    # df['Win_Rate'] = df['Esport_Wins'] / (df['Esport_Wins'] + df['Esport_Loss'])
    # df['Hard_Engage'] = (df['Phy_Damage'] + df['Mov_Speed'])
    # df['Team_Fight'] = (df['Phy_Damage'] + df['Hp'] + df['Hero_Defense'])
    df['total_base_attribute'] = pd.to_numeric(df['total_base_attribute'])
    df['movement_speed'] = pd.to_numeric(df['movement_speed'])
    df['complexity'] = pd.to_numeric(df['complexity'])
    df['win_rate'] = pd.to_numeric(df['win_rate'])
    df['pick_rate'] = pd.to_numeric(df['pick_rate'])
    df['Balanced']= ((df['total_base_attribute']+ df['movement_speed'])/df['complexity']) * ((df['win_rate']+ df['pick_rate']) / 2)
    hero_df = df[['hero', 'primary_role', 'Balanced']]
#primary
    safe = df[df['primary_role'] == 'safelane']
    mid = df[df['primary_role'] == 'midlane']
    off = df[df['primary_role'] == 'offlane']
    supp = df[df['primary_role'] == 'support']
    # Create a list of dataframes for each role
    roles = [safe, mid, off, supp]

    # Calculate the sum of (Hard_Engage * Win_Rate) and (Team_Fight * Win_Rate) for each role
    # max_hard_engage_sums = [role.groupby('Lane').apply(lambda x: (x['Hard_Engage'] * x['Win_Rate']).max()).sum() for role in roles]
    # max_team_fight_sums = [role.groupby('Lane').apply(lambda x: (x['Team_Fight'] * x['Win_Rate']).max()).sum() for role in roles]
    max_balanced_sums = [role.groupby('primary_role').apply(lambda x: (x['Balanced']).max()).sum() for role in roles]
    # Create a DataFrame to display the results
    result_df = pd.DataFrame({
        'Role': ['safelane', 'midlane', 'offlane', 'support'],
        'max_balanced_sums': max_balanced_sums,
        # 'Max_Team_Fight_Sum': max_team_fight_sums
    })

    # Calculate the total sum of (Hard_Engage * Win_Rate) and (Team_Fight * Win_Rate)
    total_balance = result_df['max_balanced_sums'].sum()
    # total_tf = result_df['Max_Team_Fight_Sum'].sum()
    return df, hero_df, total_balance

file_path = 'dataset\dota2_heroes.csv'

preprocess_data(file_path)

print(df)