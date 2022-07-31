from tkinter import *
from tkinter import ttk

# for background image
from PIL import Image, ImageTk # pip install pillow

# for error messages
from tkinter import messagebox
from colorama import Cursor

# sql connector
import mysql.connector



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
        btn_2 = Button(frame, text = "Go to Login", font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "green", activeforeground="white", activebackground="green")
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
            messagebox.showerror("Error", "All fields are required")
        elif pass_ != conpass_:
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        elif check_ == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
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
                messagebox.showerror("Error", "User already exists. Try with different mail!!")
            else:
                # inserting data into DB
                sql_q2 = "INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)"
                values_q2 = (fname, lname, contact, email, securityQ, securityA, pass_)

                my_cursor.execute(sql_q2, values_q2)
                conn.commit()
                conn.close()

                # showing message
                messagebox.showinfo("Success", "Registered Successfully")

        

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
