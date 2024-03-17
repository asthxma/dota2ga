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
# st.sidebar.success("Silaahkan memilih laman yang ingin dituju.")
st.write("# Test")




import streamlit as st

def main():
    st.title("Informasi 4 Orang")

    # Informasi orang pertama
    with st.expander("Orang Pertama"):
        st.write("Nama: John Doe")
        st.image("Hero.png", caption="Foto John Doe", width=150)

    # Informasi orang kedua
    with st.expander("Orang Kedua"):
        st.write("Nama: Jane Doe")
        st.image("https://via.placeholder.com/150", caption="Foto Jane Doe", use_column_width=True)

    # Informasi orang ketiga
    with st.expander("Orang Ketiga"):
        st.write("Nama: Alice Smith")
        st.image("https://via.placeholder.com/150", caption="Foto Alice Smith", use_column_width=True)

    # Informasi orang keempat
    with st.expander("Orang Keempat"):
        st.write("Nama: Bob Johnson")
        st.image("https://via.placeholder.com/150", caption="Foto Bob Johnson", use_column_width=True)

if __name__ == "__main__":
    main()



