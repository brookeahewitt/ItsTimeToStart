import tkinter as tk
import datetime as dt
import time
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
# Tkinter checkbox link: https://pythonbasics.org/tkinter-checkbox/


window = tk.Tk()

window.title("Timer")  # Temporary Title
window.geometry("800x600")
window.config(bg="white")


# Menu Code - Start
# - https://www.tutorialspoint.com/python/tk_menu.htm - menus
# - https://www.pythontutorial.net/tkinter/tkinter-menu/ - submenus
def donothing():  # Placeholder Function
    filewin = tk.Toplevel(window)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()


global nameOfTasks
nameOfTasks = []
global startValues
startValues = []
global endValues
endValues = []
global elapsedTimeTotal
elapsedTimeTotal = []
global nameOfGoalTasks
nameOfGoalTasks = []
global secondsGoal
secondsGoal = []
global minsGoal
minsGoal = []
global hoursGoal
hoursGoal = []

global nameOfLimit
nameOfLimit = []
global secondsLimit
secondsLimit = []
global minsLimit
minsLimit = []
global hoursLimit
hoursLimit = []


# source: https://datatofish.com/matplotlib-charts-tkinter-gui/
def bargraph():
    data1 = {'Task': nameOfTasks,
             'Time in Minutes': elapsedTimeTotal
             }
    df1 = DataFrame(data1, columns=['Task', 'Time in Minutes'])
    root = tk.Tk()
    root.title("Time Task Bar Graph")  # Temporary Title
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    df1 = df1[['Task', 'Time in Minutes']].groupby('Task').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Time Spent Per Task')

    # root.mainloop()


global taskNameGoal
taskNameGoal = "Empty"
global taskSecsGoal
taskSecsGoal = 0
global taskMinsGoal
taskMinsGoal = 0
global taskHoursGoal
taskHoursGoal = 0

global goalIndex
goalIndex = 0.4

global limitIndex
limitIndex = 0.4


def setGoals():
    goalWindow = tk.Toplevel(window)
    goalWindow.geometry("800x600")
    goalWindow.title("Set Goals")
    goalWindow.config(bg="white")
    label1 = tk.Label(goalWindow,text="Enter task name: ", bg="white").place(relx=.05,rely=.2)
    taskEntry = tk.Entry(goalWindow)
    taskEntry.place(relx=.2,rely=.2)
    label2 = tk.Label(goalWindow,text="Enter time goal: ", bg= "white").place(relx=.4,rely=.2)
    secondsEntry = tk.Entry(goalWindow)
    secondsEntry.place(relx=.55,rely=.2,width= 30)
    label3 = tk.Label(goalWindow,text=" : ",bg="white").place(relx=.59,rely=.2)
    minsEntry = tk.Entry(goalWindow)
    minsEntry.place(relx=.61,rely=.2,width=30)
    label3 = tk.Label(goalWindow,text=" : ",bg="white").place(relx=.64,rely=.2)
    hoursEntry = tk.Entry(goalWindow)
    hoursEntry.place(relx=.66,rely=.2,width=30)
    taskDetailsName = tk.Label(goalWindow, text="Name: ", background="white")
    taskDetailsName.pack()
    taskDetailsName.place(relx=0.15, rely=goalIndex)

    taskDetailsTime = tk.Label(goalWindow, text="Goal Time: ", background="white")
    taskDetailsTime.pack()
    taskDetailsTime.place(relx=0.35, rely=goalIndex)



    def clearTextForOtherWindow():
        global taskNameGoal
        global taskSecsGoal
        global taskMinsGoal
        global taskHoursGoal
        taskNameGoal = taskEntry.get()
        taskSecsGoal = secondsEntry.get()
        taskMinsGoal = minsEntry.get()
        taskHoursGoal = hoursEntry.get()
        nameOfGoalTasks.append(taskNameGoal)
        secondsGoal.append(taskSecsGoal)
        minsGoal.append(taskMinsGoal)
        hoursGoal.append(taskHoursGoal)
        taskEntry.delete(0, tk.END)
        secondsEntry.delete(0,tk.END)
        minsEntry.delete(0,tk.END)
        hoursEntry.delete(0,tk.END)

        def listGoals():
            # nameOfGoalTasksLabel
            # secondsGoalLabel
            # minsGoalLabel
            # hoursGoalLabel
            global goalIndex

            goalIndex = goalIndex + 0.053

            goalName = taskNameGoal
            goalTime = taskSecsGoal + ":" + taskMinsGoal + ":" + taskHoursGoal

            taskName = tk.Label(goalWindow,text=goalName, background="white")
            taskName.pack()
            taskName.place(relx=0.15, rely=goalIndex)

            taskGT = tk.Label(goalWindow,text=goalTime, background="white")
            taskGT.pack()
            taskGT.place(relx=0.35, rely=goalIndex)

            # taskDetailsST = tk.Label(text="Goal: ", background="white")
            # taskDetailsST.pack()
            # taskDetailsST.place(relx=0.35, rely=y)
            #
            # taskDetailsET = tk.Label(text="End Time:", background="white")
            # taskDetailsET.pack()
            # taskDetailsET.place(relx=0.55, rely=y)
            #
            # taskDetailsTT = tk.Label(text="Total Time:", background="white")
            # taskDetailsTT.pack()
            # taskDetailsTT.place(relx=0.75, rely=y)

        listGoals()

    enterButton = tk.Button(goalWindow, text="Enter", command=clearTextForOtherWindow).place(relx=.4, rely=.3,
                                                                                                 width=70)





global taskNameLimit
taskNameLimit = "Empty"
global taskSecsLimit
taskSecsLimit = 0
global taskMinsLimit
taskMinsLimit = 0
global taskHoursLimit
taskHoursLimit = 0
def setLimits():
    goalWindow = tk.Toplevel(window)
    goalWindow.geometry("800x600")
    goalWindow.title("Set Limits")
    goalWindow.config(bg="white")
    label1 = tk.Label(goalWindow,text="Enter task name: ", bg="white").place(relx=.05,rely=.2)
    taskEntry = tk.Entry(goalWindow)
    taskEntry.place(relx=.2,rely=.2)
    label2 = tk.Label(goalWindow,text="Enter time limit: ", bg= "white").place(relx=.4,rely=.2)
    secondsEntry = tk.Entry(goalWindow)
    secondsEntry.place(relx=.55,rely=.2,width= 30)
    label3 = tk.Label(goalWindow,text=" : ",bg="white").place(relx=.59,rely=.2)
    minsEntry = tk.Entry(goalWindow)
    minsEntry.place(relx=.61,rely=.2,width=30)
    label3 = tk.Label(goalWindow,text=" : ",bg="white").place(relx=.64,rely=.2)
    hoursEntry = tk.Entry(goalWindow)
    hoursEntry.place(relx=.66,rely=.2,width=30)
    taskDetailsName = tk.Label(goalWindow, text="Name: ", background="white")
    taskDetailsName.pack()
    taskDetailsName.place(relx=0.15, rely=goalIndex)
    taskDetailsTime = tk.Label(goalWindow, text="Limit Time: ", background="white")
    taskDetailsTime.pack()
    taskDetailsTime.place(relx=0.35, rely=limitIndex)

    def clearTextForOtherWindow():
        global taskNameLimit
        global taskSecsLimit
        global taskMinsLimit
        global taskHoursLimit
        taskNameLimit = taskEntry.get()
        taskSecsLimit = secondsEntry.get()
        taskMinsLimit = minsEntry.get()
        taskHoursLimit = hoursEntry.get()
        nameOfLimit.append(taskNameLimit)
        secondsLimit.append(taskSecsLimit)
        minsLimit.append(taskMinsLimit)
        hoursLimit.append(taskHoursLimit)
        taskEntry.delete(0, tk.END)
        secondsEntry.delete(0,tk.END)
        minsEntry.delete(0,tk.END)
        hoursEntry.delete(0,tk.END)

        def listLimits():
            # nameOfGoalTasksLabel
            # secondsGoalLabel
            # minsGoalLabel
            # hoursGoalLabel
            global limitIndex

            limitIndex = limitIndex + 0.053

            limitName = taskNameLimit
            limitTime = taskSecsLimit + ":" + taskMinsLimit + ":" + taskHoursLimit

            taskNameL = tk.Label(goalWindow, text=limitName, background="white")
            taskNameL.pack()
            taskNameL.place(relx=0.15, rely=limitIndex)

            taskGT = tk.Label(goalWindow,text=limitTime, background="white")
            taskGT.pack()
            taskGT.place(relx=0.35, rely=limitIndex)

            # taskDetailsST = tk.Label(text="Goal: ", background="white")
            # taskDetailsST.pack()
            # taskDetailsST.place(relx=0.35, rely=y)
            #
            # taskDetailsET = tk.Label(text="End Time:", background="white")
            # taskDetailsET.pack()
            # taskDetailsET.place(relx=0.55, rely=y)
            #
            # taskDetailsTT = tk.Label(text="Total Time:", background="white")
            # taskDetailsTT.pack()
            # taskDetailsTT.place(relx=0.75, rely=y)

        listLimits()

    enterButton = tk.Button(goalWindow, text="Enter", command=clearTextForOtherWindow).place(relx=.4, rely=.3, width=70)




menubar = tk.Menu(window)
optionsmenu = tk.Menu(menubar, tearoff=0)
sub_menu = tk.Menu(optionsmenu, tearoff=0)
sub_menu.add_command(label='Set Goals', command=setGoals)
sub_menu.add_command(label='Set Limits', command=setLimits)
sub_menu.add_command(label='Analyze Goals', command=donothing)

optionsmenu.add_command(label="Task Time Bar Graph", command=bargraph)

optionsmenu.add_cascade(
    label="Task Time Goals",
    menu=sub_menu
)

optionsmenu.add_separator()

optionsmenu.add_command(label="Exit Program", command=window.quit)

menubar.add_cascade(label="Menu", menu=optionsmenu)

window.config(menu=menubar)
# Menu Code - End

greeting = tk.Label(text="Press 'Start Timer' to start logging time.", bg="white")
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

global taskName
taskName = ""

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
        startValues.append(startTime)


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
    endValues.append(endTime)

global y
y = 0.68

taskDetailsN = tk.Label(text="Name:", background="white")
taskDetailsN.pack()
taskDetailsN.place(relx=0.15, rely=y)

taskDetailsST = tk.Label(text="Start Time:", background="white")
taskDetailsST.pack()
taskDetailsST.place(relx=0.35, rely=y)

taskDetailsET = tk.Label(text="End Time:", background="white")
taskDetailsET.pack()
taskDetailsET.place(relx=0.55, rely=y)

taskDetailsTT = tk.Label(text="Total Time:", background="white")
taskDetailsTT.pack()
taskDetailsTT.place(relx=0.75, rely=y)
def displayOutput():
    # print(taskName + "\t" + time.strftime('%H:%M:%S', time.localtime(startTime)) + "\t" + time.strftime("%H:%M:%S",
    # time.localtime(endTime)) + "\t" + time.strftime("%H:%M:%S", time.gmtime(totalTime)))
    global y
    y = y + 0.053
    minutes = totalTime / 60
    hours = minutes / 60
    elapsedTimeTotal.append(minutes)
    name = taskName
    start = time.strftime("%H:%M:%S", time.localtime(startTime))
    end = time.strftime("%H:%M:%S", time.localtime(endTime))
    allTime = time.strftime("%H:%M:%S", time.gmtime(totalTime))

    taskN = tk.Label(text=name, background="white")
    taskN.pack()
    taskN.place(relx=0.15, rely=y)

    taskST = tk.Label(text=start, background="white")
    taskST.pack()
    taskST.place(relx=0.35, rely=y)

    taskET = tk.Label(text=end, background="white")
    taskET.pack()
    taskET.place(relx=0.55, rely=y)

    taskTT = tk.Label(text=allTime, background="white")
    taskTT.pack()
    taskTT.place(relx=0.75, rely=y)

    taskTT = tk.Label(text=allTime, background="white")
    taskTT.pack()
    taskTT.place(relx=0.75, rely=y)


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
    width=12,
    height=2,
    bg="gold3",
    fg="white",
    command=pauseTime
)

pauseButton.pack()
pauseButton.place(relx=.448, rely=.5)


def changeButtonName(name):
    pauseButton['text'] = name


askTaskName = tk.Label(text="Enter the name of the task below.", bg="white")
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

    nameOfTasks.append(taskName)
    entry.delete(0, tk.END)
    addCurrentlyWorkingOn()


# Clock Code - start
# https://bytes.com/topic/python/answers/629499-dynamically-displaying-time-using-tkinter-label - source
time1 = ''
clock = tk.Label(window, font=('times', 20, 'bold'), bg='white')
clock.pack()
clock.place(relx=.328, rely=.6)


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
        # time1 = time2
        time3 = time2 - startTime - pauseTimeDuration
        time4 = time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(time3))
        if showTimer == 1:
            clock.config(text=time4)
        else:
            clock.config(text="")
        totalTime = time3
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)


# Clock Code - end


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

global currentlyWorkingOn
currentlyWorkingOn = tk.Label(text="", bg="white")


def addCurrentlyWorkingOn():
    global currentlyWorkingOn
    currentlyWorkingOn.destroy()
    if (not (taskName == "" or not taskName.strip())):
        currentlyWorkingOn = tk.Label(text="Currently working on: " + taskName, bg="white")
    currentlyWorkingOn.pack()
    currentlyWorkingOn.place(relx=.42, rely=.4)


taskKeyList = []
minutesValueList = []
for key in taskDict:
    taskKeyList.append(key)

data1 = {'Task': taskKeyList,
         'Time in Minutes': minutesValueList
         }


window.mainloop()

