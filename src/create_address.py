import streamlit as st
# from database import create_table_address
from database import add_data_address
from database import view_address
import pandas as pd



def create_address():
    col1,col2=st.columns(2)
    with col1:
        aadhar=st.text_input("Enter aadhar details")
    with col2:
        street=st.text_input("Enter street details")
        city=st.text_input("Enter city")
        state_code=st.text_input("Enter PIN code")
    if st.button("add address"):
        add_data_address(aadhar,street,city,state_code)
        st.success("address successfully added")
        result2 = view_address()
        df2 = pd.DataFrame(result2 , columns=["aadhar","street","city","state_code"])
        with st.expander("Viewing address data"):
            st.dataframe(df2)
