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
        self.lbl1=Label(win, text='Write Label')
      
        self.t1=Entry(bd=3)
      
         
        
        self.lbl1.place(x=100, y=50)
         
        self.t1.place(x=200, y=50)
        
   
    
        self.b1=Button(win, text='Press Button')
       
        self.b1.place(x=100, y=150)
      
        self.lb=Listbox(window, height=10, selectmode='multiple')
        self.lb.place(x=100, y=250)
      

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

   

   

 


