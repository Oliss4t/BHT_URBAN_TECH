import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Feature Importance", page_icon="📈")

st.markdown("# Feature Importance")
st.sidebar.header("Feature Importance")
st.write(
    """This barplot plots the global feature importance, where the global importance of each feature is taken to be the mean absolute value for that feature over all the given samples."""
)

st.image('./plots/feature_importance.jpg')








st.button("Re-run")