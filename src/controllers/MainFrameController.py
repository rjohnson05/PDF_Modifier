class MainFrameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["main"]
        self.bind()

    def bind(self):
        # Binds the buttons on the main frame to the correct functions, moving to the merge frame
        self.frame.merge_image_button.config(command=lambda: self.view.switch("merge"))
        self.frame.merge_label_button.config(command=lambda: self.view.switch("merge"))
