import imp
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

import random
import mysql.connector
from tkinter import messagebox


class Customer_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1295x550+230+220")

        # ------------------------------------ declaring variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_father = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_country = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()


        # ---------------------- Title
        lbl_title = Label(self.root, text = "Add Customer Detail", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold", bd = 4, relief=RIDGE)
        lbl_title.place(x = 0, y = 0, width=1295, height=50)

        #---------------------- Logo
        img1 = Image.open(r"Images\\3_HMS\\2_Logo.jpg")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)


        # creating label
        lblimg1 = Label(self.root, image=self.photoimg1, bd = 1, relief=RIDGE)
        lblimg1.place(x = 4, y = 1, width = 100, height=48)


        # ----------------------- Label Frame
        label_frame_left = LabelFrame(self.root, bd = 2, relief=RIDGE, text="Customer Detials", font = ("times new roman", 12, "bold"), pady=1)
        label_frame_left.place(x = 0, y = 50, width=425, height=490)


        # ----------------------- Labels and entry
        # cust_ref
        lbl_cust_ref = Label(label_frame_left, text="Customer Ref:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row = 0, column=0, sticky=W)
        entry_ref = ttk.Entry(label_frame_left, textvariable=self.var_ref, width=29, font = ("arial", 13), state="readonly")
        entry_ref.grid(row=0, column=1)

        # cust_name
        cname = Label(label_frame_left, text="Customer Name:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        cname.grid(row = 1, column=0, sticky=W)
        txt_name = ttk.Entry(label_frame_left, textvariable=self.var_cust_name, width=29, font = ("arial", 13))
        txt_name.grid(row=1, column=1)

        # cust father name
        lbl_mname = Label(label_frame_left, text="Father Name:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row = 2, column=0, sticky=W)
        txtfname = ttk.Entry(label_frame_left, textvariable=self.var_father, width=29, font = ("arial", 13))
        txtfname.grid(row=2, column=1)

        # gender combo box
        label_gender = Label(label_frame_left, text="Gender:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(label_frame_left, textvariable=self.var_gender, font = ("arial", 12), width = 27, state = "readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        lbl_postCode = Label(label_frame_left, text="PostCode", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_postCode.grid(row = 4, column=0, sticky=W)
        txtPostCode = ttk.Entry(label_frame_left, textvariable=self.var_post, width=29, font = ("arial", 13))
        txtPostCode.grid(row=4, column=1)

        # mobile number
        lbl_Mobile = Label(label_frame_left, text="Mobile No.:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Mobile.grid(row = 5, column=0, sticky=W)
        txtMobile = ttk.Entry(label_frame_left, textvariable=self.var_mobile, width=29, font = ("arial", 13))
        txtMobile.grid(row=5, column=1)

        # email
        lbl_Email = Label(label_frame_left, text="Email", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Email.grid(row = 6, column=0, sticky=W)
        txtEmail = ttk.Entry(label_frame_left, textvariable=self.var_email, width=29, font = ("arial", 13))
        txtEmail.grid(row=6, column=1)

        # Nationality combo box
        label_Country = Label(label_frame_left, text="Country", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        label_Country.grid(row=7, column=0, sticky=W)
        combo_Country = ttk.Combobox(label_frame_left, textvariable=self.var_country, font = ("arial", 12), width = 27, state = "readonly")
        combo_Country["value"] = ("India", "USA", "UK", "Russia", "Chine", "Other")
        combo_Country.current(0)
        combo_Country.grid(row=7, column=1)

        # Id Proof type combo box
        label_IdProof = Label(label_frame_left, text="Id Proof Type:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        label_IdProof.grid(row=8, column=0, sticky=W)
        combo_IdProof = ttk.Combobox(label_frame_left, textvariable=self.var_id_proof, font = ("arial", 12), width = 27, state = "readonly")
        combo_IdProof["value"] = ("Aadhar Card", "PAN Card", "License", "Voter Id")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8, column=1)

        # id number
        lbl_IdNumber = Label(label_frame_left, text="Id Number:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_IdNumber.grid(row = 9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(label_frame_left, textvariable=self.var_id_number, width=29, font = ("arial", 13))
        txtIdNumber.grid(row=9, column=1)

        # address
        lbl_Address = Label(label_frame_left, text="Address:", font = ("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Address.grid(row = 10, column=0, sticky=W)
        txtAddress = ttk.Entry(label_frame_left, textvariable=self.var_address, width=29, font = ("arial", 13))
        txtAddress.grid(row=10, column=1)


        # --------------------------------- Buttons 
        btn_frame = Frame(label_frame_left, bd=2, relief=RIDGE)
        btn_frame.place(x = 0, y = 400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width=9)
        btnAdd.grid(row=0, column=0, padx = 1)

        btnUpdate = Button(btn_frame, text="Update", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width=9)
        btnUpdate.grid(row=0, column=1, padx = 1)

        btnDelete = Button(btn_frame, text="Delete", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width=9)
        btnDelete.grid(row=0, column=2, padx = 1)

        btnReset = Button(btn_frame, text="Reset", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width=9)
        btnReset.grid(row=0, column=3, padx = 1)


        # --------------------------------- Table frame on the right of Customer details
        table_frame = LabelFrame(self.root, bd = 2, relief=RIDGE, text="View Details and Search", font = ("times new roman", 12, "bold"), pady=1)
        table_frame.place(x = 435, y = 50, width=860, height=490)

        # Search by option
        lbl_SearchBy = Label(table_frame, text="Search By:", font = ("times new roman", 12, "bold"), bg = "red", fg = "white")
        lbl_SearchBy.grid(row = 0, column=0, sticky=W, padx = 2)

        combo_Search = ttk.Combobox(table_frame, font = ("arial", 12), width = 24, state = "readonly")
        combo_Search["value"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx = 2)

        # to get text
        txtSearch = ttk.Entry(table_frame, width=29, font = ("arial", 13))
        txtSearch.grid(row=0, column=2, padx = 2)

        # submit button
        btnSearch = Button(table_frame, text="Search", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width=9)
        btnSearch.grid(row=0, column=3, padx = 1)

        btnShowAll = Button(table_frame, text="Show All", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width=9)
        btnShowAll.grid(row=0, column=4, padx = 1)

        # ---------------------------------------------- creating table to show the data from DB
        detail_table = Frame(table_frame, bd = 2, relief=RIDGE)
        detail_table.place(x = 0, y = 50, width=860, height=350)

        # create scroll bar if we have large data
        scroll_x = ttk.Scrollbar(detail_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient = VERTICAL)

        self.Cust_Details_Tables = ttk.Treeview(detail_table, column = ("ref", "name", "father", 
                                                                        "gender", "post", "mobile", 
                                                                        "email", "country", "idproof", 
                                                                        "idnumber", "address"), 
                                                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # packing scroll to the buttom of screen and to the right of screen
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_x.pack(side = RIGHT, fill = Y)

        # configure the scroll with the data from DB
        scroll_x.config(command=self.Cust_Details_Tables.xview)
        scroll_y.config(command=self.Cust_Details_Tables.yview)


        # Creating heading of the table
        self.Cust_Details_Tables.heading("ref", text = "Refer No.")
        self.Cust_Details_Tables.heading("name", text = "Name")
        self.Cust_Details_Tables.heading("father", text = "Father Name")
        self.Cust_Details_Tables.heading("gender", text = "Gender")
        self.Cust_Details_Tables.heading("post", text = "Post Code")
        self.Cust_Details_Tables.heading("mobile", text = "Mobile")
        self.Cust_Details_Tables.heading("email", text = "Email")
        self.Cust_Details_Tables.heading("country", text = "Country")
        self.Cust_Details_Tables.heading("idproof", text = "Id Proof")
        self.Cust_Details_Tables.heading("idnumber", text = "Id Number")
        self.Cust_Details_Tables.heading("address", text = "Address")

        # showing heading
        self.Cust_Details_Tables["show"] = "headings"
        
        # adjusting the width of columns
        self.Cust_Details_Tables.column("ref", width=100)
        self.Cust_Details_Tables.column("name", width=100)
        self.Cust_Details_Tables.column("father", width=100)
        self.Cust_Details_Tables.column("gender", width=100)
        self.Cust_Details_Tables.column("post", width=100)
        self.Cust_Details_Tables.column("mobile", width=100)
        self.Cust_Details_Tables.column("email", width=100)
        self.Cust_Details_Tables.column("country", width=100)
        self.Cust_Details_Tables.column("idproof", width=100)
        self.Cust_Details_Tables.column("idnumber", width=100)
        self.Cust_Details_Tables.column("address", width=100)
        
        self.Cust_Details_Tables.pack(fill = BOTH, expand=1)


    # to add data to the DB
    def add_data(self):
        # validating inputs
        if self.var_mobile.get() == "" or self.var_father.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            print("HEllo")




if __name__ == "__main__":
    root = Tk()
    obj = Customer_window(root)
    root.mainloop()