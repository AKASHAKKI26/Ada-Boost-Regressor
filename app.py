import streamlit as st
import numpy as np
import pickle

# Load model
with open("house_regressor.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("AdaBoost House Price Prediction")

st.write("Enter house details below")

# Inputs
medinc = st.number_input(
    "Median Income",
    min_value=0.0,
    value=3.0
)

houseage = st.number_input(
    "House Age",
    min_value=0.0,
    value=20.0
)

averooms = st.number_input(
    "Average Rooms",
    min_value=0.0,
    value=5.0
)

population = st.number_input(
    "Population",
    min_value=0.0,
    value=1000.0
)

# Predict button
if st.button("Predict Price"):

    input_data = np.array([[
        medinc,
        houseage,
        averooms,
        population
    ]])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: {prediction[0]:.2f}"
    )