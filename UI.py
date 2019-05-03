#!/Users/admin/anaconda3/bin/python3
import mainApp
from tkinter import *
import settings
import languageDao
import resultByIDDao

if __name__ == "__main__":
    settings.init()
    settings.language = 2 #French as default language
    languageDao.LanguageDao.get_strings()
    settings.test_number = resultByIDDao.ResultByIDDao.get_test_number()[0]
    #settings.failure_mode = resultByIDDao.ResultByIDDao.get_failure_mode(settings.test_number)[0] #Can't remember what this was for exactly
    app = mainApp.MainApp()
    app.attributes("-fullscreen", True)
    #app.config(cursor="none")
    app.mainloop()
