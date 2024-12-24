import json
filename = "students.json"


def update_student(student_id):
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())
        student = list(filter(lambda x: x["id"] == student_id, students))
        if student:
            student = student[0]
            key = input("Enter the info you want to update ")
            if key.lower() not in ["name", "age", "address"]:
                print("invalid User info")
            else:
                value = input("Enter the new value ")
                student[key] = value
                fp.seek(0)
                fp.write(json.dumps(students, indent=2))
                print("Student Updated Successfully !!")

        else:
            print("Please enter a valid student ID")
        repeat = input("Do you want to continue? (y/n)")
        return True if repeat.lower() == "y" else False
