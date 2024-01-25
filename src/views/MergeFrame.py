import tkinter as tk
from tkinter import LEFT

from PIL import Image, ImageTk


class MergeFrame(tk.Frame):
    # Contains all display features for the merge frame
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.constant_widgets = ["!button", "!label", "!label2", "!button2", "!button3", "!label3", "!label4"]
        self.order_boxes_list = []

        # Creates the Back Button
        orig_back_image = Image.open("../images/arrow.png").resize((10, 15))
        back_image = ImageTk.PhotoImage(orig_back_image)
        self.back_image_button = tk.Button(self, image=back_image, borderwidth=1, cursor="hand2", text=' Back',
                                           font=("Helvetica", 10), compound=LEFT)
        self.back_image_button.image = back_image
        self.back_image_button.grid(row=0, column=0, padx=(10, 0))

        # Creates the title and instruction labels
        merge_title_label = tk.Label(self, text="PDF Merger", font=("Helvetica", 20, "bold"))
        merge_instruction_label = tk.Label(self, text="Load the PDF files you wish to merge below.",
                                           font=("Helvetica", 15))
        merge_title_label.grid(row=0, column=1, columnspan=3, pady=(20, 0), sticky='we')
        merge_instruction_label.grid(row=1, column=1, columnspan=4, pady=(10, 50), sticky='we')

        # Creates the button to select .pdf files
        self.choose_button = tk.Button(self, text="Choose a File", font=("Helvetica", 15))
        self.choose_button.grid(row=3, column=1, pady=(0, 20), sticky='w')

        # Creates the merge button to merge the selected .pdf files
        self.merge_button = tk.Button(self, text="Merge PDFs", font=("Helvetica", 15))
        self.merge_button.grid(row=3, column=2, pady=(0, 20), sticky='e')

        # Creates possible errors that may arise based upon user interaction
        self.min_files_error_label = tk.Label(self, text="You must have at least 2 files to merge.", font=("Helvetica", 10),
                                    foreground="red")
        self.same_file_error_label = tk.Label(self, text="That file is already selected.", font=("Helvetica", 10),
                                    foreground="red")

    def display_files(self, file_list):
        # Reloads the files every time a new file is selected or deleted
        for widget in self.winfo_children():
            if widget.winfo_name() not in self.constant_widgets:
                widget.destroy()
        for i in range(len(file_list)):
            file_label = tk.Label(self, text=f"{file_list[i]}", font=("Helvetica", 10))
            delete_button = tk.Button(self, text="Delete", font=("Helvetica", 10))

            # order_text.grid(row=i + 5, column=0)
            file_label.grid(row=i + 5, column=1, pady=5)
            delete_button.grid(row=i + 5, column=2, pady=5)
