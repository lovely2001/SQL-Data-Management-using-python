import mysql.connector

# Replace these values with your MySQL Workbench credentials and database information
host = "localhost"
username = "user"
password = "123456"
database_name = "new_database"

# Establish a connection to MySQL
try:
    connection = mysql.connector.connect(host=host, user=username, password=password)
    cursor = connection.cursor()

    # Create a new database
    create_database_query = "CREATE DATABASE IF NOT EXISTS {}".format(database_name)
    cursor.execute(create_database_query)
    print("Database '{}' created successfully.".format(database_name))

    # Switch to the new database
    connection.database = database_name

    # Ask user for table name and attributes
    table_name = input("Enter the table name: ")
    attributes = input("Enter table attributes and data types (comma-separated): ").split(',')

    # Create table query
    create_table_query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, ', '.join(attributes))
    cursor.execute(create_table_query)
    print("Table '{}' created successfully.".format(table_name))

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
