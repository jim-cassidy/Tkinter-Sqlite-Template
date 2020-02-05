
## Import necessary libraries

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from sqlite3 import Error
from tkinter import *
import time
import datetime
from datetime import datetime

class MyWindow:

    def __init__(self, win):
        self.label1=Label(win, text='Label1')
        self.label2=Label(win, text='Label2')
        self.entry1=Entry(bd=3)
        self.entry2=Entry(bd=3)
        self.label1.place(x=100, y=50)
        self.label2.place(x=100, y=100)
        self.entry1.place(x=200, y=50)
        self.entry2.place(x=200, y=100)
        self.button1=Button(win, text='Press Button', command=self.select)
        self.button1.place(x=100, y=150)
        self.lb=Listbox(window, height=10, selectmode='multiple')
        self.lb.place(x=100, y=200)
       
       
    def select(self):
       
        self.lb.delete(0,100)
        conn = None
        try:
            conn = sqlite3.connect("sample.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * from sampletable")
 
        rows = cur.fetchall()
 
        for row in rows:
            showlist = str(row[0])
        #    showname = str(row[1])
        #    showdate = str(row[2])
        #    showdate1 = showdate[0:4]
        #    showdate2 = showdate[4:6]
        #    showdate3 = showdate[6:8]
        #    showfulldate = showdate1 + " " + showdate2 + " " + showdate3            

            showline = showlist
            print ("list: " , row[0] )
            
            self.lb.insert(END,showline)

  
 

window=Tk()
mywin=MyWindow(window)
window.title('Title goes here')
window.geometry("800x600+10+10")
window.mainloop() 
