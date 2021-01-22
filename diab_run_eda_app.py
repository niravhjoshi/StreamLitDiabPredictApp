import streamlit as st
import pandas as pd

# Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

def diab_run_eda_app():
    st.subheader('Werlcome to EDA Section')
    df = load_data("data/CleanDiabData.csv")
    df_clean= load_data("data/CleanDiabData.csv")
    submenu = st.sidebar.selectbox("SubMenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df)
        with st.beta_expander("Data Types Summary"):
            st.dataframe(df.dtypes)

        with st.beta_expander("Descriptive Summary"):
            st.dataframe(df_clean.describe())

        with st.beta_expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())

        with st.beta_expander("Diabetes Status Count"):
            st.dataframe(df['DiabetesStatus'].value_counts())

    else:
        st.subheader("Plots")
        col1, col2 = st.beta_columns([2, 1])

        with col1:
            with st.beta_expander('Plot for Gender Distribution'):
                st.write(df)
                gen_df=df['Gender'].value_counts().to_frame()
                st.write(gen_df)
                gen_df= gen_df.reset_index()
                gen_df.columns=['Gender Type','Counts']
                p01=px.pie(gen_df, names='Gender Type',values='Counts')
                st.plotly_chart(p01,use_container_width=True)

            with st.beta_expander("Dist Plot of Diabetes"):
                fig = plt.figure()
                sns.countplot(df['DiabetesStatus'])
                st.pyplot(fig)

        with col2:
            with st.beta_expander("Gender Distribution"):
                st.dataframe(df['Gender'].value_counts())

            with st.beta_expander("Diabetes Distribution"):
                st.dataframe(df['DiabetesStatus'].value_counts())

        with st.beta_expander("Outlier Detection Plot"):
            # outlier_df =
            fig = plt.figure()
            sns.boxplot(df['Age'])
            st.pyplot(fig)

            p3 = px.box(df, x='Age', color='Gender')
            st.plotly_chart(p3)

        #Coreleation Chart
        with st.beta_expander("Correlation Plot"):
            corr_matrix = df_clean.corr()
            fig = plt.figure(figsize=(20, 10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)

            p3 = px.imshow(corr_matrix)
            st.plotly_chart(p3)