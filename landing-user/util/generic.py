from PIL import ImageTk, Image

def leer_imagen(path, size):
    """Lee y redimensiona una imagen desde el archivo especificado."""
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))

def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):

    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (aplicacion_ancho / 2))
    y = int((pantalla_alto / 2) - (aplicacion_largo / 2))
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
