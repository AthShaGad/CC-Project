import pandas as pd
import streamlit as st
from database import delete_address_db,view_address
def delete_address():
    result = view_address()
    df = pd.DataFrame(result, columns=['aadhar', 'street', 'city', 'state_code'])
    with st.expander("View citizen"):
        st.dataframe(df)
    del_aadhar=st.text_input("Enter the aadhar to be deleted")
    delete_address_db(del_aadhar)
    st.success("Deleted successfully")
