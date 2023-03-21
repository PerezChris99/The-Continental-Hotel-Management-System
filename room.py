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
        self.root.geometry("1285x530+210+200")

if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
    