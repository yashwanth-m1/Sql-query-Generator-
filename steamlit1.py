import streamlit as st
from app import get_gemini_response, read_sql_query
from app import prompt



#set page configuration
st.set_page_config(page_title="AI SQL Query Generator", page_icon=":robot_face:")
st.image("1234.png", width=200)
st.markdown(" ai powered sql query Assitent ")

#user input
user_question=st.text_input("Enter your question about the student database:")
submit = st.button("Generate SQL Query")
if submit :
    response=get_gemini_response(user_question,prompt)
    print("Generated SQL Query:", response)
    response =read_sql_query(response, 'student.db')
    st.subheader("Generated SQL Query:")
    
    for row in response:
        print(row)
        st.header(row)
