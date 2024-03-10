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


st.sidebar.success("Silahkan memilih laman yang ingin dituju.")

st.write("# Genetic Algorithm for DOTA 2 Team Composition :face_with_spiral_eyes:")
    
st.subheader('What is Dota 2?', divider='rainbow')
st.write("Dota 2 is a multiplayer online battle arena game , \
        and is the sequel to the Defense of the Ancients mod on Warcraft \
        3: Reign of Chaos and Warcraft 3: The Frozen Throne . DotA 2 was developed by Valve Corporation, \
        published in July 2013. Dota 2 can be played for free on Microsoft Windows , OS X and Linux operating systems. \
        Dota 2 can be played exclusively through Valve's official distributor, Steam.")

#with st.container():
    #image = Image.open('strixrog.png')
    #st.image(image, caption='ASUS ROG STRIX')

st.subheader("Gameplay Introduction", divider='violet')

video_file = open('simulasi.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
with st.container():
    st.write("Dota 2 is a highly strategic multiplayer online battle arena (MOBA) game where two teams, \
            Radiant and Dire, each consisting of five players, clash to destroy the opposing team's Ancient - their main base. \
            The battlefield consists of three distinct lanes: the offlane, midlane, and safe lane, each guarded by three towers and two barracks. \
            Destroying barracks grants the team advantages, empowering their creeps to become stronger. \
            Additionally, players can farm in the forest to gain experience and gold. \
            Securing immortality through the Aegis of the Immortal requires defeating Roshan, a formidable jungle monster. \
            Runes scattered throughout the map provide temporary power-ups every two minutes. \
            With over 100 heroes to choose from, each categorized into Strength, Agility, and Intelligence, \
            players must utilize their hero's unique abilities and strategic decision-making to navigate the map, \
            eliminate enemy forces, and ultimately achieve victory by destroying the opponent's Ancient. \
            In Dota 2, heroes not only have distinct abilities but also feature customizable costumes, adding to the game's immersive experience.")
    
with st.container():
    st.subheader("Hero Of Dota 2", divider='blue')
    st.write("Here are some examples of heroes in Dota 2: ")
    multi = ''' 
        1. Anti-Mage 
        2. Crystal Maiden 
        3. Pudge
        4. Sniper
        5. Phantom Assassin
        6. Invoker
        7. Tidehunter
        8. Lina
        9. Faceless Void
        10. Drow Ranger
        11. Axe
        12. Shadow Fiend
        13. Templar Assassin
        14. Zeus
        15. Earthshaker

        These are just a few of the over 100 heroes available in the game. Each hero has unique abilities, roles, and characteristics, contributing to the diverse strategies and gameplay experiences in Dota 2.
    '''
    st.markdown(multi)

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
    image = Image.open('Hero.png')
    st.image(image, caption='HEROES OF DOTA 2')

with st.container():
    st.subheader("Team Player", divider='red')
    st.write("Dota 2 is played by 2 teams consisting of 5 players, \
        each team has a base in a corner of the map, each base has a building called (Ancient), \
        where the team must try to destroy the opposing team's (Ancient)\
        in order to win the match. Each player can only control one (Hero)\
        character who focuses on leveling up, collecting gold, buying items and fighting the opposing team to win.")

with st.container():
    st.subheader("Creator", divider='grey')
    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        st.write(":anguished: DMH")
    with col2:
        st.write(":smirk: MIW")
    with col3:
        st.write(":unamused: MS")
    with col4:
        st.write(":grimacing: NHD")



#col1, col2 = st.columns(2)

#with col1:
    #data_laptop = st.button("Data Laptop")
    #image = Image.open('laptopmany.png')
    #st.image(image)
    #if data_laptop:
        #switch_page("data_laptop")

#with col2:
    #sistem_rek = st.button("Rekomendasi Laptop")
    #image = Image.open('rekom.png')
    #st.image(image)
    #if sistem_rek:
        #switch_page("rekomendasi laptop")


