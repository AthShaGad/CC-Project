import streamlit as st
import  pandas as pd
from database import create_table_dl
from database import add_data_dl
# from database import checker
from read_dl import read_dl


def create_dl():
    col1,col2=st.columns(2)
    with col1:
        dl_id = st.text_input("Enter aadhar no")
        dl_date = st.date_input("Enter DL_date")
    if st.button("Create DL"):
        create_table_dl()
        # read_dl()
        add_data_dl(dl_id , dl_date)
        st.success("Created DL")
        read_dl()
        