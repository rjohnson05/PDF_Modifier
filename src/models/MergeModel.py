from tkinter import filedialog
from PyPDF2 import PdfWriter


class MergeModel:
    def __init__(self):
        self.selected_file_list = list()

    def choose_file(self):
        # Allows the user to select a .pdf file
        file_name = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_name != "" and file_name not in self.selected_file_list:
            self.selected_file_list.append(file_name)

    def delete_file(self, file_index):
        self.selected_file_list.pop(file_index)

    def merge_files(self):
        # Deletes a file previously selected
        if len(self.selected_file_list) < 2:
            return False
        merger = PdfWriter()
        for pdf in self.selected_file_list:
            merger.append(pdf)

        merger.write("merged-pdf.pdf")
        merger.close()
        return True

    def delete_all_files(self):
        # Removes all files from the selected list after a successful merge
        self.selected_file_list = list()