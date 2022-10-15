import tkinter as tk
#Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
window = tk.Tk()

greeting = tk.Label(text = "Hello, Tkinter")
greeting.pack()

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