import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

im = Image.open("dota2ga\iconsdota.png")
st.set_page_config(
    page_title="Dota 2",
    page_icon=im,
    layout="wide",
)

# st.sidebar.success("Silahkan memilih laman yang ingin dituju.")
st.write("# Team Composition Dota 2")

st.header("Genetic Algorithm Implementation", divider='rainbow')
with st.container():
    st.write("""
             1. The initial population is done by forming as many teams as the specified population value. Each team consists of random heroes.
            2. Calculate the fitness of the formed team (Balance or Teamfight).
            3. Tournament selection is used as the selection method for selecting parents.
            4. The 2 parents are crossovered with 1 cut point. The cut point is chosen randomly
            """)