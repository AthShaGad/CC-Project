import pandas as pd
import  streamlit as st
from database import view_ll
def read_ll():
    result=view_ll()
    df = pd.DataFrame(result, columns=["L_ID", 'll_status' , 'lldate' , 'aadhar'])
    with st.expander("View Learner license"):
        st.dataframe(df)