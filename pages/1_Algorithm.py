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
st.write("# Algorithm Dota 2")

# st.write("Dota 2 is a multiplayer online battle arena game , \
#         and is the sequel to the Defense of the Ancients mod on Warcraft \
#         3: Reign of Chaos and Warcraft 3: The Frozen Throne . DotA 2 was developed by Valve Corporation, \
#         published in July 2013. Dota 2 can be played for free on Microsoft Windows , OS X and Linux operating systems. \
#         Dota 2 can be played exclusively through Valve's official distributor, Steam.")

st.header("Problem Assumptions", divider='rainbow')
with st.container():
    st.write("""
             1. The dataset is assumed to be stable, i.e. it does not change significantly over time.
            2. Each hero is assumed to have only 1 primary role and 1 teamfight role.
            3. The team formed does not lean towards one game strategy, so the team formed has heroes with various roles.
            4. The team composition is done without considering the enemy team being played against.
            5. The parameter of each hero is a real value, so value encoding is used.
            """)
    
st.header("Ideal Team Composition", divider='rainbow')
with st.container():
    # Membuat dua kolom
    col1, col2 = st.columns(2)

    # Kontainer 1
    with col1:
        st.subheader("Balanced Team", divider='violet')
        # Tambahkan konten untuk container 1 di sini
        st.write("tim yang dibentuk dipastikan seimbang memiliki hero dengan peran yang sesuai. Untuk tim jenis ini, komposisi tim terdiri dari: <b> 1 Carry, 1 Midlaner, 1 Offlaner, 1 Support, dan 1 Hard Support. </b>", unsafe_allow_html=True)

    # Kontainer 2
    with col2:
        st.subheader("Teamfight Team", divider='violet')
        # Tambahkan konten untuk container 2 di sini
        st.write("tim yang dibentuk dipastikan memiliki hero yang unggul dalam perang tim. Untuk tim jenis ini, komposisi tim terdiri dari: <b>1 Carry, 1 Midlaner, 1 Offlaner, 2 Support.</b>", unsafe_allow_html=True)
    
    with st.container():
        image = Image.open('dota2ga\img\Marci.png')
        st.image(image, caption='HEROES OF DOTA 2')
        
st.header("Fitness Function", divider='rainbow')
with st.container():
    st.subheader("Balanced Team", divider='violet')
    st.write("Untuk Balanced Team, dirumuskan penghitungan fitness function dari masing-masing hero sebagai berikut.")  
    st.latex(r'''
                a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                \sum_{k=0}^{n-1} ar^k =
                a \left(\frac{1-r^{n}}{1-r}\right)
                ''')
    st.write("")
    
    st.subheader("Teamfight Team", divider='violet')
    st.write("Untuk Teamfight, dirumuskan penghitungan fitness function dari masing-masing hero sebagai berikut.")  
    st.latex(r'''
                a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                \sum_{k=0}^{n-1} ar^k =
                a \left(\frac{1-r^{n}}{1-r}\right)
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
    
