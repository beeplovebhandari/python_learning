from estd_connection import estd_connection

def delete_student():
    cursor = estd_connection()
    id = input("Enter Student ID ")
    sql = f"""
    DELETE FROM INFORMATION WHERE ID='{id}'
    """
    cursor.execute(sql)
    print("Student Deleted Successfully !!")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == 'y' else False
