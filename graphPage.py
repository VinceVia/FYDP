import tkinter as tk
from tkinter import *
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import settings
import detailedResultsDao
import resultByIDDao
import misc

class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.plotGraph()
        self.status = self.getStatus()
        machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number)[0]

        self.progress_label = Label(self, text=settings.languageList[1][settings.language] + ' ' + self.status)
        self.progress_label.config(font=("Arial", 45))
        self.progress_label.grid(sticky=W, row=1, column=0, columnspan=2, pady=5, padx=10)

        if(machine_status == 3):
            self.infoButton = Button(self, borderwidth=5, text=settings.languageList[30][settings.language], command=self.getFailureInfo, bg="green")
            self.infoButton.config(font=("Arial", 45))
            self.infoButton.grid(sticky=E, row=1, column=1, pady=5, padx=10)

        self.returnButton = Button(self, text=settings.languageList[8][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("StartPage"))
        self.returnButton.config(font=("Arial", 45))
        self.returnButton.grid(sticky=W, row=2, column=0, pady=10)

        self.csvButton = Button(self, borderwidth=5, text=settings.languageList[9][settings.language], command=self.csvExport, bg="green")
        self.csvButton.config(font=("Arial", 45))
        self.csvButton.grid(sticky=E, row=2, column=1, pady=5, padx=10)

    def plotGraph(self):
        velocity = detailedResultsDao.DetailedResultsDao.get_velocities(settings.test_number)
        time = detailedResultsDao.DetailedResultsDao.get_times(settings.test_number)

        if(velocity==[] and time==[]):
            velocity = [0]
            time = [0]

        Data = {'Time': time,
                 'Velocity': velocity
                }
        df = DataFrame(Data)

        figure = plt.Figure(figsize=(12,4.5), dpi=60)
        ax = figure.add_subplot(111)
        ax.set_title(settings.languageList[10][settings.language], fontweight="bold", fontsize=16)
        ax.set_xlabel(settings.languageList[12][settings.language])
        ax.set_ylabel(settings.languageList[11][settings.language])
        ax.set_axisbelow(True)
        line = FigureCanvasTkAgg(figure, self)
        line.get_tk_widget().grid(sticky=E+W, row=0, columnspan=2, padx=10)
        ax2 = df.plot(kind='line', y='Velocity', ax=ax, legend=False, fontsize=11)
        ax2.grid()

    def getStatus(self):
        switcher = { 
            0: settings.languageList[13][settings.language], #Ready to Start
            1: settings.languageList[17][settings.language], #In Progress
            2: settings.languageList[16][settings.language], #Stopped
            3: settings.languageList[15][settings.language], #Failure
            4: settings.languageList[14][settings.language]  #Success
        }
        machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number)[0]
        return switcher.get(machine_status, settings.languageList[18][settings.language])

    def getFailureInfo(self):
        misc.createPopup('FAILED BRO')

    def csvExport(self):
        misc.csvExport()
        misc.createPopup(settings.languageList[32][settings.language])

    def setEnglish(self):
        settings.language = 1
        self.setLanguage()

    def setFrench(self):
        settings.language = 2
        self.setLanguage()

    def setLanguage(self):
        self.status = self.getStatus()
        self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
        self.csvButton.configure(text=settings.languageList[9][settings.language])
        self.returnButton.configure(text=settings.languageList[8][settings.language])
        self.plotGraph()
