import tkinter as tk
import time

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/



window = tk.Tk()

window.title("Timer")  # Temporary Title

window.geometry("800x600")

greeting = tk.Label(text = "Press 'Start Timer' to start logging time.")
greeting.pack()

label = tk.Label(
    text="Press 'Stop Timer' to stop logging time.",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()


def setStartTime():
    global startTime
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
    endTime = time.time()
    global totalTime
    totalTime = endTime - startTime
    displayOutput()
    taskDict[taskName] = time.strftime("%H:%M:%S", time.gmtime(totalTime))







def displayOutput():
    print(taskName + "\t" + time.strftime('%H:%M:%S', time.localtime(startTime)) + "\t" + time.strftime("%H:%M:%S",
                                time.localtime(endTime)) + "\t" + time.strftime("%H:%M:%S", time.gmtime(totalTime)))


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

askTaskName = tk.Label(text="Enter the name of the task below.")
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
        currentlyWorkingOn = tk.Label(text="Currently working on: " + taskName)
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
