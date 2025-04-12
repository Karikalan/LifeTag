import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='#..Dhanush@16042006..#',
        database='HackHive'
    )
