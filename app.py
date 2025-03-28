import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import streamlit as st

model = pickle.load(open('model.pkl','rb'))
st.title('Heart Disease have or not')
#'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal',

age = st.slider("Choose age",0,100)
sex = st.slider("Choose sex", 0,1,)

cp = st.slider("chest pain type", 0,3)
trestbps = st.slider("resting blood pressure", 94,220)
chol  = st.slider("serum cholestoral in mg/dl", 126,560)
fbs = st.slider("fasting blood sugar > 120 mg/dl",0,1)

restecg = st.slider("resting electrocardiographic results",0,2)
thalach = st.slider("maximum heart rate achieved",77,212)
exang = st.slider("exercise induced angina", 0,1)
oldpeak = st.slider("oldpeak = ST depression induced by exercise relative to rest", 0,7)
slope = st.slider("the slope of the peak exercise ST segment", 0,2)
ca = st.slider("number of major vessels (0-3) colored by flourosopy", 0,4)
thal = st.slider("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect",0,2)

def predict():
    prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
    if prediction[0] == 1:
        st.success('Patient has Heart Disease :thumbsup:')
    else:
        st.error('Passenger did not has Heart Disease:thumbsdown:') 

trigger = st.button('Predict', on_click=predict)
