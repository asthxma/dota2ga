import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

im = Image.open("iconsdota.png")
st.set_page_config(
    page_title="Dota 2 GA - Dataset",
    page_icon=im,
    layout="wide",
)

st.write("# Dataset")
st.write('<i> What dataset is being utilized?</i>', unsafe_allow_html=True)

st.header("Hero Stats", divider='violet')
with st.container():
    st.write("A typical hero in Dota 2 has various stats. For example, here are Marci's stats in the game.")
    image = Image.open('Marci.png')
    st.image(image, caption="Marci's Stat (Credit: Valve Corporation)")
    st.write("Our dataset consists of hero stats that we consider important in the genetic algorithm calculation, \
             along with how the heroes perform in matches.")

st.header("Data Table", divider='blue')
with st.container():
    st.write("This dataset presents information about 124 heroes in Dota 2 that can be played by the players. \
             The data provided includes win rate, pick rate, primary role, and various other important information \
             that can help in-game strategy. With this dataset, players can conduct in-depth analysis to choose the \
             optimal team composition and plan effective strategies to achieve victory.")
    
df = pd.read_csv('dataset\dota2_heroes.csv')
st.write(df)

st.write("""<span style="color:red">**Note:**</span> Match data is collected from matches played between February 1 \
         and 29, 2024, during <b> Dota 2 patch 7.35b </b>  and <b> 7.35c</b>.""", unsafe_allow_html=True)

st.header('Reference : Data Sources', divider='rainbow')
with st.container():
    data_sources = {
    "Dota 2 Official Website": "https://www.dota2.com/heroes",
    "Dota 2 Pro Tracker": "https://dota2protracker.com/meta",
    "Dota 2 Fandom - Table of Hero Attributes": "https://dota2.fandom.com/wiki/Table_of_hero_attributes",
    "Dota 2 Fandom - Heroes Mechanics": "https://dota2.fandom.com/wiki/Heroes/Mechanics",
    "Dotabuff Matches": "https://www.dotabuff.com/heroes/winning"
    }
    
    for i, (source, link) in enumerate(data_sources.items(), start=1):
        st.write(f"{i}. [{source}]({link})")