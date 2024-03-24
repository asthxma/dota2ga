import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

im = Image.open("iconsdota.png")
st.set_page_config(
    page_title="Dota 2 - GA",
    page_icon=im,
    layout="wide",
)


st.write("# Genetic Algorithm for Dota 2 Team Composition :smirk:")
    
st.subheader('What is Dota 2?', divider='rainbow')
st.write("Dota 2 is a multiplayer online battle arena (MOBA) game developed and published by Valve Corporation. \
            It is a sequel to the very popular Defense of the Ancients (DotA) mod, which originated as a modification for the game Warcraft III: Reign of Chaos and its expansion, \
            Warcraft III: The Frozen Throne. Released in July 2013, Dota 2 can be played for free on Microsoft Windows, OS X, \
            and Linux operating systems, and can only be played via Valve's official distribution platform, namely Steam.\
            The game is renowned for its incredible complexity, which includes intricate game mechanics, strategic depth, and the individual skills required to succeed. \
            Dota 2 has a large and active community, as well as major eSports tournaments such as The International, which is hosted by Valve every year and offers millions of dollars in prizes. \
            With its unique features and characteristics, Dota 2 has become one of the most popular games in the gaming world, and continues to play an important role in the global gaming community.")

st.subheader("Gameplay", divider='violet')
with st.container():
    VIDEO_URL = "https://youtu.be/M-gnC9Yi728"
    st.video(VIDEO_URL)
    st.write('<i> <div style="text-align: center"> Credit: ESL DOTA 2 & NoobFromUA </div> </i>', unsafe_allow_html=True)

with st.container():
    st.write("A game of Dota 2 consisted of two teams, \
            Radiant and Dire, each consisting of five players, clash to destroy the opposing team's Ancient - their main base. \
            The battlefield consists of three distinct lanes: the offlane, midlane, and safe lane, each guarded by three towers and two barracks. \
            Destroying barracks grants the team advantages, empowering their creeps to become stronger. \
            Additionally, players can farm in the forest to gain experience and gold. \
            Securing immortality through the Aegis of the Immortal requires defeating Roshan, a formidable jungle monster. \
            Runes scattered throughout the map provide temporary power-ups every two minutes. \
            With 124 heroes to choose from, each categorized into Strength, Agility, Intelligence, and Universal attribute \
            players must utilize their hero's unique abilities and strategic decision-making to navigate the map, \
            eliminate enemy forces, and ultimately achieve victory by destroying the opponent's Ancient. \
            In Dota 2, heroes not only have distinct abilities but also feature customizable costumes, adding to the game's\
              immersive experience.", unsafe_allow_html=True)
    
with st.container():
    st.subheader("Heroes", divider='blue')
    st.write("Here are some examples of heroes in Dota 2: ")
    image = Image.open('Hero.png')
    st.image(image, caption='Dota 2 Heroes (Credit: Valve Corporation)')
    st.write("These are just a few of the 124 heroes available in the game. Each hero has unique abilities, roles, \
        and characteristics, contributing to the diverse strategies and gameplay experiences in Dota 2.")

def open_page(url):
    open_script = """
        <script type="text/javascript">
            var url = '%s';
            window.open(url, '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

if st.button('VIEW ALL HEROES'):
    open_page('https://www.dota2.com/heroes')

with st.container():
    st.subheader("Creators", divider='green')
    st.write("""
             <b> DISCLAIMER: </b> This program is intended for non-profit or educational use only. Any utilization of Dota 2 \
             assets is strictly in compliance with fair use principles outlined by Valve Corporation.
            - :disappointed: March
            - :sleepy: WaveA-
            - :grimacing: Haz
            - :sob: Nature.
            """, unsafe_allow_html=True)