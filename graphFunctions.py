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
import detailedResultsDao
import resultByIDDao
import misc

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

    figure = plt.Figure(figsize=(8,4), dpi=80)
    ax = figure.add_subplot(111)
    ax.set_title(settings.languageList[10][settings.language], fontweight="bold", fontsize=16)
    ax.set_xlabel(settings.languageList[12][settings.language])
    ax.set_ylabel(settings.languageList[11][settings.language])
    line = FigureCanvasTkAgg(figure, self)
    line.get_tk_widget().grid(sticky=E+W, row=0, columnspan=2)
    ax2 = df.plot(kind='line', color='black', y='Velocity', ax=ax, legend=False, fontsize=11, marker='o', markevery=self.markers_on, 
        markerfacecolor='red', markeredgecolor='red', markersize=10)
    ax2.grid()

def getStatus(self, isPrevious):
    if(isPrevious):
        test_number = settings.test_number - 1
    else:
        test_number = settings.test_number

    switcher = { 
        0: settings.languageList[13][settings.language], #Ready to Start
        1: settings.languageList[17][settings.language], #In Progress
        2: settings.languageList[16][settings.language], #Stopped
        3: settings.languageList[15][settings.language], #Failure
        4: settings.languageList[14][settings.language]  #Success
    }
    machine_status = resultByIDDao.ResultByIDDao.get_test_status(test_number)[0]
    return switcher.get(machine_status, settings.languageList[18][settings.language])

def getFailureInfo(self, isPrevious):
    if(isPrevious):
        test_number = settings.test_number - 1
    else:
        test_number = settings.test_number

    message = settings.languageList[40][settings.language] + ' '
    failure_mode = resultByIDDao.ResultByIDDao.get_failure_mode(test_number)[0]
    detailed_id = detailedResultsDao.DetailedResultsDao.get_first_id_by_test_id(test_number)[0]

    if(failure_mode == 1): #overheat
        overheat_vals = detailedResultsDao.DetailedResultsDao.get_overheat(test_number)
        for val in overheat_vals:
            if(val>0):
                test_section=detailedResultsDao.DetailedResultsDao.get_test_section_by_id(detailed_id)[0]
                time = detailedResultsDao.DetailedResultsDao.get_time_by_id(detailed_id)[0]
                velocity = detailedResultsDao.DetailedResultsDao.get_velocity_by_id(detailed_id)[0]

                message += (test_section + '\n' + '\n' + settings.languageList[33][settings.language] + ' ' + settings.languageList[36][settings.language] 
                + '\n' + settings.languageList[34][settings.language] + ' ' + str(time) + ' s ' + settings.languageList[35][settings.language] 
                + ' ' + str(velocity) +' m/s ')
                misc.createPopup(message)
                break
            detailed_id += 1

    elif(failure_mode == 2): #Air Leak or Device Activation
        errorFound = False
        sectionList = ['1A', '1B', '4A', '4B']

        for test_section in sectionList:
            detailed_id = detailedResultsDao.DetailedResultsDao.get_first_id_by_test_section(test_number, test_section)[0]
            errorFound = findPressureError(detailed_id, test_section, test_number, message)
            if(errorFound):
                break;

    elif(failure_mode == 3): #Failure to Exhaust Air
        sectionList = ['2A', '2B', '3A', '3B']

        for test_section in sectionList:
            detailed_id = detailedResultsDao.DetailedResultsDao.get_first_id_by_test_section(test_number, test_section)[0]
            errorFound = findNoExhaustError(detailed_id, test_section, test_number, message)
            if(errorFound):
                break;

    elif(failure_mode == 4): #Failure to Exhaust Air
        sectionList = ['2A', '2B', '3A', '3B']

        for test_section in sectionList:
            detailed_id = detailedResultsDao.DetailedResultsDao.get_first_id_by_test_section(test_number, test_section)[0]
            errorFound = findOverExhaustError(detailed_id, test_section, test_number, message)
            if(errorFound):
                break;

def findPressureError(detailed_id, test_section, test_number, message):
    retval = False
    pressure_vals = detailedResultsDao.DetailedResultsDao.get_pressure_by_test_section(test_number, test_section)
    for pressure in pressure_vals:
        if(pressure>0):
            time = detailedResultsDao.DetailedResultsDao.get_time_by_id(detailed_id)[0]
            velocity = detailedResultsDao.DetailedResultsDao.get_velocity_by_id(detailed_id)[0]

            message += (test_section + '\n' + '\n' + settings.languageList[33][settings.language] + ' ' + settings.languageList[37][settings.language] 
            + '\n' + settings.languageList[34][settings.language] + ' ' + str(time) + ' s ' + settings.languageList[35][settings.language] 
            + ' ' + str(velocity) +' m/s ')
            misc.createPopup(message)
            retval=True
            break
        detailed_id +=1
    return retval

#NOT SURE HOW TO DO THESE YET
def findNoExhaustError(detailed_id, test_section, test_number, message):
    retval = False

def findOverExhaustError(detailed_id, test_section, test_number, message):
    retval = False

def getFailurePoints(self, isPrevious):
    if(isPrevious):
        test_number = settings.test_number - 1
    else:
        test_number = settings.test_number

    failure_mode = resultByIDDao.ResultByIDDao.get_failure_mode(test_number)[0]
    if(failure_mode == 1): #overheat
        times_overheated = detailedResultsDao.DetailedResultsDao.get_times_overheated(test_number)
        self.markers_on = times_overheated
    elif(failure_mode == 2): #Air Leak or Device Activation
        times_activated = detailedResultsDao.DetailedResultsDao.get_times_activated(test_number)
        self.markers_on = times_activated
    elif(failure_mode == 3): #Failure to Exhaust Air
        print("Failed to Exhaust")
    elif(failure_mode == 4): #Exhausting Too Long (>1 s)
        print("Exhausting too long")
