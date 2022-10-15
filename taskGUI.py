import tkinter as tk
import time
#Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/

window = tk.Tk()

window.title("Timer") #Temporary Title

window.geometry("800x600")

greeting = tk.Label(text = "Press 'Start Timer' to start logging time.")
greeting.pack()

label = tk.Label(
    text="Press 'Stop Timer' to stop logging time.",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

global startTime
def setStartTime():
    global startTime
    startTime = time.time()

startButton = tk.Button(
    text="Start Timer",
    width=10,
    height=2,
    bg="green",
    fg="white",
    command = setStartTime()
)
startButton.pack()
startButton.place(relx=.3, rely=.5)

global endTime
def setEndTime():
    global endTime
    endTime = time.time()

def setTotalTime():
    global startTime
    global endTime
    setEndTime()
    totalTime = startTime - endTime
    print(totalTime)

stopButton = tk.Button(
    text="Stop Timer",
    width=10,
    height=2,
    bg="red",
    fg="white",
    command = setTotalTime(),
)

stopButton.pack()
stopButton.place(relx = .6, rely=.5)

askTaskName = tk.Label(text="Enter the name of the task below.")
entry = tk.Entry()
askTaskName.pack()
entry.pack()
def clearText():
    global taskName
    taskName = entry.get()
    entry.delete(0, tk.END)
    addCurrentlyWorkingOn()

submitButton = tk.Button(
    text="Submit Task Name",
    width=14,
    height=2,
    bg="blue",
    fg="white",
    command = clearText
)
submitButton.pack()

submitButton.place(relx=.45, rely=.3)


def addCurrentlyWorkingOn():
    currentlyWorkingOn = tk.Label(text = "Currently working on: " + taskName)
    currentlyWorkingOn.pack()
    currentlyWorkingOn.place(relx = .42, rely = .4)


window.mainloop()

# tk = Tk()
# frame = Frame(tk, borderwidth=2)
# frame.pack(fill=BOTH, expand=1)
# label = Label(frame, text="Button Example")
# label.pack(fill=X, expand=1)
#
# button = Button(frame, text="Exit", command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()

