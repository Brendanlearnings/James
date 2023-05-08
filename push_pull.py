#################### IMPORTS ####################
import streamlit as st
from datetime import date
import snowflake.connector
#################################################

def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )
    
st.title('Read and write to Snowflake Database')
st.markdown('This demo sets out to showcase the ease at which data can be captured and retrieved!')

name = st.text_input('Name')
surname = st.text_input('Surname')
dob = st.date_input(
    'Date of Birth',
    min_value = date(1900,1,1),
    max_value = date.today()
    
)

phone = st.text_input('Phone Number')

if st.button('Submit'):
    with init_connection().cursor() as cur:
        cur.execute(f"INSERT INTO GRAFANA.DEMO.USER_INFO (NAME,SURNAME,DOB,PHONE) VALUES('{name}','{surname}','{dob}','{phone}');")
        st.write('Your data has been successfully captured!')


        data = cur.execute('SELECT COUNT(1) FROM GRAFANA.DEMO.USER_INFO;')
        counts = cur.fetchall()
        counts = counts[0]
        st.write(type(counts))
        st.write(f'There has been {counts} submissions')
        cur.close()

    



