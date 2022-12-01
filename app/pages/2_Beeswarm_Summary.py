import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Feature Importance", page_icon="📈")

st.markdown("# Feature Importance")
st.sidebar.header("Feature Importance")
st.write(
    """The beeswarm plot is designed to display an information-dense summary of how the top features in a dataset impact the model’s output. Each instance the given explanation is represented by a single dot on each feature fow. The x position of the dot is determined by the SHAP value"""
)

st.image('./plots/beeswarm.jpg')








st.button("Re-run")