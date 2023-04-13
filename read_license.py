import streamlit as st
import pandas as pd
from database import view_license

def read_license():
    result=view_license()
    df = pd.DataFrame(result, columns=['lid','aadhar','name','license_no','license_issue_date','license_expiry_date'])
    with st.expander("View citizen"):
        st.dataframe(df)