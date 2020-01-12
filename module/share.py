import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

import sqlite3
from sqlite3 import Error

from tkinter import *

import time
import datetime

from datetime import datetime
#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

class MyWindow:

    def __init__(self, win):
        self.lbl1=Label(win, text='Student ID')
        self.lbl2=Label(win, text='Date')
        self.lbl3=Label(win, text='Score')
        self.lbl4=Label(win, text='Name')
        
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t2a=Entry()
        self.t2b=Entry()
  	self.t3=Entry()
        self.t4=Entry()
        
       
        self.degreeentry=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Show Chart')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.lbl4.place(x=100, y=100)
        
      
        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=150, width=40)
        self.t2a.place(x=240, y=150, width=40)
        self.t2b.place(x=280, y=150, width=40)
        self.t3.place(x=200, y=200)
        self.t4.place(x=200, y=100) 
     
        self.b1=Button(win, text='Show Scores', command=self.select2)
        self.b6=Button(win, text='Delete Scores', command=self.deletescore)
        self.b2=Button(win, text='Show Chart')
        self.b2.bind('<Button-1>', self.showchart)
        self.b1.place(x=100, y=250)
        self.b2.place(x=200, y=250)
      
       
        self.lb=Listbox(window, height=5, selectmode='multiple')

        self.lb.place(x=150, y=350)
        self.lb2=Listbox(window, height=5, selectmode='multiple')
        self.lb2.place(x=350, y=350)

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

    def select2(self):
        self.lb2.delete(0,100)
        selectid=self.t1.get()
        conn = None
        try:
            conn = sqlite3.connect("students.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * FROM scores WHERE id = ?", selectid)
      #  cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
 
        for row in rows:
            a1 = str(row[0])
            a2 = str(row[1])
            a3 = str(row[2])
            a2a = a2[0:4]
            a2b = a2[4:6]
            a2c = a2[6:8]
            a2d = a2a + " " + a2b + " " + a2c 
          
            
            showdate = a2d + "  |  " + a3
            bb = self.lb2.insert(END, showdate)

    def insertscore(self):
        self.lb2.delete(0,100)
        insertid=self.t1.get()
        insertyear=self.t2.get()
        insertmonth=self.t2a.get()
        insertday=self.t2b.get()
        insertscore=self.t3.get()
        conn = None
        try:
            conn = sqlite3.connect("students.db")
        except Error as e:
            print(e)

        insertdate = insertyear + insertmonth + insertday

        cur = conn.cursor()
        cur.execute("INSERT INTO scores ( id, satdate, score) VALUES (?, ?, ?)", (insertid, insertdate, insertscore))
      #  cur.execute("SELECT * FROM students")

        rows = cur.fetchall()
 
        for row in rows:
            print(row)
            self.lb2.insert(END,row)

        conn.commit()
        conn.close()


    def displaygraph(self):
        self.lb2.delete(0,100)
        insertid=self.t1.get()
        insertyear=self.t2.get()
        insertmonth=self.t2a.get()
        insertday=self.t2b.get()
        insertscore=self.t3.get()
        conn = None
        try:
            conn = sqlite3.connect("students.db")
        except Error as e:
            print(e)

        insertdate = insertyear + insertmonth + insertday

        cur = conn.cursor()
        cur.execute("INSERT INTO scores ( id, satdate, score) VALUES (?, ?, ?)", (insertid, insertdate, insertscore))
      #  cur.execute("SELECT * FROM students")

        rows = cur.fetchall()
 
        for row in rows:
            print(row)
            self.lb2.insert(END,row)

        conn.commit()
        conn.close()


    def deletescore(self):
        self.lb2.delete(0,100)
        deleteid=self.t1.get()
        deleteyear = self.t2.get()
        deletemonth = self.t2a.get()
        deleteday = self.t2b.get()

        deletedate = deleteyear + deletemonth + deleteday
        conn = None
        try:
            conn = sqlite3.connect("students.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("DELETE from scores where id = ? AND satdate = ?", (deleteid, deletedate))
      #  cur.execute("SELECT * FROM students")

 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)
            self.lb2.insert(END,row)

        conn.commit()
        conn.close()


    def deletestudent(self):
        self.lb2.delete(0,100)
        deleteid=self.t1.get()
        print ("DELETE ID ------------>", deleteid)
      #  deletedate =self.t2.get()
        conn = None
        try:
            conn = sqlite3.connect("students.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
        #cur.execute('DELETE from scores where id = %s ', deleteid)
        cur.execute("DELETE from scores where id = ?", (deleteid,))
      #  cur.execute("SELECT * FROM students")
        cur.execute("DELETE from students where id = ? ", (deleteid,))
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)
            self.lb2.insert(END,row)

        conn.commit()
        conn.close()



    def newstudent(self):
        max = 0
       # deleteid=self.t1.get()
        insertname = self.t4.get()
        insertdate = self.t2.get()

        insertyear=self.t2.get()
        insertmonth=self.t2a.get()
        insertday=self.t2b.get()

        insertdate = insertyear + insertmonth + insertday

        print ("insertname:",insertname)
        print ("insertdate:",insertdate)
        maxid = 0
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
            print(row[0])
            self.lb.insert(END,row[0])
            if ( max <= int(row[0]) ):
                max = int(row[0]) +1

            
        print ("max:" , max) 
        cur.execute("INSERT INTO students ( id, name, startingdate) VALUES (?, ?, ?)", (max, insertname, insertdate))
        conn.commit()


    def showchart(self, event):

        x5 = []
        y5 = []

        selectdegree = self.degreeentry.get()

        selectid=self.t1.get()
      
        predictdate=self.t5.get()
        predictdatestr = str(predictdate)


##
 
        insertyear=self.t5.get()
        insertmonth=self.t5a.get()
        insertday=self.t5b.get()
        insertscore=self.t3.get()

##

        
       
        predictyearf = predictdatestr[0:4]
        predictmonthf = predictdatestr[4:6]
        predictdayf = predictdatestr[6:8]
        print ("))))))))))))))))))))))))))))))))")
        print ( predictyearf )
       # pdate = datetime(int(predictyearf), int(predictmonthf), int(predictdayf))

##

        predictyearf = insertyear
        predictmonthf = insertmonth
        predictdayf = insertday
        print (predictyearf)
        print (predictmonthf)
        print (predictdayf)
        pdate = datetime(int(predictyearf), int(predictmonthf), int(predictdayf))
        


        conn = None
        try:
            conn = sqlite3.connect("students.db")
        except Error as e:
            print(e)

        cur = conn.cursor()
     
     #   cur.execute("SELECT * FROM scores where id = ?", (selectid,))
    #    cur.execute("SELECT startingdate FROM students where id = '1'")
 
        cur.execute("SELECT startingdate FROM students where id = ?", (selectid))
        with conn:

            cur.execute("SELECT * FROM scores where id = ?", (selectid))

            row = cur.fetchone()
           # if row == None:
          #      break
  
            year = "year"
            year = str(row[1])
            print ( "----> " , year[0:4])
            yearf = year[0:4]
            month = "month"
            month= str(row[1])
            print ( "----------> " , month[4:6])
            monthf = month[4:6]
            day = "day"
            day = str(row[1])
            print ( "----------> " , day[6:8])
            dayf = day[6:8]

            sdate = datetime(int(yearf), int(monthf), int(dayf))
            print ("The sd is -->" , sdate )
	    #sd = datetime(2018, 11, 28)


            x5.append(1)
            y5.append(row[2])
            print ("FIRST!!!!!!!!!!!!!!!")

       
        while True:

            row = cur.fetchone()
           # print (row)
            if row == None:
                break

            year = "year"
            year = str(row[1])
            print ( "----> " , year[0:4])
            yearf = year[0:4]
            month = "month"
            month= str(row[1])
            print ( "----------> " , month[4:6])
            monthf = month[4:6]
            day = "day"
            day = str(row[1])
            print ( "----------> " , day[6:8])
            dayf = day[6:8]

            sd = datetime(int(yearf), int(monthf), int(dayf))
            print ("The sd is -->" , sd )
	    #sd = datetime(2018, 11, 28)

            print ("Difference: " , sdate - sd )
           
            dif = sdate - sd
            dif2 = dif.days

            print ("sdate:",sdate)
            print ("pdate:",pdate )

            x5.append ( -dif2  )
            y5.append ( row[2] )
 
        print (" *________________*")
        print ( x5 )
        print (" _________________")
        print ( y5 )
        print (" *________________*")


       
        print ("difference:", dif2)
  
        fdiff = -(sdate - pdate)
        fdiff2 = fdiff.days

 


        print ("final date difference",fdiff2)
        x = np.array([1,2,3,4,5,6])
        x = np.array(x5)
      #  x_plot = np.array([1,2,3,4,5])
        x_plot = np.array(x5)

       
        x_plot = np.append(x_plot, fdiff2)
        print ("xplot:",x_plot)
      #  y = np.array([400,530,560])
        y = np.array(y5)
       
   

        X = x[:, np.newaxis]
        X_plot = x_plot[:, np.newaxis]

        plt.scatter(x, y, color='blue', s=30, marker='o', label="SAT scores")

        model = make_pipeline(PolynomialFeatures(int(selectdegree)), Ridge())
        model.fit(X, y)
        y_plot = model.predict(X_plot)
        plt.plot(x_plot, y_plot, color='red', linewidth=2,
            label="degree %d" % 1)


        plt.legend(loc='lower left')


        plt.show()
        print ( y_plot )
        print ("**")
        


        plt.show()
        print ( y_plot )
        print ("**")

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
       


    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

    

 
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file



        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
 
        return conn
 
 
    def select_all_tasks(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("select * from scores")

        rows = cur.fetchall()
 
        for row in rows:
            print(row)
 
 
    def select_task_by_priority(conn, priority):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM STUDENTS", (priority,))
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)

       

    database = r"students.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
         
 
        print("Starting program...")
        select_all_tasks(conn)
   


window=Tk()
mywin=MyWindow(window)
window.title('Cambridge SAT score Prediction')
window.geometry("800x600+10+10")
window.mainloop()



 


