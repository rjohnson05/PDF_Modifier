from src.models.MergeModel import MergeModel


class Model:
    # Serves as the central Model class in the MVC model, allowing for easy addition of more model classes
    def __init__(self):
        self.merge_model = MergeModel()
