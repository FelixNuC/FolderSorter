import tkinter as tk
from tkinter import filedialog

ruta = ""
tipos = [] 

opciones = {
    "Imágenes": [".jpg", ".jpeg", ".png"],
    "PDF": [".pdf"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Documentos Word": [".doc", ".docx"],
    "Textos": [".txt", ".md"],
    "Otros": []  
}


vars_opciones = {}

def buscar_archivo():
    global ruta
    ruta = filedialog.askdirectory()
    if ruta:
        boton_buscar.config(text=ruta)
    else:
        boton_buscar.config(text="Por favor, selecciona una carpeta")

def confirmar_opciones():
    global tipos
    if not ruta:
        etiqueta_resultado.config(text="Por favor, selecciona una carpeta.", fg="#ffa833")  # Mensaje amarillo
        return 


    tipos.clear()
    for nombre, var in vars_opciones.items():
        if var.get():
            tipos.append(nombre)
    
    if not tipos: 
        etiqueta_resultado.config(text="Por favor, selecciona al menos una opción.", fg="#ffa833")  # Mensaje amarillo
        return 
    
    ventana.quit()  

def mostrar_mensaje_final():
    etiqueta_resultado.config(text="Archivos ordenados correctamente")
    ventana.update()
    ventana.after(2000, ventana.destroy)  

ventana = tk.Tk()
ventana.title("")
ventana.geometry("600x400")
ventana.config(bg="#E6F0FF")  

titulo = tk.Label(ventana, text="Ordenador de Archivos", font=("Arial", 16, "bold"), bg="#E6F0FF", fg="#2C3E50")
titulo.pack(pady=10)

boton_buscar = tk.Button(ventana, text="Buscar carpeta", command=buscar_archivo, bg="#ffffff", fg="black", font=("Arial", 12), relief="flat", bd=1, padx=20, pady=1, borderwidth=5, highlightthickness=1)
boton_buscar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Ninguna carpeta seleccionada", font=("Arial", 12), bg="#E6F0FF", fg="#2C3E50")
etiqueta_resultado.pack(pady=10)

tk.Label(ventana, text="Selecciona los tipos de archivos a ordenar:", font=("Arial", 12), bg="#E6F0FF", fg="#2C3E50").pack(pady=10)

marco_checkboxes = tk.Frame(ventana, bg="#E6F0FF")
marco_checkboxes.pack(pady=10)

columna1 = tk.Frame(marco_checkboxes, bg="#E6F0FF")
columna1.pack(side="left", padx=10)

columna2 = tk.Frame(marco_checkboxes, bg="#E6F0FF")
columna2.pack(side="left", padx=10)

for i, nombre in enumerate(opciones.keys()):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(columna1 if i % 2 == 0 else columna2, text=nombre, variable=var, font=("Arial", 10), bg="#E6F0FF", fg="#2C3E50")
    chk.pack(anchor='w', pady=5)
    vars_opciones[nombre] = var

boton_confirmar = tk.Button(ventana, text="Confirmar selección", command=confirmar_opciones, bg="#2C3E50", fg="white", font=("Arial", 12), relief="flat", bd=1, padx=20, pady=10, borderwidth=1, highlightthickness=1)
boton_confirmar.pack(pady=20)

ventana.mainloop()
