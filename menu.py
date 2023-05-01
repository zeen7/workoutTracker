import os
import tkinter as tk
from tkinter import ttk  
from tkinter import Menu 
from tkinter import *

win = tk.Tk()  
win.title("Workout Tracker")  

#Exit action  
def _quit():  
   win.quit()  
   win.destroy()  
   exit()

#Create Menu Bar  
menuBar=Menu(win)  
win.config(menu=menuBar)

#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="New")  
fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)

#Help Menu  
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="About")  
menuBar.add_cascade(label="Help", menu=helpMenu)

def runBarbell():
   os.system('python app.py')
   win.quit()
   win.destroy()
   exit()

button1 =  Button(win, text="Barbell Curls Tracker", command=runBarbell)
#put on screen
button1.pack()

#Calling Main()  
win.mainloop()  