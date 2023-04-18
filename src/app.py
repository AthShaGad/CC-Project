import streamlit as st
import pandas as pd
from create_citizen import create_citizen
from read_citizen import read_citizen
from delete_citizen import delete_citizen
from database import query_line
from database import create_table_address
from create_address import create_address
from read_adress import read_address
from create_ll import create_ll
from create_dl import create_dl
from read_dl import read_dl
# from create_license import create_license
# from read_license import read_license
from update_citizen import update_citizen
from update_address import update_address
from delete_address import delete_address
from update_ll import update_ll
from read_ll import read_ll
from PIL import Image
from database import add_function
from database import display_join1
from database import display_join2
from database import display_procedure
from database import display_procedure_mod

def main():
    st.title("Rto system")
    st.subheader("Created for CC_Project")
    # inspector=0
    #
    # if st.button("press if you are a citizen"):
    #     inspector=10
    #     st.write("hello loser")
    # if st.button("press if you are inspector"):
    #     inspector=11
    #     st.write("enter password")
    # image = Image.open('sunrise.jpg')
    # st.image(image, caption='RTO Office pic')

    # not inspector case

    menu=["Citizen", "address","Details", "Query Line","apply for ll","Apply for DL","Function","LicenseRaj","gender","mod"]
    choice=st.sidebar.selectbox("Menu", menu)
    if choice == "Citizen":
        st.subheader("Citizen details")
        citizen_menu=["Add","View","Update","Delete"]
        citizen_choice=st.selectbox("Menu",citizen_menu)
        if citizen_choice=="Add":
            st.subheader("Enter details")
            create_citizen()
        elif citizen_choice=="View" :
            read_citizen()
        elif citizen_choice=="Update" :
            st.write("Update mode on")
            update_citizen()
        elif citizen_choice=="Delete" :
            delete_citizen()

    elif choice=="address":
        read_citizen()
        create_table_address()
        st.subheader("address details")
        address_menu=["Add","View","Update","Delete"]
        address_choice=st.selectbox("Menu",address_menu)
        if address_choice=="Add":
            st.subheader("enter details")
            create_address()
            #call the add function for address addtion
        elif address_choice=="View" :
            # st.subheader("view baby")
            read_address()
            #call the view function
        elif address_choice=="Update":
            update_address()
        elif address_choice=="Delete":
            delete_address()

    elif choice=="apply for ll":
        # st.write("apply for dl")
        ll_menu=["Apply for ll","Set ll status","View ll"]
        ll_choice=st.selectbox("Menu",ll_menu)
        read_citizen()
        if ll_choice=="Apply for ll":
            create_ll()
        elif ll_choice=="Set ll status":
            update_ll()
        elif ll_choice=="View ll":
            read_ll()

    elif choice=="Apply for DL":
        DL_menu=["Add","View"]
        dl_choice=st.selectbox("Menu",DL_menu)
        read_citizen()
        read_ll()
        if dl_choice=="Add":
            create_dl()
        elif dl_choice=="View":
            read_dl()

    elif choice == "Query Line":
            query_line()
    elif choice=="Function":
        state_code= st.text_input("Enter state details")
        if st.button("add statecode"):

            data=add_function(state_code)
            st.dataframe(data)

            st.success("Query submitted")
    elif choice =="Details":
        if st.button("Display information"):
            results=display_join1()
            df = pd.DataFrame(results, columns=['firstname','lastname','aadhar','gender','dob','phone_no','street','city','state_code'])
            with st.expander("Citizen details"):
                st.dataframe(df)
    

if __name__ == "__main__":
    main()
