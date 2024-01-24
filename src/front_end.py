import tkinter as tk
from PIL import ImageTk, Image


class FrameController(tk.Tk):
    """
    Controller class for the PDFModifier program, which provides various services concerning .pdf files.
    This class creates the container in which all frames, each placed in their own class, are later placed.
    All frames are placed into a dictionary with the frame type as the key and the frame itself as the value.
    This dictionary allows for the switching of frames within this controller frame.

    This class was taken from Meghna Gangwar:
    https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
    """

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.title("PDF Modifier")
        # Creates a dictionary for storing the frames used throughout the program, which allows the user to switch
        # between frames
        self.frames = {}
        for FrameType in (MainFrame, MergeFrame, SplitFrame, OrganizeFrame, ConvertFrame, RotateFrame):
            frame = FrameType(container, self)
            self.frames[FrameType] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainFrame)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        welcome_label = tk.Label(self, text="Welcome to PDF Modifier!", font=("Helvetica", 25))
        instruction_label = tk.Label(self, text="Click on one of the buttons below to start modifying your PDF.",
                                     font=("Helvetica", 15))
        welcome_label.grid(row=0, column=1, columnspan=4)
        instruction_label.grid(row=1, column=1, columnspan=4, padx=40, pady=(10, 50))

        # Creates the Merge PDF Button
        orig_merge_image = Image.open("../images/merge.png").resize((90, 90))
        merge_image = ImageTk.PhotoImage(orig_merge_image)
        merge_image_button = tk.Button(self, image=merge_image, borderwidth=0, cursor="hand2",
                                       command=lambda: controller.show_frame(MergeFrame))
        merge_image_button.image = merge_image
        merge_image_button.grid(row=3, column=1)
        merge_label_button = tk.Button(self, text="Merge PDF Files", borderwidth=0, font=("Helvetica", 15),
                                       cursor="hand2", command=lambda: controller.show_frame(MergeFrame))
        merge_label_button.grid(row=4, column=1)

        # Creates the Rotate PDF Button
        orig_rotate_image = Image.open("../images/rotate.png").resize((90, 90))
        rotate_image = ImageTk.PhotoImage(orig_rotate_image)
        rotate_image_button = tk.Button(self, image=rotate_image, borderwidth=0, cursor="hand2",
                                        command=lambda: controller.show_frame(RotateFrame))
        rotate_image_button.image = rotate_image
        rotate_image_button.grid(row=3, column=2)
        rotate_label_button = tk.Button(self, text="Rotate PDF", borderwidth=0, font=("Helvetica", 15),
                                        cursor="hand2", command=lambda: controller.show_frame(RotateFrame))
        rotate_label_button.grid(row=4, column=2)

        # Creates the Convert PDF Button
        orig_export_image = Image.open("../images/convert.png").resize((90, 90))
        export_image = ImageTk.PhotoImage(orig_export_image)
        export_image_button = tk.Button(self, image=export_image, borderwidth=0, cursor="hand2",
                                        command=lambda: controller.show_frame(ConvertFrame))
        export_image_button.image = export_image
        export_image_button.grid(row=3, column=3)
        export_label_button = tk.Button(self, text="Rotate PDF", borderwidth=0, font=("Helvetica", 15),
                                        cursor="hand2", command=lambda: controller.show_frame(ConvertFrame))
        export_label_button.grid(row=4, column=3)


class MergeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class SplitFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Other stuff


class OrganizeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Other stuff


class ConvertFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Other stuff


class RotateFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Other stuff


if __name__ == "__main__":
    pdfApp = FrameController()
    pdfApp.mainloop()
