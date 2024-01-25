class SuccessFrameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["success"]
        self.bind()

    def bind(self):
        # Binds the button on the success frame, allowing the user to move back to the main frame
        self.frame.back_image_button.config(command=lambda: self.view.switch("main"))
