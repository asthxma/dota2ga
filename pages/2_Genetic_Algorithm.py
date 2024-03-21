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
            3. The team formed composed of one hero each from these five roles: <b> safelane, midlane, offlane, soft support, and hard support.</b>
            4. The team composition is done without considering the enemy team being played against.
            5. The heroes are considered in initial base starting game, which is without items and abilities.
            """, unsafe_allow_html=True)
    
st.header("Ideal Team Composition", divider='red')
with st.container():
    st.write("tim yang dibentuk dipastikan seimbang memiliki hero dengan peran yang sesuai. \
                 Untuk tim jenis ini, komposisi tim terdiri dari: <b> 1 Carry, 1 Midlaner, 1 Offlaner,\
                  1 Support, dan 1 Hard Support. </b>", unsafe_allow_html=True)
    
        
st.header("Fitness Function", divider='rainbow')
with st.container():
    st.write("Untuk Balanced Team, dirumuskan penghitungan fitness function dari masing-masing hero sebagai berikut.")  
    st.latex(r'''
                f_{balanced} = \sum_{i=1}^{5}  \left[ \frac{Total Base Attribute + Movement Speed}{Complexity} \times 
                \frac{Win Rate + Pick Rate}{2} \right]_i
                ''')
    st.write("")
    
st.header("Genetic Algorithm Implementation", divider='rainbow')
with st.container():
    st.write("""
             1. The initial population is done by forming as many teams as the specified population value. Each team consists of random heroes.
            2. Calculate the fitness of the formed team (Balance or Teamfight).
            3. Tournament selection is used as the selection method for selecting parents.
            4. The 2 parents are crossovered with 1 cut point. The cut point is chosen randomly
            """)
    
