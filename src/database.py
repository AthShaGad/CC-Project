
import boto3
import mysql.connector
import streamlit as st
import pandas as pd
ENDPOINT="cc-clone-1.c5l9me1mzs0v.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
REGION="us-east-1"
DBNAME="rtoC"

# session = boto3.Session(profile_name='default')
# client = session.client('rds')

# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

mydb = mysql.connector.connect(
host=ENDPOINT, user='admin', password='lemon1234',port=PORT, database=DBNAME
)
c = mydb.cursor()


def create_table_citizen():
    c.execute('create table if not exists citizen(firstname varchar(30),lastname varchar(30),aadhar varchar(12),gender char(1),dob DATE ,phone_no varchar(12),PRIMARY KEY (aadhar))')


def add_data_citizen(firstname,lastname,aadhar,gender,dob,phone_no):
    c.execute("insert into citizen(firstname,lastname,aadhar,gender,dob,phone_no) values (%s,%s,%s,%s,%s,%s )",(firstname,lastname,aadhar,gender,dob,phone_no))
    mydb.commit()


def view_citizen():
    c.execute('select * from citizen')
    data = c.fetchall()
    return data

def update_data_citizen(firstname,lastname,aadhar,gender,dob,phone_no):
    c.execute("update citizen set firstname=%s,lastname=%s,gender=%s,dob=%s,phone_no=%s where aadhar = %s",(firstname,lastname,gender,dob,phone_no,aadhar))
    mydb.commit()
    return

def delete_citizen_db(aadhar):
    c.execute('delete from citizen where aadhar="{}"'.format(aadhar))
    mydb.commit()

def create_table_address():
     c.execute('create table if not exists address(aadhar varchar(10) ,street varchar(50),city varchar(30),state_code varchar(30) ,primary key(aadhar),foreign key(aadhar) references citizen(aadhar))')

def add_data_address(aadhar,street,city,state_code):
    c.execute("insert into address(aadhar,street,city,state_code) values (%s,%s,%s,%s)",(aadhar,street,city,state_code))
    mydb.commit()

def view_address():
    c.execute('select * from address')
    data=c.fetchall()
    return data

def update_data_address(aadhar, street, city, state_code):
    c.execute("update address set street=%s,city=%s,state_code=%s where aadhar=%s",(street, city, state_code , aadhar))
    mydb.commit()
    return

def delete_address_db(aadhar):
    c.execute('delete from address where aadhar="{}"'.format(aadhar))
    mydb.commit()

def create_table_ll():
    c.execute('create table if not exists ll (ll_id int NOT NULL AUTO_INCREMENT , ll_status char(1) , ll_date date ,aadhar varchar(10) , primary key(ll_id),foreign key(aadhar) references citizen(aadhar))')

def add_table_ll(aadhar,ll_date,ll_status):
    c.execute("insert into ll(ll_status,ll_date,aadhar) values (%s,%s,%s)",(ll_status,ll_date,aadhar))
    mydb.commit()

def view_ll():
    c.execute('select * from ll')
    data=c.fetchall()
    return data

def update_data_ll(aadhar):
    c.execute("update ll set ll_status=%s where aadhar=%s",(1,aadhar))
    mydb.commit()
    return 

def create_table_dl():
        c.execute('create table if not exists dl (dl_id int NOT NULL AUTO_INCREMENT, dl_status char(1) , dl_date date  ,aadhar varchar(10), primary key(dl_id), foreign key (aadhar) references  citizen (aadhar) )')

def add_data_dl(aadhar,dl_date):
        c.execute("insert into dl (aadhar,dl_status,dl_date)values (%s,%s,%s)",(aadhar,1,dl_date))
        mydb.commit()

def view_dl():
    c.execute('select * from dl')
    return c.fetchall()

# def create_table_license():
#     c.execute('create table if not exists license (lid int ,aadhar varchar(10) ,name varchar(10),license_no int,license_issue_date date,license_expiry_date date,primary key(lid,aadhar),foreign key (aadhar) references  citizen (aadhar))')

# def add_data_license(lid,aadhar,name,license_no,license_issue_date,license_expiry_date):
#     c.execute("insert into license values (%s,%s,%s,%s,%s,%s)",(lid,aadhar,name,license_no,license_issue_date,license_expiry_date))
#     mydb.commit()
#     pass

# def view_license():
#     c.execute('select * from license')
#     return c.fetchall()

def add_function(text):
    # st.text(text)

    c.execute('select state_code({})'.format(text))

    return c.fetchall()

def display_join1():

    c.execute('select firstname,lastname ,citizen.aadhar,gender,dob,phone_no,street,city,state_code from citizen inner join address on address.aadhar=citizen.aadhar')
    return c.fetchall()


def display_join2():
    c.execute('select firstname,lastname,dl.aadhar,dob from citizen inner join dl on dl.aadhar=citizen.aadhar')
    return c.fetchall()


def display_procedure_mod():
    c.execute('create  or replace view aadhars as select  aadhar from ll except select aadhar from dl')
    data=c.callproc("class_mod")
    for result in c.stored_results():
        st.dataframe(result.fetchall())


def display_procedure(text):
    if text=="M":
        data=c.callproc("GetCitizen1",["M",])
        for result in c.stored_results():
            st.dataframe(result.fetchall())
    elif text == "F":
        data = c.callproc("GetCitizen1", ["F", ])
        for result in c.stored_results():
            st.dataframe(result.fetchall())
    # st.dataframe(data)
    # return  c.fetchall()

def query_line():
    txt = st.text_input("enter sql")
    c.execute(txt)
    data=c.fetchall()
    st.dataframe(data)
    # st.write(data)
    # df = pd.DataFrame(data, columns=['First Name', 'Last Name', 'aadhar', 'gob', 'dob', 'pno'])
    # with st.expander("View citizen"):
    #     st.dataframe(df)