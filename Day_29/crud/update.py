from estd_connection import estd_connection


def update_student(id):
    cursor = estd_connection()
    to_change = input("Enter the field to change ")
    changed_value = input("Enter the new value ")


    sql = f"""
    UPDATE INFORMATION SET {to_change}='{changed_value}' WHERE ID='{id}'
    """

    cursor.execute(sql)
    print("Student Updated Successfully !!")
    repeat = input("Do you want to continue?(y/n) ")
    return True if repeat.lower() == 'y' else False

