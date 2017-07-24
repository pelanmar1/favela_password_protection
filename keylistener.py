from Tkinter import *
from datetime import datetime

root = Tk()

timeBetweenPresses = []
lastTime = -1

def pressReturn(event):
    print("Train model")
    root.destroy()

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
