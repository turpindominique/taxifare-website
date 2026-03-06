import streamlit as st
import requests

'''
# Taxifare Predict App !
'''

st.markdown('''
Welcome ! Hey !
''')

'''
# Hey ! Select the parameters of your ride

'''

date = st.date_input('Date', format='YYYY-MM-DD', value='2014-07-06')
time = st.time_input('Time', value='19:18:00')
pickup_longitude = st.number_input('Pickup longitude', value=-73.950655)
pickup_latitude = st.number_input('Pickup latitude', value=40.783282)
dropoff_longitude = st.number_input('Dropoff longitude', value=-73.984365)
dropoff_latitude = st.number_input('Dropoff latitude', value=40.769802)
passenger_count = st.slider('Passenger count', 1, 6, 1)

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

st.write(f"Our prediction : {prediction}")
