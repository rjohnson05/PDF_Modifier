from src.controllers.MainFrameController import MainFrameController
from src.controllers.MergeFrameController import MergeFrameController
from src.controllers.SuccessFrameController import SuccessFrameController


class Controller:
    # Serves as the central controller in the MVC model for the PDF Modifier program
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.main_controller = MainFrameController(model, view)
        self.merge_controller = MergeFrameController(model, view)
        self.success_controller = SuccessFrameController(model, view)

    def start(self):
        # Sets the start screen to the main frame and begins the program
        self.view.switch("main")
        self.view.start_mainloop()
