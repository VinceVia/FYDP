#!/usr/bin/python3
from tkinter import *
#import tkFont
import tkinter as tk

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("MWX GUI")

        self.label = Label(master, text="MWX Sensor Test Bench")
        self.label.config(font=("Times", 70, 'bold'))
        self.label.grid(row=0, column=0, padx=20)
        
        self.progress_label = Label(master, text="Test Status:")
        self.progress_label.config(font=("Times", 30))
        self.progress_label.grid(row=1, column=0)
        
        self.results_link = Button(master, text="View Test Results", fg="blue", relief="flat", command=self.viewResults)
        self.results_link.config(font=("Times", 30, "italic"))
        self.results_link.grid(row=2, column=0)

        self.start_button = Button(master, borderwidth=5, padx=16, text="Start", command=self.start, bg="green")
        self.start_button.config(font=("Times", 40, 'bold'))
        self.start_button.grid(sticky=W, row=3, column=0, padx=40)

        self.stop_button = Button(master, borderwidth=5, padx=16, text="Stop", command=self.stop, bg="red")
        self.stop_button.config(font=("Times", 40, 'bold'))
        self.stop_button.grid(sticky=E, row=3, column=0, padx=40)
        
        self.previous_results = Button(master, text="Return To The Previous Test", fg="blue", relief="flat", command=self.returning)
        self.previous_results.config(font=("Times", 30, "italic"))
        self.previous_results.grid(sticky=W, row=4, column=0, padx=40)
        
        self.quit = Button(master, text="Quit Program", fg="blue", relief="flat", command=master.quit)
        self.quit.config(font=("Times", 30, "italic"))
        self.quit.grid(sticky=W, row=5, column=0, padx=40)
        
        self.EN_button = Radiobutton(master, text="EN", indicatoron = 0, variable=v, value=1, command=self.showChoice)
        self.EN_button.config(font=("Times", 20, 'bold'))
        self.EN_button.grid(sticky=E, row=5, column=0, padx=40)
        
        self.FR_button = Radiobutton(master, text="FR", indicatoron = 0, variable=v, value=0, command=self.showChoice)
        self.FR_button.config(font=("Times", 20, 'bold'))
        self.FR_button.grid(sticky=E, row=6, column=0, padx=40)
      

    def start(self):
        print("Starting!")
        
    def stop(self):
        print("Stopping!")
        
    def viewResults(self):
        print("Results!")
        
    def returning(self):
        print("Returning!")
        
    def showChoice(self):
        print(v.get())
       


root = Tk()
v = tk.IntVar()
my_gui = MyFirstGUI(root)
root.mainloop()
