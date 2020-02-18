import mysql.connector


def mysqlopen():
    connection = mysql.connector.connect(
        host='localhost',
        user='aidan',
        password='Watermelon@3489',
        database='hockey_data'
    )
    return connection


def mysqlclose(connection):
    connection.close()
