#!/usr/bin/python3
import mainApp
import sqlite3
import tkinter as tk
from tkinter import *
import settings
import dao

def get_posts():
    database = dao.Database('fydp')
    database.execute("SELECT * FROM language")
    settings.languageList = database.fetchall()

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == "__main__":
    settings.init()
    settings.language = 2 #French as default language
    get_posts()
    app = mainApp.MainApp()
    center(app)
    app.mainloop()