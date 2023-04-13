import streamlit as st
import pandas as pd
import datetime
from database import create_table_ll
from database import add_table_ll
from read_ll import read_ll

def create_ll():
    col1,col2=st.columns(2)
    with col1:
        aadhar=st.text_input("Enter aadhar number")  
        ll_date=st.date_input("Enter LL_date")


    if st.button("Apply for ll"):
        ll_status=0
        create_table_ll()
        add_table_ll(aadhar,ll_date,ll_status)
        st.success("successfully applied for ll")
            # result2 = view_citizen()
            # df2 = pd.DataFrame(result2 , columns=['First Name' , 'Last Name' , "aadhar" , "gob" , "dob" , "pno"])
            # with st.expander("Updated data"):
            #     st.dataframe(df2)
        read_ll()

