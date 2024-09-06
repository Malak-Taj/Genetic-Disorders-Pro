import streamlit as st
import pandas as pd
# Load the data
gene = pd.read_csv("cleaned_gene.csv")  # Load the CSV file
# gene = pd.read_pickle('gene.pkl')
st.markdown("""
    <h1 style='text-align: center; color: #ff6347; font-family: Arial; font-size: 2em;'>Genetic Disorders In Chidren!</h1>
""", unsafe_allow_html=True)
st.write("""          
 """)
col1, col2 = st.columns(2)
with col1:
    st.write(""" A genetic disorder is a health problem caused by one or more abnormalities in the genome. It can be caused by a mutation in a single gene (monogenic) or multiple genes (polygenic) or by a chromosome abnormality.
            Genetic disorders are present before birth, and some genetic disorders produce birth defects.
            [ Explore More !](https://en.wikipedia.org/wiki/Genetic_disorder)""")
with col2:
    st.image("https://media.istockphoto.com/id/1345840773/photo/girl-with-down-syndrome-is-preparing-to-go-to-first-class.jpg?s=612x612&w=0&k=20&c=o4Ll3H-01WRIYHexkKo0eXASJeukiTVC4hd7h3u3F-g=")
# Create a selectbox
options = [ "" ,"Medical Terminologies"," Simple Data Description","Data Features","Data Sample", "Questions For Analysis" ]
selected_option = st.selectbox("Choose An Option And Get familiar with the data !", options)

# Display a sentence based on the selected option
if selected_option == options[0]:
    st.write("<p style='color:red'>Please, Select The Option That Makes You Feel Familiar With The Data !</p>", unsafe_allow_html=True) 
elif selected_option == options[1]:
    st.write("""
    - **Birth Asphyxia**: A condition where the baby does not receive enough oxygen during birth.
    - **Heart Rate (rates/min)**: The number of heartbeats per minute for the patient.
    - **Respiratory Rate (breaths/min)**: The number of breaths the patient takes per minute.
    - **Anomalies in Previous Pregnancies**: Complications in previous pregnancies.
    - **Abortion**: Death of the baby.
    - **Birth Defects**: Complications in the baby's birth.
    - **Folic Acid (mg/dL)**: A hormone that affects the growth and development of the baby.
    - **Maternal Illness**: Any medical condition affecting the mother.
    - **Blood Cell Count (mcL)**: The number of blood cells per microliter of blood.
    - **White Blood Cell Count (mcL)**: The number of white blood cells per microliter of blood.
    """)
elif selected_option == options[2]:
    st.write("""
    * The dataset contains the following:
    * 31,548 rows and 25 features.
    * The target variable is 'Disorder Genetic Class' with 3 classes.
    * This dataset is part of the HackerEarth Machine Learning Challenge: Genetic Disorders.
    * [SOURCE!](https://www.hackerearth.com/challenges/new/competitive/hackerearth-machine-learning-challenge-genetic-testing/)
    """)
elif selected_option == options[3]:
    st.write("""
    * Patient_Age: Age of the patient.
    * Maternal_gene: Genetic information from the mother.
    * Paternal_gene: Genetic information from the father.
    * Blood_cell_count_(mcL): The count of blood cells per microliter of blood.
    * Mother's_age: Age of the mother.
    * Father's_age: Age of the father.
    * Status: Current status of the patient(alive, deceased).
    * Respiratory_Rate_(breaths/min): Number of breaths taken per minute.
    * Heart_Rate_(rates/min): Number of heartbeats per minute.
    * Follow-up: Details on actions taken after initial diagnosis.
    * Gender: Gender of the patient.
    * Birth_asphyxia: Lack of oxygen at birth.
    * Autopsy_shows_birth_defect: Indicates whether an autopsy revealed birth defects.
    * Folic_acid_details: Information about folic acid intake.
    * H/O_serious_maternal_illness: History of serious illness in the mother.
    * H/O_radiation_exposure_(x-ray): History of radiation exposure(X-rays).
    * H/O_substance_abuse: History of substance abuse by the mother or father.
    * Assisted_conception_IVF/ART: Whether assisted reproductive technologies.
    * History_of_anomalies_in_previous_pregnancies: complications in previous pregnancies.
    * No._of_previous_abortion: Number of previous abortions the mother has had.
    * Birth_defects: Any defects present at birth.
    * White_Blood_cell_count_(thousand_per_microliter): The count of white blood cells per microliter of blood.
    * Blood_test_result: Results from blood tests.
    * Genetic_Disorder: The specific genetic disorder diagnosed.
    * Disorder_Subclass: A subclass or type within the broader category of the genetic disorder.""")
elif selected_option == options[4]:
    st.write(gene.head())
elif selected_option == options[5] :
    st.write("""
    **Questions:**
    1. Which genetic disorder is most common among people?
    2. Which genetic disorder subclass is most common among Major Classes?
    3. Are genetic disorders mostly paternal or maternal?
    4. What is the relation between gender and these disorders?
    5. Did Folic Acid affect the cases?
    6. What is the relation between Birth Asphyxia (Lack of Oxygen) and Birth Defects?
    """)

# Link to the dataset in kaggle
if st.button("Go to the dataset in Kaggle"):
    st.markdown("[Click here to view the dataset](https://www.kaggle.com/datasets/aryarishabh/of-genomes-and-genetics-hackerearth-ml-challenge/data)", unsafe_allow_html=True)

