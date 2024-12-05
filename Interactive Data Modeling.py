from tkinter import *
from tkinter import ttk,filedialog,messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
config = {}



if __name__ == "__main__":
    _root = Tk()
    #mainframe
    mainframe = ttk.Frame(_root, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    #title and size of application
    _root.geometry("1200x900")
    _root.title('Interactive Data Acoustic Modeling')
    #load button
    load_button = Button(_root, text="Load")
    load_button.grid(column=1, row=0, padx=10, pady=20)

    #graph 1

    fig1, ax1 = plt.subplots(figsize=(3, 2))
    ax1.set_title("graph1")

    canvas = FigureCanvasTkAgg(fig1, mainframe)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=2, columnspan=2, padx=10, pady=10)



    _root.mainloop()