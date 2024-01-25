from src.controllers.Controller import Controller
from src.views.View import View
from src.models.Model import Model


def main():
    """
    PDF Modifier App, which allows the user to merge several .pdf files into one single file.

    Project organization inspired by Nazmul Ahsan:
    https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
    """
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.start()


if __name__ == '__main__':
    main()
