import tkinter as tk
from tkinter import LEFT

from PIL import Image, ImageTk


class SuccessFrame(tk.Frame):
    # Contains all display features for the success frame
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # Creates the Back Button
        orig_back_image = Image.open("../images/arrow.png").resize((10, 15))
        back_image = ImageTk.PhotoImage(orig_back_image)
        self.back_image_button = tk.Button(self, image=back_image, borderwidth=1, cursor="hand2", text=' Back',
                                           font=("Helvetica", 10), compound=LEFT)
        self.back_image_button.image = back_image
        self.back_image_button.grid(row=0, column=0, padx=(10, 0))
        # Creates the title and instruction labels
        merge_title_label = tk.Label(self, text="PDF Merger", font=("Helvetica", 20, "bold"))
        success_instruction_label = tk.Label(self, text="Success!", font=("Helvetica", 15))
        merge_title_label.grid(row=0, column=1, columnspan=4, padx=(100, 0), pady=(20, 0))
        success_instruction_label.grid(row=1, column=1, columnspan=4, padx=(100, 0), pady=(10, 50))