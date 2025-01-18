import mysql.connector

class Customer:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "mysql1234",
            database = "customers_information_database"
        )
        self.customer_cursor = self.db.cursor()

    def create_database(self):
        self.customer_cursor.execute("CREATE DATABASE customers_information_database")

    def create_table_customer_information(self):
        self.customer_cursor.execute("""CREATE TABLE customer_information (
                            customerID INT PRIMARY KEY AUTO_INCREMENT,
                            fullname VARCHAR(200) NOT NULL, 
                            username VARCHAR(200) NOT NULL UNIQUE,
                            password VARCHAR(200) NOT NULL
                             """)
        
    def create_table_shopping_history(self):
        self.customer_cursor.execute("""CREATE TABLE customer_shopping_history (
                            product_name VARCHAR(200) NOT NULL,
                            price DECIMAL(10,2) NOT NULL, 
                            quantity INT UNSIGNED NOT NULL, 
                            total_price DECIMAL (10,2) NOT NULL,
                            date_time DATETIME
                             """)
        
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
    # # customer_cursor.execute("CREATE DATABASE customers_information_database")

    # # customer_cursor.execute("""CREATE TABLE customer_information(
    # #                         customerID INT PRIMARY KEY AUTO_INCREMENT,
    # #                         fullname VARCHAR(200) NOT NULL, 
    # #                         username VARCHAR(200) NOT NULL UNIQUE,
    # #                         password VARCHAR(200) NOT NULL
    # #                         )""")

    # customer_cursor.execute("""CREATE TABLE customer_shopping_history(
    #                         product_name VARCHAR(200) NOT NULL,
    #                         price DECIMAL(10,2) NOT NULL, 
    #                         quantity INT UNSIGNED NOT NULL, 
    #                         total_price DECIMAL (10,2) NOT NULL,
    #                         date_time DATETIME
    #                         )""")

    # def signup(fullname, username, password):
    #     Customer.customer_cursor.execute("INSERT INTO customer_information (fullname, username, password) VALUES (%s, %s, %s)", (fullname, username, password))
    #     Customer.db.commit()

    # def login(username, password):
    #     Customer.customer_cursor.execute("")