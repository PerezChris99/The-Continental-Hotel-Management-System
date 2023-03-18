from tkinter import*
from PIL import ImageTk, Image


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        img1=Image.open(r"images/img1.jpg")
        img1=img1.resize((1550, 140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        Ibling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        Ibling.place(x=0,y=0, width=1550,height=140)




if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()