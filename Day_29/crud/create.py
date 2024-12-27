from estd_connection import estd_connection

def create_student():
    cursor = estd_connection()
    id = input("Enter Student ID ")
    name = input("Enter Student Name ")
    age = int(input("Enter Student's Age "))
    address = input("Enter Student's Address ")
    sql = f"""
    INSERT INTO INFORMATION (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', '{age}', '{address}')
    """
    cursor.execute(sql)
    print("Student added successfully !!")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == 'y' else False
