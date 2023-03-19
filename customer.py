from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1285x540+220+210")

        ###title####
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ####logo####
        img2=Image.open(r"images/logo.jpg")
        img2=img2.resize((100, 40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Ibling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        Ibling.place(x=5,y=2, width=100,height=40)

        ###labelframe####
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        ####labels and entry###
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtname.grid(row=1,column=1)
        


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()