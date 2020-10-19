from tkinter import *
from tkinter import font as tkFont
import time
import tkinter.messagebox
from typing import Union

root = Tk()  # create window

root.title("Job 1")  # title for window
root.geometry('302x100')  # main window geometry
# change font size
largerFont = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
persons = [['Joe', 2, True], ['Jose', 7, False], ['Maria', 12, True], ['Mary', 17, False]]


def arrival_time(data):
    return data.__getitem__(1)


entrance = [person[1] for person in persons]

timeCount = -1  # counter for the current time
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
logPadding = 25
labelName = Label(logWindow, text="Name", font=largerFont)
labelName.grid(column=1, row=1, ipadx=logPadding)
labelEvent = Label(logWindow, text="Event", font=largerFont)
labelEvent.grid(column=2, row=1, ipadx=logPadding)
labelEvent = Label(logWindow, text="Time", font=largerFont)
labelEvent.grid(column=3, row=1, ipadx=logPadding)


# print the employee arrival information
def arrive_write(time_stamp):
    location = entrance.index(time_stamp)
    lbl_log_output_name = Label(logWindow, text=persons[location][0])
    lbl_log_output_name.grid(column=1, row=1 + time_stamp)
    lbl_log_output_visit = Label(logWindow, text='arrive')
    lbl_log_output_visit.grid(column=2, row=1 + time_stamp)
    lbl_log_output_time = Label(logWindow, text=convert_time(time_stamp))
    lbl_log_output_time.grid(column=3, row=1 + time_stamp)


# manage popup window for employee based on whether they are a laggard or a nonlaggard
def manage_employee_visit(time_stamp):
    location = entrance.index(time_stamp)
    person = persons[location]
    print(person)


# function for managing employees input into the log based on real time
def employee_info(time_stamp):
    if entrance.__contains__(time_stamp):
        arrive_write(time_stamp)  # add start time to log
        manage_employee_visit(time_stamp)  # begin function to manage employee's visit


# return current internal time no longer needed
def current_time():
    return time.strftime("%H:%M:%S")


# converts and returns the counter time in format HR:MIN:SEC
def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    minutes = seconds // 60 - (hour * 60)
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


# function to update the running timer and check if employee activities must be done
def manage_time():
    global timeCount
    global timerRunning
    if timerRunning:
        timeCount += 1
    employee_info(timeCount)  # begin managing employee info based on current time
    timeNow.config(text="T: " + convert_time(timeCount))
    root.after(1000, manage_time)  # tell program to wait 1 second before executing this command again


manage_time()  # begin timer


# button action listeners
def clicked_pause():
    global timerRunning
    timerRunning = False


def clicked_unpause():
    global timerRunning
    timerRunning = True


def clicked_end():
    root.destroy()


# button creation
btnPause = Button(root, text="Pause", fg="black", bg="gray", command=clicked_pause, height=1, width=13)

btnUnPause = Button(root, text="Un Pause", fg="black", bg="gray", command=clicked_unpause, height=1, width=13)

btnEnd = Button(root, text="End", fg="black", bg="gray", command=clicked_end, height=1, width=13)

# button placement
btnPause.grid(column=1, row=1)

btnUnPause.grid(column=2, row=1)

btnEnd.grid(column=3, row=1)

root.mainloop()
