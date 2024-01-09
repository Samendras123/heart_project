import streamlit as st
import pandas as pd
import pickle

def project():
    # Load the trained model and feature scaler
    model = pickle.load(open('heart_disease_model.pkl', 'rb'))
    scaler = pickle.load(open('feature_scaler.pkl', 'rb'))


    # Function to preprocess the input data
    def preprocess_data(data):
        # Apply feature scaling
        scaled_data = scaler.transform(data)

        return scaled_data

    # Function to predict heart disease
    def predict_heart_disease(data):
        # Preprocess the input data
        preprocessed_data = preprocess_data(data)

        # Make predictions
        prediction = model.predict(preprocessed_data)
        prediction_proba = model.predict_proba(preprocessed_data)[:, 1]  # Probability of heart disease

        return prediction, prediction_proba

    
    # Input form for user to enter features
    st.image('./img1.gif')
    st.write("**Enter the following details to predict the probability of heart disease :**")

    col1, col2 = st.columns(2)

    with col1:
        cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=80, max_value=300, value=150)
        oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, value=1.0)
        age = st.number_input("Age", min_value=1, max_value=100, value=25)

    with col2:
        ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4, value=0)
        thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])
        chol = st.number_input("Cholesterol (mg/dL)", min_value=1, max_value=1000, value=200)
        exang = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])

    cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
    exang = ["No", "Yes"].index(exang)
    thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

    # Create a dataframe with the user input
    data = pd.DataFrame({
        
        "cp": cp,
        "thalach": thalach,
        "oldpeak": oldpeak,
        "age": age,
        "ca": ca,
        "thal": thal,
        "chol": chol,
        "exang": exang
    }, index=[0])

    # Make a prediction when the user clicks the "Predict" button
    st.markdown("***Press the button for Prediction***")
    if st.button("Predict"):
        prediction, prediction_proba = predict_heart_disease(data)


        if prediction[0]:
            st.warning(f"Probability is : {prediction_proba[0]:.3}")
            st.error('Heart disease is Present.')
        else :
            st.info(f"Probability is : {prediction_proba[0]:.3}")
            st.success('Heart disease is not Present.')

