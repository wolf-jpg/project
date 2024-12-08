from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import wave
from pathlib import Path
from scipy.io import wavfile
from pydub import AudioSegment
from scipy.signal import welch, butter, filtfilt

class Model:
    def __init__(self):
        self.file = None
        self.data = None
        self.samplerate = None
        self.mono = None
        self.duration = None
        self.res_freq = None
        self.selected_freq = 0

model = Model()
info_str = ""

def low_pass(data, cut, fs):
    nyq = 0.5 * fs
    normal_cut = cut / nyq
    b, a = butter(4, normal_cut, btype='lowpass')
    return filtfilt(b,a,data)

def high_pass(data, cut, fs):
    nyq = 0.5 * fs
    normal_cut = cut / nyq
    b, a = butter(4, normal_cut, btype='highpass')
    return filtfilt(b,a,data)

def digital_to_decibel(signal):
    ref = 1
    if signal != 0:
        return 20 * np.log10(abs(signal) / ref)
    else:
        return -60

def toggle_frequency():
    global model
    model.selected_freq += 1
    if model.selected_freq > 2:
        model.selected_freq = 0
    update_canvas()

def update_canvas():
    global model
    for widget in middle_frame.winfo_children():
        widget.destroy()

    if model.selected_freq == 0:
        canvas2 = FigureCanvasTkAgg(fig2, middle_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)
    elif model.selected_freq == 1:
        canvas3 = FigureCanvasTkAgg(fig3, middle_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)
    elif model.selected_freq == 2:
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
    global model
    new_model = Model()
    new_model.file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
    if new_model.file:
        ext = Path(new_model.file).suffix.lower()
        if ext == ".wav":
            new_model.samplerate, new_model.data = wavfile.read(new_model.file)
        elif ext == ".mp3":
            AudioSegment.from_mp3(new_model.file).export("convert.wav", format="wav")
            new_model.samplerate,new_model.data = wavfile.read(new_model.file)
            Path("convert.wav").unlink()
        else:
            print("Invalid file type")
        if len(new_model.data.shape) > 1:
            new_model.mono = np.array([(x[0] + x[1]) / 2 for x in new_model.data]).astype(np.int16)
        else:
            new_model.mono = new_model.data
        new_model.duration = model.data.shape[0] / model.samplerate
        model = new_model

    try:
        with wave.open(model.file, "rb") as new_file:
            frame = new_file.getnframes()
            frame = new_file.readframes(frame)
            wave_graph = np.frombuffer(frame, dtype=np.int16)

            ax1.plot(wave_graph)
            canvas1.draw()
    except FileNotFoundError:
        messagebox.showerror("Error", "Could not display waveform.")

def analyze():
    global model


if __name__ == "__main__":
    _root = tk.Tk()
    _root.configure(bg="white")

    # Create windows and charts
    _root.title("SPIDAM - Acoustic Modeling")

    # Create the button frame
    button_frame = ttk.Frame(_root)
    button_frame.pack(side='top', pady=10)

    # Create frames to hold the canvases
    upper_frame = tk.Frame(_root)  # _root is the parent of upper_frame
    upper_frame.pack(fill="both", expand=True)  # 'both' makes sure it uses both x and y, expand maximizes the space

    middle_frame = tk.Frame(_root)
    middle_frame.pack(fill="both", expand=True)

    lower_frame = tk.Frame(_root)
    lower_frame.pack(fill="both", expand=True)

    # Buttons
    load_button = ttk.Button(button_frame, text="Load file", command=file_load)
    load_button.pack(side='left', pady=10)

    file_name = ttk.Label(button_frame, text="No file chosen")
    file_name.pack(side='left', pady=10)

    analyze_button = ttk.Button(button_frame, text='Analyze', command=analyze)
    analyze_button.pack(side='left', pady=10)

    toggle_button = ttk.Button(button_frame, text='Toggle Frequency', command=toggle_frequency)
    toggle_button.pack(side='left', pady=10)

    # Graphs
    # Upper Section
    canvas1 = FigureCanvasTkAgg(fig1, upper_frame)  # figure one. upper_frame is the parent of this widget
    canvas1.draw()  # draws the graph
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    # Lower Section
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
