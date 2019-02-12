import tkinter as tk
from tkinter import font as tkfont
import startPage
import graphPage
import settings

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = startPage.StartPage(parent=container, controller=self)
        self.frames["GraphPage"] = graphPage.GraphPage(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["GraphPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if(page_name == "GraphPage"):
            if(settings.language == 1):
                graphPage.GraphPage.setEnglish(self.frames["GraphPage"])
            else:
                graphPage.GraphPage.setFrench(self.frames["GraphPage"])
        frame.tkraise()