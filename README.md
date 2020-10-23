# Job1
Initial job for managing employees

In current state:
The application has three windows
  1. The main window to control pause, unpause, and end program commands
  2. A running timer in format of Hours:Minutes:Seconds
  3. A layout for the log with 
      Worker name  |    Event  |  time
      
      
Successfully added the implementation of employee arrivals to the log file with the above layout
I am currently still trying to figure out how to best implement the handling of laggards and the best way to manage the pop up windows.
The way that the built in pop up windows are created and managed in tkinter actually puases the main loop while waiting for input from the user.
This means that the timer stops and the program does not push forward unto the window has been exited.
That being said, the likely solution for this is to have a small window created with a name and an exit button (managed appropriately given the laggard status) that will destroy the window either based on time (for non laggards) or on user input (for the laggards).
Will need to do a bit of research on the managing of windows in Tkinter in order for this to run smoothly and I will do so tomorrow before continuing with the project.
=======
Job 1.txt

The program will show four staff members who appear at specified times and then either disappear on their own or need to be dismissed. 

Initial Data:

To start the data on the staff members looks like this:
    name     arrival*      laggard
    ----     --------      -------
    Joe         2          True   
    Jose        7          False
    Maria      12          True
    Mary       17          False
 * where arrival is time in seconds from the program launch. 

Specs:

The program is written in python and uses tkinter to do the graphics. 

The UI: 

A. has a timer window that increments every second (counts forward as the program runs)

B. pops up a window for each staff member at the time of their arrival

C. the window displays the staff member's name

D. if the staff member is not a laggard, the window closes after 1 second. 

E. if the staff member is a laggard, the window has a button labelled "Dismiss" that when pressed closes that window. 

F. there is a log window that writes a line whenever a staff members arrives or departs,
   So, for example, which at 14 seconds, if it took eight seconds to dismiss Joe, and we haven't yet dismissed Maria, would look like this:
    name     event      time 
    ----     ------     -------
    Joe      arrive      2
    Jose     arrive      7
    Jose     depart      8
    Joe      depart      10
    Maria    arrive      12
   to be clear, this is a continuous logging window, it opens immediately and updates as events happen (not appearing at the end of the program running as a summary). 

G. none of the windows overlap one another. 

H. there are three buttons:
   Pause: pauses the timer and the progress of the program
   Restart: restarts the timer and the progress of the program
   End: ends the program

Purpose: Why build this

The clinic app has a protocol engine and protocols that specify what each staff member should do a point in time in the care of a person, and needs to be able to give a person responsibility, and then when they complete their task continue to run down the protocol, making other things happen for that person (either running algorithms or assigning tasks to the same or other staff members). 

Two current obstacles to progress are that I don't know how to:
-- create a graphical UI where we can watch even the simple scenario above play out (much less do with the more complex clinic app)
-- choose which staff member to interact with when more than one is in the room (I'm hoping creating the UI solves that)

Building this will overcome those two obstacles. After completing this the next two steps will (likely) be to:
1. Add a couple more features to what the staff do (besides just leaving the room) and integrating a rudimentary "vocabulary service."
2. Then take what we've learned and adapt this to work with clinic app. 

Remember:
1. When it is unclear from the spec what to build: Never guess, Always ask.
2. The spec will (almost) always have leave something unclear.

