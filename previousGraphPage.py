import tkinter as tk
from tkinter import *
import settings
import detailedResultsDao
import resultByIDDao
import misc
import graphFunctions

class PreviousGraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.status = self.getStatus()
        self.machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number - 1)[0]
        self.markers_on = []
        if(self.machine_status == 3):
            self.getFailurePoints()
        graphFunctions.plotGraph(self, True)

        self.progress_label = Label(self, text=settings.languageList[1][settings.language] + ' ' + self.status)
        self.progress_label.config(font=("Arial", 45))
        self.progress_label.grid(sticky=W, row=1, column=0, columnspan=2, pady=5, padx=10)

        if(self.machine_status == 3):
            self.infoButton = Button(self, borderwidth=5, text=settings.languageList[30][settings.language], command=self.getFailureInfo, bg="green")
            self.infoButton.config(font=("Arial", 45))
            self.infoButton.grid(sticky=E, row=1, column=1, pady=5, padx=10)

        self.returnButton = Button(self, text=settings.languageList[8][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("StartPage"))
        self.returnButton.config(font=("Arial", 45))
        self.returnButton.grid(sticky=W, row=2, column=0, pady=10)

        self.csvButton = Button(self, borderwidth=5, text=settings.languageList[9][settings.language], command=self.csvExport, bg="green")
        self.csvButton.config(font=("Arial", 45))
        self.csvButton.grid(sticky=E, row=2, column=1, pady=5, padx=10)

    def getStatus(self):
        switcher = { 
            0: settings.languageList[13][settings.language], #Ready to Start
            1: settings.languageList[17][settings.language], #In Progress
            2: settings.languageList[16][settings.language], #Stopped
            3: settings.languageList[15][settings.language], #Failure
            4: settings.languageList[14][settings.language]  #Success
        }
        machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number - 1)[0]
        return switcher.get(machine_status, settings.languageList[18][settings.language])

    def getFailureInfo(self):
        message = settings.languageList[40][settings.language] + ' '

        overheat_vals = detailedResultsDao.DetailedResultsDao.get_overheat(settings.test_number - 1)
        detailed_id = detailedResultsDao.DetailedResultsDao.get_first_id_by_test_id(settings.test_number - 1)[0]
        for val in overheat_vals:
            if(val>0):
                test_section=detailedResultsDao.DetailedResultsDao.get_test_section_by_id(detailed_id)[0]
                time = detailedResultsDao.DetailedResultsDao.get_time_by_id(detailed_id)[0]
                velocity = detailedResultsDao.DetailedResultsDao.get_velocity_by_id(detailed_id)[0]

                message += (test_section + '\n' + '\n' + settings.languageList[33][settings.language] + ' ' + settings.languageList[36][settings.language] 
                + '\n' + settings.languageList[34][settings.language] + ' ' + str(time) + ' s ' + settings.languageList[35][settings.language] 
                + ' ' + str(velocity) +' m/s ')

                break
            detailed_id += 1
        misc.createPopup(message)

    def getFailurePoints(self):
        times_overheated = detailedResultsDao.DetailedResultsDao.get_times_overheated(settings.test_number - 1)
        self.markers_on = times_overheated

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
        if(self.machine_status == 3):
            self.infoButton.configure(text=settings.languageList[30][settings.language])
        graphFunctions.plotGraph(self, True)
