from tkinter import *
from tkinter import ttk

# for background image
from PIL import Image, ImageTk # pip install pillow

# for error messages
from tkinter import messagebox

# sql connector
import mysql.connector



class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1536x864+0+0")

        # creating background image
        self.bg = ImageTk.PhotoImage(file = r"Images\\1_LogIn\\1_Background.jpg")
        # create label
        lbl_bg = Label(self.root, image = self.bg)
        # place the bg image
        lbl_bg.place(x = 0, y = 0, relwidth=1, relheight=1)


        # creating frame
        frame = Frame(self.root, bg = 'Black')
        frame.place(x = 610, y = 170, width= 340, height= 450)


        # Insert image in frame
        img1 = Image.open(r"Images\\1_LogIn\\2_logIn_Icon.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image = self.photoimage1, bg = 'black', borderwidth = 0)
        lbl_img1.place(x = 730, y = 175, width=100, height=100)


        # creating label --> Get Started
        get_str = Label(frame, text = "Get Started", font = ("times new roman", 20, "bold"), fg = "white", bg = "black")
        get_str.place(x = 95, y = 100)


        # creating label for username
        username_lbl = Label(frame, text="Username", font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        username_lbl.place(x = 70, y = 155)

        # input-textbox for username
        self.txtuser = ttk.Entry(frame, font = ("times new roman", 15, "bold"))
        self.txtuser.place(x = 40, y = 180, width=270)


        # creating label for password
        password_lbl = Label(frame, text="Password", font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        password_lbl.place(x = 70, y = 225)

        # input-textbox for password
        self.txtpass = ttk.Entry(frame, font = ("times new roman", 15, "bold"))
        self.txtpass.place(x = 40, y = 250, width=270)


        # insert images before the label for username
        img2 = Image.open(r"Images\\1_LogIn\\2_logIn_Icon.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image = self.photoimage2, bg = 'black', borderwidth = 0)
        lbl_img2.place(x = 650, y = 323, width=25, height=25)

        # insert images before the label for password
        img3 = Image.open(r"Images\\1_LogIn\\3_Password_logo.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image = self.photoimage3, bg = 'black', borderwidth = 0)
        lbl_img3.place(x = 650, y = 395, width=25, height=25)


        # login button when clicked go to login function
        log_in_bt = Button(frame, command=self.login, text = "Login", font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "blue", activeforeground="white", activebackground="blue")
        log_in_bt.place(x = 110, y = 300, width= 120, height=35)


        # register new-user
        register_bt = Button(frame, text = "New user register", font = ("times new roman", 10, "bold"), borderwidth=0, fg = "white", bg = "black", activeforeground="white", activebackground="black")
        register_bt.place(x = 15, y = 350, width= 160)

        # Forget password
        f_pass_bt = Button(frame, text = "Forget Password", font = ("times new roman", 10, "bold"), borderwidth=0, fg = "white", bg = "black", activeforeground="white", activebackground="black")
        f_pass_bt.place(x = 10, y = 370, width= 160)



    # For validating and login
    def login(self):
        # get data from text username
        txt_username = self.txtuser.get()
        txt_password = self.txtpass.get()

        # validating data Default => [username : root, password : vinod]
        if txt_username == "" or  txt_password == "":
            # if anyone of the field is empty
            messagebox.showerror("Error", "All Fields are required")
        elif txt_username == "root" and txt_password == "vinod":
            # if both are correct
            messagebox.showinfo("Success", "Login Successful")
        else:
            # if wrong data is entered
            messagebox.showerror("Error", "Wrong username and password")



if __name__ == "__main__":
    root = Tk()
    app = login_window(root)
    root.mainloop()