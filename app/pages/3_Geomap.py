import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Geomap", page_icon="📈")

st.markdown("""# Geomap: LSOA_of_Accident_Location""")
st.sidebar.header("Geomap")
st.write(
    """This Geomap shows the most important feature LSOA_of_Accident_Location. \n\r <font style='color: #000000; background-color: #FFFF00'>**Yellow**</font> means positive impact for the model --> **'Serious or Fatal'** \n\r <font style='color: #000000; background-color: #800080'>**Purple**</font> means negative impact for the model --> **'Slight'**.
    """, unsafe_allow_html=True
)

st.image('./plots/geomap_overplot4.PNG')