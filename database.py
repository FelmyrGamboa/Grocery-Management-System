import mysql.connector

class Customer:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "mysql1234",
        database = "customers_information_database"
    )

    customer_cursor = db.cursor()
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