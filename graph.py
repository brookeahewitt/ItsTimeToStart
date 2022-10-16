from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def piechart() :
    minutes = np.array([35, 25, 25, 15])
    completedtasks = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(minutes, labels = completedtasks)
    plt.show()

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

bargraph()