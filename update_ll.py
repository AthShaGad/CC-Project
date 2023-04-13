import pandas as pd
import streamlit as st
from  database import update_data_ll
from read_ll import read_ll
def update_ll():
    # result = view_ll()
    # df = pd.DataFrame(result, columns=['aadhar', 'll_date' ,'ll_status'])
    # with st.expander("Learner license"):
    #     st.dataframe(df)
    read_ll()
    col1,col2=st.columns(2)
    with col1:
        aadhar=st.text_input("Enter aadhar to be update")

    if st.button("Set ll Status"):
        update_data_ll(aadhar)
        st.success("Updated successfully")
        read_ll()


