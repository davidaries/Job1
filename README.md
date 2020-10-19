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
