## We are going to be using numpy

import numpy as np
import matplotlib.pyplot as plt

## import scikit-learn

import sklearn

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

## we will be using sqlite

import sqlite3
from sqlite3 import Error

## here is our tkinter import

from tkinter import *

## here is the date and time function import

import time
import datetime


class MyWindow:

    def __init__(self, win):
        self.lbl1=Label(win, text='Student ID')
        self.lbl2=Label(win, text='Date')
        self.lbl3=Label(win, text='Score')
        self.lbl4=Label(win, text='Name')
        self.lbl5=Label(win, text='SAT Date')
        self.t1=Entry(bd=3)
        self.t4=Entry()
        self.t2=Entry()
        self.t2a=Entry()
        self.t2b=Entry()
        self.t3=Entry()
        self.t5=Entry()
        self.t5a=Entry()
        self.t5b=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Show Chart')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.lbl4.place(x=100, y=100)
        self.lbl5.place(x=100, y=250)
        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=150, width=40)
        self.t2a.place(x=240, y=150, width=40)
        self.t2b.place(x=280, y=150, width=40)
        self.t3.place(x=200, y=200)
        self.t4.place(x=200, y=100) 
        self.t5.place(x=200, y=250, width = 40)   
        self.t5a.place(x=240, y=250, width = 40)   
        self.t5b.place(x=280, y=250, width = 40)   
    
        self.b1=Button(win, text='Show Scores')
        self.b6=Button(win, text='Delete Scores' )
        self.b3=Button(win, text='List Students' )
        self.b5=Button(win, text='Insert Score' )
        self.b7=Button(win, text="Delete Student" )
        self.b8=Button(win, text="New Student" )
        self.b8.place ( x = 50, y=350 )
        self.b7.place ( x = 350, y = 350 )
        self.b3.place ( x=150, y=350 )
        self.b5.place ( x = 250, y = 350)
        self.b4=Button(win, text='Scores', command=self.select)
        self.b4.place ( x=350, y=500 )
        self.b2=Button(win, text='Show Chart')
        self.b2.bind('<Button-1>' )
        self.b1.place(x=100, y=300)
        self.b2.place(x=200, y=300)
        self.b6.place(x=300, y=300)
       
        self.lb=Listbox(window, height=5, selectmode='multiple')

        self.lb.place(x=150, y=450)
        self.lb2=Listbox(window, height=5, selectmode='multiple')
        self.lb2.place(x=350, y=450)

    ### --- select 

    def select(self):
       
           self.lb.delete(0,100)
           conn = None
           try:
               conn = sqlite3.connect("students.db")
           except Error as e:
               print(e)

           cur = conn.cursor()
           cur.execute("SELECT * FROM STUDENTS")
 
           rows = cur.fetchall()
 
           for row in rows:
               showid = str(row[0])
               showname = str(row[1])
               showdate = str(row[2])
               showdate1 = showdate[0:4]
               showdate2 = showdate[4:6]
               showdate3 = showdate[6:8]
               showfulldate = showdate1 + " " + showdate2 + " " + showdate3            

               showline = showid + " " + showname + " " + showfulldate
               print ("name: " , row[1] )
            
               self.lb.insert(END,showline)


window=Tk()
mywin=MyWindow(window)
window.title('Cambridge SAT score Prediction')
window.geometry("800x600+10+10")
window.mainloop()

   

   

 


