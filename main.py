import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ExifTags
import sv_ttk


def remove_exif(image_path):
    try:
        img = Image.open(image_path)
        data = list(img.getdata())
        img_without_exif = Image.new(img.mode, img.size)
        img_without_exif.putdata(data)
        img_without_exif.save(image_path, format=img.format)
        img.close()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")


def has_exif_data(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        img.close()
        return bool(exif_data)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False


def add_files():
    filepaths = filedialog.askopenfilenames(title="Select images", filetypes=[("JPEG files", "*.jpg;*.jpeg")])

    for filepath in filepaths:
        has_exif = has_exif_data(filepath)
        file_table.insert("", tk.END, values=(filepath, os.path.basename(filepath), has_exif))


def remove_selected_files():
    selected_items = file_table.selection()
    for item in selected_items:
        file_table.delete(item)


def batch_remove_exif():
    total_files = len(file_table.get_children())
    progress_bar["maximum"] = total_files
    progress_bar["value"] = 0

    for item in file_table.get_children():
        filepath = file_table.item(item, "values")[0]
        remove_exif(filepath)
        has_exif = has_exif_data(filepath)
        file_table.item(item, values=(filepath, os.path.basename(filepath), has_exif))

        progress_bar["value"] += 1
        root.update_idletasks()


root = tk.Tk()
root.title("Batch EXIF Data Remover")
#root.wm_iconbitmap("your_icon.ico")  # Replace with the path to your icon file

frame = ttk.Frame(root, padding="20 20 20 20")
frame.pack()

btn_frame = ttk.Frame(frame)
btn_frame.pack()

btn_add = ttk.Button(btn_frame, text="Add images", command=add_files, width=20)
btn_add.pack(side=tk.LEFT, padx=5)

btn_remove = ttk.Button(btn_frame, text="Remove selected", command=remove_selected_files, width=20)
btn_remove.pack(side=tk.LEFT, padx=5)

file_table = ttk.Treeview(frame, columns=("Path", "File", "EXIF Data"), show="headings")
file_table.heading("Path", text="Path")
file_table.heading("File", text="File")
file_table.heading("EXIF Data", text="EXIF Data")
file_table.column("Path", width=0, minwidth=0, stretch=tk.NO)
file_table.pack(pady=10)

progress_bar = ttk.Progressbar(frame, orient="horizontal", mode="determinate")
progress_bar.pack(fill=tk.X, pady=10)

btn_delete_exif = ttk.Button(frame, text="Delete EXIF data from all listed images", command=batch_remove_exif, width=40)
btn_delete_exif.pack()

sv_ttk.set_theme("dark")

root.mainloop()
