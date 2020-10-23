
from tkinter import *
from tkinter import font as tk_font
import time
#import staff_manager as sm

root = Tk()  # create window

popup_spacer = 150
root.title("Job 1")  # title for window
root.geometry('302x100+0+0')  # main window geometry
# changed font sizes
medium_font = tk_font.Font(family='Helvetica', size=10, weight=tk_font.BOLD)
larger_font = tk_font.Font(family='Helvetica', size=12, weight=tk_font.BOLD)
persons = [['Joe', 2, True], ['Jose', 2, False], ['Maria', 12, True], ['Mary', 17, False]]

time_count = -1  # counter for the current time
timer_running = True
# create Timer Window
time_window = Toplevel(root)
time_window.title("Timer")
time_window.geometry("200x200+600+0")
time_now = Label(time_window, text=" ", font=larger_font)
time_now.pack()

# create Log Window
log_window = Toplevel(root)
log_window.title("Log")
log_window.geometry("300x300+1000+0")

# creation of labels for the Log Window
logPadding = 25
log_row = 1  # value to handle where in the log grid values should be placed
label_name = Label(log_window, text="Name", font=larger_font)
label_name.grid(column=1, row=1, ipadx=logPadding)
label_event = Label(log_window, text="Event", font=larger_font)
label_event.grid(column=2, row=1, ipadx=logPadding)
label_event = Label(log_window, text="Time", font=larger_font)
label_event.grid(column=3, row=1, ipadx=logPadding)


# print the staff arrival information
def write_person_event(person, action):
    global log_row
    lbl_log_output_name = Label(log_window, text=person[0])
    lbl_log_output_name.grid(column=1, row=1 + log_row)
    lbl_log_output_visit = Label(log_window, text=action)
    lbl_log_output_visit.grid(column=2, row=1 + log_row)
    lbl_log_output_time = Label(log_window, text=convert_time(time_count))
    lbl_log_output_time.grid(column=3, row=1 + log_row)
    log_row += 1


def create_staff_popup(person_data):
    global popup_spacer

    def clicked_exit():  # function to handle the clicking of exit and close a window for the non laggards
        write_person_event(person_data, 'depart')  # write event to the log
        person_popup.destroy()

    # create the popup window for a person
    person_popup = Toplevel(root)
    person_popup.title("Action")
    # trying to figure out the best way to get the windows to not overlap and am currently using a set size spacer
    # for the windows. Will try to find a better more dynamic way to do so
    person_popup.geometry("100x80+0+" + popup_spacer.__str__())
    person_name = Label(person_popup, text=person_data[0], font=medium_font)
    popup_spacer += 120
    person_name.pack()
    # create an exit button
    btn_exit = Button(person_popup, text="Exit", fg="black", bg="gray", command=clicked_exit, height=1, width=10)
    btn_exit.pack(side=BOTTOM)
    write_person_event(person_data, 'arrive')  # add start time to log
    # handle laggard status
    if not person_data[2]:
        person_popup.after(4000, clicked_exit)  # if the staff is not a laggard close window after 3 seconds


# function for managing staff input into the log based on real time
def staff_entrance(time_stamp):
    global persons
    staff = [person for person in persons if person[1] == time_stamp]
    if len(staff) > 0:
        for member in staff:
            create_staff_popup(member)


# converts and returns the counter time in format HR:MIN:SEC
def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    minutes = seconds // 60 - (hour * 60)
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


# function to update the running timer and check if staff activities must be done
def manage_time():
    global time_count
    global timer_running
    if timer_running:
        time_count += 1
    staff_entrance(time_count)  # begin managing staff info based on current time
    time_now.config(text="T: " + convert_time(time_count), font=larger_font)
    root.after(1000, manage_time)  # tell program to wait 1 second before executing this command again


manage_time()  # begin timer


# button action listeners
def clicked_pause():
    global timer_running
    timer_running = False


def clicked_unpause():
    global timer_running
    timer_running = True


def clicked_end():
    root.destroy()


# button creation
btn_pause = Button(root, text="Pause", fg="black", bg="gray", command=clicked_pause, height=1, width=13)

btn_un_pause = Button(root, text="Un Pause", fg="black", bg="gray", command=clicked_unpause, height=1, width=13)

btn_end = Button(root, text="End", fg="black", bg="gray", command=clicked_end, height=1, width=13)

# button placement
btn_pause.grid(column=1, row=1)

btn_un_pause.grid(column=2, row=1)

btn_end.grid(column=3, row=1)

root.mainloop()
