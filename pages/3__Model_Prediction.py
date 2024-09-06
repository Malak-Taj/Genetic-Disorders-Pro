import streamlit as st
import joblib
import numpy as np

# Load model file
model = joblib.load("genes_model.pkl")

# Streamlit app title
st.markdown("""
    <h1 style='text-align: center; color: #ff6347; font-family: Arial; font-size: 2em;'>Model Prediction</h1>
""", unsafe_allow_html=True)

# Get user inputs
Patient_Age = st.slider("Enter Patient's Age", min_value=0, max_value=10)
gender = st.selectbox("Gender", ['', 'Male', 'Female', 'Ambiguous'])
Mother_age = st.slider("Enter Mother's Age", min_value=0, max_value=70)
father_age = st.slider("Enter Father's Age", min_value=0, max_value=70)
maternal_gene = st.selectbox("Is It Inherited From Mother?", ['', 'Yes', 'No'])
serious_maternal_illness = st.selectbox("Any Historical Maternal Illness?", ['', 'Yes', 'No'])
Previous_abortion = st.slider("No. Of Previous Abortions", min_value=0, max_value=10)
blood_test_result = st.selectbox("Blood Test Result", ['', 'slightly abnormal', 'normal', 'inconclusive', 'abnormal'])
birth_defects = st.selectbox("Any Birth Defects?", ['', 'Multiple', 'Singular'])
Folic_acid = st.selectbox("Did The Mother Take Folic Acid During Pregnancy?", ['', 'Yes', 'No'])
Birth_asphyxia = st.selectbox("Birth Asphyxia?", ['', 'Yes', 'No'])
radiation_exposure_x_ray = st.selectbox("Any Historical Radiation Exposure?", ['', 'Yes', 'No'])
History_of_anomalies_in_previous_pregnancies = st.selectbox("Anomalies in Previous Pregnancies?", ['', 'Yes', 'No'])
Blood_cell_count = st.slider("Red Blood Cells Rate", min_value=0, max_value=10000)
White_Blood_cell_count_thousand_per_microliter = st.slider("White Blood Cells Rate", min_value=0, max_value=10000)
Heart_Rate = st.selectbox("Heart Rate Of The Patient", ['','Normal', 'Tachycardia'])
Respiratory_Rate = st.selectbox("Respiratory Rate Of The Patient", ['','Normal', 'Tachypnea'])
Status = st.selectbox("Patient's Status?", ['', 'Alive', 'Deceased'])
Assisted_conception_IVF_ART = st.selectbox("Assisted Conception IVF/ART?", ['', 'Yes', 'No'])

# Convert categorical inputs to numerical values
gender_mapping = {'Male': 0, 'Female': 1, 'Ambiguous': 2}
maternal_gene_mapping = {'Yes': 1, 'No': 0}
serious_maternal_illness_mapping = {'Yes': 1, 'No': 0}
blood_test_result_mapping = {'slightly abnormal': 1, 'normal': 0, 'inconclusive': 2, 'abnormal': 3}
birth_defects_mapping = {'Multiple': 1, 'Singular': 0}
Folic_acid_mapping = {'Yes': 1, 'No': 0}
Birth_asphyxia_mapping = {'Yes': 1, 'No': 0}
radiation_exposure_mapping = {'Yes': 1, 'No': 0}
History_of_anomalies_mapping = {'Yes': 1, 'No': 0}
Heart_Rate_mapping = {'Normal': 1, 'Tachycardia': 0}
Respiratory_Rate_mapping = {'Normal': 1, 'Tachypnea': 0}
status_mapping = {'Alive': 0, 'Deceased': 1}
Assisted_conception_mapping = {'Yes': 1, 'No': 0}

# Multiply Blood Cell Count by 1000
Blood_cell_count_adjusted = Blood_cell_count * 1000

# Collect input features in the correct order
input_data = np.array([
    Patient_Age,
    Mother_age,
    father_age,
    gender_mapping.get(gender, 0),  # Default to 0 if no input
    maternal_gene_mapping.get(maternal_gene, 0),
    serious_maternal_illness_mapping.get(serious_maternal_illness, 0),
    Previous_abortion,
    blood_test_result_mapping.get(blood_test_result, 0),
    birth_defects_mapping.get(birth_defects, 0),
    Folic_acid_mapping.get(Folic_acid, 0),
    Birth_asphyxia_mapping.get(Birth_asphyxia, 0),
    radiation_exposure_mapping.get(radiation_exposure_x_ray, 0),
    History_of_anomalies_mapping.get(History_of_anomalies_in_previous_pregnancies, 0),
    Blood_cell_count_adjusted,  # Use the adjusted value
    White_Blood_cell_count_thousand_per_microliter,
    Heart_Rate_mapping.get(Heart_Rate, 0),
    Respiratory_Rate_mapping.get(Respiratory_Rate, 0),
    status_mapping.get(Status, 0),
    Assisted_conception_mapping.get(Assisted_conception_IVF_ART, 0),
    *([0] * (50 - 19))  # Example placeholder for remaining features
]).reshape(1, -1)

# Prediction
class_mapping = {
    1: 'Mitochondrial Genetic Disorder Class',
    2: 'Single Gene Genetic Disorder Class',
    3: 'Multifactorial Genetic Disorder Class',
    # Add more classes if your model has more
}
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        predicted_class_num = prediction[0]
        predicted_class = class_mapping.get(predicted_class_num, "Unknown")
        st.success(f"The predicted class is: **{predicted_class}**")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
