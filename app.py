import streamlit as st
import requests

'''
# Taxifare Predict App !
'''

st.markdown('''
Welcome !
''')

'''
# Hey ! Select the parameters of your ride

'''

date_time = st.datetime_input('Date and time')
pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.slider('Passenger count', 1, 6, 1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-232784860219.europe-west1.run.app'

params = {
    'pickup_lat': pickup_latitude,
    'pickup_lon': pickup_longitude,
    'dropoff_lat': dropoff_latitude,
    'dropoff_lon': dropoff_longitude,
    'pickup_datetime': date_time,
    'passenger_count': passenger_count
}

response = requests.get(url, params=params)

prediction = response.json()

st.write(f"Our prediction : {prediction}")
