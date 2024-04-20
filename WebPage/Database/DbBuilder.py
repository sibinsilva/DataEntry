import sqlite3

def connect_to_sqlite(db_file):
    try:
        # Connect to SQLite database
        connection = sqlite3.connect(db_file)
        print("Connected to SQLite database!")
        return connection
    except sqlite3.Error as error:
        print("Failed to connect to SQLite database:", error)
        return None

# Example usage
if __name__ == "__main__":
    db_file = "./WebPage/Database/formDB.db"
    
    # Connect to SQLite database
    connection = connect_to_sqlite(db_file)
    if connection:
        # Perform database operations
        # For example, create a table
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    gender TEXT CHECK (gender IN ('male', 'female', 'other')),
    address1 VARCHAR(100),
    address2 VARCHAR(100),
    address3 VARCHAR(100),
    address4 VARCHAR(100),
    postcode VARCHAR(20),
    phone VARCHAR(20) UNIQUE,
    email VARCHAR(20)
);

        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()
