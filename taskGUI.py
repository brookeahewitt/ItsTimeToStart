import tkinter as tk
import datetime as dt
import time

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/



window = tk.Tk()

window.title("Timer")  # Temporary Title
window.geometry("800x600")
window.config(bg = "white")

#Menu Code - Start
# - https://www.tutorialspoint.com/python/tk_menu.htm
def donothing():
   filewin = tk.Toplevel(window)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
#Menu Code - End

greeting = tk.Label(text = "Press 'Start Timer' to start logging time.", bg = "white")
greeting.pack()

label = tk.Label(
    text="Press 'Stop Timer' to stop logging time.",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

global startTime
global timerStarted
timerStarted = 0

def setStartTime():
    global timerStarted
    global startTime
    timerStarted = 1
    startTime = time.time()
    tick()



startButton = tk.Button(
    text="Start Timer",
    width=10,
    height=2,
    bg="green",
    fg="white",
    command = setStartTime

)
startButton.pack()
startButton.place(relx=.3, rely=.5)


global endTime

def setEndTime():
    global endTime
    global timerStarted
    endTime = time.time()
    global totalTime
    if timerStarted == 0:
        timerStartedFalseLabel = tk.Label(
            text="(Please start timer first)",
            foreground="red",
            background="white",
        )
        timerStartedFalseLabel.pack()
        timerStartedFalseLabel.place(relx=.575, rely=.58)
        window.after(1500, timerStartedFalseLabel.destroy)
        print("You haven't started the timer yet.")
    totalTime = endTime - startTime
    displayOutput()
    taskDict[taskName] = time.strftime("%H:%M:%S", time.gmtime(totalTime))
    timerStarted = False



def displayOutput():
    print(taskName + "\t" + time.strftime('%H:%M:%S', time.localtime(startTime)) + "\t" + time.strftime("%H:%M:%S",
                                time.localtime(endTime)) + "\t" + time.strftime("%H:%M:%S", time.gmtime(totalTime)))
    minutes = totalTime / 60
    hours = minutes / 60
    totalTimeLabel = tk.Label(
        #text = "Elapsed time: " + str(round(minutes, 2)) + " minutes.",
        text = "Elapsed time: " + time.strftime("%H:%M:%S", time.gmtime(totalTime)),
        foreground="black",
        background="white"
    )
    totalTimeLabel.pack()
    totalTimeLabel.place(relx=.44, rely=.7)


stopButton = tk.Button(
    text="Stop Timer",
    width=10,
    height=2,
    bg="red",
    fg="white",
    command = setEndTime

)

stopButton.pack()
stopButton.place(relx=.6, rely=.5)

askTaskName = tk.Label(text="Enter the name of the task below.", bg = "white")
entry = tk.Entry()


askTaskName.pack()
entry.pack()

taskDict = {}


def clearText():
    global taskName
    taskName = entry.get()
    if (taskName == "" or not taskName.strip()):
        warningLabel = tk.Label(
            text="(Please enter task)",
            foreground="red",
            background="white",
        )
        warningLabel.pack()
        window.after(1500, warningLabel.destroy)

    taskDict[entry.get()] = None
    entry.delete(0, tk.END)
    addCurrentlyWorkingOn()

# Clock Code - start
# https://bytes.com/topic/python/answers/629499-dynamically-displaying-time-using-tkinter-label - source
time1 = ''
clock = tk.Label(window, font=('times', 20, 'bold'), bg='white')
clock.pack()
clock.place(relx=.44, rely=.8)

def tick():
    #global time1
    # get the current local time from the PC
    time2 = time.time()
    #time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != startTime:
        #time1 = time2
        time3 = time2-startTime
        time4 = time.strftime("%H:%M:%S", time.gmtime(time3))
        clock.config(text=time4)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)
#Clock Code - end


submitButton = tk.Button(
    text="Submit Task Name",
    width=14,
    height=2,
    bg="blue",
    fg="white",
    command=clearText
)
submitButton.pack()

submitButton.place(relx=.45, rely=.3)


def addCurrentlyWorkingOn():
    if(not(taskName == "" or not taskName.strip())):
        currentlyWorkingOn = tk.Label(text="Currently working on: " + taskName, bg = "white")
    currentlyWorkingOn.pack()
    currentlyWorkingOn.place(relx = .42, rely = .4)


window.mainloop()
print(taskDict)

# tk = Tk()
# frame = Frame(tk, borderwidth=2)
# frame.pack(fill=BOTH, expand=1)
# label = Label(frame, text="Button Example")
# label.pack(fill=X, expand=1)
#
# button = Button(frame, text="Exit", command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()
