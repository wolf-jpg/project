from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

config = {}

# Graphs
fig1, ax1 = plt.subplots(figsize=(3, 2))
ax1.set_title("Wavefrom")

fig2, ax2 = plt.subplots(figsize=(3, 2))
ax2.set_title("Low Frequency")

fig3, ax3 = plt.subplots(figsize=(3, 2))
ax3.set_title("Mid Frequency")

fig4, ax4 = plt.subplots(figsize=(3, 2))
ax4.set_title("High Frequency")

fig5, ax5 = plt.subplots(figsize=(3, 2))
ax5.set_title("graph5")

fig6, ax6 = plt.subplots(figsize=(3, 2))
ax6.set_title("graph6")

if __name__ == "__main__":
    _root = tk.Tk()
    # Mainframe setup (commented out in your example)
    """
    mainframe = ttk.Frame(_root, padding="20 20 20 20")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    # Title and size of application
    _root.geometry("1200x900")
    _root.title('Interactive Data Acoustic Modeling')
    # Load button
    load_button = Button(_root, text="Load")
    load_button.grid(column=1, row=0, padx=10, pady=20)
    """


    # Mou Changes:

    #Create windows and charts
    _root.title("SPIDAM - Acoustic Modeling")
    _root.state('zoomed') #this makes sure the window is maxed in the screen.

    #Creates the upper frame to hold: Graph 1&2
    upper_frame = tk.Frame(_root) #root is the parent of upper frame
    upper_frame.pack(fill="both", expand=True) #both makes sure it uses both x and y, expand maximized the space

    middle_frame = tk.Frame(_root)
    middle_frame.pack(fill="both", expand=True)

    lower_frame = tk.Frame(_root)
    lower_frame.pack(fill="both", expand=True)

    #They are stacked so Since upper goes first it will be loaded/stacked first and their graphs will appear on top.


    #Upper Section
    # Create canvases for each figure
    canvas1 = FigureCanvasTkAgg(fig1, upper_frame) #figure one. upper frame is the parent of this widget
    canvas1.draw() #draws the graph
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

    #Middle Section

    # Create canvases for each figure
    canvas3 = FigureCanvasTkAgg(fig3, middle_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas4 = FigureCanvasTkAgg(fig4, middle_frame)
    canvas4.draw()
    canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

    #Lower section

    # Create canvases for each figure
    canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas6 = FigureCanvasTkAgg(fig6, lower_frame)
    canvas6.draw()
    canvas6.get_tk_widget().pack(side="left", fill="both", expand=True)





    # Start the Tkinter main loop
    _root.mainloop()
