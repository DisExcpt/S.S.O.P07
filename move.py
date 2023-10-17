import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import threading
from selectImg import abrir_imagen
# Clase principal de la aplicación
class MoverImagenesApp:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("practica 07 Hilos")

        # Crear un lienzo para mostrar las imágenes
        self.canvas = tk.Canvas(ventana, width=400, height=400)
        self.canvas.pack()

        # Cargar imágenes desde archivos y crear objetos PhotoImage
        imagen_vertical = Image.open(abrir_imagen())
        self.imagen_vertical = ImageTk.PhotoImage(imagen_vertical)
        self.img_vertical = self.canvas.create_image(200, 450, image=self.imagen_vertical)

        imagen_horizontal = Image.open(abrir_imagen())
        self.imagen_horizontal = ImageTk.PhotoImage(imagen_horizontal)
        self.img_horizontal = self.canvas.create_image(450, 200, image=self.imagen_horizontal)

        # Botón para iniciar la animación
        self.boton_iniciar = tk.Button(ventana, text="Iniciar", command=self.iniciar_animacion)
        self.boton_iniciar.pack()

        # Botón para detener la animación
        self.boton_detener = tk.Button(ventana, text="Detener", command=self.detener_animacion, state=tk.DISABLED)
        self.boton_detener.pack()

        # Variable para controlar el estado de la animación
        self.animacion_activa = False

    # Función para mover la imagen verticalmente
    def mover_imagen_vertical(self):
        dy = 15
        while self.animacion_activa:
            for _ in range(40):
                self.canvas.move(self.img_vertical, 0, -dy)
                self.canvas.update()
                self.ventana.after(10)  # Mantener la aplicación receptiva
            for _ in range(40):
                self.canvas.move(self.img_vertical, 0, dy)
                self.canvas.update()
                self.ventana.after(10)

    # Función para mover la imagen horizontalmente
    def mover_imagen_horizontal(self):
        dx = 15
        while self.animacion_activa:
            for _ in range(40):
                self.canvas.move(self.img_horizontal, -dx, 0)
                self.canvas.update()
                self.ventana.after(10)  # Mantener la aplicación receptiva
            for _ in range(40):
                self.canvas.move(self.img_horizontal, dx, 0)
                self.canvas.update()
                self.ventana.after(10)

    # Función para iniciar la animación
    def iniciar_animacion(self):
        self.boton_iniciar['state'] = tk.DISABLED
        self.boton_detener['state'] = tk.NORMAL
        self.animacion_activa = True

        # Crear hilos para mover las imágenes
        thread_vertical = threading.Thread(target=self.mover_imagen_vertical)
        thread_horizontal = threading.Thread(target=self.mover_imagen_horizontal)

        # Iniciar los hilos
        thread_vertical.start()
        thread_horizontal.start()

    # Función para detener la animación
    def detener_animacion(self):
        self.animacion_activa = False
        self.boton_iniciar['state'] = tk.NORMAL
        self.boton_detener['state'] = tk.DISABLED


