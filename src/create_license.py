import streamlit as st
from database import create_table_license
from database import add_data_license

def create_license():
    col1,col2=st.columns(2)
    with col1:
        lid=st.number_input("enter license id")
        aadhar=st.text_input("enter aadhar")
    with col2:
        name=st.text_input("Enter name")
        license_no=st.number_input("Enter license no")
        license_issue_date=st.date_input("Enter license issue date")
        license_expiry_date=st.date_input("Enter license expiry date")
    if st.button("Create License"):
        create_table_license()
        add_data_license(lid,aadhar,name,license_no,license_issue_date,license_expiry_date)
        lula=name
        st.success(f"Driving license created for'{lula}'")

