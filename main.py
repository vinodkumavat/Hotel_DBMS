import email
from tkinter import *
from tkinter import ttk

# for background image
from PIL import Image, ImageTk # pip install pillow

# for error messages
from tkinter import messagebox

# sql connector
import mysql.connector


def main_():
    win = Tk()
    app = login_window(win)
    win.mainloop()



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


        # register new-user when clicked go to register_window function
        register_bt = Button(frame, command=self.register_window, text = "New user register", font = ("times new roman", 10, "bold"), borderwidth=0, fg = "white", bg = "black", activeforeground="white", activebackground="black")
        register_bt.place(x = 15, y = 350, width= 160)

        # Forget password when clicked go to forgot_password_window function
        f_pass_bt = Button(frame, command=self.forgot_password_window , text = "Forget Password", font = ("times new roman", 10, "bold"), borderwidth=0, fg = "white", bg = "black", activeforeground="white", activebackground="black")
        f_pass_bt.place(x = 10, y = 370, width= 160)


    # for directing to register window
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    # For validating and login
    def login(self):
        # get data from text username
        txt_username = self.txtuser.get()
        txt_password = self.txtpass.get()

        # validating data
        if txt_username == "" or  txt_password == "":
            # if anyone of the field is empty
            messagebox.showerror("Error", "All Fields are required")
        elif txt_username == "root" and txt_password == "vinod":
            # if both are correct
            messagebox.showinfo("Success", "Login Successful")
        else:
            # connecting mysql
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "vinod_sql"
            )
            my_cursor = conn.cursor()
            # getting email & password from DB
            sql_q = ("SELECT * FROM register WHERE email = %s AND password = %s")
            value_sql_1 = (txt_username, txt_password)
            my_cursor.execute(sql_q, value_sql_1)
            
            # store data in variable
            row = my_cursor.fetchone()
            # validating user entered data from DB
            if row == None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("Yes No", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel()
                    # opening the hotel system
                    self.app = Hotel_Management_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
        


    # to create forgot password window
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter username")
        else:
            # connecting mysql
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "vinod_sql"
            )
            my_cursor = conn.cursor()
            # getting username from DB
            query_ = ("SELECT * FROM register WHERE email = %s")
            values_ = (self.txtuser.get(),)
            my_cursor.execute(query_, values_)
            # store in variable
            row = my_cursor.fetchone()
            # close mysql connection
            conn.close()

            # print(row) # Returns if data is matching --> ('vinod', 'kumavat', '883031146', 'vinodkumawat17378@gmail.com', 'Your GF name', 'Imaginary', '789')
            if row == None:
                messagebox.showerror("Error", "Username is not present")
            else:
                # creating forgot password window
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                # creating label
                lbl = Label(self.root2, text = "Forgot Password", font = ("times new roman", 20, "bold"), fg = "orange", bg = "black")
                lbl.place(x = 0, y = 10, relwidth = 1)

                # adding security Q&A, new password, submit button --> copy from register class
                security_q = Label(self.root2, text = "Select Security Question", font = ("times new roman", 15, "bold"), bg = "white")
                security_q.place(x = 50, y = 80)

                self.combo_security_Q = ttk.Combobox(self.root2, font = ("times new roman", 15), state = "readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your GF name", "Your Pet name")
                self.combo_security_Q.place(x = 50, y = 110, width=250)
                self.combo_security_Q.current(0)

                security_a = Label(self.root2, text = "Security Answer", font = ("times new roman", 15, "bold"), bg = "white")
                security_a.place(x = 50, y = 150)

                self.txt_security_a = ttk.Entry(self.root2, font = ("times new roman", 15))
                self.txt_security_a.place(x = 50, y = 180, width=250)

                new_pass = Label(self.root2, text = "New Password", font = ("times new roman", 15, "bold"), bg = "white")
                new_pass.place(x = 50, y = 220)

                self.txt_new_pass = ttk.Entry(self.root2, font = ("times new roman", 15))
                self.txt_new_pass.place(x = 50, y = 250, width=250)

                # on submitting call reset_password function
                btn_1 = Button(self.root2, command=self.reset_password, text = "Reset Password", font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "green", activeforeground="white", activebackground="green")
                btn_1.place(x = 100, y = 300, width= 150, height=35)




    # to reset password from forgot password window
    def reset_password(self):
        # getting into varibale
        username_ = self.txtuser.get()
        securityQ = self.combo_security_Q.get()
        securityA = self.txt_security_a.get()
        new_pass = self.txt_new_pass.get()

        # validating from frontend
        if securityQ == "Select":
            messagebox.showerror("Error", "All fields are required", parent = self.root2)
        elif securityA == "":
            messagebox.showerror("Error", "Please enter the answer", parent = self.root2)
        elif new_pass == "":
            messagebox.showerror("Error", "Please enter new password", parent = self.root2)
        else:
            # messagebox.showinfo("Success", "Welcome Bro!!")
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "vinod_sql"
            )
            my_cursor = conn.cursor()


            # checking for email, securityA already there or not
            sql_q1 = ("SELECT * FROM register WHERE email = %s AND securityQ = %s AND securityA = %s")
            value_q1 = (username_, securityQ, securityA)

            my_cursor.execute(sql_q1, value_q1)
            row = my_cursor.fetchone()

            if row == None:
                # validing from BD
                messagebox.showerror("Error", "Please enter the correct security answer", parent = self.root2)
            else:
                # UPDATE data into DB
                sql_q2 = "UPDATE register SET password = %s WHERE email = %s"
                values_q2 = (new_pass, username_)

                my_cursor.execute(sql_q2, values_q2)
                conn.commit()
                conn.close()

                # showing message
                messagebox.showinfo("Success", "Password updated succesfully", parent = self.root2)

                # destroy the root2 window i.e. reset password window
                self.root2.destroy()





# ------------------------------- Register Class ------------------------------
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("New Register")
        self.root.geometry("1536x864+0+0")


        # creating varibales to get data from user. Will need to insert them into Entry field
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()


        # creating background image
        self.bg = ImageTk.PhotoImage(file = r"Images\\2_New Register\\1_Background.jpg")
        # create label
        lbl_bg = Label(self.root, image = self.bg)
        # place the bg image
        lbl_bg.place(x = 0, y = 0, relwidth=1, relheight=1)


        # creating left sided image
        bg1 = Image.open(r"Images\\2_New Register\\2_Frame.jpg")
        # resizing
        bg1 = bg1.resize((470, 550), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(bg1)
        # create label
        lbl_left = Label(self.root, image = self.bg1)
        # place the bg image
        lbl_left.place(x = 50, y = 100, width=470, height=550)


        # creating frame
        frame = Frame(self.root, bg = 'white')
        frame.place(x = 520, y = 100, width= 800, height= 550)


        # creating label in frame --> Register Here
        register_lbl = Label(frame, text = "REGISTER HERE", font = ("times new roman", 20, "bold"), fg = "green", bg = "white")
        register_lbl.place(x = 20, y = 20)


        # Creating Form i.e. entry and labels
        # -----------------------------> Row - 1
        fname = Label(frame, text = "First Name", font = ("times new roman", 15, "bold"), bg = "white")
        fname.place(x = 50, y = 100)

        self.txt_fname = ttk.Entry(frame, textvariable = self.var_fname, font = ("times new roman", 15, "bold"))
        self.txt_fname.place(x = 50, y = 130, width=250)

        lname = Label(frame, text = "Last Name", font = ("times new roman", 15, "bold"), bg = "white")
        lname.place(x = 370, y = 100)
        
        self.txt_lname = ttk.Entry(frame, textvariable = self.var_lname, font = ("times new roman", 15))
        self.txt_lname.place(x = 370, y = 130, width=250)

        
        # -----------------------------> Row - 2
        contact = Label(frame, text = "Contact No.", font = ("times new roman", 15, "bold"), bg = "white")
        contact.place(x = 50, y = 170)

        self.txt_contact = ttk.Entry(frame, textvariable = self.var_contact, font = ("times new roman", 15))
        self.txt_contact.place(x = 50, y = 200, width=250)

        email = Label(frame, text = "Email", font = ("times new roman", 15, "bold"), bg = "white")
        email.place(x = 370, y = 170)
        
        self.txt_email = ttk.Entry(frame, textvariable = self.var_email, font = ("times new roman", 15))
        self.txt_email.place(x = 370, y = 200, width=250)


        # -----------------------------> Row - 3
        security_q = Label(frame, text = "Select Security Question", font = ("times new roman", 15, "bold"), bg = "white")
        security_q.place(x = 50, y = 240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable = self.var_securityQ, font = ("times new roman", 15), state = "readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your GF name", "Your Pet name")
        self.combo_security_Q.place(x = 50, y = 270, width=250)
        self.combo_security_Q.current(0)

        security_a = Label(frame, text = "Security Answer", font = ("times new roman", 15, "bold"), bg = "white")
        security_a.place(x = 370, y = 240)

        self.txt_security_a = ttk.Entry(frame, textvariable = self.var_securityA, font = ("times new roman", 15))
        self.txt_security_a.place(x = 370, y = 270, width=250)


        # -----------------------------> Row - 4
        pswd = Label(frame, text = "Password", font = ("times new roman", 15, "bold"), bg = "white")
        pswd.place(x = 50, y = 310)

        self.txt_pswd = ttk.Entry(frame, textvariable = self.var_pass, font = ("times new roman", 15))
        self.txt_pswd.place(x = 50, y = 340, width=250)

        confirm_pswd = Label(frame, text = "Confirm Password", font = ("times new roman", 15, "bold"), bg = "white")
        confirm_pswd.place(x = 370, y = 310)
        
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable = self.var_confpass, font = ("times new roman", 15))
        self.txt_confirm_pswd.place(x = 370, y = 340, width=250)


        # -----------------------------> Row - 5 (Check Button)
        check_btn = Checkbutton(frame, variable = self.var_check, text = "I agree to all the terms and conditions", font = ("times new roman", 12, "bold"), bg = "white", onvalue=1, offvalue=0)
        check_btn.place(x = 50, y = 380)


        # register now button when clicked go to submit function
        btn_1 = Button(frame, command = self.register_data, text = "Register Now", font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "green", activeforeground="white", activebackground="green")
        btn_1.place(x = 50, y = 420, width= 120, height=35)


        # back to login button when clicked go to submit function
        btn_2 = Button(frame, command=self.return_logIn,text = "Go to Login", font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "green", activeforeground="white", activebackground="green")
        btn_2.place(x = 370, y = 420, width= 120, height=35)



    # vaidating data and insert into DB
    def register_data(self):
        # getting into varibale
        fname = self.var_fname.get()
        lname = self.var_lname.get()
        contact = self.var_contact.get()
        email = self.var_email.get()
        securityQ = self.var_securityQ.get()
        securityA = self.var_securityA.get()
        pass_ = self.var_pass.get()
        conpass_ = self.var_confpass.get()
        check_ = self.var_check.get()

        # validating from frontend
        if fname == "" or email == "" or securityQ == "Select":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        elif pass_ != conpass_:
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent = self.root)
        elif check_ == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions", parent = self.root)
        else:
            # messagebox.showinfo("Success", "Welcome Bro!!")
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "vinod_sql"
            )
            my_cursor = conn.cursor()


            # checking for email already there or not
            sql_q1 = ("SELECT * FROM register WHERE email = %s")

            my_cursor.execute(sql_q1, (email, ))
            row = my_cursor.fetchone()

            if row != None:
                # validing from BD
                messagebox.showerror("Error", "User already exists. Try with different mail!!", parent = self.root)
            else:
                # inserting data into DB
                sql_q2 = "INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)"
                values_q2 = (fname, lname, contact, email, securityQ, securityA, pass_)

                my_cursor.execute(sql_q2, values_q2)
                conn.commit()
                conn.close()

                # showing message
                messagebox.showinfo("Success", "Registered Successfully", parent = self.root)



    # return to logIn page when login button is pressed
    def return_logIn(self):
        # closing new resitered window
        self.root.destroy()


# ------------------------------- Hotel Management Class ------------------------------
class Hotel_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1536x864+0+0")


if __name__ == "__main__":
    main_()