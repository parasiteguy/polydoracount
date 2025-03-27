#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:36:36 2025

@author: w00451725
"""

#App Streamlit File

import streamlit as st
import pandas as pd
import joblib

# Load the trained Random Forest model
rf_model = joblib.load('dummymodel.pkl')

st.title('Polydora Intensity Predictor')

temperature = st.number_input('Temperature (°C)', value=15.0)
salinity = st.number_input('Salinity (ppt)', value=28.0)
ph = st.number_input('pH', value=8.0)
oyster_size = st.number_input('Oyster Size (mm)', value=80)

if st.button('Predict Intensity'):
    future_conditions = pd.DataFrame([[temperature, salinity, ph, oyster_size]],
                                     columns=['Temperature (°C)', 'Salinity (ppt)', 'pH', 'Oyster Size (mm)'])
    prediction = rf_model.predict(future_conditions)
    st.write(f'Predicted Polydora Intensity: {prediction[0]:.2f}')
