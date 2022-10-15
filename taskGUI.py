import tkinter as tk
#Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/

window = tk.Tk()

window.title("Timer") #Temporary Title

window.geometry("500x300")

greeting = tk.Label(text = "Press 'Start' to start logging time.")
greeting.pack()

label = tk.Label(
    text="Press 'Stop' to stop logging time.",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()


startButton = tk.Button(
    text="Start Timer",
    width=10,
    height=2,
    bg="green",
    fg="white",

)
startButton.pack()
startButton.place(x=100, y=150)

stopButton = tk.Button(
    text="Stop Timer",
    width=10,
    height=2,
    bg="red",
    fg="white",
)
stopButton.pack()
stopButton.place(x=317, y=150)

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
submitButton.place(x=195, y=100)

def addCurrentlyWorkingOn():
    currentlyWorkingOn = tk.Label(text = "Currently working on: " + taskName)
    currentlyWorkingOn.pack()
    currentlyWorkingOn.place(x=200, y=200)

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

