import tkinter as tk
#Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
window = tk.Tk()

window.title("Timer") #Temporary Title

window.geometry("500x300")

greeting = tk.Label(text = "Press 'Start' to start logging time")
greeting.pack()

label = tk.Label(
    text="Press 'Stop' to stop logging time",
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
startButton.place(x=100, y=100)

stopButton = tk.Button(
    text="Stop Timer",
    width=10,
    height=2,
    bg="red",
    fg="white",
)
stopButton.pack()
stopButton.place(x=300, y=100)

window.mainloop()