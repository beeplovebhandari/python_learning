from estd_connection import estd_connection

cursor = estd_connection()

#cursor.execute("DROP TABLE STUDENT")
sql = """
CREATE TABLE USERINFO(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20) NOT NULL,
    TITLE CHAR(10),
    AGE INT CHECK (AGE >= 18),
    NATIONALITY CHAR(50),
    NUM_COURSES INT DEFAULT 0,
    NUM_SEMESTERS INT DEFAULT 0,
    REGISTRATION_STATUS CHAR(50) DEFAULT 'Not Registered',
    TERMS_ACCEPTED BOOLEAN NOT NULL
)
"""

cursor.execute(sql)
print("Table Creates Successfully !!")