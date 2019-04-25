import tkinter as tk
from tkinter import *
import settings
import resultByIDDao
import misc
import graphFunctions

class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.status = graphFunctions.getStatus(self, False)
        self.machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number)[0]
        self.markers_on = []
        if(self.machine_status == 3):
            graphFunctions.getFailurePoints(self, False)
        graphFunctions.plotGraph(self, False)

        self.progress_label = Label(self, text=settings.languageList[1][settings.language] + ' ' + self.status)
        self.progress_label.config(font=("Arial", 18))
        self.progress_label.grid(sticky=W, row=1, column=0, columnspan=2, pady=5, padx=13)

        if(self.machine_status == 3):
            self.infoButton = Button(self, borderwidth=5, text=settings.languageList[30][settings.language], command=self.getFailureInfo, bg="grey70")
            self.infoButton.config(font=("Arial", 18))
            self.infoButton.grid(sticky=E, row=1, column=1, pady=5)

        self.returnButton = Button(self, text=settings.languageList[8][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("StartPage"))
        self.returnButton.config(font=("Arial", 18))
        self.returnButton.grid(sticky=W, row=2, column=0, pady=5)

        self.csvButton = Button(self, borderwidth=5, text=settings.languageList[9][settings.language], command=self.csvExport, bg="green3")
        self.csvButton.config(font=("Arial", 18))
        self.csvButton.grid(sticky=E, row=2, column=1, pady=5)

    def getFailureInfo(self):
        graphFunctions.getFailureInfo(self, False)

    def csvExport(self):
        misc.csvExport()
        misc.createPopup(settings.languageList[32][settings.language], "200x150")

    def setEnglish(self):
        settings.language = 1
        self.setLanguage()

    def setFrench(self):
        settings.language = 2
        self.setLanguage()

    def setLanguage(self):
        self.status = graphFunctions.getStatus(self, False)
        self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
        self.csvButton.configure(text=settings.languageList[9][settings.language])
        self.returnButton.configure(text=settings.languageList[8][settings.language])
        if(self.machine_status == 3):
            self.infoButton.configure(text=settings.languageList[30][settings.language])
        graphFunctions.plotGraph(self, False)
