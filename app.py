from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from google import genai
import os
import sqlite3

#Initialize the client with the API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

#funvtion load the google model and generate response
def get_gemini_response( question,prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt[0], question]
    )
    return response.text

#function to retrive query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    data=cursor.execute(sql)
    rows=data.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows
prompt=[""" You are an expert AI assistant that converts natural-language questions into a single, correct, efficient SQL query for a SQLite database named student with the following columns and types:

NAME (VARCHAR)

CLASS (VARCHAR)

SECTION (VARCHAR)

MARKS (INT)

Rules:

Output only the SQL query and nothing else (no explanations, no comments, no extra text).

Use proper SQL syntax and capitalization (e.g., SELECT, FROM, WHERE, GROUP BY, ORDER BY).

Terminate the query with a single semicolon (;).

When filtering, use a WHERE clause with exact string quotes for text (single quotes).

Use appropriate aggregate functions when needed (e.g., COUNT(), AVG(), SUM(), MAX(), MIN()) and include GROUP BY if necessary.

If the user asks for a list of values (e.g., names), return those columns; if they ask for a single metric, return an aggregate.

If the user asks for "all" or no filters, return SELECT * FROM student;.

Avoid unnecessary columns or calculations — return the minimal correct result.

If the user’s request is ambiguous but can be reasonably interpreted, generate the most likely SQL that matches natural interpretation (do not ask clarification).

Do not include markdown code fences or any surrounding formatting — return raw SQL only.

Examples:
Input: GET THE NAMES OF STUDENTS IN CLASS 10th
Output: SELECT NAME FROM student WHERE CLASS='10th';

Input: GET THE AVERAGE MARKS OF STUDENTS IN SECTION A
Output: SELECT AVG(MARKS) FROM student WHERE SECTION='A';
        

convet natural language query to sql query
        """]


#set page configuration
st.set_page_config(page_title="AI SQL Query Generator", page_icon=":robot_face:")
st.image("1234.png", width=200)
st.markdown(" ai powered sql query Assitent ")

st.subheader("Database Schema Summary")
st.write("**Table Name:** `student`")
st.write("**Columns:** `NAME` (VARCHAR), `CLASS` (VARCHAR), `SECTION` (VARCHAR), `MARKS` (INT)")

#user input
user_question=st.text_input("Enter your question about the student database:")
submit = st.button("Generate SQL Query")
if submit :
    query=get_gemini_response(user_question,prompt)
    print("Generated SQL Query:", query)
    
    st.subheader("Generated SQL Query:")
    st.code(query, language="sql")
    
    data = read_sql_query(query, 'student.db')
    st.subheader("Query Results:")
    
    for row in data:
        print(row)
        st.write(row)

    
