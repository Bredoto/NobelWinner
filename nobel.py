import csv
from Winner import Winner
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def main():
    create_database_query = "CREATE DATABASE NobelWinners"
    create_database(connection, create_database_query)

    with open('archive.csv', newline='') as f:
    #with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

a = Winner('2016', 'Physics', 'The Nobel Prize in Physics 2016', '"for theoretical discoveries of topological phase transitions and topological phases of matter"', '1/4', '930', 'Individual', 'J. Michael Kosterlitz', '1943-06-22', 'Aberdeen', 'United Kingdom', 'Male', 'Brown University', 'Providence, RI', 'United States of America', '', '', '')





if __name__ == "__main__":
    main()
