from src.views.MainFrame import MainFrame
from src.views.MergeFrame import MergeFrame
from src.views.Root import Root
from src.views.SuccessFrame import SuccessFrame


class View:
    # Serves as the central View class in the MVC model, loading all the frames and allowing the user to switch frames
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self.add_frame(MainFrame, "main")
        self.add_frame(MergeFrame, "merge")
        self.add_frame(SuccessFrame, "success")

    def add_frame(self, frame, frame_name):
        # Creates a new frame
        self.frames[frame_name] = frame(self.root)
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        # Displays a new frame to the user
        frame = self.frames[frame_name]
        frame.tkraise()

    def start_mainloop(self):
        # Begins the display of the root frame
        self.root.mainloop()
