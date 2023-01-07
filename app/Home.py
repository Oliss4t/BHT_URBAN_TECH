import streamlit as st
st.set_page_config(
    page_title="Data",
)
st.write("""# UK Government
## Use-Case: Explanation of Accident Severity""")
st.markdown(
    """
    The data is not included in the github. You can download it at the following links.
### Data
* London Boroughs boundaries: https://skgrange.github.io/data.html 
* UK Traffic Accidents: https://www.kaggle.com/datasets/tsiaras/uk-road-safety-accidents-and-vehicles?select=Vehicle_Information.csv
* LOAS: https://data.london.gov.uk/dataset/lsoa-atlas

#### Business Question:
„How can we further reduce the serious traffic accidents in London? -
We did already simple data analysis but couldn’t find interesting insights.“

#### Question to Answer via ML approach:
„What features are important to classify a traffic accident as serious?“


"""
)