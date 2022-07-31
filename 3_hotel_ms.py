from tkinter import *
from PIL import Image, ImageTk
from customer import Customer_window


class Hotel_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ---------------------- Top 1st background image
        img1 = Image.open(r"Images\\3_HMS\\1_top_bg.jpg")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # creating label
        lblimg = Label(self.root, image=self.photoimg1, bd = 4, relief=RIDGE)
        lblimg.place(x = 0, y = 0, width = 1550, height=140)

        #---------------------- Logo
        img2 = Image.open(r"Images\\3_HMS\\2_Logo.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # creating label
        lblimg2 = Label(self.root, image=self.photoimg2, bd = 4, relief=RIDGE)
        lblimg2.place(x = 0, y = 0, width = 230, height=140)

        # ---------------------- Title
        lbl_title = Label(self.root, text = "HOTEL MANAGEMENT SYSTEM", font = ("times new roman", 40, "bold"), bg = "black", fg = "gold", bd = 4, relief=RIDGE)
        lbl_title.place(x = 0, y = 140, width=1550, height=50)

        # ----------------------- Creating main frame
        main_frame = Frame(self.root, bd = 4, relief=RIDGE)
        main_frame.place(x = 0, y = 190, width=1550, height=620)

        # ----------------------- Menu
        lbl_menu = Label(main_frame, text = "MENU", font = ("times new roman", 20, "bold"), bg = "black", fg = "gold", bd = 4, relief=RIDGE)
        lbl_menu.place(x = 0, y = 0, width=230)

        # ----------------------- Button frame
        btn_frame = Frame(main_frame, bd = 4, relief=RIDGE)
        btn_frame.place(x = 0, y = 35, width=230, height=190)

        # creating buttons
        cus_btn = Button(btn_frame, command=self.customer_win, text = "Customers", width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor="hand1")
        cus_btn.grid(row = 0, column=0, pady=1)

        room_btn = Button(btn_frame, text = "Room", width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor="hand1")
        room_btn.grid(row = 1, column=0, pady=1)

        detail_btn = Button(btn_frame, text = "Details", width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor="hand1")
        detail_btn.grid(row = 2, column=0, pady=1)

        report_btn = Button(btn_frame, text = "Report", width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor="hand1")
        report_btn.grid(row = 3, column=0, pady=1)

        logout_btn = Button(btn_frame, text = "Log Out", width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor="hand1")
        logout_btn.grid(row = 4, column=0, pady=1)


        # ------------------------------- Right side image
        img3 = Image.open(r"Images\\3_HMS\\3_Right_img.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # creating label
        lblimg3 = Label(main_frame, image=self.photoimg3, bd = 4, relief=RIDGE)
        lblimg3.place(x = 225, y = 0, width = 1310, height=590)

        # -------------------------------- Down image
        img4 = Image.open(r"Images\\3_HMS\\4_Down_1.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # creating label
        lblimg4 = Label(main_frame, image=self.photoimg4, bd = 4, relief=RIDGE)
        lblimg4.place(x = 0, y = 225, width = 230, height=210)

        img5 = Image.open(r"Images\\3_HMS\\5_Down_2.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # creating label
        lblimg5 = Label(main_frame, image=self.photoimg5, bd = 4, relief=RIDGE)
        lblimg5.place(x = 0, y = 420, width = 230, height=190)


    # calling function when customer button is clicked
    def customer_win(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_window(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Hotel_Management_System(root)
    root.mainloop()
