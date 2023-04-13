import pandas as pd
import streamlit as st
from database import view_citizen


def read_citizen():
    result=view_citizen()   # this is defined in the database.py and it basically selects
    df=pd.DataFrame(result,columns=['First Name','Last Name','aadhar','gob','dob','pno'])
    with st.expander("View citizen"):
        st.dataframe(df)

# def edit_citizen():
