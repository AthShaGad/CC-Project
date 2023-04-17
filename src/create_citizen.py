import streamlit as st
from database import add_data_citizen
from database import create_table_citizen


def create_citizen():

    col1,col2=st.columns(2)
    with col1:
        firstname=st.text_input("First Name")
        lastname=st.text_input("Last Name")
    with col2:
        aadhar=st.text_input("Enter valid aadhar ")
        gender=st.text_input("Add gender")
        dob=st.date_input("Enter dob")
        phone_no=st.text_input("enter phone no")
    if st.button("Add citizen"):
        create_table_citizen()
        add_data_citizen(firstname,lastname,aadhar,gender,dob,phone_no)
        st.success("Successfully added citizen")