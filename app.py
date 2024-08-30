import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''

Taxifare

''')

url = 'https://taxifare.lewagon.ai/predict'


pickup_datetime = st.date_input(
        "Pickup datetime:",
        datetime.date.today())
# st.write("Your datetime is:", pickup_datetime)

pickup_time = st.time_input(
        "Pickup time:",
        datetime.datetime.now())
# st.write("Time", pickup_time)

st.write(pickup_datetime, pickup_time)

#

pickup_latitude = st.number_input(
        "Pickup Latitude")

pickup_longitude = st.number_input(
        "Pickup Longitude")

dropoff_longitude = st.number_input(
        "Dropout Longitude")

dropoff_latitude = st.number_input(
        "Dropout Latitude")

st.write(pickup_latitude, pickup_longitude)

#

passenger_count = st.number_input("Passanger count",
        min_value=1,
        max_value=8)

st.write(passenger_count)

# Button to get prediction
if st.button('Get Fare'):
    # Params dictionary with input data
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_latitude": pickup_latitude,
        "pickup_longitude": pickup_longitude,
        "dropoff_latitude": dropoff_latitude,
        "dropoff_longitude": dropoff_longitude,
        "passenger_count": passenger_count
    }
    # Sending request to the API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        fare = response.json().get('fare')
        st.success(f'Predicted Fare: ${fare:.2f}')
    else:
        st.error(f"Error: {response.status_code}")
