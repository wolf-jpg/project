from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

config = {}

frequency = 0

def toggle_frequency():
    global frequency
    frequency += 1
    if frequency > 2:
        frequency = 0
    update_canvas()

def update_canvas():
    global frequency
    for widget in middle_frame.winfo_children():
        widget.destroy()

    if frequency == 0:
        canvas2 = FigureCanvasTkAgg(fig2, middle_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)
    elif frequency == 1:
        canvas3 = FigureCanvasTkAgg(fig3, middle_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)
    elif frequency == 2:
        canvas4 = FigureCanvasTkAgg(fig4, middle_frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

# Graphs
fig1, ax1 = plt.subplots(figsize=(3, 2))
ax1.set_title("Waveform")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")

fig2, ax2 = plt.subplots(figsize=(3, 2))
ax2.set_title("Low Frequency")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Amplitude")

fig3, ax3 = plt.subplots(figsize=(3, 2))
ax3.set_title("Mid Frequency")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Amplitude")


fig4, ax4 = plt.subplots(figsize=(3, 2))
ax4.set_title("High Frequency")
ax4.set_xlabel("Time (s)")
ax4.set_ylabel("Amplitude")

fig5, ax5 = plt.subplots(figsize=(3, 2))
ax5.set_title("Frequency Response")
ax5.set_xlabel("Time (s)")
ax5.set_ylabel("Amplitude")

fig6, ax6 = plt.subplots(figsize=(3, 2))
ax6.set_title("Combined RT60 Comparison")
ax6.set_xlabel("Time (s)")
ax6.set_ylabel("Amplitude")


def file_load():
    filedialog.askopenfilename()


if __name__ == "__main__":
    _root = tk.Tk()



    _root.configure(bg="white")



    # Create windows and charts
    _root.title("SPIDAM - Acoustic Modeling")
    _root.state('zoomed')  # this makes sure the window is maximized on the screen.
    #Creates the button frame
    button_frame = ttk.Frame(_root)
    button_frame.pack(side='top', pady=10)
    # Create frames to hold the canvases
    upper_frame = tk.Frame(_root)  # _root is the parent of upper_frame
    upper_frame.pack(fill="both", expand=True)  # both makes sure it uses both x and y, expand maximizes the space

    middle_frame = tk.Frame(_root)
    middle_frame.pack(fill="both", expand=True)

    lower_frame = tk.Frame(_root)
    lower_frame.pack(fill="both", expand=True)


    #Buttons
    # load button
    load_button = ttk.Button(button_frame, text="Load file", command=file_load)
    load_button.pack(side='left', pady=10)

    # Toggle button
    _fetch_btn = ttk.Button(button_frame, text='Analyze')  #add command= function-name
    _fetch_btn.pack(side='left', pady=10)

    #Toggle button
    _fetch_btn = ttk.Button(button_frame,text='Toggle Frequency', command=toggle_frequency)
    _fetch_btn.pack(side='left', pady=10)



    #Graphs
    # Upper Section
    # Create canvases for each figure
    canvas1 = FigureCanvasTkAgg(fig1, upper_frame)  # figure one. upper_frame is the parent of this widget
    canvas1.draw()  # draws the graph
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)





    # Lower Section
    # Create canvases for each figure
    canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas6 = FigureCanvasTkAgg(fig6, lower_frame)
    canvas6.draw()
    canvas6.get_tk_widget().pack(side="left", fill="both", expand=True)

    # Initialize the canvas in the middle frame
    update_canvas()

    # Start the Tkinter main loop
    _root.mainloop()
