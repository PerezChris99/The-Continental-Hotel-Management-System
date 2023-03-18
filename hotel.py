from tkinter import*

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()