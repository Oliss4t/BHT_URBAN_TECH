# BHT_URBAN_TECH

The data is not included in the github. You can download it at the following links:
London Boroughs boundaries: https://skgrange.github.io/data.html 
UK Traffic Accidents: https://www.kaggle.com/datasets/tsiaras/uk-road-safety-accidents-and-vehicles?select=Vehicle_Information.csv
LOAS: https://data.london.gov.uk/dataset/lsoa-atlas


Customer Question:
Increase in traffic accidents... find source

What drives the severity of traffic accidents?
What can we do to work against it? What are the leverages? 

* check data types
* restrict to london
* handling missing values
* feature engineering and only use relevant columns

* like many other permutation-based interpretation methods, the Shapley value method suffers from inclusion of unrealistic data instances when features are correlated
* The Shapley value returns a simple value per feature, but no prediction model like LIME. This means it cannot be used to make statements about changes in prediction for changes in the input, such as: “If I were to earn €300 more a year, my credit score would increase by 5 points.”

* Exploratory Data Analysis
* visualize
* clustering on data

* build classification model for severtity prediction
* LIME and SHAP
* SHAP feature importance
* SHAP Summary Plot -->  first indications of the relationship between the value of a feature and the impact on the prediction
* SHAP Dependence Plot --> SHAP feature dependence detailed
* SHAP Interaction Values
* Clustering Shapley Values --> cluster instances by explanation similarity
* shap values on outlier
* average shap values on class, the most important factors for the serverity class 

* create beautiful vizualization
* streamlit app