import shap
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pickle
from streamlit_shap import st_shap

st.set_page_config(page_title="Local Feature Importance", page_icon="📈", layout="wide")

st.markdown("# Local Feature Importance")
st.sidebar.header("Local Feature Importance")


number = 0
number = st.sidebar.number_input('Choose sample to create local feature importance plot', min_value =0, max_value=308197)

st.write('The current sample is ', number)
st.write(
    """Waterfall plots are designed to display explanations for individual predictions, so they expect a single row of an Explanation object as input. The bottom of a waterfall plot starts as the expected value of the model output, and then each row shows how the positive (red) or negative (blue) contribution of each feature moves the value from the expected model output over the background dataset to the model output for this prediction."""
)


@st.cache
def load_data():
    with open('./data/shap_values_e.pkl', 'rb') as f:
        shap_values = pickle.load(f)
    # with open('./data/explainer.pkl', 'rb') as f:
    #     explainer = pickle.load(f)
    return shap_values #, explainer



shap_values = load_data()

st_shap(shap.plots.waterfall(shap_values[number]))



st.button("Re-run")