import tkinter as tk
from tkinter import *
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import settings

Data2 = {'Time': [10,20,30,40,50,60,70,80,90,100],
        'Speed': [10,30,50,60,70,90,100,60,30,0]
       }
  
df2 = DataFrame(Data2,columns=['Time','Speed'])
df2 = df2[['Time', 'Speed']].groupby('Time').sum()

class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainLabel = Label(self, text=settings.languageList[7][settings.language])
        self.mainLabel.config(font=("Times", 22, 'bold'))
        self.mainLabel.grid(sticky=E+W, row=0, columnspan=2, padx=20)

        figure2 = plt.Figure(figsize=(4,2), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self)
        line2.get_tk_widget().grid(sticky=E+W, row=2, columnspan=2, pady=10)
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('Speed Vs. Time')

        self.progress_label = Label(self, text=settings.languageList[1][settings.language])
        self.progress_label.config(font=("Times", 18))
        self.progress_label.grid(sticky=W, row=3, column=0, columnspan=2, padx=20)

        self.returnButton = Button(self, text=settings.languageList[8][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("StartPage"))
        self.returnButton.config(font=("Times", 18))
        self.returnButton.grid(sticky=W, row=4, column=0, pady=5, padx=20)

        self.csvButton = Button(self, borderwidth=5, text=settings.languageList[9][settings.language], command=self.csvExport, bg="green")
        self.csvButton.config(font=("Times", 18))
        self.csvButton.grid(row=4, column=1, pady=5, padx=0)

    def csvExport(self):
        print("Exporting!")

    def setEnglish(self):
        settings.language = 1
        self.setLanguage()

    def setFrench(self):
        settings.language = 2
        self.setLanguage()

    def setLanguage(self):
        self.mainLabel.configure(text=settings.languageList[7][settings.language])
        self.progress_label.configure(text=settings.languageList[1][settings.language])
        self.csvButton.configure(text=settings.languageList[9][settings.language])
        self.returnButton.configure(text=settings.languageList[8][settings.language])
