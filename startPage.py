import tkinter as tk
from tkinter import *
import multiprocessing
import settings
import graphPage
import resultByIDDao
import misc
#import motorRoutine 
import testMotorRoutine #FOR TEST
import subprocess

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.label = Label(self, text=settings.languageList[0][settings.language])
        self.label.config(font=("Arial", 32, 'bold'))
        self.label.grid(row=0, columnspan=3, pady=10, ipady=15)
        
        self.status = self.getStatus()
        self.progress_label = Label(self, text=settings.languageList[1][settings.language] + ' ' + self.getStatus())
        self.progress_label.config(font=("Arial", 23))
        self.progress_label.grid(row=1, columnspan=3, pady=5)

        self.results_link = Button(self, text=settings.languageList[2][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("GraphPage"))
        self.results_link.config(font=("Arial", 23, "italic"))
        self.results_link.grid(row=2, columnspan=3)

        self.start_button = Button(self, borderwidth=5, padx=16, text=settings.languageList[3][settings.language], command=self.start, bg="green3")
        self.start_button.config(font=("Arial", 17, 'bold'))
        self.start_button.grid(sticky=W, row=3, column=0, pady=80, padx=5, ipady=15)

        self.stop_button = Button(self, borderwidth=5, padx=16, text=settings.languageList[4][settings.language], command=self.stop, bg="red")
        self.stop_button.config(font=("Arial", 17, 'bold'))
        self.stop_button.grid(sticky=E, row=3, column=1, pady=80, ipady=15)

        self.reset_button = Button(self, borderwidth=5, padx=16, text=settings.languageList[29][settings.language], command=self.reset, bg="red")
        self.reset_button.config(font=("Arial", 17, 'bold'))
        self.reset_button.grid(sticky=W, row=3, column=2, pady=80, ipady=15)

        if(settings.test_number > 1):
            self.previous_results = Button(self, text=settings.languageList[5][settings.language], fg="blue", relief="flat", command=lambda: controller.show_frame("PreviousGraphPage"))
            self.previous_results.config(font=("Arial", 21, "italic"))
            self.previous_results.grid(sticky=W, row=4, column=0)
        
        self.quit = Button(self, text=settings.languageList[6][settings.language], fg="blue", relief="flat", command=self.quit)
        self.quit.config(font=("Arial", 21, "italic"))
        self.quit.grid(sticky=W, row=5, column=0, ipady=10)
        
        self.EN_button = Radiobutton(self, text="EN", indicatoron = 0, value=0, command=self.setEnglish)
        self.EN_button.config(bd=5, relief='raised', font=("Arial", 20, 'bold'))
        self.EN_button.grid(sticky=E, row=4, column=2, padx=1, ipadx=12)
        
        self.FR_button = Radiobutton(self, text="FR", indicatoron = 0, value=1, command=self.setFrench)
        self.FR_button.config(bd=5, relief='raised', font=("Arial", 20, 'bold'))
        self.FR_button.grid(sticky=E, row=5, column=2, padx=1, ipadx=12)

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

    def start(self):
        machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number)[0]
        if(machine_status == 1):
            misc.createPopup(settings.languageList[27][settings.language], "310x100")
        elif(machine_status == 2):
            resultByIDDao.ResultByIDDao.setTestStatus(1) #In Progress
            self.status = self.getStatus()
            self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
            #motorRoutine.fakeMotorRoutine(self) TODO: modify this after testing
        elif(machine_status == 0):
            self.win = tk.Toplevel(self)
            self.win.config(bd=5, relief='raised')
            #self.win.config(cursor="none")

            if(settings.language==2):
                self.win.geometry("600x250")
            else:
                self.win.geometry("450x250")

            misc.center(self.win)
            self.win.wm_title(settings.languageList[21][settings.language])

            idLabelTitle = Label(self.win, text=settings.languageList[22][settings.language])
            idLabelTitle.config(font=("Arial", 17, 'bold'))
            idLabelTitle.grid(row=0, columnspan=2)
            
            idLabel = Label(self.win, text=settings.languageList[23][settings.language])
            idLabel.config(font=("Arial", 17))
            idLabel.grid(sticky=E, row=1, column=0, padx=10, pady=50)

            self.e1 = Entry(self.win, font=("Arial", 18))
            self.e1.bind('<Button-1>', self.keyboard)
            self.e1.grid(sticky=E, row=1, column=1)

            quitButton = Button(self.win, borderwidth=5, text=settings.languageList[25][settings.language], command=self.win.destroy, bg="red")
            quitButton.config(font=("Arial", 20))
            quitButton.grid(row=2, column=1, sticky=E, pady=5, padx=10)
            
            submitButton = Button(self.win, borderwidth=5,  text=settings.languageList[24][settings.language], command=self.submit, bg='green3')
            submitButton.config(font=("Arial", 20))
            submitButton.grid(row=2, column=0, sticky=W, pady=5, padx=10)
        else:
            resultByIDDao.ResultByIDDao.setNewRow()
            settings.test_number += 1
            resultByIDDao.ResultByIDDao.setTestStatus(0) #Ready to start
            self.status = self.getStatus()
            self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
            self.start()

    def keyboard(self, event):                
        result = subprocess.Popen(['matchbox-keyboard'], stdout=subprocess.PIPE)

    def submit(self):
        sensorID = self.e1.get()
        if(sensorID != ''):
            self.win.destroy()
            resultByIDDao.ResultByIDDao.setSensorID(sensorID)
            resultByIDDao.ResultByIDDao.setTestStatus(1) #In Progress
            self.status = self.getStatus()
            self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
            #TODO: change motorProcess target to motorRoutine.py
            motorProcess = multiprocessing.Process(name='motorProcessTest', target=testMotorRoutine.processTest,)
            motorProcess.start()
            #motorRoutine.fakeMotorRoutine(self)
    
    def stop(self):
        machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number)[0]
        if(machine_status == 0 or machine_status == 3 or machine_status == 4):
            misc.createPopup(settings.languageList[20][settings.language], "390x150")
        elif(machine_status == 1):
            resultByIDDao.ResultByIDDao.setTestStatus(2)
            self.status = self.getStatus()
            self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
        else:
            misc.createPopup(settings.languageList[28][settings.language], "390x150")
        #motor stuff here

    def reset(self):
        machine_status = resultByIDDao.ResultByIDDao.get_test_status(settings.test_number)[0]
        if(machine_status == 1 or machine_status == 2):
            resultByIDDao.ResultByIDDao.setTestStatus(0)
            self.status = self.getStatus()
            self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status) 
        elif(machine_status == 0):
            misc.createPopup(settings.languageList[13][settings.language] + '!', "340x140")
        else:
            resultByIDDao.ResultByIDDao.setNewRow()
            settings.test_number += 1
            self.status = self.getStatus()
            self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)

    def setEnglish(self):
        settings.language = 1
        self.setLanguage()

    def setFrench(self):
        settings.language = 2
        self.setLanguage()

    def setLanguage(self):
        self.label.configure(text=settings.languageList[0][settings.language])
        self.status = self.getStatus()
        self.progress_label.configure(text=settings.languageList[1][settings.language] + ' ' + self.status)
        self.results_link.configure(text=settings.languageList[2][settings.language])
        self.start_button.configure(text=settings.languageList[3][settings.language])
        self.stop_button.configure(text=settings.languageList[4][settings.language])
        self.reset_button.configure(text=settings.languageList[29][settings.language])

        if(settings.test_number > 1):
            self.previous_results.configure(text=settings.languageList[5][settings.language])

        self.quit.configure(text=settings.languageList[6][settings.language])
