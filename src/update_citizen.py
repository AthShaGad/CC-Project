import pandas as pd
import streamlit as st
from database import update_data_citizen
from database import view_citizen
def update_citizen():
    result = view_citizen()
    # df = pd.DataFrame(result,
    #                   columns=['lid', 'aadhar', 'name', 'license_no', 'license_issue_date', 'license_expiry_date'])
    df = pd.DataFrame(result , columns=['First Name' , 'Last Name' , "aadhar" , "gob" , "dob" , "pno"])
    with st.expander("View citizen"):
        st.dataframe(df)
    col1, col2 = st.columns(2)
    with col1:
        new_firstname = st.text_input("First Name")
        new_lastname = st.text_input("Last Name")
    with col2:
        new_aadhar = st.text_input("Enter valid aadhar ")
        new_gender = st.text_input("Add gender")
        new_dob = st.date_input("Enter dob")
        new_phone_no = st.text_input("enter phone no")
    if st.button("Update citizen"):
        update_data_citizen(new_firstname,new_lastname,new_aadhar,new_gender,new_dob,new_phone_no)
        st.success("Successfully updated citizen")
        result2 = view_citizen()
        df2 = pd.DataFrame(result2 , columns=['First Name' , 'Last Name' , "aadhar" , "gob" , "dob" , "pno"])
        with st.expander("Updated data"):
            st.dataframe(df2)