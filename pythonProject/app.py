import streamlit as st
import helper
import pickle

rf_final = pickle.load(open('C:/Users/mansi/OneDrive/Desktop/Study/Data Science Projects/Quora_Question_Pairs/pythonProject/rf_final.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = rf_final.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
