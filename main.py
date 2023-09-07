import streamlit as st
from project_diabities_prediction import predict_

st.write('#  Diabetes prediction')  

col1,col2,col3 = st.columns(3)

with col1:
    pr = st.number_input('Enter Pregnancies')
    Glucose = st.number_input('Glucose')
    BloodPressure = st.number_input('BloodPressure')
    
with col2:
    SkinThickness = st.number_input('SkinThickness')
    Insulin = st.number_input('Insulin')
    BMI = st.number_input('BMI ')
with col3:
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
    Age = st.number_input('Age')

def generate_output():
    res = predict_(input_data = (pr,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age))
    if (res == 1):
        st.write("Diabitic")
    else:
        st.write("Non diabitic")

# Create a Streamlit web app
st.title("DIABETES PREDICTION")


# Create a button
if st.button("Check"):
    generate_output()
