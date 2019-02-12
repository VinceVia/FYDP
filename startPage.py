import tkinter as tk
from tkinter import *
import settings
import graphPage

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.label = Label(self, text=settings.languageList[0][settings.language])
        self.label.config(font=("Times", 70, 'bold'))
        self.label.grid(row=0, column=0, padx=20)
        
        self.progress_label = Label(self, text=settings.languageList[1][settings.language])
        self.progress_label.config(font=("Times", 30))
        self.progress_label.grid(row=1, column=0)
        
        self.results_link = Button(self, text=settings.languageList[2][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("GraphPage"))
        self.results_link.config(font=("Times", 30, "italic"))
        self.results_link.grid(row=2, column=0)

        self.start_button = Button(self, borderwidth=5, padx=16, text=settings.languageList[3][settings.language], command=self.start, bg="green")
        self.start_button.config(font=("Times", 40, 'bold'))
        self.start_button.grid(sticky=W, row=3, column=0, padx=40)

        self.stop_button = Button(self, borderwidth=5, padx=16, text=settings.languageList[4][settings.language], command=self.stop, bg="red")
        self.stop_button.config(font=("Times", 40, 'bold'))
        self.stop_button.grid(sticky=E, row=3, column=0, padx=40)
        
        self.previous_results = Button(self, text=settings.languageList[5][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("GraphPage"))
        self.previous_results.config(font=("Times", 30, "italic"))
        self.previous_results.grid(sticky=W, row=4, column=0, padx=40)
        
        self.quit = Button(self, text=settings.languageList[6][settings.language], fg="blue", relief="flat", command=self.quit)
        self.quit.config(font=("Times", 30, "italic"))
        self.quit.grid(sticky=W, row=5, column=0, padx=40)
        
        self.EN_button = Radiobutton(self, text="EN", indicatoron = 0, value=0, command=self.setEnglish)
        self.EN_button.config(font=("Times", 20, 'bold'))
        self.EN_button.grid(sticky=E, row=4, column=0, padx=40)
        
        self.FR_button = Radiobutton(self, text="FR", indicatoron = 0, value=1, command=self.setFrench)
        self.FR_button.config(font=("Times", 20, 'bold'))
        self.FR_button.grid(sticky=E, row=5, column=0, padx=40)

    def start(self):
        print("Starting!")
    
    def stop(self):
        print("Stopping!")
            
    def viewResults(self):
        print("Results!")
        
    def returning(self):
        print("Returning!")

    def setEnglish(self):
        settings.language = 1
        self.setLanguage()

    def setFrench(self):
        settings.language = 2
        self.setLanguage()

    def setLanguage(self):
        self.label.configure(text=settings.languageList[0][settings.language])
        self.progress_label.configure(text=settings.languageList[1][settings.language])
        self.results_link.configure(text=settings.languageList[2][settings.language])
        self.start_button.configure(text=settings.languageList[3][settings.language])
        self.stop_button.configure(text=settings.languageList[4][settings.language])
        self.previous_results.configure(text=settings.languageList[5][settings.language])
        self.quit.configure(text=settings.languageList[6][settings.language])
