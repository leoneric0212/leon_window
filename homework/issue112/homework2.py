import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("300x200")

        ttk.Button(self,text='頭').pack()

        ttk.Button(self,text='肩').pack(fill='x')

        ttk.Button(self,text='腰').pack(fill='both',expand=1)

        ttk.Button(self,text='臀').pack(fill='x')

        ttk.Button(self,text='腳').pack()
if __name__ == '__main__':
    window:Window=Window()
    window.mainloop()