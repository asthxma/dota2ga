import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html
import random
import numpy as np
import matplotlib.pyplot as plt
from geneticalgorithm.Data import preprocess_data
from geneticalgorithm.GeneticAlgorithm import genetic_algorithm

im = Image.open("iconsdota.png")
st.set_page_config(
    page_title="Dota 2 - Team Composition",
    page_icon=im,
    layout="wide",
)


file_path = 'dataset/dota2_heroes.csv'
df, hero_df, total_fit= preprocess_data(file_path)
hero_data = hero_df.to_dict(orient='records')
st.write("# Team Composition")
st.write('<i> Based on genetic algorithm, what would the best team look like?</i>', unsafe_allow_html=True)

st.header("Genetic Algorithm Parameters", divider='rainbow')
st.write("You can try setting the parameter and then tweaking it according to the results to see how the genetic algorithm fares!")
# Set algorithm parameters
target_positions = st.multiselect(
    'Input Target Lineup',
    ['safelane', 'midlane', 'offlane', 'soft support', 'hard support'],
    ['safelane', 'midlane', 'offlane', 'soft support', 'hard support']
    )


# Initialize input
pop_size = st.number_input('Population Size', min_value=1, value=10)
population = [random.sample(hero_data[:-1], 5) for _ in range(pop_size)]

generations = st.number_input('Number of Generations', min_value=1, value=30)
tournament_size = st.number_input('Tournament Size', min_value=1,max_value=pop_size, value=3)
crossover_rate = st.number_input('Crossover Rate', value=0.8, max_value=1.00)
mutation_rate = st.number_input('Mutation Rate', value=0.10, max_value=1.00)

# Run genetic algorithm for hard engage
result, temp_result = genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, pop_size)

chart_data = pd.DataFrame({
    "Generations": list(range(1, len(temp_result)+1)),
    "Fitness": (temp_result / total_fit) * 100
    #"Team Fight": (temp_result_team_fight / total_tf) * 100
})
st.header("Result", divider='violet')

col1, col2, col3 = st.columns([0.5, 0.1, 0.5])
with col1:
    st.subheader('Fitness Graph')
    st.line_chart(chart_data, x='Generations', y="Fitness", color="#dc143c", width=0, height=0, use_container_width=True)

with col3:
    st.subheader("Team Composition")
    st.write("Here's the team composition based on genetic algorithm!")
    result_df = pd.DataFrame.from_dict(result)
    st.dataframe(result_df.drop(columns='fitness'))
    fitness_tf = ((temp_result[-1] / total_fit) * 100)
    st.write("With the fitness value reaching",f"{fitness_tf:.2f}%.")
