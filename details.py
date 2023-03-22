from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
#import mysql.connector
from tkinter import messagebox


class RoomDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
      
        ###title####
        lbl_title=Label(self.root,text="ROOM DETAILS",font=("Times New Roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ####logo####
        img2=Image.open(r"images/logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Ibling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Ibling.place(x=5,y=2, width=100,height=40)

        ###labelframe####
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #Floor##
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        entry_floor=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room Number##
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        entry_RoomNo=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=20)
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type##
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        entry_RoomType=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=20)
        entry_RoomType.grid(row=2,column=1,sticky=W)

        ###btns####
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        #===table frame search system===
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="CheckIn")
        self.room_table.heading("checkout",text="CheckOut")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        

if __name__=="__main__":
    root=Tk()
    obj=RoomDetails(root)
    root.mainloop()