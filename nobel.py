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
            database=db_name,
            use_unicode=True,
            charset="utf8"
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
        # with open('archive.csv', newline='') as f:
        f = open('archive2.csv', newline='')
        reader = csv.reader(f)

        connection = create_connection("localhost", "root", "qazxswED4$", "NobelWinners")
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database ();")
            record = cursor.fetchone()
            print("Connected to database:", record)
            cursor.execute("SET NAMES utf8mb4;")  # or utf8 or any other charset you want to handle
            cursor.execute("SET CHARACTER SET utf8mb4;")  # same as above
            cursor.execute("SET character_set_connection=utf8mb4;")  # same as above

            cursor.execute(
                "CREATE TABLE winners (Year CHAR(11) NOT NULL,Category CHAR(11) NOT NULL,Prize CHAR(254) NOT NULL,Motivation VARCHAR (500) NOT NULL,PrizeShare  CHAR(254) NOT NULL,LaureateID CHAR(11) NOT NULL,LaureateType CHAR(48) NOT NULL,FullName CHAR(254) NOT NULL,BirthDate CHAR(48) NOT NULL,BirthCity  CHAR(48) NOT NULL,BirthCountry CHAR(48) NOT NULL,Sex CHAR(11) NOT NULL,OrganizationName CHAR(254) NOT NULL,OrganizationCity CHAR(48) NOT NULL,OrganizationCountry CHAR(48) NOT NULL,DeathDate CHAR(48) NOT NULL,DeathCity  CHAR(48) NOT NULL,DeathCountry CHAR(48) NOT NULL)")
            print("winners table is created....")
            for row in reader:
                sql = u"""INSERT INTO NobelWinners.winners VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql, row)  # cursor.execute(sql, tuple(row))
                print("Record inserted")
                connection.commit()
        f.close()
    except Error as e:
        print("Error while connecting to MySQL", e)


if __name__ == "__main__":
    main()
