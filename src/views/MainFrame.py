import tkinter as tk

from PIL import Image, ImageTk


class MainFrame(tk.Frame):
    # Contains all display features for the main frame
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        welcome_label = tk.Label(self, text="Welcome to PDF Modifier!", font=("Helvetica", 25))
        instruction_label = tk.Label(self, text="Click on the button below to start modifying your PDF.",
                                          font=("Helvetica", 15))
        welcome_label.grid(row=0, column=1, columnspan=4)
        instruction_label.grid(row=1, column=1, columnspan=4, padx=40, pady=(10, 50))

        # Creates the Merge PDF Button
        orig_merge_image = Image.open("../images/merge.png").resize((90, 90))
        merge_image = ImageTk.PhotoImage(orig_merge_image)
        self.merge_image_button = tk.Button(self, image=merge_image, borderwidth=0, cursor="hand2")
        self.merge_image_button.image = merge_image
        self.merge_image_button.grid(row=3, column=2)
        self.merge_label_button = tk.Button(self, text="Merge PDF Files", borderwidth=0, font=("Helvetica", 15),
                                            cursor="hand2")
        self.merge_label_button.grid(row=4, column=2)
