# from dotenv import load_dotenv
# load_dotenv()  #load all envirom=nment variable
# import streamlit as st
# import os
# import sqlite3
# import google.generativeai as genai
# ## configure Genai key

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(question, prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt[0], question])
#     return response.text

# ## Fucntion To retrieve query from the database

# def read_sql_query(sql,db):
#     conn=sqlite3.connect(db)
#     cur=conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()  ##
#     conn.close()   ##
#     for row in rows:
#         print(row)
#     return rows

# ## Define Your Prompt
# prompt=['''
# You are an expert in converting English questions to SQL query!
# The SQL database has the name STUDENT and has the following columns NAME, CLASS, SECTION ,  MARKS .
# For example,
#     Example 1 - How many entries of records are present?,
#                 the SQL command will be something like this 
#                     SELECT COUNT(*) FROM STUDENT ;
#     Example 2 - Tell me all the students studying in Data Science class?,
#                 the SQL command will be something like this 
#                     SELECT * FROM STUDENT where CLASS="Data Science";
# also the sql code should not have ``` in beginning or end and sql word in output
# '''
# ]

# ## Streamlit App

# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")
# question=st.text_input("Input: ", key="input")
# submit=st.button("Ask the question")

# #if submit is clicked
# if submit:
#     response=get_gemini_response (question, prompt)
#     print(response)
#     response=read_sql_query(response, "student.db")
#     st.subheader("The Response is")
#     for row in response:
#         print(row)
#         st.header(row)

from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Genai key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit App Configuration
st.set_page_config(page_title="SQL Query Generator", layout="wide")

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    try:
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            columns = [description[0] for description in cur.description]  # Extract column names
            return columns, rows
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []

# Define your prompt
prompt = ['''
          
You are a highly advanced SQL query generator. Your task is to convert natural language questions into accurate SQL queries for a database named STUDENT. The database schema is as follows:

- **Table Name:** STUDENT
- **Columns:**
  - **NAME** (TEXT): The name of the student.
  - **CLASS** (TEXT): The class the student is enrolled in.
  - **SECTION** (TEXT): The section the student belongs to.
  - **MARKS** (INTEGER): The marks obtained by the student.

### Guidelines:
1. **Query Format:** Generate SQL queries without any leading or trailing backticks (```) or the SQL keyword.
2. **Ensure Accuracy:** Your SQL queries should be syntactically correct and accurately reflect the schema.
3. **Complex Queries:** Consider advanced SQL functionalities such as joins, subqueries, and complex conditions where appropriate.
4. **Use Examples:** Review the diverse examples below to understand how to structure your queries and handle different scenarios.

### Examples:

1. **Basic Count:**
   - **Question:** "How many records are in the database?"
   - **SQL Query:** `SELECT COUNT(*) FROM STUDENT;`

2. **List All Students in a Class:**
   - **Question:** "List all students in the Data Science class."
   - **SQL Query:** `SELECT * FROM STUDENT WHERE CLASS = "Data Science";`

3. **Names of Students with High Marks:**
   - **Question:** "What are the names of students who scored more than 90?"
   - **SQL Query:** `SELECT NAME FROM STUDENT WHERE MARKS > 90;`

4. **Students in a Specific Section:**
   - **Question:** "Which students are in section B?"
   - **SQL Query:** `SELECT NAME FROM STUDENT WHERE SECTION = "B";`

5. **Average Marks in a Class:**
   - **Question:** "What is the average marks for students in the 'NLP' class?"
   - **SQL Query:** `SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = "NLP";`

6. **Students with Minimum Marks:**
   - **Question:** "Who scored the minimum marks in the 'Data Science' class?"
   - **SQL Query:** `SELECT NAME FROM STUDENT WHERE CLASS = "Data Science" ORDER BY MARKS ASC LIMIT 1;`

7. **Total Marks per Class:**
   - **Question:** "What is the total marks obtained by students in each class?"
   - **SQL Query:** `SELECT CLASS, SUM(MARKS) FROM STUDENT GROUP BY CLASS;`

8. **Top 3 Students by Marks:**
   - **Question:** "Who are the top 3 students with the highest marks?"
   - **SQL Query:** `SELECT NAME FROM STUDENT ORDER BY MARKS DESC LIMIT 3;`

9. **Students with Specific Marks:**
   - **Question:** "List the names of students who scored exactly 88 marks."
   - **SQL Query:** `SELECT NAME FROM STUDENT WHERE MARKS = 88;`

10. **Students in Multiple Classes:**
    - **Question:** "List all students who are in both 'Data Science' and 'DL' classes."
    - **SQL Query:** `SELECT NAME FROM STUDENT WHERE CLASS IN ("Data Science", "DL");`

11. **Students with Highest Marks in Each Class:**
    - **Question:** "List the student(s) with the highest marks in each class."
    - **SQL Query:** `SELECT CLASS, NAME, MARKS FROM STUDENT WHERE (CLASS, MARKS) IN (SELECT CLASS, MAX(MARKS) FROM STUDENT GROUP BY CLASS);`

12. **Students with Above Average Marks:**
    - **Question:** "Who scored above the average marks in their class?"
    - **SQL Query:** `SELECT NAME, CLASS, MARKS FROM STUDENT WHERE MARKS > (SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = STUDENT.CLASS);`

13. **Marks Distribution Across Sections:**
    - **Question:** "What is the distribution of marks across different sections?"
    - **SQL Query:** `SELECT SECTION, MIN(MARKS) AS MinMarks, MAX(MARKS) AS MaxMarks, AVG(MARKS) AS AvgMarks FROM STUDENT GROUP BY SECTION;`

14. **Students with the Same Marks:**
    - **Question:** "Find students who have the same marks."
    - **SQL Query:** `SELECT NAME, MARKS FROM STUDENT WHERE MARKS IN (SELECT MARKS FROM STUDENT GROUP BY MARKS HAVING COUNT(*) > 1);`

15. **Students with Recent Changes:**
    - **Question:** "List students who have been enrolled in a class since the start of the year."
    - **SQL Query:** `-- This example assumes you have a DATE column to track enrollment changes. If not, this is a hypothetical example.`

16. **Join Example:**
    - **Question:** "If there was another table 'COURSES' with columns 'COURSE_NAME' and 'STUDENT_ID', write a query to join STUDENT with COURSES based on STUDENT_ID."
    - **SQL Query:** `SELECT STUDENT.NAME, COURSES.COURSE_NAME FROM STUDENT JOIN COURSES ON STUDENT.ID = COURSES.STUDENT_ID;`

### Instructions:
- Convert the given natural language question into an SQL query based on the schema provided.
- Ensure the query is executable and retrieves the correct data from the database.
- The SQL query should handle complex conditions, joins, and aggregations where required.
- also the sql code should not have ``` in beginning or end and sql word in output
**Natural Language Question:**
'''
]



# Streamlit UI
st.title("SQL Query Generator")
st.sidebar.header("Instructions")
st.sidebar.write("Enter a question in natural language to generate an SQL query and retrieve data from the SQLite database.")

question = st.text_input("Enter your question:", key="input", placeholder="e.g., How many students are there?")
submit = st.button("Generate Query")

if submit:
    if question:
        response = get_gemini_response(question, prompt)
        if response:
            with st.expander("Generated SQL Query", expanded=True):
                st.code(response, language='sql')

            columns, result = read_sql_query(response, "student.db")
            if result:
                with st.expander("Query Results", expanded=True):
                    df = pd.DataFrame(result, columns=columns)
                    st.dataframe(df, width=800)
            else:
                st.warning("No data returned or invalid SQL query.")
        else:
            st.error("Failed to generate SQL query.")
    else:
        st.warning("Please enter a question before submitting.")

# Custom CSS
st.markdown(
    """
    <style>
    .css-18e3th9 {
        background-color: #f0f2f6;
    }
    .css-1d391kg {
        color: #005aab;
    }
    .css-1v0mbdj {
        color: #007bff;
    }
    .css-1v0mbdj h1 {
        font-size: 2.5em;
    }
    .css-1v0mbdj h2 {
        font-size: 2em;
    }
    .css-1v0mbdj pre {
        background-color: #f5f5f5;
        border-radius: 5px;
    }
    .css-1v0mbdj code {
        background-color: #f5f5f5;
        padding: 0.2em 0.4em;
        border-radius: 3px;
    }
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

