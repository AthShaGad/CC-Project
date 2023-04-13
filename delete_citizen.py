import pandas as pd
import streamlit as st
from database import view_citizen,delete_citizen_db


def delete_citizen():
    result = view_citizen()  # this is defined in the database.py and it basically selects
    df = pd.DataFrame(result, columns=['First Name', 'Last Name', 'aadhar', 'gob', 'dob', 'pno'])
    with st.expander("View citizen"):
        st.dataframe(df)
    del_aadhar = st.text_input("enter aadhar no to be deleted")
    if(st.button("Delete citizen")):    
        delete_citizen_db(del_aadhar)
        st.success("Deleted successfully")
        result2 = view_citizen()
        df2 = pd.DataFrame(result2 , columns=['First Name' , 'Last Name' , "aadhar" , "gob" , "dob" , "pno"])
        with st.expander("Updated data"):
            st.dataframe(df2)