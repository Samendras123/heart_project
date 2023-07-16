import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import model
import home
import about


st.set_page_config(
    page_title="Heart Model",
)


with st.sidebar:
    selected = option_menu(
        menu_title = "Menu",
        options=["Home", "Project", "Process"],
        icons = ["house", "book", "gear"],
        menu_icon="heart-pulse",
        default_index = 0

    )


if selected == "Home":
    home.main()
    

if selected == "Project":
    st.title("Machine Learning Model")
    model.project()

if selected == "Process":
    about.main()


with open("app.css") as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)
