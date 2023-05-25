import streamlit as st
import pandas as pd
import numpy as np
import requests


def fetch(session, url, inputs):
    try:
        result = session.get(url)
        st.write(inputs)
        return requests.post(url, json=inputs)
    except Exception:
        return {}

st.title('Flower prediction')

session = requests.Session()

with st.form("my_form"):
  # Buttons to enter figures
  sepal_length = st.number_input('Insert sepal length')
  st.write('Sepal length = ', sepal_length)
  sepal_width = st.number_input('Insert sepal width')
  st.write('Sepal width = ', sepal_width)
  petal_length = st.number_input('Insert petal length')
  st.write('Petal length = ', petal_length)
  petal_width = st.number_input('Insert petal width')
  st.write('Petal width = ', petal_width)

  new_measurement = {
      'sepal_length': sepal_length,
      'sepal_width': sepal_width,
      'petal_length': petal_length,
      'petal_width': petal_width
  }

  submitted = st.form_submit_button("Submit")

  if submitted:
    response = fetch(session, 'https://firstappvba.azurewebsites.net/predict', new_measurement)
    #response = fetch(session, 'http://127.0.0.1:8000/predict', new_measurement)
    st.write(response.content)