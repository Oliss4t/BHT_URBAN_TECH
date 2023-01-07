import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Feature Importance: Categorical Features", page_icon="📈", layout="wide")
st.markdown("# Feature Importance Categorical Features")
st.sidebar.header("Feature Importance Categorical Features")


feature_columns = [
    "Number_of_Vehicles",
    "Day_of_Week",
    "Daytime",
    "Vehicle_Type",
    "Did_Police_Officer_Attend_Scene_of_Accident",
    "Vehicle_Manoeuvre",
    "Light_Conditions",
    "Weather_Conditions",
]
feature_column = st.sidebar.selectbox(
    "Choose feature column to inspect", (feature_columns)
)

st.write(
    """On the left we see the transformed shap values for one category. By plotting a beeswarm plots, the categorical distribution gets visible, which is not visible in the bar plot.
A problem with the beeswarm plot is, that it uses common norm over all categorical values. If one category outnumbers the others, only the distribution of the majority category is visible.
All other categories are only visible as a line, even if that is not the case.
That is why i decided to plot a density diagram without a common norm. Thereby the distribution for each category gets visible.

"""
)
col1, col2 = st.columns(2)


with col1:
   st.header("Transformed SHAP Values for Categorical Features - common norm")
   st.image("./plots/categorical_plot_"+feature_column+".jpg")

with col2:
   st.header("Transformed SHAP Values for Categorical Features - individual norm")
   st.image("./plots/density_kde_"+feature_column+".jpg")


