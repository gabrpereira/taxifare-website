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

dropout_longitude = st.number_input(
        "Dropout Longitude")

dropout_latitude = st.number_input(
        "Dropout Latitude")

st.write(pickup_latitude, pickup_longitude)

#

passenger_count = st.number_input("Passanger count",
        min_value=1,
        max_value=8)

st.write(passenger_count)

api = "url"
data = requests.get(api)

st.write(data)
