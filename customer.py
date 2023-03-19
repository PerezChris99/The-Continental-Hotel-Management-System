from tkinter import*

class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+0+0")

if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()