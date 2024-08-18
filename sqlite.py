import sqlite3
## connect to the SQlite

connection=sqlite3.connect("student.db")

## Create a cursor object to insert record create table

cursor=connection.cursor()

## create the table

table_info="""

Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Sabbir', 'LLMs', 'A',89)''')
cursor.execute('''Insert Into STUDENT values('Rizvi', 'Data Science', 'B',90)''')
cursor.execute('''Insert Into STUDENT values('Selim', 'Data Science', 'C',88)''')
cursor.execute('''Insert Into STUDENT values('Mustshid', 'DEVOPS', 'A',87)''')
cursor.execute('''Insert Into STUDENT values('Mufassir', 'DL', 'C',92)''')
cursor.execute('''Insert Into STUDENT values('Rabbi', 'NLP', 'A',89)''')
cursor.execute('''Insert Into STUDENT values('Kabid', 'NLP', 'B',92)''')
cursor.execute('''Insert Into STUDENT values('Alomgir', 'Computer Vision', 'C',86)''')
cursor.execute('''Insert Into STUDENT values('Nayem', 'DL', 'A',91)''')
cursor.execute('''Insert Into STUDENT values('Sani', 'DEVOPS', 'C',90)''')
cursor.execute('''Insert Into STUDENT values('Tamim', 'LLMs', 'B',89)''')
cursor.execute('''Insert Into STUDENT values('Shohan', 'DL', 'A',89)''')

## Display All the records

print("The inserted records are :-> ")
data=cursor.execute(''' Select * from STUDENT ''') 
for row in data:
    print(row)
    
    
connection.commit() 
connection.close()      