#################### IMPORTS ####################
import streamlit as st
from datetime import date
import snowflake.connector
#################################################

def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )
st.write(f'{date.today()}')
st.title('Read and write to Snowflake Database')
st.markdown('This demo sets out to showcase the ease at which data can be captured and retrieved!')

name = st.text_input('Name')
surname = st.text_input('Surname')
dob = st.date_input(
    'Date of Birth',
    date.today()
)
phone = st.text_input('Phone Number')

if st.button('Submit'):
    with init_connection.cursor() as cur:
        cur.execute(f"INSERT INTO VALUES('{name}','{surname}',{dob},'{phone}');")

    



