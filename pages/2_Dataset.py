import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 

<<<<<<< Updated upstream
df = pd.read_csv('dota2ga/dataset/dota2_dataset.csv')
print(df)

=======
st.set_page_config(
    page_title="Dataset Dota 2",
    page_icon="👋",
    layout="wide",
)

st.sidebar.success("Silahkan memilih laman yang ingin dituju.")

st.write("# Dataset Dota 2")
    
st.subheader('Berikut merupakan penjabaran dari dataset dota 2 yang dimana menampilkan 124 hero', divider='rainbow')

df = pd.read_csv('F:\\applications\\Python\\Magister\\KKPM\\dota2ga\\dataset\\dota2_heroes.csv')
st.write(df)
>>>>>>> Stashed changes
