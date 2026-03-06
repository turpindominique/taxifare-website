import streamlit as st
import requests
import pandas as pd
from numpy.random import default_rng as rng

'''
# Taxifare Predict App !
'''

st.markdown('''
Welcome !
''')

'''
# Hey ! Select the parameters of your ride :sunglasses:

'''

col1, col2 = st.columns(2)

with col1:
    date = st.date_input('Enter the date', format='YYYY-MM-DD', value='2014-07-06')
    time = st.time_input('Enter the time', value='19:18:00')
    pickup_longitude = st.number_input('Enter the pickup longitude', value=-73.950655)
    pickup_latitude = st.number_input('Enter the pickup latitude', value=40.783282)
    dropoff_longitude = st.number_input('Enter the dropoff longitude', value=-73.984365)
    dropoff_latitude = st.number_input('Enter the dropoff latitude', value=40.769802)
    passenger_count = st.slider('How many passengers ?', 1, 8, 1)

    date_time = f"{date} {time}"

# url = 'https://taxifare.lewagon.ai/predict'
url = 'https://taxifare-232784860219.europe-west1.run.app/predict'

params = {
    'pickup_latitude': pickup_latitude,
    'pickup_longitude': pickup_longitude,
    'dropoff_latitude': dropoff_latitude,
    'dropoff_longitude': dropoff_longitude,
    'pickup_datetime': date_time,
    'passenger_count': passenger_count
}

response = requests.get(url, params=params)

prediction = response.json()['fare']

with col2:
    st.space(size="stretch")
    st.header('Your trip')
    df = pd.DataFrame(
        [[pickup_latitude, pickup_longitude], [dropoff_latitude, dropoff_longitude]],
        columns=["lat", "lon"],
    )

    st.map(df)


    st.write(f"Your cost : {round(prediction, 2)}$")

'''

## Note your experience !

'''
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
