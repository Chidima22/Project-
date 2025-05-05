import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import math

st.set_page_config(page_title="ForecastX", page_icon=":bar_chart:", layout="wide")
col1,  col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", use_container_width=True)  # Replace "logo.png" with the path to your logo file
with col2:
    st.title(":red[ForecastX]: Bike Demand Prediction")
    st.markdown("Predicting Bike Demand with Machine Learning.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    return df

# Load model
@st.cache_resource
def load_model():
    # LOAD MODEL WITH PICKLE
    with open('random_forest.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Forecast function
def forecast_demand(model, features):
    prediction = model.predict(features)
    return prediction




df = load_data()
model = load_model()

# Contact Section
st.sidebar.markdown("# Contact")
st.sidebar.write("""
📱 +2347072730822
chidimaakabogu@gmail.com
""")

st.sidebar.markdown("#### 💼 Connect with Me")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/feed/)")


day_of_week_map ={
     'Sunday':1,
     'Monday':2,
     'Tuesday':3,
     'Wednesday':4,
     'Thursday':5,
     'Friday':6,
     'Saturday':7,
   
}
weather_condition_map = {
    'Clear, Few clouds, Partly cloudy, Partly cloudy': 1,
    'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist': 2,
      'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds':3, 
        'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog':4,     
}

month_map = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
workingday_map = {
    'Yes': 1,
    'No': 0
}

holiday_map = {
    'Yes': 1,
    'No': 0
}

season_map = {
    'Spring': 1,
    'Summer': 2,
    'Fall': 3,
    'Winter': 4
}

# Sidebar Inputs
st.title("Adjust Input Parameters ⚙️")
hour = st.slider("Select the Hour of Day", 1, 24, 1)
day_of_week = day_of_week_map[st.selectbox("Select the Day of Week", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])]
season = season_map[st.selectbox("Select Weather Condition", ['Spring', 'Summer', 'Fall', 'Winter'])]
weather_condition = weather_condition_map[st.selectbox("Select Weather Condition", ['Clear, Few clouds, Partly cloudy, Partly cloudy', 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist', 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds', 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'])]
month = month_map[st.selectbox("Select Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])]
workingday = workingday_map[st.radio("Is it a Working Day?", ('Yes', 'No'))]
holiday= holiday_map[st.radio("Is it a Holiday?", ('Yes', 'No'))]
temperature = st.slider("Select Temperature (Celsius)", -10, 40, 20)
humidity = st.slider("Select Humidity (%)", 0, 100, 50)
windspeed = st.slider("Select Wind Speed (km/h)", 0, 100, 20)


# Prepare Features for Prediction
input_df = pd.DataFrame({
    'season': season,
     'hour' : hour,
     'holiday': holiday,
     'month' : month,
     'workingday': workingday,
    'dayofweek' : day_of_week,
    'temp' : temperature,
    'humidity' : humidity,
    'windspeed' : windspeed,
    'weather': weather_condition
}, index=[0])




if st.button("Predict Demand"):
    demand_prediction = forecast_demand(model, input_df)
    st.success(f"Predicted Bike Ride Demand: {math.ceil(demand_prediction[0])} rides")



# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "© 2025 Chidima / Nigeria. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)








