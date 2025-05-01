import os
import shutil
import view

def ordenar_archivos(ruta, tipos):
    for carpeta in tipos:
        ruta_carpeta = os.path.join(ruta, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.mkdir(ruta_carpeta)

    for archivo in os.listdir(ruta):
        archivo_path = os.path.join(ruta, archivo)
        if not os.path.isfile(archivo_path):
            continue

        if archivo.endswith((".jpg", ".jpeg", ".png")) and "Imágenes" in tipos:
            shutil.move(archivo_path, os.path.join(ruta, "Imágenes", archivo))
        elif archivo.endswith(".pdf") and "PDF" in tipos:
            shutil.move(archivo_path, os.path.join(ruta, "PDF", archivo))
        elif archivo.endswith((".mp4", ".avi", ".mov")) and "Videos" in tipos:
            shutil.move(archivo_path, os.path.join(ruta, "Videos", archivo))
        elif archivo.endswith((".doc", ".docx")) and "Documentos Word" in tipos:
            shutil.move(archivo_path, os.path.join(ruta, "Documentos Word", archivo))
        elif archivo.endswith((".txt", ".md")) and "Textos" in tipos:
            shutil.move(archivo_path, os.path.join(ruta, "Textos", archivo))
        elif "Otros" in tipos:
            shutil.move(archivo_path, os.path.join(ruta, "Otros", archivo))

if __name__ == "__main__":
    view.ventana.mainloop()  
    ruta = view.ruta
    tipos = view.tipos

    if ruta and tipos:
        ordenar_archivos(ruta, tipos)
        view.mostrar_mensaje_final()
