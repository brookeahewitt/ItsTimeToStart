import numpy
from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np




def piechart():
    root = tk.Tk()

    def prop(n):
        return 360.0 * n / 1000

    tk.Label(root, text='Pie Chart').pack()
    c = tk.Canvas(width=154, height=154)
    c.pack()
    c.create_arc((2, 2, 152, 152), fill="#FAF402", outline="#FAF402", start=prop(0), extent=prop(200))
    c.create_arc((2, 2, 152, 152), fill="#2BFFF4", outline="#2BFFF4", start=prop(200), extent=prop(400))
    c.create_arc((2, 2, 152, 152), fill="#E00022", outline="#E00022", start=prop(600), extent=prop(50))
    c.create_arc((2, 2, 152, 152), fill="#7A0871", outline="#7A0871", start=prop(650), extent=prop(200))
    c.create_arc((2, 2, 152, 152), fill="#294994", outline="#294994", start=prop(850), extent=prop(150))

    root.mainloop()


piechart()

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
    root.mainloop()


