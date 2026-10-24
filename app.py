import streamlit as st

from datetime import date, time, datetime
import requests




'''
# TaxiFareModel front
'''


st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

pickup_datetime = st.datetime_input(
    "What's the pickup date and time?", "2014-07-06 19:18:00")

pickup_longitude = st.number_input('Pickup longitude', -73.950655)

pickup_latitude = st.number_input('Pickup latitude', 40.783282)

dropoff_longitude = st.number_input('Dropoff longitude', -73.984365)

dropoff_latitude = st.number_input('Dropoff latitude', 40.769802)

passenger_count = st.number_input('Insert a number', 1)



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')




#pickup_datetime = datetime.combine(pickup_date, pickup_time)
#"pickup_datetime": "2014-07-06+19:18:00",



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
