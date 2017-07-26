from Tkinter import *
from datetime import datetime
import numpy
import csv
import math

root = Tk()

timeBetweenPresses = []
lastTime = -1

def pressReturn(event):
    print("Train model")
    global timeBetweenPresses
    global lastTime
    with open("csv/dan_test.csv", "a") as fp:
        timeBetweenPresses = timeBetweenPresses[0:8]
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(timeBetweenPresses)
    
    timeBetweenPresses = []
    lastTime = -1
    
def key(event):
    global lastTime
    if lastTime is not -1:
        timeBetweenPresses.append((datetime.now() - lastTime).total_seconds())
    lastTime = datetime.now()
    print(timeBetweenPresses)

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.bind("<Return>", pressReturn)
frame.pack()
root.mainloop()


def addRndGuy():
    with open("rnd_test.csv", "a") as fp:
        for i in range(18):
            y = []
            for j in range(8):
                y.append(round(random.random(),6))
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(y)
            
        