import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Feature Importance", page_icon="📈")

st.markdown("# Global Feature Importance")
st.sidebar.header("Global Feature Importance")
st.write(
    """
    The Global Feature Importance orders the features by there overall importance for the model. The features at the top, were the most usefull for predicting the classification **'Serious or Fatal'** vs. **'Slight'**.

    This barplot plots the global feature importance, where the global importance of each feature is taken to be the mean absolute value for that feature over all the given samples.
    """
)

st.image('./plots/feature_importance.jpg')

