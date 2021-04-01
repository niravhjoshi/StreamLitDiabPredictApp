import streamlit as st
import streamlit.components.v1 as stc
from diab_run_eda_app import diab_run_eda_app as run_eda_app
from diab_run_ml_app import diab_run_ml_app as rum_ml_app

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Welcome to Diabetes prediction App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""

def main():
	# st.title("ML Web App with Streamlit")
	stc.html(html_temp)


	menu = ["Home", "EDA", "ML", "About"]
	choice = st.sidebar.selectbox("Menu", menu)
	if choice =='Home':
		st.subheader("Home")
		st.write(("""
			### Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
			"""))
	elif choice == "EDA":
		run_eda_app()
	elif choice == "ML":
		rum_ml_app()

	else:
		st.subheader("About")
		st.text("Welcome to Informatica Hackathon 2021")
		st.text("Team AI/ML IICS")
		st.text("By Nirav,Chandra,Vineeth,Mary,Vishal")

if __name__ == '__main__':
	main()