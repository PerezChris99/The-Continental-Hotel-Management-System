from tkinter import*
from PIL import ImageTk, Image


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
      
        ####image#####
        img1=Image.open(r"images/img1.jpg")
        img1=img1.resize((1550, 140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        Ibling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        Ibling.place(x=0,y=0, width=1550,height=140)

        ####logo####
        img2=Image.open(r"images/logo.jpg")
        img2=img2.resize((230, 140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Ibling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Ibling.place(x=0,y=0, width=230,height=140)

        ###title####
        lbl_title=Label(self.root,text="CONTINENTAL HOTEL MGT SYS",font=("Times New Roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        ##main frame##
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        ######menu######
        lbl_menu=Label(main_frame,text="MENU",font=("Times New Roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)




if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()