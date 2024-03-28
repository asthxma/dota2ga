import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

im = Image.open("iconsdota.png")
st.set_page_config(
    page_title="Dota 2 GA - Algorithm",
    page_icon=im,
    layout="wide",
)

st.write("# Genetic Algorithm")
st.write('<i> So how does the algorithm work in forming the team composition?</i>', unsafe_allow_html=True)

st.header("Problem Assumptions", divider='rainbow')
with st.container():
    st.write("""
            1. The dataset is assumed to be stable, i.e. it does not change significantly over time during the one month interval of data collected.
            2. Each hero is assumed to have only one primary role.
            3. The team formed composed of one hero each from these five roles: <b> safelane, midlane, offlane, soft support,\
              and hard support</b>.
            4. The team composition is done without considering the enemy team being played against.
            5. The heroes are considered in initial base starting game, which is without items and abilities.
            """, unsafe_allow_html=True)
    
st.header("Fitness Function", divider='violet')
with st.container():
    st.write("For each hero, first we define hero's fitness with the following formula:")  
    st.latex(r'''
                h = \frac{Total Base Attribute + Movement Speed}{Complexity} \times 
                \frac{Win Rate + Pick Rate}{2},
                ''')
    st.write("then, we define the maximum possible hero fitness for each position, which is:")  
    st.latex(r'''
            max_i = \max_{i=1}^{5} (h_i),
            ''')
    st.write("where <b> i </b> represents each position: safelane, midlane, offlane, soft support, and hard support.\
             Using this max possible values, we define the combination with the maximum hero fitness for each position \
             as", unsafe_allow_html=True)
    st.latex(r'''
                maxteam = \sum_{i=1}^{5} max_i
                ''')
    st.write("Finally we use this <b> maxteam </b> as the constant in the fitness function, that is ", unsafe_allow_html=True)
    st.latex(r'''
                f = \frac{\sum_{i=1}^{5} h_i}{maxteam} \times 100 \%
                ''')
    st.write("For each team, the fitness value is the sum of fitness values from each individual heroes compared with the ideal team\
             . This team fitness function then is used for comparing the team composition made.")
    
st.header("Genetic Algorithm Implementation", divider='green')
with st.container():
    st.write("""
            1. The initial population is created by composing as many teams as the specified population value. Each team consists of \
             randomly selected heroes with suitable roles.
            2. Calculate the fitness of the composed team.
            3. Tournament selection is used as the selection method for choosing parents.
            4. The two parents undergo crossover with a single cut point, which is chosen randomly. This process results in two \
             children (teams of the next generation).
            5. For the mutation process, if the randomly generated value for a hero is lower than the mutation rate, the hero will be swapped\
              with another random hero.
            6. Repeat the process until the specified number of generations is reached.
            """)
    
