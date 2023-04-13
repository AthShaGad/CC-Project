import pandas as pd
import streamlit  as st
from database  import view_dl
def read_dl():
    result = view_dl()  # this is defined in the database.py and it basically selects
    df = pd.DataFrame(result, columns=['dl_id','DL_STATUS' , 'DL_DATE' , "AADHAR"])
    with st.expander("View Dl"):
        st.dataframe(df)