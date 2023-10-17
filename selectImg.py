import tkinter as tk  # this is the preferred import for tkinter
from tkinter import filedialog

def abrir_imagen():
    tipos_de_archivo = (
        ("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp"),
        ("Todos los archivos", "*.*")
    )
    archivo = filedialog.askopenfilename(
        title="Seleccionar una imagen",
        filetypes=tipos_de_archivo
    )
    if archivo:
        return archivo