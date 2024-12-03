from tkinter import *
from tkinter import ttk,filedialog,messagebox
config = {}



if __name__ == "__main__":
    _root = Tk()

    mainframe = ttk.Frame(_root, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    _root.title('Interactive Data Acoustic Modeling')
    load_button = Button(_root, text="Load")




    _root.mainloop()