import mysql.connector

class Customer:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "mysql1234",
<<<<<<< HEAD
            database = "customers_information_database"
=======
            database = "customers_information_database",
>>>>>>> a08497f9d78f7b155431074073bfd4ad805686eb
        )
        self.customer_cursor = self.db.cursor()

    def create_database(self):
<<<<<<< HEAD
        self.customer_cursor("CREATE DATABASE customers_information_database")

    def create_table_customer_information(self):
        self.customer_cursor("""CREATE TABLE customer_information (
=======
        self.customer_cursor.execute("CREATE DATABASE customers_information_database")

    def create_table_customer_information(self):
        self.customer_cursor.execute("""CREATE TABLE customer_information (
>>>>>>> a08497f9d78f7b155431074073bfd4ad805686eb
                            customerID INT PRIMARY KEY AUTO_INCREMENT,
                            fullname VARCHAR(200) NOT NULL, 
                            username VARCHAR(200) NOT NULL UNIQUE,
                            password VARCHAR(200) NOT NULL
<<<<<<< HEAD
                             """)
        
    def create_table_shopping_history(self):
        self.customer_cursor("""CREATE TABLE customer_shopping_history (
=======
<<<<<<< Updated upstream
                             )""")
=======
                            )""")
>>>>>>> Stashed changes
        
    def create_table_shopping_history(self):
        self.customer_cursor.execute("""CREATE TABLE customer_shopping_history (
>>>>>>> a08497f9d78f7b155431074073bfd4ad805686eb
                            product_name VARCHAR(200) NOT NULL,
                            price DECIMAL(10,2) NOT NULL, 
                            quantity INT UNSIGNED NOT NULL, 
                            total_price DECIMAL (10,2) NOT NULL,
                            date_time DATETIME
<<<<<<< HEAD
                             """)
=======
<<<<<<< Updated upstream
                             )""")
=======
                            )""")
>>>>>>> Stashed changes
>>>>>>> a08497f9d78f7b155431074073bfd4ad805686eb
        
db_table = Customer()
# db_table.create_database()
# db_table.create_table_customer_information()
# db_table.create_table_shopping_history()




    # db = mysql.connector.connect(
    #     host = "localhost",
    #     user = "root",
    #     passwd = "mysql1234",
    #     database = "customers_information_database"
    # )

    # customer_cursor = db.cursor()
    # customer_cursor.execute("CREATE DATABASE customers_information_database")

    # customer_cursor.execute("""CREATE TABLE customer_information(
    #                         customerID INT PRIMARY KEY AUTO_INCREMENT,
    #                         fullname VARCHAR(200) NOT NULL, 
    #                         username VARCHAR(200) NOT NULL UNIQUE,
    #                         password VARCHAR(200) NOT NULL
    #                         )""")

    # customer_cursor.execute("""CREATE TABLE customer_shopping_history(
    #                         product_name VARCHAR(200) NOT NULL,
    #                         price DECIMAL(10,2) NOT NULL, 
    #                         quantity INT UNSIGNED NOT NULL, 
    #                         total_price DECIMAL (10,2) NOT NULL,
    #                         date_time DATETIME
    #                         )""")

    # customer_cursor.execute("ALTER TABLE")