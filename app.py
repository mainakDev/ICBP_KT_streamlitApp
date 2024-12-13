import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

st.write(f"## Disease Prediction Application")
st.write("Author: Mainak Dev")

#name = st.text_input("Full Name")
#age = st.text_input("Type your age")

#st.write(f"The name of the user is: {name}")
#st.write(f"The address of {name} is: {age}")

heart_disease_model = pickle.load(open("models/diabetes_model.sav","rb"))
heart_disease_model = pickle.load(open("models/heart_disease_model.sav","rb"))
heart_disease_model = pickle.load(open("models/parkinsons_model.sav","rb"))

col1,col2,col3,col4,col5 = st.columns(5)

with st.sidebar:
    selected = option_menu("Choose the Disease", ["Heart Diesease Prediction","Diabetes Prediction","Parkinsons Disease"])

if selected == "Heart Diesease Prediction":
    st.write(f"### Heart Diesease Predictions")
    #code for heart disease prediction
    with col1:
        age = st.text_input("Type your age")
        sex = st.text_input("Type your sex")
        cp = st.text_input("Type your cp")
    with col2:
        testbps = st.text_input("Type your testbps")
        chol = st.text_input("Type your chol")
        fbs = st.text_input("Type your fbs")
    with col3:
        restecg = st.text_input("Type your restecg")
        thalach = st.text_input("Type your thalach")
        exang = st.text_input("Type your exang")
    with col4:
        oldpeak = st.text_input("Type your oldpeak")
        slope = st.text_input("Type your slope")
        ca = st.text_input("Type your ca")
    with col5:
        st.image("images/heart.png")
    thal = st.text_input("Type your thal")
        

    if st.button("Predict",use_container_width=True, type="primary"):
        try:
            # Convert inputs to numeric
            data = [[
                float(age), int(sex), int(cp), float(testbps), float(chol), int(fbs),
                int(restecg), float(thalach), int(exang), float(oldpeak), int(slope),
                int(ca), int(thal)
            ]]
            # Make prediction
            prediction = heart_disease_model.predict(data)
            st.write(f"Model prediction is: {prediction[0]}")
        except ValueError:
            st.error("Please enter valid numeric inputs.")

if selected == "Diabetes Prediction":
    st.write(f"### Diabetes Prediction")
    st.write(f"Diabetes code goes here")

if selected == "Parkinsons Disease":
    st.write(f"### Parkinsons Disease")
    st.write(f"Parkinsons code goes here")




#taking user inputs


 