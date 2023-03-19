from tkinter import*
from PIL import Image,ImageTk


class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        ###title####
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1295,height=50)

        ####logo####
        img2=Image.open(r"images/logo.jpg")
        img2=img2.resize((230, 140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        Ibling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        Ibling.place(x=0,y=0, width=230,height=140)



if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()