import mysql.connector as connector
from mysql.connector import errorcode

try:
    # Create a connection
    connection = connector.connect(
        host="localhost",
        user="your_username",  # replace with your MySQL username
        password="your_password",  # replace with your MySQL password
        database="your_database"  # replace with your MySQL database name
    )
    if connection.is_connected():
        print("Connection established!")
except connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
