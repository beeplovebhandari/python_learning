# If we want to connect database from a program (Python, Javascript)then we need a database connector
# Database connector connects your program with Database mysqlclient, psycopg2 etc.. are the db connectors


def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="userinfodb",
        user="postgres",
        password="database",
        host="127.0.0.1",
        port = 5432
    )

    conn.autocommit = True
    print("Connection established succesfully !!")
    cursor = conn.cursor()
    return cursor

if __name__ == "__main__":
    estd_connection()