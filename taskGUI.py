import tkinter as tk
import datetime as dt
import time
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
# Tkinter checkbox link: https://pythonbasics.org/tkinter-checkbox/
import graph

window = tk.Tk()

window.title("Timer")  # Temporary Title
window.geometry("800x600")
window.config(bg = "white")

#Menu Code - Start
# - https://www.tutorialspoint.com/python/tk_menu.htm - menus
# - https://www.pythontutorial.net/tkinter/tkinter-menu/ - submenus
def donothing(): #Placeholder Function
   filewin = tk.Toplevel(window)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()


def bargraph():
    data1 = {'Task': ['US', 'CA', 'GER', 'UK', 'FR'],
         'Time in Minutes': [45000, 42000, 52000, 49000, 47000]
         }
    df1 = DataFrame(data1, columns=['Task', 'Time in Minutes'])
    root = tk.Tk()
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Task', 'Time in Minutes']].groupby('Task').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Time Spent Per Task')
    #root.mainloop()

def piechart():
    def piechart():
        minutes = np.array([35, 25, 25, 15])
        completedtasks = ["Apples", "Bananas", "Cherries", "Dates"]

        plt.pie(minutes, labels=completedtasks)
        plt.show()


menubar = tk.Menu(window)
optionsmenu = tk.Menu(menubar, tearoff=0)
sub_menu = tk.Menu(optionsmenu, tearoff=0)
sub_menu.add_command(label='Pie Graph', command = piechart)
sub_menu.add_command(label='Bar Graph', command = bargraph)

optionsmenu.add_cascade(
    label="Task Time Graphs",
    menu=sub_menu
)

optionsmenu.add_command(label="Task Time Goals")

optionsmenu.add_separator()

optionsmenu.add_command(label="Exit Program", command=window.quit)


menubar.add_cascade(label="Menu", menu=optionsmenu)
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
global doTick
timerStarted = 0
doTick = 1

global pauseBeginning
global pauseEnd
global pauseTimeDuration
pauseBeginning = 0
pauseEnd = 0
pauseTimeDuration = 0

def setStartTime():
    global timerStarted
    global startTime
    global taskName
    if (taskName == "" or not taskName.strip()):
        warningLabel = tk.Label(
            text="(Please enter task)",
            foreground="red",
            background="white",
        )
        warningLabel.pack()
        window.after(1500, warningLabel.destroy)
    else:
        timerStarted = 1
        startTime = time.time()
        tick()
        global doTick
        doTick = 1



startButton = tk.Button(
    text="Start Timer",
    width=10,
    height=2,
    bg="green",
    fg="white",
    command=setStartTime

)
startButton.pack()
startButton.place(relx=.3, rely=.5)

global endTime
global totalTime
totalTime = 0

def setEndTime():
    global endTime
    global timerStarted
    global doTick
    endTime = time.time()
    if timerStarted == 0:
        timerStartedFalseLabel = tk.Label(
            text="(Please start timer first)",
            foreground="red",
            background="white",
        )
        timerStartedFalseLabel.pack()
        timerStartedFalseLabel.place(relx=.575, rely=.58)
        window.after(1500, timerStartedFalseLabel.destroy)
    displayOutput()
    taskDict[taskName] = time.strftime("%H:%M:%S", time.gmtime(totalTime))
    timerStarted = False
    doTick = 0



def displayOutput():
    #print(taskName + "\t" + time.strftime('%H:%M:%S', time.localtime(startTime)) + "\t" + time.strftime("%H:%M:%S",
                                #time.localtime(endTime)) + "\t" + time.strftime("%H:%M:%S", time.gmtime(totalTime)))
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
    command=setEndTime

)

stopButton.pack()
stopButton.place(relx=.6, rely=.5)

global pause
pause = 0
def pauseTime():
    global pause
    global timerStarted
    if timerStarted == 0:
        timerStartedFalseLabel = tk.Label(
            text="(Please start timer first)",
            foreground="red",
            background="white",
        )
        timerStartedFalseLabel.pack()
        timerStartedFalseLabel.place(relx=.42, rely=.58)
        window.after(1500, timerStartedFalseLabel.destroy)
    else:
        if pause == 0:
            pause = 1
            changeButtonName("Resume Timer")
            pauseTime(1)
        else:
            pause = 0
            changeButtonName("Pause Timer")
            pauseTime(0)
        tick()

pauseButton = tk.Button(
    text="Pause Timer",
    width=10,
    height=2,
    bg="gold3",
    fg="white",
    command=pauseTime
)

pauseButton.pack()
pauseButton.place(relx=.448, rely=.5)

def changeButtonName(name):
    pauseButton['text'] = name

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

def pauseTime(ispaused):
    global pauseBeginning
    global pauseEnd
    global pauseTimeDuration
    if ispaused == 1:
        pauseBeginning = time.time()
    else:
        pauseEnd = time.time()
        pauseTimeDuration = pauseTimeDuration + pauseEnd - pauseBeginning
global showTimer
showTimer = 1
def print_selection():
    global showTimer
    if var1.get() == 1:
        showTimer = 0
    else:
        showTimer = 1

var1 = tk.IntVar()
dontShowTimer = tk.Checkbutton(window, text="Don't show timer", variable=var1, onvalue=1, offvalue=0,
                               command=print_selection)
dontShowTimer.pack()

def tick():
    global totalTime
    # get the current local time from the PC
    if doTick != 1:
        return
    time2 = time.time()
    if pause == 1:
        return
    # if time string has changed, update it
    if time2 != startTime:
        #time1 = time2
        time3 = time2-startTime-pauseTimeDuration
        time4 = time.strftime("%H:%M:%S", time.gmtime(time3))
        if showTimer == 1:
            clock.config(text=time4)
        else:
            clock.config(text="")
        totalTime = time3
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)
#Clock Code - end


submitButton = tk.Button(
    text="Submit Task Name",
    width=16,
    height=2,
    bg="blue",
    fg="white",
    command=clearText
)
submitButton.pack()

submitButton.place(relx=.43, rely=.3)


def addCurrentlyWorkingOn():
    if(not(taskName == "" or not taskName.strip())):
        currentlyWorkingOn = tk.Label(text="Currently working on: " + taskName, bg = "white")
    currentlyWorkingOn.pack()
    currentlyWorkingOn.place(relx = .42, rely = .4)


taskKeyList = []
minutesValueList = []
for key in taskDict:
    taskKeyList.append(key)

data1 = {'Task': taskKeyList,
         'Time in Minutes': minutesValueList
         }

# df1 = DataFrame(data1, columns=['Task', 'Time in Minutes'])
#
# root = tk.Tk()

# figure1 = plt.Figure(figsize=(6, 5), dpi=100)
# ax1 = figure1.add_subplot(111)
# bar1 = FigureCanvasTkAgg(figure1, root)
# bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df1 = df1[['Task', 'Time in Minutes']].groupby('Task').sum()
# df1.plot(kind='bar', legend=True, ax=ax1)
# ax1.set_title('Time Spent Per Task')

window.mainloop()
print(taskDict)
print(taskKeyList)
print(data1)

# tk = Tk()
# frame = Frame(tk, borderwidth=2)
# frame.pack(fill=BOTH, expand=1)
# label = Label(frame, text="Button Example")
# label.pack(fill=X, expand=1)
#
# button = Button(frame, text="Exit", command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()
