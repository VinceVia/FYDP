import detailedResultsDao
import resultByIDDao
import time
import csv
import tkinter as tk
import settings
from tkinter import *

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def csvExport():
    dateTimeStamp = time.strftime('%Y%m%d%H%M%S')

    detailedResultsData = detailedResultsDao.DetailedResultsDao.get_table()

    f = open(dateTimeStamp + 'detailed_results_output.csv', 'w', newline="")
    writer = csv.writer(f,delimiter=',')
    writer.writerows(detailedResultsData)
    f.close()

    resultByIDData = resultByIDDao.ResultByIDDao.get_table()

    f = open(dateTimeStamp + 'result_by_id_output.csv', 'w', newline="")
    writer = csv.writer(f,delimiter=',')
    writer.writerows(resultByIDData)
    f.close()

def createPopup(message):
    win = tk.Toplevel()
    win.config(bd=5, relief='raised')
    win.geometry("600x300")
    center(win)
    win.wm_title(settings.languageList[31][settings.language])

    errorLabel = Label(win, text=message, justify=LEFT)
    errorLabel.config(font=("Arial", 20))
    errorLabel.grid(sticky=E, row=0, column=0, padx=5, pady=10)
    
    errorButton = Button(win, borderwidth=5, text=settings.languageList[25][settings.language], command=win.destroy, bg='red')
    errorButton.config(font=("Arial", 20))
    errorButton.grid(row=1, column=0, sticky=W, pady=20, padx=5)