import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Feature Importance", page_icon="📈")

st.markdown("# Feature Importance")
st.sidebar.header("Feature Importance")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

st.image('./plots/feature importance.jpg')








st.button("Re-run")