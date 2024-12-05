from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog
config = {}

# Graphs
# added labels and adjust spacing between graphs
fig1, ax1 = plt.subplots(figsize=(3, 2))
fig1.tight_layout()
ax1.set_title("Wavefrom")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")

fig2, ax2 = plt.subplots(figsize=(3, 2))
ax2.set_title("Low Frequency")
fig2.tight_layout()
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Amplitude")

fig3, ax3 = plt.subplots(figsize=(3, 2))
ax3.set_title("Mid Frequency")
fig3.tight_layout()
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Amplitude")

fig4, ax4 = plt.subplots(figsize=(3, 2))
ax4.set_title("High Frequency")
fig4.tight_layout()
ax4.set_xlabel("Time (s)")
ax4.set_ylabel("Amplitude")

fig5, ax5 = plt.subplots(figsize=(3, 2))
ax5.set_title("graph5")
fig5.tight_layout()
ax5.set_xlabel("Time (s)")
ax5.set_ylabel("Amplitude")

fig6, ax6 = plt.subplots(figsize=(3, 2))
ax6.set_title("graph6")
fig6.tight_layout()
ax6.set_xlabel("Time (s)")
ax6.set_ylabel("Amplitude")

#function for load button
def file_load():
    filedialog.askopenfilename()

if __name__ == "__main__":
    _root = tk.Tk()
    _root.configure(bg="white")
    #newbutton
    load_button = Button(_root, text="Load file",height=5,command=file_load)
    load_button.pack(side="left",padx=5)

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