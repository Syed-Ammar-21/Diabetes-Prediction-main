import streamlit as st
from data.base import footer_with_logo_template
from loader import logo_base64


def app():
    footer_html = footer_with_logo_template.format(logo_base64=logo_base64)
    st.markdown(footer_html, unsafe_allow_html=True)
