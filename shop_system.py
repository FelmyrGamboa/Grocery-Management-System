import datetime
from CTkMessagebox import CTkMessagebox
from database import Customer


class Accounts:
    users = []
    customer_db = Customer()


    @classmethod
    def signup_account(cls, name, username, password):
        cls.customer_db.customer_cursor.execute("SELECT * FROM customer_information WHERE username = %s", (username,))
        data = cls.customer_db.customer_cursor.fetchall()
           
        if not data:
            cls.customer_db.customer_cursor.execute("INSERT INTO customer_information (fullname, username, password) VALUES (%s, %s, %s)", (name, username, password))
            cls.customer_db.db.commit()
            return True
        else:
            CTkMessagebox(title="Error", message="The username used was already been taken, please try another username to signup.", icon="cancel", sound=True)
            return False


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


class Cart:
    cart_items = {}
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    @classmethod
    def manage_cart(cls, user):
        while True:            
            #ADDED
            # user_cart = [item for item in cls.cart_items if item.user == user]
            user_cart = cls.cart_items.get(user, [])
            # cart_items = []

            if not user_cart:
                return False
            return user_cart
           
            # for item in user_cart:
            #     cart_items.append({item.user : (item.product, item.quantity, item.price, (item.quantity * item.price), item.category)})
            # return cart_items


    @classmethod
    # self.product, self.price, self.quantity, self.total_price, self.category
    def checkout(cls, user, product_name, quantity):
        user_cart = cls.cart_items.get(user)
        for item in user_cart:
            if product_name == item[0] and int(quantity) == item[2]:
                ShoppingHistory.add_product_to_history(user.username, item[0], item[1], item[2], item[3], cls.date_time)
                ShoppingHistory(item[0], item[1], item[2])
                cls.cart_items[user].remove(item)
                return

    # def checkout(cls, user, total_price):
    #     user_cart = [item for item in cls.cart_items if item.user == user]

    #     for idx, item in enumerate(user_cart, start=1):
    #         ShoppingHistory.add_product_to_history(user.username, item.product, item.price, item.quantity, total_price, cls.date_time)
    #         ShoppingHistory(item.product, item.price, item.quantity)
    #         cls.cart_items.remove(item)


    #     cls.cart_items = [item for item in cls.cart_items if item not in user_cart]  # Clear purchased items


    def __init__(self, product, price, quantity, category, user):
        self.product = str(product)
        self.price = float(price)
        self.quantity = int(quantity)
        self.total_price = self.price * self.quantity
        self.category = category
        self.user = user
        # Cart.cart_items[self.user].append(self.product, self.price, self.quantity, self.category)

        if self.user not in Cart.cart_items:
            Cart.cart_items[self.user] = []
        Cart.cart_items[self.user].append((self.product, self.price, self.quantity, self.total_price, self.category))


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


    @classmethod
    def add_product_to_history(cls, username, product_name, price, quantity, total_price, date_time):
        cls.customer_db.customer_cursor.execute("INSERT INTO customer_shopping_history (username, product_name, price, quantity, total_price, date_time) VALUES (%s, %s, %s, %s, %s, %s)", (username, product_name, price, quantity, total_price, date_time))
        cls.customer_db.db.commit()


    @classmethod
    def view_shopping_history(cls, username):
        cls.retrieve_shopping_history(username)
        try:
            history = [item for item in cls.records if item.get(username)]
            if not history:
                return False
            else:
                return history
           
        except KeyError:
            return False


    def __init__(self, product, price, quantity):
        self.product = str(product)
        self.price = float(price)
        self.quantity = int(quantity)
        self.total_price = float(self.price * self.quantity)


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
   
    def add_products(self, category, product, quantity, logged_user, status):
        grocery = GroceryItems()
        products = grocery.items[category]
       
        for items in products:
            if items[0] == product:
                return self.product_finalization(items, quantity, logged_user, category, status)


    def product_finalization(self, selected_product, quantity, logged_user, category, status):
        if status == "add_to_cart":
            chosen_product = Cart(selected_product[0], selected_product[1], quantity, category, logged_user)
            return True
       
        elif status == "buy_now":
            chosen_product = Cart(selected_product[0], selected_product[1], quantity, category, logged_user)
            # user_cart=[item for item in Cart.cart_items if item.user == logged_user]
            user_cart = Cart.cart_items.get(logged_user)
            for items in user_cart:
                if selected_product[0] == items[0] and int(quantity) == items[2]:
                    # total_price = sum((item.quantity * item.price) for item in user_cart)
                    # self.product, self.price, self.quantity, self.total_price, self.category
                    chosen_product.checkout(logged_user, selected_product[0], quantity)
                    return True
       
class ShopSystem:
    def __init__(self):
        self.logged_user = None


    def signup(self, name, username, password):
        Accounts.users.append({"name": name, "username": username, "password": password})
        signup = Accounts.signup_account(name, username, password)


        if signup:
            CTkMessagebox(title="Success!", message=f"Registration successful! Welcome, {name}!!", icon="check", sound=True)
            return True


    def login(self, username, password):
        for user in Accounts.users:
            if user["username"] == username and user["password"] == password and Accounts.verify_account(username, password):
                logged_user = Accounts(user['name'], user['username'], user['password'])
                CTkMessagebox(title="Success!", message=f"Login successful! Welcome back, {user['name']}!", icon="check", sound=True)
                return True, logged_user
   
        CTkMessagebox(title="Error", message="Invalid username or password.", icon="cancel", sound=True)
        return False


    def cart_purchase(self, category, product, quantity, user, status):
        grocery = GroceryItems()
        return grocery.add_products(category, product, quantity, user, status)
   
    def view_cart(self, user):
        return Cart.manage_cart(user)
   
    def view_shopping_history(self, user):
        return ShoppingHistory.view_shopping_history(user)



