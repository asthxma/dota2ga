import streamlit as st
from streamlit_option_menu import option_menu

# 1. sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=["Home", "Project", "About"],  # required
    )
    
if selected == "Home":
    st.title(f"You have selected {selected}")
elif selected == "Project":  # Use elif instead of multiple if conditions
    st.title(f"You have selected {selected}")
elif selected == "About":  # Use elif instead of multiple if conditions
    st.title(f"You have selected {selected}")
