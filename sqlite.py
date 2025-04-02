import sqlite3

##conect to sqlite
connection = sqlite3.connect("Student.db")

## create a cursor object to insert record create table
cursor = connection.cursor()

##create a table
table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert some records
cursor.execute('''Insert into STUDENT values('Krish','Data Science','A',93)''')
cursor.execute('''Insert into STUDENT values('John','Data Science','B',99)''')
cursor.execute('''Insert into STUDENT values('Gukesh','Data Science','A',82)''')
cursor.execute('''Insert into STUDENT values('Alana','Information Science','C',70)''')
cursor.execute('''Insert into STUDENT values('Jacob','Devops','A',50)''')

##Display all the records
print("Inserted records are")
data = cursor.execute('''Select * FROM STUDENT''')
for row in data:
    print(row)

##Commit changes in database
connection.commit()
connection.close()