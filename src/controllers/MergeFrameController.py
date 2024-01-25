import tkinter as tk


class MergeFrameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["merge"]
        self.bind_static_btns()

    def bind_static_btns(self):
        # Binds the buttons that remain visible at all times
        self.frame.back_image_button.config(command=lambda: self.view.switch("main"))
        self.frame.choose_button.config(command=self.choose_file)
        self.frame.merge_button.config(command=self.merge_files)

    def bind_dynamic_btns(self):
        # Binds the delete buttons that are added and removed based on user input
        constant_widgets = self.view.frames["merge"].constant_widgets
        button_index = -1
        if (len(self.model.merge_model.selected_file_list)) > 0:
            for widget in self.view.frames["merge"].winfo_children():
                if widget.winfo_name() not in constant_widgets and isinstance(widget, tk.Button):
                    button_index += 1
                    i = 0
                    widget.config(command=lambda index=button_index: self.delete_file(index))

    def choose_file(self):
        # Allows the user to select a .pdf file
        self.frame.same_file_error_label.grid_forget()
        original_list_length = len(self.model.merge_model.selected_file_list)
        self.model.merge_model.choose_file()
        self.view.frames["merge"].display_files(self.model.merge_model.selected_file_list)
        self.bind_dynamic_btns()
        new_list_length = len(self.model.merge_model.selected_file_list)
        if new_list_length == original_list_length:
            self.frame.same_file_error_label.grid(row=2, column=0, columnspan=3)

    def delete_file(self, file_index):
        # Deletes a file previously selected
        self.model.merge_model.delete_file(file_index)
        new_file_list = self.model.merge_model.selected_file_list
        self.frame.display_files(new_file_list)

        self.bind_dynamic_btns()

    def merge_files(self):
        # Merges 2+ .pdf files together
        if not self.model.merge_model.merge_files():
            self.frame.min_files_error_label.grid(row=2, column=0, columnspan=3)
            return False
        self.model.merge_model.merge_files()
        self.frame.min_files_error_label.pack_forget()
        self.model.merge_model.delete_all_files()
        self.frame.display_files(self.model.merge_model.selected_file_list)
        self.view.switch("success")
        return True
