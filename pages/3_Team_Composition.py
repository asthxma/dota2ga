import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

im = Image.open("iconsdota.png")
st.set_page_config(
    page_title="Dota 2 - Team Composition",
    page_icon=im,
    layout="wide",
)

st.write("# Team Composition Dota 2")

