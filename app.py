import streamlit as st
import joblib
import numpy as np
import pandas as pd


# Load the saved model and scaler
with open(r"best_rf_pipeline.pkl", "rb") as model_file:
    pipeline = joblib.load(model_file)
# pipeline = pickle.load('House_predictor.pkl')
cities = [
    'Shoreline', 'Kent', 'Bellevue', 'Redmond', 'Seattle',
       'Maple Valley', 'North Bend', 'Lake Forest Park', 'Sammamish',
       'Auburn', 'Des Moines', 'Bothell', 'Federal Way', 'Kirkland',
       'Issaquah', 'Woodinville', 'Normandy Park', 'Fall City', 'Renton',
       'Carnation', 'Snoqualmie', 'Duvall', 'Burien', 'Covington',
       'Inglewood-Finn Hill', 'Kenmore', 'Newcastle', 'Black Diamond',
       'Ravensdale', 'Clyde Hill', 'Algona', 'Mercer Island', 'Skykomish',
       'Tukwila', 'Vashon', 'SeaTac', 'Enumclaw', 'Snoqualmie Pass',
       'Pacific', 'Beaux Arts Village', 'Preston', 'Milton',
       'Yarrow Point', 'Medina'
]


# Streamlit UI
st.title("House Price Predictor App")

# User input
city = st.selectbox("Select City", cities)
yr_built = st.slider("Year Built", 1800, 2027, 2010)  
yr_renovated = st.slider("Year Renovated", 1800, 2027, 2010)
bedrooms = st.number_input("Number of bedrooms", min_value=1)
bathrooms = st.number_input("Number of bathrooms", min_value=1)
sqft_living = st.number_input("sqft_living", min_value = 1)
sqft_lot = st.number_input("sqft_lot", min_value = 1)
floors = st.number_input("Floors", min_value=1.0)
waterfront = st.number_input("Waterfront", min_value=0, max_value = 1)
view = st.number_input("View", min_value = 0, max_value = 4)
condition = st.number_input("COndition", min_value=0, max_value = 5)
sqft_above = st.number_input("SQFT ABOVE")
sqft_basement = st.number_input("sqft_basement")


input_data = pd.DataFrame({
    'bedrooms':[bedrooms],
    'bathrooms' : [bathrooms],
    'sqft_living' : [sqft_living], 
    'sqft_lot' : [sqft_lot],
    'floors': [floors],
    'waterfront': [waterfront],
    'view' : [view],
    'condition': [condition],
    'sqft_above': [sqft_above],
    'sqft_basement' : [sqft_basement],
    'yr_built': [yr_built],
    'yr_renovated': [yr_renovated],
    'city': [city]
})
# Predict
if st.button("Predict House Price"):
    prediction = pipeline.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]:.2f}")