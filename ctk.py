from customtkinter import CTk, CTkButton
from tkinter.filedialog import askopenfilename, askdirectory
import crop_rotate_link
import os

def open_file():
    # Using askopenfilename returns the path string directly
    file_path = askopenfilename(filetypes=[
        ('Image files', '*.bmp *.tiff *.tif *.jpg *.jpeg *.png')
    ])
    if file_path:
        crop_rotate_link.run_pipeline(input_path=file_path)


def select_folder():
    # Using askdirectory returns the folder path string
    folder_path = askdirectory()
    if folder_path:
        crop_rotate_link.run_pipeline(input_path=folder_path)


def main():
    app = CTk()
    app.title('Smart Crop')
    app.geometry('300x200')
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(1, weight=1)
    # Buttons
    open_btn = CTkButton(app, text='Open a File', command=open_file)
    open_btn.grid(column=0, row=0, padx=10, pady=10)

    folder_btn = CTkButton(app, text='Select a Folder', command=select_folder)
    folder_btn.grid(column=1, row=0, padx=10, pady=10)

    app.mainloop()


if __name__ == "__main__":
    main()