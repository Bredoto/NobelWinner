import csv
from Winner import Winner
import mysql.connector
from mysql.connector import Error
# Simple python tool to create SQL INSERT statements from CSV files.  https://github.com/najiji/csv2sql

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def main():
    try:
        connection = create_connection("localhost", "root", "qazxswED4$", "NobelWinners")
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database ();")
            record = cursor.fetchone()
            print("Connected to database:", record)
            cursor.execute("CREATE TABLE winners (Year FLOAT(2,1) NOT NULL,Category CHAR(11) NOT NULL,Prize CHAR(11) NOT NULL,Motivation CHAR(11) NOT NULL,PrizeShare  CHAR(11) NOT NULL,LaureateID CHAR(11) NOT NULL,LaureateType CHAR(11) NOT NULL,FullName CHAR(11) NOT NULL,BirthDate CHAR(11) NOT NULL,BirthCity  CHAR(11) NOT NULL,BirthCountry CHAR(11) NOT NULL,Sex CHAR(11) NOT NULL,OrganizationName CHAR(11) NOT NULL,OrganizationCity CHAR(11) NOT NULL,OrganizationCountry CHAR(11) NOT NULL,DeathDate CHAR(11) NOT NULL,DeathCity  CHAR(11) NOT NULL,DeathCountry CHAR(11) NOT NULL)")
            print("winners table is created....")
    except Error as e:



    #with open('archive.csv', newline='') as f:
        # with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        # for row in reader:
        # print(row)


# a = Winner('2016', 'Physics', 'The Nobel Prize in Physics 2016', '"for theoretical discoveries of topological phase transitions and topological phases of matter"', '1/4', '930', 'Individual', 'J. Michael Kosterlitz', '1943-06-22', 'Aberdeen', 'United Kingdom', 'Male', 'Brown University', 'Providence, RI', 'United States of America', '', '', '')


if __name__ == "__main__":
    main()
