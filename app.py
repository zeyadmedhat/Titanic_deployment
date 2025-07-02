
import pandas as pd
import plotly.express as px
import streamlit as st

# page layout
st.set_page_config(layout='wide', page_title='Titanic Survival Analysis', page_icon=':ship:')

# Add image
st.image('https://raw.githubusercontent.com/Masterx-AI/Project_Titanic_Survival_Prediction_/main/titanic.jpg')

# Add title
# st.title('Titanic Survival Analysis')

# Add centered Title
st.markdown("""
    <h1 style='text-align: center; color: white;'>Titanic Survival Analysis</h1>
    <p style='text-align: center; color: white;'>An interactive analysis of Titanic passenger data</p>
""", unsafe_allow_html=True)

# Read the dataset
st.subheader('Dataset Overview')
st.write('This dataset contains information about the passengers aboard the Titanic, including their demographics and survival status.')
df = pd.read_csv('Titanic-Dataset.csv')
st.dataframe(df.head())

page = st.sidebar.radio('Pages', ['Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis'])

if page == 'Univariate Analysis':
    # st.plotly_chart(px.histogram(data_frame=df, x='Age', title='Age Distribution of Titanic Passengers'))

    # st.plotly_chart(px.pie(data_frame=df, names='Survived', title='Survival Distribution of Titanic Passengers'))

    col = st.selectbox('Select Column', df.columns)

    chart = st.selectbox('Select Chart Type', ['Histogram', 'Box Plot', 'Pie Chart'])

    if chart == 'Histogram':
        st.plotly_chart(px.histogram(data_frame=df, x=col, title=f'{col} Distribution of Titanic Passengers'))

    elif chart == 'Box Plot':
        st.plotly_chart(px.box(data_frame=df, x=col, title=f'{col} Distribution of Titanic Passengers'))

    elif chart == 'Pie Chart':
        st.plotly_chart(px.pie(data_frame=df, names=col, title=f'{col} Distribution of Titanic Passengers'))

elif page == 'Bivariate Analysis':
    st.write('Bivariate Analysis')

elif page == 'Multivariate Analysis':
    st.write('Multivariate Analysis')

