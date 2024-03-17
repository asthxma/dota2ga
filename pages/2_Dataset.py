import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

im = Image.open("iconsdota.png")
st.set_page_config(
    page_title="Dota 2",
    page_icon=im,
    layout="wide",
)
# st.sidebar.success("Silahkan memilih laman yang ingin dituju.")
st.write("# Dataset Dota 2")
    
st.header('About Dataset?', divider='rainbow')
with st.container():
    st.write("This dataset presents information about 124 heroes in Dota 2 that can be played by teams. The data provided includes win rate, pick rate, primary role, and various other important information that can help in game strategy. With this dataset, teams can conduct in-depth analysis to choose the optimal team composition and plan effective strategies to achieve victory.")
    
df = pd.read_csv('dataset\dota2_heroes.csv')
cleaned_df = df.dropna()
st.write(cleaned_df)


st.write("""<span style="color:red">**Note:**</span> Match data is taken for matches that took place between February 1-29, 2024.""", unsafe_allow_html=True)


st.header('Reference : Data Sources', divider='rainbow')
with st.container():
    data_sources = {
    "Dota 2 Official Website": "https://www.dota2.com/heroes",
    "Dota 2 Pro Tracker": "https://dota2protracker.com/meta",
    "Dota 2 Fandom - Table of Hero Attributes": "https://dota2.fandom.com/wiki/Table_of_hero_attributes",
    "Dota 2 Fandom - Heroes Mechanics": "https://dota2.fandom.com/wiki/Heroes/Mechanics",
    "Dotabuff": "https://www.dotabuff.com/heroes/winning"
    }
    
    for i, (source, link) in enumerate(data_sources.items(), start=1):
        st.write(f"{i}. [{source}]({link})")
        
    
    
    
    
    