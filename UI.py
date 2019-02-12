#!/Users/admin/anaconda3/bin/python3
import mainApp
import sqlite3
import tkinter as tk
from tkinter import *
import settings

settings.init()
settings.language = 2 #French as default language

with sqlite3.connect("/Users/admin/FYDP/FYDP/db/fydp.db") as db:
    cur = db.cursor()

def get_posts():
    with db:
        cur.execute("SELECT * FROM language")
        settings.languageList = cur.fetchall()

if __name__ == "__main__":
    get_posts()
    app = mainApp.MainApp()
    app.mainloop()