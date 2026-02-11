from function.function import *
import streamlit as st
from loader import page_icon


st.set_page_config(
    page_title="Asaan Zindagi Diabetes Prediction ",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
from app.header import app as header_app
header_app()

# Inputs
from app.input import app as input_app
input_data = input_app()

# Prediction
from app.predict import app as predict_app
predict_app(input_data)

#### Explain
from app.explainer import app as explainer_app
explainer_app(input_data)

# Model performance
from app.performance import app as performance_app
performance_app()

# perm_importance
from app.perm_importance import app as perm_app
perm_app()

# About
from app.about import app as about_app
about_app()

# Footer: logo + credits at bottom
from app.footer import app as footer_app
footer_app()

