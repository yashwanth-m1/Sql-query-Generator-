import sqlite3
connection=sqlite3.connect('student.db')

#cursor object
cursor=connection.cursor()

#Create table
table_info="""CREATE TABLE IF NOT EXISTS student(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);"""
cursor.execute(table_info)

cursor.execute("INSERT INTO student VALUES('Yeshwant','10th','A',95)")
cursor.execute("INSERT INTO student VALUES('Anika','10th','B',80)")
cursor.execute("INSERT INTO student VALUES('Kabir','10th','C',70)")
cursor.execute("INSERT INTO student VALUES('Sara','10th','A',88)")              
cursor.execute("INSERT INTO student VALUES('Diya','10th','A',90)")
               

print(" the inserted data are:")
data=cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

connection.commit()
connection.close()
