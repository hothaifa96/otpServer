import mysql.connector


def get_connection():
    conn = mysql.connector.connect(host="localhost", user="root", password="hothaifa526618", db="Cardiokol")
    cur = conn.cursor()
    return cur, conn

