import mysql.connector


def mysqlopen():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Watermelon@3489',
        database='Hockey_Data'
    )
    return connection


def mysqlclose(connection):
    connection.close()
