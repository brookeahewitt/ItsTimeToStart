import tkinter as tk
#Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
window = tk.Tk()

window.title("Timer") #Temporary Title

window.geometry("500x300")

greeting = tk.Label(text = "Hello, Tkinter")
greeting.pack()

label = tk.Label(
    text="Hello, Tkinter",
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

# tk = Tk()
# frame = Frame(tk, borderwidth=2)
# frame.pack(fill=BOTH, expand=1)
# label = Label(frame, text="Button Example")
# label.pack(fill=X, expand=1)
#
# button = Button(frame, text="Exit", command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()