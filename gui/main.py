
import sys
from glob import glob
URL_SET = "/Users/gabrielelfassi/Documents/github/BotLogger/"
sys.path.insert(0, URL_SET)
import os
os.chdir(URL_SET)

import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import modules
from modules.bot import BotLOG
from modules.listner import ListenerLOG


class MainWindow:
    def __init__(self):
        win = Tk()
        self.tab_control = ttk.Notebook(win)
        self.notebookWidget(win)
        win.mainloop()
        pass

    def notebookWidget(self, window):
        PlayWindow(self.tab_control, window)
        RecordWindow(self.tab_control)
        self.tab_control.pack(expand=1, fill='both')
        pass


class PlayWindow:
    def __init__(self, tab_control, window):
        """ init tab control and view"""
        self.window = window
        self.tab_control = tab_control
        self.setPlayView()

    def stopButton(self):
        self.text_btn.set("Play")
        self.b1.configure(textvariable=self.text_btn, command=self.playButton)
        pass
    
    def resumeButton(self): 
        self.window.update()
        self.result_read_log = self.blog.read_log()
        pass

    def playButton(self):
        """ play action linked to play button"""
        # self.window.withdraw()
        log = select.get(select.curselection())
        self.blog = BotLOG(log)
        self.result_read_log = self.blog.run()
        self.text_btn.set("Resume")
        self.b1.configure(textvariable=self.text_btn, command=self.resumeButton)
        pass

    def makePlayWindow(self, win):
        """init play view with components"""
        global select
        frame3 = Frame(win)       # select of names
        frame3.pack()
        scroll = Scrollbar(frame3, orient=VERTICAL)
        select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
        scroll.config (command=select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        select.pack(side=LEFT,  fill=BOTH, expand=1)

        frame1 = Frame(win)
        frame1.pack()

        self.text_btn =  tk.StringVar()
        self.text_btn.set("Play")

        frame2 = Frame(win)       # Row of buttons
        frame2.pack()
        self.b1 = Button(frame2,textvariable=self.text_btn,command=self.playButton)
        self.b2 = Button(frame2,text="Stop",command=self.stopButton)
        self.b1.pack(side=LEFT)
        self.b2.pack(side=LEFT)
        self.setSelect()
    
    def setSelect(self):
        """ display all matching files into .logs/ folder"""
        for pos_json in os.listdir('.logs/'):
            if pos_json.endswith('.json'):
                select.insert(END, pos_json)
    
    def setPlayView(self):
        set_view = ttk.Frame(self.tab_control)
        self.makePlayWindow(set_view)
        self.tab_control.add(set_view, text='Play')


class RecordWindow:
    def __init__(self, tab_control):
        """ init tab control and view"""
        self.tab_control = tab_control
        self.setRecordView()


    def recordButton(self):
        """ start to record"""
        self.llog = ListenerLOG("azee.json")
        self.text_btn.set("Is Recording..")
        pass

    def makeRecordView(self, win):
        """init play view with components"""
        global select
        frame3 = Frame(win)       # select of names
        frame3.pack()
        frame1 = Frame(win)
        frame1.pack()

        frame2 = Frame(win)       # Row of buttons
        frame2.pack()

        self.text_btn =  tk.StringVar()
        self.text_btn.set("Record")

        self.b1 = Button(frame2,textvariable=self.text_btn,command=self.recordButton)
        self.b1.pack(side=LEFT)

    def startRecording(self):
        if self.text_btn == "Is Recording":
            self.llog.run()
    def setRecordView(self):
        set_view = ttk.Frame(self.tab_control)
        self.makeRecordView(set_view)
        self.tab_control.add(set_view, text='Record')
        self.startRecording()


MainWindow()