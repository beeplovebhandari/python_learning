from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter Student ID ")
name = input("Enter Student Name ")
age = int(input("Enter Student's Age "))

sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{id}', '{name}', '{age}')
"""

cursor.execute(sql)
print("Student added successfully !!")