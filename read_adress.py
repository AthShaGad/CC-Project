import pandas as pd
import streamlit as st
from database import view_address


def read_address():
    result=view_address()
    df = pd.DataFrame(result, columns=['aadhar','street','city','state_code'])
    with st.expander("View citizen"):
        st.dataframe(df)
