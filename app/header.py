import streamlit as st
from data.base import head_template, st_style


def app():
    st.markdown(st_style, unsafe_allow_html=True)
    st.markdown(head_template, unsafe_allow_html=True)