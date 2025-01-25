# import datetime
# from database import Customer


# # new file
# class Accounts:
#     users = []
#     customer_db = Customer()

#     @classmethod
#     def signup_account(cls, name, username, password):
#         cls.customer_db.customer_cursor.execute("INSERT INTO customer_information (fullname, username, password) VALUES (%s, %s, %s)", (name, username, password))
#         cls.customer_db.db.commit()

#     @classmethod
#     def verify_account(cls, username, password):
#         cls.customer_db.customer_cursor.execute("SELECT * FROM customer_information WHERE username = %s AND password = %s", (username, password))
#         data = cls.customer_db.customer_cursor.fetchall()
        
#         for result in data:
#             return result
        
#     @classmethod
#     def retrieve_accounts(cls):
#         cls.customer_db.customer_cursor.execute("SELECT * FROM customer_information")
#         data = cls.customer_db.customer_cursor.fetchall()
#         return data

#     def __init__(self, name, username, password):
#         self.name = str(name)
#         self.username = str(username)
#         self.password = str(password)


# # new file not sure pa
# class Cart:
#     cart_items = []

#     #ADDED (PACHECK)
#     @classmethod
#     def manage_cart(cls, user):
#         while True:
#             print("\n=== Shopping Cart ===")
            
#             #ADDED
#             user_cart = [item for item in cls.cart_items if item.user == user]

#             if not user_cart:
#                 return print("Your cart is empty")
            
#             total_price = sum(item.quantity * item.price for item in user_cart)

#                         # Display cart items
#             print("Items in your cart:")
#             for idx, item in enumerate(user_cart, start=1):
#                 print(f"{idx}. {item.product} ({item.quantity}x) - {item.price} PHP")
#             print(f"Total Price: {total_price} PHP")

#             # Provide options
#             print("\n1. Remove item")
#             print("2. Proceed to checkout")
#             print("3. Back")
#             choice = input("Enter your choice: ")

#             if choice == "1":
#                 item_idx = int(input("Enter the item number to remove: ")) - 1
#                 if 0 <= item_idx < len(user_cart):
#                     removed_item = user_cart.pop(item_idx)
#                     cls.cart_items.remove(removed_item)  # Remove item from the global cart
#                     print(f"{removed_item.product} removed from cart.")
#                 else:
#                     print("Invalid item number.")
#             elif choice == "2":
#                 #added
#                 cls.checkout(cls, user_cart, total_price)
#                 user_cart=[item for item in Cart.cart_items if item.user == user]
#                 total_price = sum((item.quantity * item.price) for item in user_cart)
#                 Cart.cart_items = [item for item in Cart.cart_items if item.user != user]
#                 return
#             elif choice == "3":
#                 break
#             else:
#                 print("Invalid choice. Please try again.")


#     def __init__(self, product, price, quantity, user):
#         self.product = str(product)
#         self.price = float(price)
#         self.quantity = int(quantity)
#         self.user = user

#         Cart.cart_items.append(self)

#     #rearrange 
#     def checkout(self,  user, total_price):
#         print("\n=== Checkout ===")
#         print("Items being purchased:")


#         print(f"Total Price: {total_price} PHP")
#         print("Thank you for shopping with us!")

# # new file not sure pa
# class ShoppingHistory:
#     records = []
#     customer_db = Customer()

#     def __init__(self, product, price, quantity):
#         self.product = str(product)
#         self.price = float(price)
#         self.quantity = int(quantity)
#         self.total_price = float(self.price * self.quantity) #abck sa old format


# # new file
# class GroceryItems:
#     def __init__(self):
#         self.items = {
#             "vegetables" : [
#                 ("Carrot", 50),
#                 ("Tomato", 30),
#                 ("Potato", 40), 
#                 ("Cabbage", 20),
#                 ("Eggplant", 25), 
#                 ("Onion", 60), 
#                 ("Garlic", 70), 
#                 ("Peas", 35),
#                 ("Lettuce", 45), 
#                 ("Spinach", 55)
#             ],
#             "fruits" : [
#                 ("Apple", 100), 
#                 ("Banana", 40), 
#                 ("Grapes", 120), 
#                 ("Orange", 80),
#                 ("Pineapple", 150), 
#                 ("Mango", 90), 
#                 ("Papaya", 60), 
#                 ("Watermelon", 110),
#                 ("Strawberry", 200), 
#                 ("Melon", 70)
#             ]
#         }
    
#     def browse_products(self, category, logged_user):
#         grocery = GroceryItems()
#         while True:
#             print(f"\n=== {category.capitalize()} ===")
#             products = grocery.items[category]

#             print("1. Sort by Price")
#             print("2. Sort Alphabetically")
#             print("3. Search Product")
#             print("4. Back")
#             choice = input("Enter your choice: ")

#             # insertion sort
#             if choice == "1":
#                 print("\nProducts sorted by price:")
#                 sorted_prices = []
#                 for i in enumerate(products):
#                     sorted_prices.append(i[1])

#                 for items in range(1, len(sorted_prices)):
#                     while sorted_prices[items][1] < sorted_prices[items-1][1] and items > 0:
#                         sorted_prices[items], sorted_prices[items-1] = sorted_prices[items-1], sorted_prices[items]
#                         items -= 1

#                 for idx, (product, price) in enumerate(sorted_prices, start=1):
#                     print(f"{idx}. {product} - {price} PHP")

#             elif choice == "2":
#                 products = sorted(products, key=lambda x: x[0].lower())  # Sort alphabetically
#                 print("\nProducts sorted alphabetically:")
#                 for idx, (product, price) in enumerate(products, start=1):
#                     print(f"{idx}. {product} - {price} PHP")

#             # changed 
#             # searching techniques
#             elif choice == "3":
#                 search_query = input("Enter product name to search: ").lower()
#                 for idx, (product, price) in enumerate(products, start=1):
#                     if product.lower() == search_query:
#                         print(f"\nFound: {idx}. {product} - {price} PHP")
#                         break
#                     else:
#                         print("\nProduct not available.")
#                         break

#             elif choice == "4":
#                 break

#             else:
#                 print("Invalid choice. Please try again.")
#                 continue
            
#             choice = input("\nEnter the product number to add to cart (or 'b' to go back): ")
#             if choice.lower() == 'b':
#                 return
            
#             if choice.isdigit() and 1 <= int(choice) <= len(products):
#                 selected_product = products[int(choice) - 1]

#                 try:
#                     quantity= int(input("Enter quantity: "))
#                     chosen_product = Cart(selected_product[0], selected_product[1], quantity, logged_user)

                    

#                     print("\n1. Buy Now")
#                     print("2. Add to cart")
#                     action_choice = input("Enter your choice: ")
#                     if action_choice == "1":
                        
#                         #chinange ang format 
#                         total_price = chosen_product.quantity * chosen_product.price

#                         Cart.cart_items.remove(chosen_product)
#                         print(f"{chosen_product.product} has been removed from your cart after purchase.")  
                        
#                         chosen_product.checkout(self,total_price)

#                     elif action_choice == "2":
#                         print(f"{selected_product[0]} added to cart.")
#                 except ValueError:
#                     print("Invalid input. Please enter valid numbers.")
#             else:
#                 print("Invalid product number. Please try again.")


# # new file
# class ShopSystem:
#     # def __init__(self):
#     #     self.grocery_items = {
#     #         "vegetables" 
#     #     }

#     def signup(self):
#         print("\n=== Sign Up ===")
#         name = str(input("Enter your full name: "))
#         username = str(input("Enter username: "))
#         password = str(input("Enter password: "))  # Use input() for password
#         Accounts.users.append({"name": name, "username": username, "password": password})
#         Accounts.signup_account(name, username, password)
#         print(f"Registration successful! Welcome, {name}!")

#     def login(self):
#         print("\n=== Login ===")
#         username = input("Enter username: ")
#         password = input("Enter password: ")  # Use input() for password

#         for user in Accounts.users:
#             if user["username"] == username and user["password"] == password and Accounts.verify_account(username, password):
#                 print(f"Login successful! Welcome back, {user['name']}!")
#                 return user
#         print("Invalid username or password.")
#         return None
    
#     def view_shopping_history(self):
#         print("\n=== Shopping History ===")
#         if not ShoppingHistory.records:
#             print("No shopping history found.")
#             return

#         for record in ShoppingHistory.records:
#             print(f"Date/Time: {record['date_time']}")
#             for item in record['items']:
#                 print(f"Product: {item['product']}, Quantity: {item['quantity']}, Price: {item['price']} PHP")
#             print(f"Total Price: {record['total_price']} PHP\n")

#     def shop_now(self, logged_user):
#         while True:
#             print("\n=== Shop Now ===")
#             print("1. Vegetables")
#             print("2. Fruits")
#             print("3. Shopping Cart")
#             print("4. View All Products")
#             print("5. Back to Welcome Page")
#             choice = input("Enter your choice: ")

#             grocery = GroceryItems()
#             if choice == "1":
#                 grocery.browse_products("vegetables", logged_user)
#             elif choice == "2":
#                 grocery.browse_products("fruits", logged_user)
#             elif choice == "3":
#                Cart.manage_cart(logged_user)

#             # dito ako natapos
#             elif choice == "4":
#                 products = []
#                 for vegetable in grocery.items["vegetables"]:
#                     products.append(vegetable)
#                 for fruit in grocery.items["fruits"]:
#                     products.append(fruit)
#                 print("\nAll Products:")
#                 for idx, (product, price) in enumerate(products, start=1):
#                     print(f"{idx}. {product} - {price} PHP")
#             elif choice == "5":
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
        
#     def show_welcome_page(self, logged_user):
#         while True:
#             print("\n=== Welcome to ShopeeLengke ===")
#             print("1. Shop Now")
#             print("2. Shopping History")
#             print("3. Logout")
#             choice = input("Enter your choice: ")

#             if choice == "1":
#                 self.shop_now(logged_user)
#             elif choice == "2":
#                 self.view_shopping_history()
#             elif choice == "3":
#                 print("Logged out successfully!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")


# # new file
# def main():
#     while True:
#         print("\n=== ShopeeLengke ===")
#         print("1. Login")
#         print("2. Sign up")
#         print("3. Exit")
#         choice = input("Enter your choice: ")
        
#         system = ShopSystem()
#         if choice == "1":
#             user = system.login()
#             if user:
#                 system.show_welcome_page(user)
#         elif choice == "2":
#             system.signup()
#         elif choice == "3":
#             print("Thank you for using the ShopeeLengke System!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     Users = Accounts.retrieve_accounts()
#     if Users:
#         for data in Users:
#             Accounts.users.append({"name": data[1], "username": data[2], "password": data[3]})
#     else:
#         pass
#     main()

# ------------------------------------------------------
# KAY FELMYR 
import datetime
from database import Customer


# new file
class Accounts:
    users = []
    customer_db = Customer()

    @classmethod
    def signup_account(cls, name, username, password):
        cls.customer_db.customer_cursor.execute("INSERT INTO customer_information (fullname, username, password) VALUES (%s, %s, %s)", (name, username, password))
        cls.customer_db.db.commit()

    @classmethod
    def verify_account(cls, username, password):
        cls.customer_db.customer_cursor.execute("SELECT * FROM customer_information WHERE username = %s AND password = %s", (username, password))
        data = cls.customer_db.customer_cursor.fetchall()
        
        for result in data:
            return result
        
    @classmethod
    def retrieve_accounts(cls):
        cls.customer_db.customer_cursor.execute("SELECT * FROM customer_information")
        data = cls.customer_db.customer_cursor.fetchall()
        return data

    def __init__(self, name, username, password):
        self.name = str(name)
        self.username = str(username)
        self.password = str(password)


# new file not sure pa
class Cart:
    cart_items = []
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #ADDED (PACHECK)
    @classmethod
    def manage_cart(cls, user):
        while True:
            print("\n=== Shopping Cart ===")
            
            #ADDED
            user_cart = [item for item in cls.cart_items if item.user == user]

            if not user_cart:
                return print("Your cart is empty")
            
            total_price = sum((item.quantity * item.price) for item in user_cart)

            # Display cart items
            print("Items in your cart:")
            for idx, item in enumerate(user_cart, start=1):
                print(f"{idx}. {item.product} ({item.quantity}x) x {item.price} PHP")
            print(f"Total Price: {total_price} PHP")

            # Provide options
            print("\n1. Remove item")
            print("2. Proceed to checkout")
            print("3. Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                item_idx = int(input("Enter the item number to remove: ")) - 1
                if 0 <= item_idx < len(user_cart):
                    removed_item = user_cart.pop(item_idx)
                    cls.cart_items.remove(removed_item)  # Remove item from the global cart
                    print(f"{removed_item.product} removed from cart.")
                else:
                    print("Invalid item number.")
            elif choice == "2":
                cls.checkout(user, total_price)
                return
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    #added done (pacheck)
    @classmethod
    def checkout(cls, user, total_price):
        print("\n=== Checkout ===")
        print("Items being purchased:")

        user_cart = [item for item in cls.cart_items if item.user == user]

        for idx, item in enumerate(user_cart, start=1):
            print(f"Product: {item.product}, Quantity: {item.quantity}, Price: {item.price} PHP")
            # added
            ShoppingHistory.add_product_to_history(user.username, item.product, item.price, item.quantity, total_price, cls.date_time)
            ShoppingHistory(item.product, item.price, item.quantity)
            cls.cart_items.remove(item)

        print(f"Total Price: {total_price} PHP")
        print("Thank you for shopping with us!")
        cls.cart_items = [item for item in cls.cart_items if item not in user_cart]  # Clear purchased items

    def __init__(self, product, price, quantity, user):
        self.product = str(product)
        self.price = float(price)
        self.quantity = int(quantity)
        self.user = user
        Cart.cart_items.append(self)

# new file not sure pa
class ShoppingHistory:
    records = []
    customer_db = Customer()

    # added
    @classmethod
    def retrieve_shopping_history(cls, username):
        cls.customer_db.customer_cursor.execute("SELECT * FROM customer_shopping_history WHERE username = %s", (username,))
        data = cls.customer_db.customer_cursor.fetchall()
        
        for result in data:
            cls.records.append({result[0] : (result[1], result[2], result[3], result[4], result[5])})

    # added
    @classmethod
    def add_product_to_history(cls, username, product_name, price, quantity, total_price, date_time):
        cls.customer_db.customer_cursor.execute("INSERT INTO customer_shopping_history (username, product_name, price, quantity, total_price, date_time) VALUES (%s, %s, %s, %s, %s, %s)", (username, product_name, price, quantity, total_price, date_time))
        cls.customer_db.db.commit()

    @classmethod
    def view_shopping_history(cls, username):
        print("\n=== Shopping History ===")
        cls.retrieve_shopping_history(username)
        history = [item for item in cls.records if item[username]]
        if not history:
            print("No shopping history found.")
        
        for record in history:
            print(f"Date/Time: {record[username][4]}")
            print(f"Product: {record[username][0]}, Quantity: {record[username][2]}, Price: {record[username][1]} PHP\n Total Price: {record[username][3]} PHP\n")

        # for record in cls.records:
        #     print(f"Date/Time: {record['date_time']}")
        #     for item in record['items']:
        #         print(f"Product: {item.product}, Quantity: {item.quantity}, Price: {item.price} PHP")
        #     print(f"Total Price: {record.total_price} PHP\n")

    def __init__(self, product, price, quantity):
        self.product = str(product)
        self.price = float(price)
        self.quantity = int(quantity)
        self.total_price = float(self.price * self.quantity) #changed and added format
        ShoppingHistory.records.append(self)

# new file
class GroceryItems:
    def __init__(self):
        self.items = {
            "vegetables" : [
                ("Carrot", 50),
                ("Tomato", 30),
                ("Potato", 40), 
                ("Cabbage", 20),
                ("Eggplant", 25), 
                ("Onion", 60), 
                ("Garlic", 70), 
                ("Peas", 35),
                ("Lettuce", 45), 
                ("Spinach", 55)
            ],
            "fruits" : [
                ("Apple", 100), 
                ("Banana", 40), 
                ("Grapes", 120), 
                ("Orange", 80),
                ("Pineapple", 150), 
                ("Mango", 90), 
                ("Papaya", 60), 
                ("Watermelon", 110),
                ("Strawberry", 200), 
                ("Melon", 70)
            ]
        }
    
    def browse_products(self, category, logged_user):
        grocery = GroceryItems()
        while True:
            print(f"\n=== {category.capitalize()} ===")
            products = grocery.items[category]

            print("1. Sort by Price")
            print("2. Sort Alphabetically")
            print("3. Search Product")
            print("4. Back")
            choice = input("Enter your choice: ")

            # insertion sort
            if choice == "1":
                print("\nProducts sorted by price:")
                sorted_prices = []
                for i in enumerate(products):
                    sorted_prices.append(i[1])

                for items in range(1, len(sorted_prices)):
                    while sorted_prices[items][1] < sorted_prices[items-1][1] and items > 0:
                        sorted_prices[items], sorted_prices[items-1] = sorted_prices[items-1], sorted_prices[items]
                        items -= 1

                for idx, (product, price) in enumerate(sorted_prices, start=1):
                    print(f"{idx}. {product} - {price} PHP")

                choice = input("\nEnter the product number to add to cart (or 'b' to go back): ")
                if choice.lower() == 'b':
                    return
                
                if choice.isdigit() and 1 <= int(choice) <= len(sorted_prices):
                    selected_product = sorted_prices[int(choice) - 1]
                    self.product_finalization(selected_product, logged_user)
                else:
                    print("Invalid product number. Please try again.")

            elif choice == "2":
                products = sorted(products, key=lambda x: x[0].lower())  # Sort alphabetically
                print("\nProducts sorted alphabetically:")
                for idx, (product, price) in enumerate(products, start=1):
                    print(f"{idx}. {product} - {price} PHP")

                choice = input("\nEnter the product number to add to cart (or 'b' to go back): ")
                if choice.lower() == 'b':
                    break
                
                if choice.isdigit() and 1 <= int(choice) <= len(products):
                    selected_product = products[int(choice) - 1]
                    self.product_finalization(selected_product, logged_user)

            # changed 
            # searching techniques
            elif choice == "3":
                search_query = input("Enter product name to search: ").lower()
                for idx, (product, price) in enumerate(products, start=1):
                    if product.lower() == search_query:
                        print(f"\nFound: {idx}. {product} - {price} PHP")
                        while True:
                            proceed_product = input("Enter the product number to add to cart (or 'b' to go back): ")
                            if proceed_product == f"{idx}":
                                return self.product_finalization([product, price], logged_user)
                            elif proceed_product.lower() == "b":
                                break
                            else:
                                print("Invalid product number. Please try again.")
                        
            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")
                continue

    # added
    def product_finalization(self, selected_product, logged_user):
        try:
        # changed
            while True:
                quantity= int(input("Enter quantity: "))
                chosen_product = Cart(selected_product[0], selected_product[1], quantity, logged_user)

                print("\n1. Buy Now")
                print("2. Add to cart")
                print("3. Back")
                action_choice = input("Enter your choice: ")
                if action_choice == "1":
                    user_cart=[item for item in Cart.cart_items if item.user == logged_user]
                    total_price = sum((item.quantity * item.price) for item in user_cart)
                    chosen_product.checkout(logged_user,total_price)
                    break
                elif action_choice == "2":
                    print(f"{selected_product[0]} added to cart.")
                    break
                elif action_choice == "3":
                    break
                else:
                    print("Invalid input. Please enter valid numbers.")
                    continue
        except ValueError as e:
            print("Invalid input. Please enter valid numbers.")

# new file
class ShopSystem:

    def signup(self):
        print("\n=== Sign Up ===")
        name = str(input("Enter your full name: "))
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))  # Use input() for password
        Accounts.users.append({"name": name, "username": username, "password": password})
        Accounts.signup_account(name, username, password)
        print(f"Registration successful! Welcome, {name}!")

    def login(self):
        print("\n=== Login ===")
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))  # Use input() for password

        for user in Accounts.users:
            if user["username"] == username and user["password"] == password and Accounts.verify_account(username, password):
                print(f"Login successful! Welcome back, {user['name']}!")
                logged_user = Accounts(user['name'], user['username'], user['password'])
                return logged_user
                # return user
        print("Invalid username or password.")
        return None

    def shop_now(self, logged_user):
        while True:
            print("\n=== Shop Now ===")
            print("1. Vegetables")
            print("2. Fruits")
            print("3. Shopping Cart")
            print("4. View All Products")
            print("5. Back to Welcome Page")
            choice = input("Enter your choice: ")

            grocery = GroceryItems()
            if choice == "1":
                grocery.browse_products("vegetables", logged_user)
            elif choice == "2":
                grocery.browse_products("fruits", logged_user)
            elif choice == "3":
               Cart.manage_cart(logged_user)

            # dito ako natapos
            elif choice == "4":
                products = []
                for vegetable in grocery.items["vegetables"]:
                    products.append(vegetable)
                for fruit in grocery.items["fruits"]:
                    products.append(fruit)
                print("\nAll Products:")
                for idx, (product, price) in enumerate(products, start=1):
                    print(f"{idx}. {product} - {price} PHP")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
        
    def show_welcome_page(self, logged_user):
        while True:
            print("\n=== Welcome to ShopeeLengke ===")
            print("1. Shop Now")
            print("2. Shopping History")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.shop_now(logged_user)
            elif choice == "2":
                ShoppingHistory.view_shopping_history(logged_user.username)
            elif choice == "3":
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice. Please try again.")


# new file
def main():
    while True:
        print("\n=== ShopeeLengke ===")
        print("1. Login")
        print("2. Sign up")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        system = ShopSystem()
        if choice == "1":
            user = system.login()
            if user:
                system.show_welcome_page(user)
        elif choice == "2":
            system.signup()
        elif choice == "3":
            print("Thank you for using the ShopeeLengke System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Users = Accounts.retrieve_accounts()
    if Users:
        for data in Users:
            Accounts.users.append({"name": data[1], "username": data[2], "password": data[3]})
    else:
        pass
    main()