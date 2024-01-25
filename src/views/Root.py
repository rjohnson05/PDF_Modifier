import tkinter as tk
from functools import partial


class Root(tk.Tk):
    # Serves as the root frame that all other frames sit within
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("PDF Modifier")
