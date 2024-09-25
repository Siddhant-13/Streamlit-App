import streamlit as st

st.title('Hello World')
st.subheader('This is the subheader')
name = st.text_input("Enter your name:")
st.write('Hello ', name)    

maths = st.slider("Enter your marks:",0,100)
st.write(name,'scored ', maths ,' in math')
exam = st.radio('Choose an exam',['GRE','GMAT'])
st.write("Start preparing for ", exam, ' kyuki ', maths , ' marks aaye hai')

subjects = st.multiselect("Choose your subject",['Phy','Chem','Bio','Math'])
st.write('You chose ', subjects)
import pandas as pd
upload = st.file_uploader('Choose a file', type = 'xlsx')

if upload is not None:
    df = pd.read_excel(upload)
    st.write(df)