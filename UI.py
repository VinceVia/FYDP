#!/usr/bin/python3
import mainApp
import sqlite3
import tkinter as tk
from tkinter import *
import settings
import languageDao
import resultByIDDao
import misc

if __name__ == "__main__":
    settings.init()
    settings.language = 2 #French as default language
    languageDao.LanguageDao.get_strings()
    settings.test_number = resultByIDDao.ResultByIDDao.get_test_number()[0]
    #settings.failure_mode = resultByIDDao.ResultByIDDao.get_failure_mode(settings.test_number)[0]
    app = mainApp.MainApp()
    misc.center(app)
    app.mainloop()
