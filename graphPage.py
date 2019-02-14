import tkinter as tk
from tkinter import *
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import settings

Data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
        'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
       }
  
df2 = DataFrame(Data2,columns=['Year','Unemployment_Rate'])
df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()

class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mainLabel = Label(self, text=settings.languageList[7][settings.language])
        self.mainLabel.config(font=("Times", 22, 'bold'))
        self.mainLabel.grid(row=0, columnspan=2, padx=20)

        figure2 = plt.Figure(figsize=(4,2), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self)
        line2.get_tk_widget().grid(row=2, columnspan=2, pady=20)
        df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('Speed Vs. Time')

        self.progress_label = Label(self, text=settings.languageList[1][settings.language])
        self.progress_label.config(font=("Times", 18))
        self.progress_label.grid(sticky=W, row=3, column=0, padx=13)

        self.csvButton = Button(self, borderwidth=5, text=settings.languageList[9][settings.language], command=self.csvExport, bg="green")
        self.csvButton.config(font=("Times", 18))
        self.csvButton.grid(sticky=E, row=4, column=1,pady=5)

        self.returnButton = Button(self, text=settings.languageList[8][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("StartPage"))
        self.returnButton.config(font=("Times", 18))
        self.returnButton.grid(sticky=W, row=4, column=0,pady=5)

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
