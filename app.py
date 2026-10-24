import streamlit as st

from datetime import date, time, datetime
import requests




'''
# TaxiFareModel front
'''


pickup_datetime = st.datetime_input(
    "Select pickup date and time", "2014-07-06 19:18:00")

pickup_longitude = st.number_input('Pickup longitude', -73.950655)

pickup_latitude = st.number_input('Pickup latitude', 40.783282)

dropoff_longitude = st.number_input('Dropoff longitude', -73.984365)

dropoff_latitude = st.number_input('Dropoff latitude', 40.769802)

passenger_count = st.number_input('Passenger count', 1)



url = 'https://taxifare.lewagon.ai/predict'



params = {
    "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),

    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

st.write(params)


if st.button("Predict"):
  response = requests.get(url, params)
  st.write(response.url)
  st.write(response.text)
