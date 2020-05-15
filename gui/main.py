
import sys
from glob import glob
URL_SET = "/Users/gabrielelfassi/Documents/github/BotLogger/"

sys.path.insert(0, URL_SET)
import os
os.chdir(URL_SET)

import tkinter
from tkinter import *
import modules
from modules.bot import BotLOG

phonelist=["01"]

class MainWindow:
    
    def __init__(self):
        win = self.makeWindow()
        self.setSelect()
        win.mainloop()

    def whichSelected(self):
        print("At %s of %d" % (select.curselection(), len(phonelist)))
        return int(select.curselection()[0])

    def addEntry(self):
        log = select.get(select.curselection())
        blog = BotLOG(log)
        blog.run()
        pass

    def updateEntry(self):
        pass

    def deleteEntry(self):
        pass

    def loadEntry(self):
        pass

    def makeWindow(self):
        global nameVar, phoneVar, select
        win = Tk()
        frame3 = Frame(win)       # select of names
        frame3.pack()
        scroll = Scrollbar(frame3, orient=VERTICAL)
        select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
        scroll.config (command=select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        select.pack(side=LEFT,  fill=BOTH, expand=1)

        frame1 = Frame(win)
        frame1.pack()

        frame2 = Frame(win)       # Row of buttons
        frame2.pack()
        b1 = Button(frame2,text=" Play  ",command=self.addEntry)
        b1.pack(side=LEFT)

        
        return win

    def setSelect(self):
        for pos_json in os.listdir('.logs/'):
            if pos_json.endswith('.json'):
                select.insert(END, pos_json)

main = MainWindow()
