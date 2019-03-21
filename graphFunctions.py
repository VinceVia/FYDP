import settings
import detailedResultsDao
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *

def plotGraph(self, isPrevious):
    if(isPrevious):
        test_number = settings.test_number - 1
    else:
        test_number = settings.test_number
        
    velocity = detailedResultsDao.DetailedResultsDao.get_velocities(test_number)
    time = detailedResultsDao.DetailedResultsDao.get_times(test_number)

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
    line = FigureCanvasTkAgg(figure, self)
    line.get_tk_widget().grid(sticky=E+W, row=0, columnspan=2)
    ax2 = df.plot(kind='line', color='black', y='Velocity', ax=ax, legend=False, fontsize=11, marker='o', markevery=self.markers_on, 
        markerfacecolor='red', markeredgecolor='red', markersize=10)
    ax2.grid()