import mysql.connector

def create_database (db_name):
    try:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="Yn@0949753643"
        )

        mycursor = mydb.cursor()

        try:
            mycursor.execute(f"DROP DATABASE IF EXISTS {alx_book_store}")
        except mysql.connector.Error as err:
            print(f"Error dropping database (if it existed): {err}")

        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
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
