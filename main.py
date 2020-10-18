from tkinter import *
from tkinter import font as tkFont
import time
import tkinter.messagebox

root = Tk()  # create window

root.title("Job 1")  # title for window
root.geometry('302x100')  # main window geometry
# change font size
largerFont = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
# persons = [['Joe', 2, True], ['Jose', 7, False], ['Maria', 12, True], ['Mary', 17, False]]


# def managePersons():
# print(persons[0][1])

# managePersons()


timeCount = 0  # counter for the current time
timerRunning = True
# create Timer Window
timeWindow = Toplevel(root)
timeWindow.title("Timer")
timeWindow.geometry("200x200+600+00")
timeNow = Label(timeWindow, text=" ", font=largerFont)
timeNow.pack()

# create Log Window
logWindow = Toplevel(root)
logWindow.title("Log")
logWindow.geometry("300x300+1000+00")

# creation of labels for the Log Window
labelName = Label(logWindow, text="Name              ", font=largerFont)
labelName.grid(column=1, row=1)
labelEvent = Label(logWindow, text="Event                ", font=largerFont)
labelEvent.grid(column=2, row=1)
labelEvent = Label(logWindow, text="Time", font=largerFont)
labelEvent.grid(column=3, row=1)


def current_time():  # return current internal time no longer needed
    return time.strftime("%H:%M:%S")


def convert_time(seconds):  # converts and returns the counter time in format HR:MIN:SEC
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    minutes = seconds // 60 - (hour * 60)
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def manage_time():
    global timeCount
    global timerRunning
    if timerRunning:
        timeCount += 1
    timeNow.config(text="T: " + convert_time(timeCount))
    root.after(1000, manage_time)


manage_time()


# button action listeners
def clickedpause():
    global timerRunning
    timerRunning = False


def clickedunpause():
    global timerRunning
    timerRunning = True


def clickedend():
    root.destroy()


# button creation
btnPause = Button(root, text="Pause", fg="black", bg="gray", command=clickedpause, height=1, width=13)

btnUnPause = Button(root, text="Un Pause", fg="black", bg="gray", command=clickedunpause, height=1, width=13)

btnEnd = Button(root, text="End", fg="black", bg="gray", command=clickedend, height=1, width=13)

# button placement
btnPause.grid(column=1, row=1)

btnUnPause.grid(column=2, row=1)

btnEnd.grid(column=3, row=1)

# tkinter.messagebox.showinfo('POP UP','NAME')  #this is a test for pop up window
root.mainloop()
