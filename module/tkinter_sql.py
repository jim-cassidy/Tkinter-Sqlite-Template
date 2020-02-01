
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
        self.label2.place(x=100, y=150)
        self.entry1.place(x=200, y=50)
        self.entry2.place(x=200, y=150)
       

window=Tk()
mywin=MyWindow(window)
window.title('Title goes here')
window.geometry("800x600+10+10")
window.mainloop()
