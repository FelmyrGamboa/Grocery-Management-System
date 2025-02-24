import customtkinter as ctk
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox
from shop_system import ShopSystem, Accounts

class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_welcome_page()
   
    def enter(self):
        self.welcome_canvas.config(cursor="hand2")

    def leave(self):
        self.welcome_canvas.config(cursor="")

    def open_welcome_page(self):
        self.welcome_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.welcome_canvas.pack(fill=ctk.BOTH, expand=True)

        # Welcome page
        self.welcome_page_img = ImageTk.PhotoImage(Image.open("images/welcome_page.png").resize((1920, 1000)))
        self.welcome_canvas.create_image(0, 0, image=self.welcome_page_img, anchor=ctk.NW)

        # x button
        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
        self.x_button = self.welcome_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.welcome_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_page)

        # shop_now_button
        self.shop_now_button_img_tk = ImageTk.PhotoImage(Image.open("images/shop_now_button.png").resize((370, 106)))
        self.shop_now_button = self.welcome_canvas.create_image(400, 210, image=self.shop_now_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.welcome_canvas.tag_bind(self.shop_now_button, "<Button-1>", self.shop_now)

        # shopping_history button
        self.shopping_history_button_img_tk = ImageTk.PhotoImage(Image.open("images/shopping_history_button.png").resize((416, 107)))
        self.shopping_history_button = self.welcome_canvas.create_image(800, 210, image=self.shopping_history_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.welcome_canvas.tag_bind(self.shopping_history_button, "<Button-1>", self.view_shopping_history)

        # log_out_button
        self.log_out_button_img_tk = ImageTk.PhotoImage(Image.open("images/log_out_button.png").resize((239, 109)))
        self.log_out_button = self.welcome_canvas.create_image(1630, 210, image=self.log_out_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.welcome_canvas.tag_bind(self.log_out_button, "<Button-1>", self.log_out)

        self.welcome_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.welcome_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def exit_page(self, event):
        self.quit()

    def shop_now(self, event):
        self.destroy()
        shop_now = ShopNow(self.parent, self.user)
        shop_now.pack(fill=ctk.BOTH, expand=True)

    def view_shopping_history(self, event):
        response= CTkMessagebox(title="Shopping History", message="Redirecting to shopping history page...", icon="info")
        if response.get()== "OK":
            self.destroy()
            shopping_history = ShoppingHistory(self.parent, self.user)
            shopping_history.pack(fill=ctk.BOTH, expand=True)

    def log_out(self, event):
        response = CTkMessagebox(master=self, title="Logout", message="Are you sure you want to log out?", icon="question", option_1="Yes", option_2="No", sound=True)
        if response.get() == "Yes":
            self.destroy()
            logout_page = Logout(self.parent, self.user)
            logout_page.pack(fill=ctk.BOTH, expand=True)

class Logout(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.logout()

    def logout(self):

        self.logout_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.logout_canvas.pack(fill=ctk.BOTH, expand=True)

        self.logout_page_img = ImageTk.PhotoImage(Image.open("images/logout_bg.png").resize((1920, 1000)))
        self.logout_canvas.create_image(0, 0, image=self.logout_page_img, anchor=ctk.NW)

        self.logout_canvas.after(2000, self.back_to_main)

    def back_to_main(self):
        self.destroy()
        self.parent.main_page()

#kay mich      
class ShopNow(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.shop_now()

    def enter(self):
        self.shop_now_canvas.config(cursor="hand2")

    def leave(self):
        self.shop_now_canvas.config(cursor="")

    def shop_now(self):
        self.shop_now_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.shop_now_canvas.pack(fill=ctk.BOTH, expand=True)

        self.shop_now_page_img = ImageTk.PhotoImage(Image.open("images/shop_now_page.png").resize((1920, 1000)))
        self.shop_now_canvas.create_image(0, 0, image=self.shop_now_page_img, anchor=ctk.NW)

        # Back Button
        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.shop_now_canvas.create_image(5, 60, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.shop_now_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_welcome_page)

        #Vegetables Button
        self.vegetable_button_img_tk = ImageTk.PhotoImage(Image.open("images/vegie_button.png").resize((300, 80)))
        self.vegetable_button = self.shop_now_canvas.create_image(10, 375, image=self.vegetable_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.shop_now_canvas.tag_bind(self.vegetable_button, "<Button-1>", self.open_vegetable_section)
       
        # Fruit Button
        self.fruit_button_img_tk = ImageTk.PhotoImage(Image.open("images/fruit_button.png").resize((300, 80)))
        self.fruit_button = self.shop_now_canvas.create_image(10, 450, image=self.fruit_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.shop_now_canvas.tag_bind(self.fruit_button, "<Button-1>", self.open_fruit_section)

        # All Products Button
        self.all_products_button_img_tk = ImageTk.PhotoImage(Image.open("images/all_products_button.png").resize((300, 80)))
        self.all_products_button = self.shop_now_canvas.create_image(10, 300, image=self.all_products_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        # self.shop_now_canvas.tag_bind(self.all_products_button, "<Button-1>", self.open_all_products_section)
       
        # Shopping Cart Button
        self.shopping_cart_button_img_tk = ImageTk.PhotoImage(Image.open("images/shopping_cart.png").resize((150, 120)))
        self.shopping_cart_button = self.shop_now_canvas.create_image(1770, 60, image=self.shopping_cart_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.shop_now_canvas.tag_bind(self.shopping_cart_button, "<Button-1>", self.open_shopping_cart)

        # Exit Button
        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.shop_now_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.shop_now_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_page)

        self.shop_now_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.shop_now_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

#---------------------------------------------
    def back_to_welcome_page(self, event):
        self.destroy()
        welcome_page = WelcomePage(self.parent, self.user)
        welcome_page.pack(fill=ctk.BOTH, expand=True)

    def open_vegetable_section(self, event):
        self.destroy()
        vegetable_section = VegetableSection(self.parent, self.user)
        vegetable_section.pack(fill=ctk.BOTH, expand=True)

    def open_fruit_section(self, event):
        self.destroy()
        fruit_section = FruitSection(self.parent, self.user)
        fruit_section.pack(fill=ctk.BOTH, expand=True)

    def open_shopping_cart(self, event):
        self.destroy()
        shopping_cart= ShoppingCart(self.parent, self.user)
        shopping_cart.pack(fill=ctk.BOTH, expand=True)

    def exit_page(self, event):
        self.quit()

#FRUIT SECTION______________________
class FruitSection(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_fruit_section()
   
    def enter(self):
        self.fruit_canvas.config(cursor="hand2")

    def leave(self):
        self.fruit_canvas.config(cursor="")

    def open_fruit_section(self):
        self.fruit_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.fruit_canvas.pack(fill=ctk.BOTH, expand=True)

        self.fruit_page_img = ImageTk.PhotoImage(Image.open("images/fruit_section_page.png").resize((1920, 1000)))
        self.fruit_canvas.create_image(0, 0, image=self.fruit_page_img, anchor=ctk.NW)
       
        self.sort_price_button_img_tk = ImageTk.PhotoImage(Image.open("images/sortbyprice_button.png").resize((250, 75)))
        self.sort_price_button = self.fruit_canvas.create_image(330, 221, image=self.sort_price_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.sort_price_button, "<Button-1>", self.sort_by_price)

        self.sort_alpha_button_img_tk = ImageTk.PhotoImage(Image.open("images/sort_by_alphabetically.png").resize((376, 90)))
        self.sort_alpha_button = self.fruit_canvas.create_image(570, 216, image=self.sort_alpha_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.sort_alpha_button, "<Button-1>", self.sort_by_alpha)

        self.search_button_img_tk = ImageTk.PhotoImage(Image.open("images/search_icon_button.png").resize((123, 78)))
        self.search_button = self.fruit_canvas.create_image(1660, 85, image=self.search_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.search_button, "<Button-1>", self.search_product)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.fruit_canvas.create_image(5, 50, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_shop_now)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.fruit_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)

        #searching for items
        self.search_bar_entry= ctk.CTkEntry(self, placeholder_text="Shope Wise!", bg_color="#FFFFFF", fg_color="#FFFFFF", border_color="#FFFFFF", width=750, height=45, font=("Poppins", 20, "bold"), text_color="#FE4402", justify='left')
        self.search_bar_entry.place(x=880, y=100, anchor=ctk.CENTER)

        self.search_button_img_tk = ImageTk.PhotoImage(Image.open("images/search_icon_button.png").resize((120,75)))
        self.search_button = self.fruit_canvas.create_image(1670, 85, image=self.search_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.search_button, "<Button-1>", self.search_product)
       
        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.fruit_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_shop_now)

        self.fruit_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.fruit_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def sort_by_price(self, event):
        self.destroy()
        sort_by_price_page= Fruit_Sortbyprice(self.parent, self.user)
        sort_by_price_page.pack(fill=ctk.BOTH, expand=True)

    def sort_by_alpha(self, event):
        self.destroy()
        sort_by_alpha_page = Fruit_SortByAlphabetical(self.parent, self.user)
        sort_by_alpha_page.pack(fill=ctk.BOTH, expand=True)

    def search_product(self, event):
        fruits_search_product= self.search_bar_entry.get().capitalize()

        if fruits_search_product == "Lettuce":
            self.destroy()
            lettuce_add_to_cart= LettuceAddToCartPage(self.parent, self.user)
            lettuce_add_to_cart.pack(fill=ctk.BOTH, expand=True)

        elif fruits_search_product== "Carrot":
            self.destroy()
            carrot_add_to_cart= CarrotAddToCartPage(self.parent, self.user)
            carrot_add_to_cart.pack(fill=ctk.BOTH, expand=True)

        else:
            CTkMessagebox(title="ShopeeLengke Warning", message="Incorrect input. Please re-enter", icon="warning", sound=True)

    def back_to_shop_now(self, event):
        self.destroy()
        shop_now = ShopNow(self.parent, self.user)
        shop_now.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()
       
#SORTING (FRUITS)
class Fruit_Sortbyprice(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_sortbyprice_page()

    def enter(self):
        self.fruit_sortbyprice_canvas.config(cursor="hand2")

    def leave(self):
        self.fruit_sortbyprice_canvas.config(cursor="")

    def open_sortbyprice_page(self):
        self.fruit_sortbyprice_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.fruit_sortbyprice_canvas.pack(fill=ctk.BOTH, expand=True)

        self.sortbyprice_page_img = ImageTk.PhotoImage(Image.open("images/sortbyprice_page_fruits.png").resize((1920, 1000)))
        self.fruit_sortbyprice_canvas.create_image(0, 0, image=self.sortbyprice_page_img, anchor=ctk.NW)

        self.banana_button_img_tk = ImageTk.PhotoImage(Image.open("images/banana.png").resize((270, 378)))
        self.banana_button = self.fruit_sortbyprice_canvas.create_image(416, 280, image=self.banana_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.fruit_sortbyprice_canvas.tag_bind(self.banana_button, "<Button-1>", self.banana_add_to_cart)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.fruit_sortbyprice_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)

        self.fruit_sortbyprice_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_fruit_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.fruit_sortbyprice_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)

        self.fruit_sortbyprice_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.fruit_sortbyprice_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def banana_add_to_cart(self, event):
        self.destroy()
        banana_add_to_cart= BananaAddToCartPage(self.parent, self.user)
        banana_add_to_cart.pack(fill=ctk.BOTH, expand=True)
       
    def back_to_fruit_section(self, event):
        self.destroy()
        back_to_fruit = FruitSection(self.parent, self.user)
        back_to_fruit.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()  

class Fruit_SortByAlphabetical(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_sortbyalpha_page()

    def enter(self):
        self.sortbyalpha_canvas.config(cursor="hand2")

    def leave(self):
        self.sortbyalpha_canvas.config(cursor="")


    def open_sortbyalpha_page(self):
        self.sortbyalpha_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.sortbyalpha_canvas.pack(fill=ctk.BOTH, expand=True)

        self.sortbyalpha_page_img = ImageTk.PhotoImage(Image.open("images/sortbyalpha_page_fruits.png").resize((1920, 1000)))
        self.sortbyalpha_canvas.create_image(0, 0, image=self.sortbyalpha_page_img, anchor=ctk.NW)

        self.watermelon_button_img_tk = ImageTk.PhotoImage(Image.open("images/watermelon.png").resize((260, 360)))
        self.watermelon_button = self.sortbyalpha_canvas.create_image(1529, 640, image=self.watermelon_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyalpha_canvas.tag_bind(self.watermelon_button, "<Button-1>", self.watermelon_add_to_cart)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.sortbyalpha_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyalpha_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_fruit_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.sortbyalpha_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyalpha_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)

        self.sortbyalpha_canvas .tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.sortbyalpha_canvas .tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def watermelon_add_to_cart(self, event):
        self.destroy()
        lettuce_add_to_cart = WatermelonAddToCartPage(self.parent, self.user)
        lettuce_add_to_cart.pack(fill=ctk.BOTH, expand=True)

    def back_to_fruit_section(self, event):
        self.destroy()
        back_to_vegetable = FruitSection(self.parent, self.user)
        back_to_vegetable.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()

class BananaAddToCartPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_banana_add_to_cart_page()
   
    def enter(self):
        self.banana_canvas.config(cursor="hand2")

    def leave(self):
        self.banana_canvas.config(cursor="")
     
    def open_banana_add_to_cart_page(self):
        self.banana_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.banana_canvas.pack(fill=ctk.BOTH, expand=True)

        self.banana_page_img = ImageTk.PhotoImage(Image.open("images/banana_addtocart_page.png").resize((1920, 1000)))
        self.banana_canvas.create_image(0, 0, image=self.banana_page_img, anchor=ctk.NW)

        self.add_cart_button_img_tk = ImageTk.PhotoImage(Image.open("images/add_cart_buttons.png").resize((300, 80)))
        self.add_cart_button = self.banana_canvas.create_image(750, 800, image=self.add_cart_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.banana_canvas.tag_bind(self.add_cart_button,"<Button-1>", self.add_to_cart)

        self.buy_now_button_img_tk = ImageTk.PhotoImage(Image.open("images/buy_now_button.png").resize((300, 80)))
        self.buy_now_button = self.banana_canvas.create_image(1100, 800, image=self.buy_now_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.banana_canvas.tag_bind(self.buy_now_button,"<Button-1>", self.buy_now)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.banana_canvas.create_image(5, 50, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.banana_canvas.tag_bind(self.back_button,"<Button-1>", self.back_to_fruit_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.banana_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)

        self.banana_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.banana_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def buy_now(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Banana Quantity", text="How many banana will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                buy_now = system.cart_purchase("fruits", "Banana", quantity, self.user, "buy_now")
                if buy_now:
                    response= CTkMessagebox(master= self, title="Buy Now", message="Check out Done! Thank you for shopping with us", icon="check", option_1="OK", sound=True)
                    if response.get()== "OK":
                        self.destroy()
                        back_to_welcome_page= FruitSection(self.parent, self.user)
                        back_to_welcome_page.pack(fill=ctk.BOTH, expand=True)

            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def add_to_cart(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Banana Quantity", text="How many banana will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                add_to_cart = system.cart_purchase("fruits", "Banana", quantity, self.user, "add_to_cart")
                if add_to_cart:
                    response= CTkMessagebox(master= self, title="Add to Cart", message="Added Done to Shopping cart.", icon="check", option_1="OK", sound=True)

                    if response.get()== "OK":
                        self.destroy()
                        back_to_sorting= FruitSection(self.parent, self.user)
                        back_to_sorting.pack(fill=ctk.BOTH, expand=True)
                        break
                
            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def back_to_fruit_section(self, event):
        self.destroy()
        back_to_vegetables= FruitSection(self.parent, self.user)
        back_to_vegetables.pack(fill=ctk.BOTH, expand=True)

class WatermelonAddToCartPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_watermelon_add_to_cart_page()

    def enter(self):
        self.watermelon_canvas.config(cursor="hand2")

    def leave(self):
        self.watermelon_canvas.config(cursor="")
   
    def open_watermelon_add_to_cart_page(self):
        self.watermelon_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.watermelon_canvas.pack(fill=ctk.BOTH, expand=True)

        self.watermelon_page_img = ImageTk.PhotoImage(Image.open("images/watermerlon_addtocart_page.png").resize((1920, 1000)))
        self.watermelon_canvas.create_image(0, 0, image=self.watermelon_page_img, anchor=ctk.NW)

        self.add_cart_button_img_tk = ImageTk.PhotoImage(Image.open("images/add_cart_buttons.png").resize((300, 80)))
        self.add_cart_button = self.watermelon_canvas.create_image(750, 800, image=self.add_cart_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.watermelon_canvas.tag_bind(self.add_cart_button,"<Button-1>", self.add_to_cart)

        self.buy_now_button_img_tk = ImageTk.PhotoImage(Image.open("images/buy_now_button.png").resize((300, 80)))
        self.buy_now_button = self.watermelon_canvas.create_image(1100, 800, image=self.buy_now_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.watermelon_canvas.tag_bind(self.buy_now_button,"<Button-1>", self.buy_now)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.watermelon_canvas.create_image(5, 50, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.watermelon_canvas.tag_bind(self.back_button,"<Button-1>", self.back_to_fruit_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.watermelon_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        
        self.watermelon_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.watermelon_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def buy_now(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Watermelon Quantity", text="How many watermelon will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                buy_now = system.cart_purchase("fruits", "Watermelon", quantity, self.user, "buy_now")
                if buy_now:
                    response= CTkMessagebox(master= self, title="Buy Now", message="Check out Done! Thank you for shopping with us", icon="check", option_1="OK", sound=True)
                    if response.get()== "OK":
                        self.destroy()
                        back_to_welcome_page= FruitSection(self.parent, self.user)
                        back_to_welcome_page.pack(fill=ctk.BOTH, expand=True)

            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def add_to_cart(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Watermelon Quantity", text="How many watermelon will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                add_to_cart = system.cart_purchase("fruits", "Watermelon", quantity, self.user, "add_to_cart")
                if add_to_cart:
                    response= CTkMessagebox(master= self, title="Add to Cart", message="Added Done to Shopping cart.", icon="check", option_1="OK", sound=True)

                    if response.get()== "OK":
                        self.destroy()
                        back_to_sorting= FruitSection(self.parent, self.user)
                        back_to_sorting.pack(fill=ctk.BOTH, expand=True)
                        break
                
            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def back_to_fruit_section(self, event):
        self.destroy()
        back_to_vegetables= FruitSection(self.parent, self.user)
        back_to_vegetables.pack(fill=ctk.BOTH, expand=True)

#-------------------------------------------------------
# SORTING (VEGETABLES )
class VegetableSection(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_vegetable_section()
       
    def enter(self):
        self.vegetable_canvas.config(cursor="hand2")

    def leave(self):
        self.vegetable_canvas.config(cursor="")

    def open_vegetable_section(self):
        self.vegetable_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.vegetable_canvas.pack(fill=ctk.BOTH, expand=True)

        self.vegetable_page_img = ImageTk.PhotoImage(Image.open("images/vegetable_section_page.png").resize((1920, 1000)))
        self.vegetable_canvas.create_image(0, 0, image=self.vegetable_page_img, anchor=ctk.NW)

        self.sort_price_button_img_tk = ImageTk.PhotoImage(Image.open("images/sortbyprice_button.png").resize((250, 80)))
        self.sort_price_button = self.vegetable_canvas.create_image(390, 220, image=self.sort_price_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.vegetable_canvas.tag_bind(self.sort_price_button, "<Button-1>", self.sort_by_price)

        self.sort_alpha_button_img_tk = ImageTk.PhotoImage(Image.open("images/sort_by_alphabetically.png").resize((300, 90)))
        self.sort_alpha_button = self.vegetable_canvas.create_image(650, 216, image=self.sort_alpha_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.vegetable_canvas.tag_bind(self.sort_alpha_button, "<Button-1>", self.sort_by_alpha)

        self.search_button_img_tk = ImageTk.PhotoImage(Image.open("images/search_icon_button.png").resize((140,75)))
        self.search_button = self.vegetable_canvas.create_image(1670, 90, image=self.search_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.vegetable_canvas.tag_bind(self.search_button, "<Button-1>", self.search_product)

        #searching for items
        self.search_bar_entry= ctk.CTkEntry(self, placeholder_text="Shope Wise!", bg_color="#FFFFFF", fg_color="#FFFFFF", border_color="#FFFFFF", width=750, height=45, font=("Poppins", 20, "bold"), text_color="#FE4402", justify='left')

        self.search_bar_entry.place(x=880, y=100, anchor=ctk.CENTER)
       
        self.search_button_img_tk = ImageTk.PhotoImage(Image.open("images/search_icon_button.png").resize((120,75)))
        self.search_button = self.vegetable_canvas.create_image(1670, 85, image=self.search_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.vegetable_canvas.tag_bind(self.search_button, "<Button-1>", self.search_product)

    
        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.vegetable_canvas.create_image(5, 50, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.vegetable_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_shop_now)

        #exit
        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.vegetable_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.vegetable_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)

        self.vegetable_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.vegetable_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def sort_by_price(self, event):
        self.destroy()
        sort_by_price_page= Vegetables_Sortbyprice(self.parent, self.user)
        sort_by_price_page.pack(fill=ctk.BOTH, expand=True)

    def sort_by_alpha(self, event):
        self.destroy()
        sort_by_alpha_page = Vegetables_SortByAlphabetical(self.parent, self.user)
        sort_by_alpha_page.pack(fill=ctk.BOTH, expand=True)

    def search_product(self, event):
        vegetables_search_product= self.search_bar_entry.get().capitalize()

        if vegetables_search_product == "Lettuce":
            self.destroy()
            lettuce_add_to_cart= LettuceAddToCartPage(self.parent, self.user)
            lettuce_add_to_cart.pack(fill=ctk.BOTH, expand=True)

        elif vegetables_search_product== "Carrot":
            self.destroy()
            carrot_add_to_cart= CarrotAddToCartPage(self.parent, self.user)
            carrot_add_to_cart.pack(fill=ctk.BOTH, expand=True)

        else:
            CTkMessagebox(title="ShopeeLengke Warning", message="Incorrect input. Please re-enter.", icon="warning", sound=True)

    def back_to_shop_now(self, event):
        self.destroy()
        shop_now = ShopNow(self.parent, self.user)
        shop_now.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()

class Vegetables_Sortbyprice(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_sortbyprice_page()

    def enter(self):
        self.sortbyprice_canvas.config(cursor="hand2")

    def leave(self):
        self.sortbyprice_canvas.config(cursor="")

    def open_sortbyprice_page(self):
        self.sortbyprice_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.sortbyprice_canvas.pack(fill=ctk.BOTH, expand=True)

        self.sortbyprice_page_img = ImageTk.PhotoImage(Image.open("images/sortbyprice_page.png").resize((1920, 1000)))
        self.sortbyprice_canvas.create_image(0, 0, image=self.sortbyprice_page_img, anchor=ctk.NW)

        self.carrot_button_img_tk = ImageTk.PhotoImage(Image.open("images/carrot.png").resize((270, 380)))
        self.carrot_button = self.sortbyprice_canvas.create_image(670, 630, image=self.carrot_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyprice_canvas.tag_bind(self.carrot_button, "<Button-1>", self.carrot_add_to_cart)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.sortbyprice_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyprice_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_shop_now)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.sortbyprice_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyprice_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)
    
        self.sortbyprice_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.sortbyprice_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def carrot_add_to_cart(self, event):
        self.destroy()
        carrot_add_to_cart= CarrotAddToCartPage(self.parent, self.user)
        carrot_add_to_cart.pack(fill=ctk.BOTH, expand=True)

    def back_to_shop_now(self, event):
        self.destroy()
        shop_now = VegetableSection(self.parent, self.user)
        shop_now.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()    

class Vegetables_SortByAlphabetical(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname= "event"
        self.open_sortbyalpha_page()

    def enter(self):
        self.sortbyalpha_canvas.config(cursor="hand2")

    def leave(self):
        self.sortbyalpha_canvas.config(cursor="")

    def open_sortbyalpha_page(self):
        self.sortbyalpha_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.sortbyalpha_canvas.pack(fill=ctk.BOTH, expand=True)

        self.sortbyalpha_page_img = ImageTk.PhotoImage(Image.open("images/sortbyalphabetical_page.png").resize((1920, 1000)))
        self.sortbyalpha_canvas.create_image(0, 0, image=self.sortbyalpha_page_img, anchor=ctk.NW)

        self.lettuce_button_img_tk = ImageTk.PhotoImage(Image.open("images/lettuce.png").resize((270, 380)))
        self.lettuce_button = self.sortbyalpha_canvas.create_image(1550, 280, image=self.lettuce_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyalpha_canvas.tag_bind(self.lettuce_button, "<Button-1>", self.lettuce_add_to_cart)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.sortbyalpha_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyalpha_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_vegetable_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.sortbyalpha_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.sortbyalpha_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)
       
        self.sortbyalpha_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.sortbyalpha_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def lettuce_add_to_cart(self, event):
        self.destroy()
        lettuce_add_to_cart = LettuceAddToCartPage(self.parent, self.user)
        lettuce_add_to_cart.pack(fill=ctk.BOTH, expand=True)

    def back_to_vegetable_section(self, event):
        self.destroy()
        back_to_vegetable = VegetableSection(self.parent, self.user)
        back_to_vegetable.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()

#-------------------------------------------------
#VEGETABLES ADD TO CART  

class LettuceAddToCartPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_lettuce_add_to_cart_page()
 
    def enter(self):
        self.lettuce_canvas.config(cursor="hand2")

    def leave(self):
        self.lettuce_canvas.config(cursor="")
   
    def open_lettuce_add_to_cart_page(self):
        self.lettuce_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.lettuce_canvas.pack(fill=ctk.BOTH, expand=True)

        self.lettuce_page_img = ImageTk.PhotoImage(Image.open("images/lettuce_addtocart_page.png").resize((1920, 1000)))
        self.lettuce_canvas.create_image(0, 0, image=self.lettuce_page_img, anchor=ctk.NW)

        self.add_cart_button_img_tk = ImageTk.PhotoImage(Image.open("images/add_cart_buttons.png").resize((300, 80)))
        self.add_cart_button = self.lettuce_canvas.create_image(750, 800, image=self.add_cart_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.lettuce_canvas.tag_bind(self.add_cart_button,"<Button-1>", self.add_to_cart)

        self.buy_now_button_img_tk = ImageTk.PhotoImage(Image.open("images/buy_now_button.png").resize((300, 80)))
        self.buy_now_button = self.lettuce_canvas.create_image(1100, 800, image=self.buy_now_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.lettuce_canvas.tag_bind(self.buy_now_button,"<Button-1>", self.buy_now)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.lettuce_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.lettuce_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_vegetables_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.lettuce_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.lettuce_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)

        self.lettuce_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.lettuce_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def buy_now(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Lettuce Quantity", text="How many lettuce will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                buy_now = system.cart_purchase("vegetables", "Lettuce", quantity, self.user, "buy_now")
                if buy_now:
                    response= CTkMessagebox(master= self, title="Buy Now", message="Check out Done! Thank you for shopping with us", icon="check", option_1="OK", sound=True)
                    if response.get()== "OK":
                        self.destroy()
                        back_to_welcome_page= VegetableSection(self.parent, self.user)
                        back_to_welcome_page.pack(fill=ctk.BOTH, expand=True)

            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def add_to_cart(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Lettuce Quantity", text="How many lettuce will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                add_to_cart = system.cart_purchase("vegetables", "Lettuce", quantity, self.user, "add_to_cart")
                if add_to_cart:
                    response= CTkMessagebox(master= self, title="Add to Cart", message="Added Done to Shopping cart.", icon="check", option_1="OK", sound=True)

                    if response.get()== "OK":
                        self.destroy()
                        back_to_sorting= VegetableSection(self.parent, self.user)
                        back_to_sorting.pack(fill=ctk.BOTH, expand=True)
                        break
                
            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def back_to_vegetables_section(self, event):
        self.destroy()
        back_to_vegetables= VegetableSection(self.parent, self.user)
        back_to_vegetables.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()

class CarrotAddToCartPage(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_carrot_add_to_cart_page()

    def enter(self):
        self.carrot_canvas.config(cursor="hand2")

    def leave(self):
        self.carrot_canvas.config(cursor="")

    def open_carrot_add_to_cart_page(self):
        self.carrot_canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.carrot_canvas.pack(fill=ctk.BOTH, expand=True)

        self.carrot_page_img = ImageTk.PhotoImage(Image.open("images/carrot_addtocart_page.png").resize((1920, 1000)))
        self.carrot_canvas.create_image(0, 0, image=self.carrot_page_img, anchor=ctk.NW)

        self.add_cart_button_img_tk = ImageTk.PhotoImage(Image.open("images/add_cart_buttons.png").resize((300, 80)))
        self.add_cart_button = self.carrot_canvas.create_image(750, 800, image=self.add_cart_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.carrot_canvas.tag_bind(self.add_cart_button,"<Button-1>", self.add_to_cart)

        self.buy_now_button_img_tk = ImageTk.PhotoImage(Image.open("images/buy_now_button.png").resize((300, 80)))
        self.buy_now_button = self.carrot_canvas.create_image(1100, 800, image=self.buy_now_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.carrot_canvas.tag_bind(self.buy_now_button,"<Button-1>", self.buy_now)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.carrot_canvas.create_image(20, 70, image=self.back_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.carrot_canvas.tag_bind(self.back_button, "<Button-1>", self.back_to_vegetables_section)

        self.x_button_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((80, 60)))
        self.x_button = self.carrot_canvas.create_image(1820, 8, image=self.x_button_img_tk, anchor=ctk.NW, tag= self.tagname)
        self.carrot_canvas.tag_bind(self.x_button, "<Button-1>", self.exit_section)

        self.carrot_canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.carrot_canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())
 
    def buy_now(self, event):
        system = ShopSystem()
        while True:
            try:
                ask_quantity = ctk.CTkInputDialog(title="Carrot Quantity", text="How many carrots will you buy?", font=("Arimo", 16))
                quantity = ask_quantity.get_input()

                if quantity.isdigit():
                    buy_now = system.cart_purchase("vegetables", "Carrot", quantity, self.user, "buy_now")
                    if buy_now:
                        response= CTkMessagebox(master= self, title="Buy Now", message="Check out Done! Thank you for shopping with us", icon="check", option_1="OK", sound=True)
                        if response.get()== "OK":
                            self.destroy()
                            back_to_welcome_page= VegetableSection(self.parent, self.user)
                            back_to_welcome_page.pack(fill=ctk.BOTH, expand=True)
                            break

                else:
                    response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                    if response.get()== "OK":
                        continue
            except AttributeError:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue

    def add_to_cart(self, event):
        system = ShopSystem()
        while True:
            ask_quantity = ctk.CTkInputDialog(title="Lettuce Quantity", text="How many lettuce will you buy?", font=("Arimo", 16))
            quantity = ask_quantity.get_input()

            if quantity.isdigit():
                add_to_cart = system.cart_purchase("vegetables", "Carrot", quantity, self.user, "add_to_cart")
                if add_to_cart:
                    response= CTkMessagebox(master= self, title="Add to Cart", message="Added Done to Shopping cart.", icon="check", option_1="OK", sound=True)
                    if response.get()== "OK":
                        self.destroy()
                        back_to_sorting= VegetableSection(self.parent, self.user)
                        back_to_sorting.pack(fill=ctk.BOTH, expand=True)
                        break
                
            else:
                response= CTkMessagebox(master= self, title="Error", message="Please input a valid quantity.", icon="cancel", option_1="OK", sound=True)
                if response.get()== "OK":
                    continue


    def back_to_vegetables_section(self, event):
        self.destroy()
        back_to_vegetables= VegetableSection(self.parent, self.user)
        back_to_vegetables.pack(fill=ctk.BOTH, expand=True)

    def exit_section(self, event):
        self.parent.destroy()

class ShoppingCart(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.open_shopping_cart()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def open_shopping_cart(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack()

        # Background Image
        self.set_bg_img = ImageTk.PhotoImage(Image.open("images/shopping_cart_bg.png").resize((1920, 1000)))
        self.bg_img_canvas = self.canvas.create_image(0, 0, image=self.set_bg_img, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.canvas.create_image(-7, -11, image=self.back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.back_button, "<Button-1>", self.back)

        # Exit Button (Top-Right Corner)
        self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
        self.exit_button = self.canvas.create_image(1840, 8, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)
        
        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        self.view_shopping_cart(self.user)

    def view_shopping_cart(self, user):
        system = ShopSystem()
        
        products = {
            "Apple" : ImageTk.PhotoImage(Image.open("images/products/apple.png").resize((100, 100))),
            "Banana": ImageTk.PhotoImage(Image.open("images/products/banana.png").resize((100, 100))),
            "Cabbage" : ImageTk.PhotoImage(Image.open("images/products/cabbage.png").resize((100, 100))),
            "Carrot" : ImageTk.PhotoImage(Image.open("images/products/carrot.png").resize((100, 100))),
            "Eggplant" : ImageTk.PhotoImage(Image.open("images/products/eggplant.png").resize((100, 100))),
            "Garlic" : ImageTk.PhotoImage(Image.open("images/products/garlic.png").resize((100, 100))),
            "Grapes" : ImageTk.PhotoImage(Image.open("images/products/grapes.png").resize((100, 100))),
            "Lettuce" : ImageTk.PhotoImage(Image.open("images/products/lettuce.png").resize((100, 100))),
            "Mango" : ImageTk.PhotoImage(Image.open("images/products/mango.png").resize((100, 100))),
            "Melon" : ImageTk.PhotoImage(Image.open("images/products/melon.png").resize((100, 100))),
            "Onions" : ImageTk.PhotoImage(Image.open("images/products/onions.png").resize((100, 100))),
            "Orange" : ImageTk.PhotoImage(Image.open("images/products/orange.png").resize((100, 100))),
            "Papaya" : ImageTk.PhotoImage(Image.open("images/products/papaya.png").resize((100, 100))),
            "Peas" : ImageTk.PhotoImage(Image.open("images/products/peas.png").resize((100, 100))),
            "Pineapple" : ImageTk.PhotoImage(Image.open("images/products/pineapple.png").resize((100, 100))),
            "Potato" : ImageTk.PhotoImage(Image.open("images/products/potato.png").resize((100, 100))),
            "Spinach" : ImageTk.PhotoImage(Image.open("images/products/spinach.png").resize((100, 100))),
            "Strawberry" : ImageTk.PhotoImage(Image.open("images/products/strawberry.png").resize((100, 100))),
            "Tomato" : ImageTk.PhotoImage(Image.open("images/products/tomato.png").resize((100, 100))),
            "Watermelon" : ImageTk.PhotoImage(Image.open("images/products/watermelon.png").resize((100, 100)))

        }

        cart_items = system.view_cart(self.user)
        if cart_items:
            self.cart = ctk.CTkScrollableFrame(self, width=1240, height=330, bg_color="#EEEAEA", fg_color="#EEEAEA", border_color="#EEEAEA")
            self.cart.place(x=140, y=395)

            for record in cart_items:
                product_name = record[0]
                price = record[1]
                quantity = record[2]
                total_price = record[3]
                category = record[4]

                record_text = f"                {product_name:<50} ₱{price:<25} {quantity:<25} ₱{total_price}"
                history_label = ctk.CTkButton(self.cart, image=products[product_name], 
                                              compound="left", text=record_text, text_color="black", 
                                              fg_color="#EEEAEA", font=("Arimo", 25), hover_color="#D4D0D0", 
                                              command=lambda product_name=product_name: self.buy_now(product_name, quantity, category))
                history_label.pack(padx= 10, pady=20, anchor = "w")                
               
        elif cart_items == False:
            self.canvas.delete("all")
            self.ads_img = ImageTk.PhotoImage(Image.open("images/shopping_cart_empty.png").resize((1920, 1000)))
            self.canvas.create_image(0, 0, image=self.ads_img, anchor=ctk.NW)

            self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
            self.back_button = self.canvas.create_image(-7, -11, image=self.back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
            self.canvas.tag_bind(self.back_button, "<Button-1>", self.back)

            # Exit Button (Top-Right Corner)
            self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
            self.exit_button = self.canvas.create_image(1840, 8, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
            self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)

    def buy_now(self, product_name, quantity, category):
        system = ShopSystem()
        cart_items = system.view_cart(self.user)

        response= CTkMessagebox(master= self, title="Buy Now", message=f"Are you sure you want to buy this {product_name}", icon="check", option_1="Cancel", option_2="Yes", sound=True)
        if response.get() == "Yes":
            purchase_now = system.cart_purchase(category, product_name, quantity, self.user, "buy_now")
            if purchase_now:
                response2= CTkMessagebox(master= self, title="Buy Now", message="Check out Done! Thank you for shopping with us", icon="check", option_1="OK", sound=True)
                if response2.get()== "OK":
                    self.destroy()
                    back_to_welcome_page= WelcomePage(self.parent, self.user)
                    back_to_welcome_page.pack(fill=ctk.BOTH, expand=True)
                    cart_items.clear()

    def back(self, event):
        self.destroy()
        back_to_last_page = ShopNow(self.parent, self.user)
        back_to_last_page.pack(fill=ctk.BOTH, expand=True)

    def exit(self, event):
        self.quit()

class ShoppingHistory(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.user = user
        self.tagname = "event"
        self.shopping_history()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def shopping_history(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.shopping_history_img = ImageTk.PhotoImage(Image.open("images/shopping_history.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.shopping_history_img, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.back_button = self.canvas.create_image(-7, -11, image=self.back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.back_button, "<Button-1>", self.back)

        # Exit Button (Top-Right Corner)
        self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
        self.exit_button = self.canvas.create_image(1840, 8, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        self.view_shopping_history(self.user)

    def back(self, event):
        self.destroy()
        welcome_page = WelcomePage(self.parent, self.user)
        welcome_page.pack(fill=ctk.BOTH, expand=True)

    def exit(self, event):
        self.quit()

    def view_shopping_history(self, user):
        system = ShopSystem()

        profile_name = ctk.CTkLabel(self.canvas, text=user.name, text_color="black", fg_color="#F4FCFE", font=("Arimo", 25, "bold"), anchor="center")
        profile_name.place(x=125, y=255)

        products = {
            "Apple" : ImageTk.PhotoImage(Image.open("images/products/apple.png").resize((100, 100))),
            "Banana": ImageTk.PhotoImage(Image.open("images/products/banana.png").resize((100, 100))),
            "Cabbage" : ImageTk.PhotoImage(Image.open("images/products/cabbage.png").resize((100, 100))),
            "Carrot" : ImageTk.PhotoImage(Image.open("images/products/carrot.png").resize((100, 100))),
            "Eggplant" : ImageTk.PhotoImage(Image.open("images/products/eggplant.png").resize((100, 100))),
            "Garlic" : ImageTk.PhotoImage(Image.open("images/products/garlic.png").resize((100, 100))),
            "Grapes" : ImageTk.PhotoImage(Image.open("images/products/grapes.png").resize((100, 100))),
            "Lettuce" : ImageTk.PhotoImage(Image.open("images/products/lettuce.png").resize((100, 100))),
            "Mango" : ImageTk.PhotoImage(Image.open("images/products/mango.png").resize((100, 100))),
            "Melon" : ImageTk.PhotoImage(Image.open("images/products/melon.png").resize((100, 100))),
            "Onions" : ImageTk.PhotoImage(Image.open("images/products/onions.png").resize((100, 100))),
            "Orange" : ImageTk.PhotoImage(Image.open("images/products/orange.png").resize((100, 100))),
            "Papaya" : ImageTk.PhotoImage(Image.open("images/products/papaya.png").resize((100, 100))),
            "Peas" : ImageTk.PhotoImage(Image.open("images/products/peas.png").resize((100, 100))),
            "Pineapple" : ImageTk.PhotoImage(Image.open("images/products/pineapple.png").resize((100, 100))),
            "Potato" : ImageTk.PhotoImage(Image.open("images/products/potato.png").resize((100, 100))),
            "Spinach" : ImageTk.PhotoImage(Image.open("images/products/spinach.png").resize((100, 100))),
            "Strawberry" : ImageTk.PhotoImage(Image.open("images/products/strawberry.png").resize((100, 100))),
            "Tomato" : ImageTk.PhotoImage(Image.open("images/products/tomato.png").resize((100, 100))),
            "Watermelon" : ImageTk.PhotoImage(Image.open("images/products/watermelon.png").resize((100, 100)))
        }
        history = system.view_shopping_history(user.username)
        if history:
            self.history_canvas = ctk.CTkScrollableFrame(self, width=1010, height=330, bg_color="#EEEAEA", fg_color="#EEEAEA", border_color="#EEEAEA")
            self.history_canvas.place(x=380, y=360)

            for record in history:
                record_text = f"        {record[user.username][0]:<30} ₱{record[user.username][1]:<35} {record[user.username][2]:<30} ₱{record[user.username][3]:<25} {record[user.username][4]}"
                history_label = ctk.CTkLabel(self.history_canvas, image=products[record[user.username][0]], compound="left", text=record_text, text_color="black", fg_color="#EEEAEA", font=("Arimo", 16))
                history_label.pack(padx= 10, pady=20, anchor = "w")
               
        elif history == False:
            self.canvas.delete("all")
            self.ads_img = ImageTk.PhotoImage(Image.open("images/shopping_history_no_order.png").resize((1920, 1000)))
            self.canvas.create_image(0, 0, image=self.ads_img, anchor=ctk.NW)

            self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
            self.back_button = self.canvas.create_image(-7, -11, image=self.back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
            self.canvas.tag_bind(self.back_button, "<Button-1>", self.back)

            # Exit Button (Top-Right Corner)
            self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
            self.exit_button = self.canvas.create_image(1840, 8, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
            self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)
