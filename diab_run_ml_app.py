import streamlit as st
import joblib
import os
import numpy as np

attrib_info = """
#### Attribute Information:
    - Age 5-90
    - Patternal Family History 0.No 1.Yes
    - Matternal Family History 0.No 1.Yes
    
    - Weight_KG 10-400KG
    - Height_Inch 3-10 Inch.
    - Gender 1.Male, 0.Female.
    - Diabetes Hyper 1.Yes, 2.No.
"""
label_dict = {"No":0,"Yes":1}
gender_map = {"Female":0,"Male":1}
target_label_map = {"Negative":0,"Positive":1}

['Age','Patternal_Family','Matternal_Family','Weight_KG',
 'Height_Inch','Gender','Diabetes_Status']


def get_fvalue(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value

# Load ML Models
@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


#run ML File function
def diab_run_ml_app():
    st.subheader("Welcome to Machine Learning Section")
    loaded_model=load_model('models/random_forst_model_Nirav.pkl');

    with st.beta_expander("Attributes Info"):
        st.markdown(attrib_info, unsafe_allow_html=True)

    #Design Layout of APP
    col1, col2 = st.beta_columns(2)

    with col1:
        age = st.number_input("Age", 5, 100)
        gender = st.radio("Gender", ("Female", "Male"))
        Patternal_DiabeticHistory = st.radio("Patternal Side DiabeticHistory", ["No", "Yes"])
        Matternal_DiabeticHistory = st.radio("Matternal Side DiabeticHistory", ["No", "Yes"])
        Weight_Kg = st.number_input("Weight in KG", 5, 400)
        Height_Inch = st.number_input("Height Inch", 2, 11)

    with st.beta_expander("Your Selected Options"):
        results = {
            'Age':age,
            'Gender':gender,
            'Patternal_Diabetic':Patternal_DiabeticHistory,
            'Matternal_Diabetic':Matternal_DiabeticHistory,
            'Weight_KG':Weight_Kg,
            'Height_Inch':Height_Inch
        }
        st.write(results)
        #
        encoded_array=[]
        for i in results.values():
            if type(i) == int:
                encoded_array.append(i)
            elif i in ["Female","Male"]:
                res = get_value(i,gender_map)
                encoded_array.append(res)
            else:
                encoded_array.append(get_fvalue(i))
        #debug info
        st.write(encoded_array)

    with st.beta_expander("Prediction Results"):
        single_sample= np.array(encoded_array).reshape(1,-1)
        st.write(single_sample)

        '''Now update using ML model to get our prediction'''
        prediction = loaded_model.predict(single_sample)
        predict_probability = loaded_model.predict_proba(single_sample)
        st.write(prediction)

        '''Now formatted prediction result'''
        if prediction ==1:
            st.warning("Positive Risk-{}".format(prediction[0]))
            pred_probability_score = {"Negative DM": predict_probability[0][0] * 100, "Positive DM": predict_probability[0][1] * 100}
            st.subheader("Prediction Probability Score")
            st.json(pred_probability_score)
        else:
            st.success("Negative Risk-{}".format(prediction[0]))
            pred_probability_score = {"Negative DM": predict_probability[0][0] * 100, "Positive DM": predict_probability[0][1] * 100}
            st.subheader("Prediction Probability Score")
            st.json(pred_probability_score)
