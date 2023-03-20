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
        #cust ref##
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #mother name
        lblmname=Label(labelframeleft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width="29")
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female")
        combo_gender.current()
        combo_gender.grid(row=3, column=1)

        #postcode
        lblPostCode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        #mobilenumber
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelfromleft,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        #nationality
        lbNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Ugandan","American")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        #idproof type combobox
        lblIdproof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Bank Card","Driving License", "National ID", "Passport", "Other")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)


        #id number
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)
        
        ###btns####
        btn_frame=frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Dekete",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        #===table frame===
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)









if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()