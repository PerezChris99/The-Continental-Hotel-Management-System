from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
#import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        ###title####
        lbl_title=Label(self.root,text="ROOM",font=("Times New Roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ####logo####
        img2=Image.open(r"images/logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Ibling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Ibling.place(x=5,y=2, width=100,height=40)

        ###labelframe####
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room BookingDetails",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #customer contact##
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29,state="readonly")
        entry_contact.grid(row=0,column=1)

        #check in date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_In Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #check out date
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        #Room type


if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
