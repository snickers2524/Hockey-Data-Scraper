import mysql.connector
from MySQLCode import DataBaseCredentials as DBC


def mysqlopen():
    connection = mysql.connector.connect(
        host=DBC.host,
        user=DBC.user,
        password=DBC.password,
        database='hockey_data'
    )
    return connection


def mysqlclose(connection):
    connection.close()
