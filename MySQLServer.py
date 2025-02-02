import mysql.connector

def create_database(db_name):
    """Creates a MySQL database."""
    try:
        # Connect to MySQL server (without specifying a database initially)
        mydb = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="root",  # Replace with your MySQL username
            password="Yn@0949753643"  # Replace with your MySQL password
        )

        mycursor = mydb.cursor()

        # Check if the database exists. If it does, try dropping it first.
        try:
            mycursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        except mysql.connector.Error as err:
            print(f"Error dropping database (if it existed): {err}")

        # Create the database
        mycursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error connecting or creating database: {err}")

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()


if __name__ == "__main__":
    database_name = "alx_book_store"
    create_database(database_name)