import pickle
import streamlit as st

model = pickle.load(open('kidney_model.sav', 'rb'))

st.title('Prediksi Penyakit Ginjal Kronis')

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1 :
    age = st.text_input('Age')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    blood_pressure = st.text_input('Blood Pressure')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    specific_gravity = st.text_input('Spesific Gravity')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    albumin = st.text_input('Albumin')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    
with col2 :
    sugar = st.text_input('Sugar')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    red_blood_cells = st.text_input('Red Blood Cells')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    pus_cell = st.text_input('Puss Cell')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    pus_cell_clumps = st.text_input('Puss Cell Clumps')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    
with col3 :
    bacteria = st.text_input('Bacteria')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    blood_glucose_random = st.text_input('Blood Glucose Random')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    blood_urea = st.text_input('Blood Urea')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    serum_creatinine = st.text_input('Serum Creatinine')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    
with col4 :
    sodium = st.text_input('Sodium')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    potassium = st.text_input('Potasium')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    hemoglobin = st.text_input('Hemoglobin')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    packed_cell_volume = st.text_input('Packed Cell Volume')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    
with col5 :
    white_blood_cell_count = st.text_input('White Blood Cell Count')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    red_blood_cell_count = st.text_input('Red Blood Cell Count')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    hypertension = st.text_input('Hypertension')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    diabetes_mellitus = st.text_input('Diabetes Mellitus')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    
with col6 :
    coronary_artery_disease = st.text_input('Coronary Artery Disease')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    appetite = st.text_input('Appetite')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    pedal_edema = st.text_input('Pedal Edema')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    anemia = st.text_input('Anemia')
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    
diagnosis = ''

if st.button('Predict'):
    prediction = model.predict([
        [age,blood_pressure,specific_gravity,albumin,
         sugar,red_blood_cells,pus_cell,pus_cell_clumps,
         bacteria,blood_glucose_random,blood_urea,serum_creatinine,
         sodium,potassium,hemoglobin,packed_cell_volume,
         white_blood_cell_count,red_blood_cell_count,hypertension,
         diabetes_mellitus,coronary_artery_disease,appetite,pedal_edema,anemia]])
    
    if (prediction[0] == 1):
        diagnosis = 'Pasien Tidak Terkena Ginjal Kronis'
    elif (prediction[0] == 0):
        diagnosis = "Pasien Terkena Ginjal Kronis"
        
st.success(diagnosis)