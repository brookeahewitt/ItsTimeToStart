import tkinter as tk
import datetime as dt
import time

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/



window = tk.Tk()

window.title("Timer")  # Temporary Title
window.geometry("800x600")
window.config(bg = "white")

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
    totalTime = endTime - startTime
    displayOutput()
    taskDict[taskName] = time.strftime("%H:%M:%S", time.gmtime(totalTime))
    if timerStarted == 0:
        timerStartedFalseLabel = tk.Label(
            text="(Please start timer first)",
            foreground="red",
            background="white",
        )
        timerStartedFalseLabel.pack()
        timerStartedFalseLabel.place(relx=.6, rely=.55)
        window.after(1500, timerStartedFalseLabel.destroy)
        print("You haven't started the timer yet.")
    timerStarted = False



def displayOutput():
    print(taskName + "\t" + time.strftime('%H:%M:%S', time.localtime(startTime)) + "\t" + time.strftime("%H:%M:%S",
                                time.localtime(endTime)) + "\t" + time.strftime("%H:%M:%S", time.gmtime(totalTime)))
    minutes = totalTime / 60
    hours = minutes / 60
    totalTimeLabel = tk.Label(
        text = "Elapsed time: " + str(round(minutes, 2)) + " minutes.",
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


def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)


tick()

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
