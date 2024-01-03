import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()
print(f'Ви вибрали папку: {folder_path}')


def convert_jpg_to_pdf(folder_path, output_file_name):
    images = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.jpg'):
            file_path = os.path.join(folder_path, file_name)
            images.append(Image.open(file_path))

    pdf_path = os.path.join(folder_path, output_file_name)
    images[0].save(pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])

    print(f'PDF file saved at {pdf_path}')


# Використовуйте цю функцію, щоб конвертувати всі файли .jpg у папці 'my_folder' в один файл PDF з ім'ям 'my_pdf.pdf'
convert_jpg_to_pdf(folder_path, 'my_pdf.pdf')
