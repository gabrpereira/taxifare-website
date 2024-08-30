import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the  functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time <
- pickup longitude < float
- pickup latitude
- dropoff longitude <
- dropoff latitude
- passenger count < int 1-8
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a  file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The  package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the  package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

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

api = "https://taxifare.lewagon.ai/predict"
data = requests.get(api)

st.write(data)
