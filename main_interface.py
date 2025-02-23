import customtkinter as ctk
from login_interface import Login, SignUp
from PIL import ImageTk, Image

class ShopeeLengke(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ShopeeLengke")
        self.tagname = "event"
        self.main_page()

    def enter(self):
        self.canvas.config(cursor="hand2")

    def leave(self):
        self.canvas.config(cursor="")

    def main_page(self):
        self.canvas = ctk.CTkCanvas(self, width=1920, height=1000)
        self.canvas.pack()

        # Background Image
        self.set_bg_img = ImageTk.PhotoImage(Image.open("images/first_page.png").resize((1920, 1000)))
        self.bg_img_canvas = self.canvas.create_image(0, 0, image=self.set_bg_img, anchor=ctk.NW)
       
        # Log In Button (Left Side)
        self.login_img_tk = ImageTk.PhotoImage(Image.open("images/login_button.png").resize((490, 120)))
        self.login_button = self.canvas.create_image(490, 820, image=self.login_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_button, "<Button-1>", self.login)

        # Sign Up Button (Right Side)
        self.signup_img_tk = ImageTk.PhotoImage(Image.open("images/sign_up_button.png").resize((490, 120)))
        self.signup_button = self.canvas.create_image(1000, 820, image=self.signup_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.signup_button, "<Button-1>", self.signup)

        # Exit Button (Top-Right Corner)
        self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
        self.exit_button = self.canvas.create_image(1845, 3, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())
 
        self.update_timer()

    def update_timer(self):
        self.canvas.after(1000, self.ad_page)

    def ad_page(self):
        self.canvas.delete("all")
        self.ads_img = ImageTk.PhotoImage(Image.open("images/ads_page.png").resize((1920, 1000)))
        self.canvas.create_image(0, 0, image=self.ads_img, anchor=ctk.NW)

        self.close_img_tk = ImageTk.PhotoImage(Image.open("images/close_button.png").resize((50, 50)))
        self.close_button = self.canvas.create_image(1380, 180, image=self.close_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.close_button, "<Button-1>", self.back)

    def back(self, event):
        self.canvas.delete("all")

        self.set_bg_img = ImageTk.PhotoImage(Image.open("images/first_page.png").resize((1920, 1000)))
        self.bg_img_canvas = self.canvas.create_image(0, 0, image=self.set_bg_img, anchor=ctk.NW)

        # # Log In Button (Left Side)
        self.login_img_tk = ImageTk.PhotoImage(Image.open("images/login_button.png").resize((490, 120)))
        self.login_button = self.canvas.create_image(490, 820, image=self.login_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.login_button, "<Button-1>", self.login)

        # # Sign Up Button (Right Side)
        self.signup_img_tk = ImageTk.PhotoImage(Image.open("images/sign_up_button.png").resize((490, 120)))
        self.signup_button = self.canvas.create_image(1000, 820, image=self.signup_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.signup_button, "<Button-1>", self.signup)

        # # Exit Button (Top-Right Corner)
        self.exit_img_tk = ImageTk.PhotoImage(Image.open("images/x_button.png").resize((64, 64)))
        self.exit_button = self.canvas.create_image(1845, 3, image=self.exit_img_tk, anchor=ctk.NW, tag=self.tagname)
        self.canvas.tag_bind(self.exit_button, "<Button-1>", self.exit)

        self.canvas.tag_bind(self.tagname, "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind(self.tagname, "<Leave>", lambda event: self.leave())

    def exit(self, event):
        self.destroy()

    def login(self, event):
        self.canvas.destroy()
        login_page = Login(self)
        login_page.pack(fill=ctk.BOTH, expand=True)

    def signup(self, event):
        self.canvas.destroy()
        login_page = SignUp(self)
        login_page.pack(fill=ctk.BOTH, expand=True)

if __name__ == "__main__":
    app = ShopeeLengke()
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.geometry("%dx%d+0+0" % (w, h))
    app.mainloop()