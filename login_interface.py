import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image
from shop_system import ShopSystem, Accounts
from shopeelengke_interface import WelcomePage

class Login(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tagname = "event"
        self.login_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def login_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height= 1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.login_page_img_tk = ImageTk.PhotoImage(Image.open("images/log_in_page.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.login_page_img_tk, anchor=ctk.NW)

        self.login_button_img_tk = ImageTk.PhotoImage(Image.open("images/log_in_button.png").resize((1026, 118)))
        self.login_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))

        self.login_button = self.canvas.create_image(445, 700, image=self.login_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_button, "<Button-1>", self.login)

        self.login_back_button = self.canvas.create_image(20, 70, image=self.login_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_back_button, "<Button-1>", self.back)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", bg_color="#F2F2F2", fg_color="#F2F2F2", border_color="#F2F2F2", width=790, height=60, font=("Poppins", 30, "bold"), text_color="#FE4402", justify='center')
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", bg_color="#F2F2F2", fg_color="#F2F2F2", border_color="#F2F2F2", width=790, height=60, font=("Poppins", 30, "bold"), text_color="#FE4402", justify='center')

        self.username_entry.place(x=765, y=410, anchor=ctk.CENTER)
        self.password_entry.place(x=765, y=510, anchor=ctk.CENTER)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

        Users = Accounts.retrieve_accounts()
        if Users:
            for data in Users:
                Accounts.users.append({"name": data[1], "username": data[2], "password": data[3]})

    def login(self, event):
        system = ShopSystem()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            CTkMessagebox(title="Error", message="Requirements cannot be empty. Please fill up.", icon="cancel", sound=True)
        else: 
            user = system.login(username, password)
            if user:
                self.destroy()
                welcome_page = WelcomePage(self.parent, user[1])
                welcome_page.pack(fill=ctk.BOTH, expand=True)

    def back(self, event):
        self.destroy()
        self.parent.main_page()

class SignUp(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tagname = "event"
        self.signup_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def signup_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height= 1000)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.set_bg_img = ImageTk.PhotoImage(Image.open("images/sign_up_page.png").resize((1920, 1000)))
        self.bg_img_canvas = self.canvas.create_image(0, 0, image=self.set_bg_img, anchor=ctk.NW)

        self.signup_button_img_tk = ImageTk.PhotoImage(Image.open("images/sign_up_page_button.png").resize((1026, 118)))
        self.signup_button = self.canvas.create_image(445, 750, image=self.signup_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.signup_button, "<Button-1>", self.signup)

        self.signup_back_button_img_tk = ImageTk.PhotoImage(Image.open("images/back_button.png").resize((120, 108)))
        self.signup_back_button = self.canvas.create_image(20, 70, image=self.signup_back_button_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.signup_back_button, "<Button-1>", self.back)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name", bg_color="#F2F2F2", fg_color="#F2F2F2", border_color="#F2F2F2", width=790, height=60, font=("Poppins", 30, "bold"), text_color="#FE4402", justify='center')
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", bg_color="#F2F2F2", fg_color="#F2F2F2", border_color="#F2F2F2", width=790, height=60, font=("Poppins", 30, "bold"), text_color="#FE4402", justify='center')
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", bg_color="#F2F2F2", fg_color="#F2F2F2", border_color="#F2F2F2", width=790, height=60, font=("Poppins", 30, "bold"), text_color="#FE4402", justify='center')

        self.name_entry.place(x=765, y=340, anchor=ctk.CENTER)
        self.username_entry.place(x=765, y=440, anchor=ctk.CENTER)
        self.password_entry.place(x=765, y=540, anchor=ctk.CENTER)
        
        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def signup(self, event):
        system = ShopSystem()
        name = self.name_entry.get().strip()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not name or not username or not password:
            CTkMessagebox(title="Error", message="Requirements cannot be empty. Please fill up.", icon="cancel", sound=True)

        else:
            user = system.signup(name, username, password)
            if user:
                self.destroy()
                self.parent.main_page()

    def back(self, event):
        self.destroy()
        self.parent.main_page()
