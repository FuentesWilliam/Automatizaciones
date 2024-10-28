import os
import zipfile
import shutil
import csv
from collections import defaultdict

# Directorio donde están los archivos zip (directorio actual)
DIRECTORIO_ZIP = '.'

# Directorio donde se moverán todas las imágenes
DIRECTORIO_DESTINO = './imagenes'

def crear_directorio_destino():
    """Crea el directorio destino si no existe."""
    os.makedirs(DIRECTORIO_DESTINO, exist_ok=True)

def descomprimir_archivos_zip():
    """Descomprime los archivos ZIP y elimina los archivos ZIP después de descomprimir."""
    for archivo in os.listdir(DIRECTORIO_ZIP):
        if archivo.endswith('.zip'):
            # Crear un subdirectorio para el archivo ZIP
            nombre_directorio = os.path.join(DIRECTORIO_DESTINO, archivo[:-4])  # Eliminar .zip
            os.makedirs(nombre_directorio, exist_ok=True)

            # Descomprimir el archivo zip en su propio directorio
            with zipfile.ZipFile(archivo, 'r') as zip_ref:
                zip_ref.extractall(nombre_directorio)  # Extraer en el subdirectorio

            # Eliminar el archivo ZIP después de descomprimir
            os.remove(os.path.join(DIRECTORIO_ZIP, archivo))

def mover_imagenes():
    """Mueve todas las imágenes de los subdirectorios al directorio destino, renombrando en caso de conflicto."""
    for root, dirs, files in os.walk(DIRECTORIO_ZIP):
        if root.startswith(DIRECTORIO_DESTINO):
            continue  # Ignorar el propio directorio destino

        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                ruta_origen = os.path.join(root, file)
                nueva_ruta = os.path.join(DIRECTORIO_DESTINO, file)

                # Mover la imagen al directorio destino, renombrando si ya existe
                if not os.path.exists(nueva_ruta):
                    shutil.move(ruta_origen, nueva_ruta)
                else:
                    # Si ya existe un archivo con el mismo nombre, renombrar antes de mover
                    base, extension = os.path.splitext(file)
                    contador = 1
                    while os.path.exists(nueva_ruta):
                        nueva_ruta = os.path.join(DIRECTORIO_DESTINO, "{}_{}{}".format(base, contador, extension))
                        contador += 1
                    shutil.move(ruta_origen, nueva_ruta)

def eliminar_subdirectorios_vacios():
    """Elimina los subdirectorios vacíos dentro del directorio destino."""
    for root, dirs, files in os.walk(DIRECTORIO_DESTINO, topdown=False):
        for dir in dirs:
            full_path = os.path.join(root, dir)
            if not os.listdir(full_path):  # Eliminar solo si el directorio está vacío
                os.rmdir(full_path)

def generar_csv_rutas():
    """Genera un archivo CSV con las rutas de las imágenes movidas, agrupadas por referencia."""
    fotos = os.listdir(DIRECTORIO_DESTINO)
    referencias = defaultdict(list)

    # Procesamos la lista de fotos
    for foto in fotos:
        foto_con_ruta = "https://uniontecnica.vrweb.cl/img/productos/" + foto

        # Extraemos la parte antes del ".jpg"
        referencia = foto.split(".")[0]

        # Si la referencia tiene un guion o subguion que indica múltiples fotos, la agrupamos
        base_referencia = referencia.rsplit("-", 1)[0] if "-" in referencia else referencia.rsplit("_", 1)[0]

        # Añadimos la foto con la ruta a la referencia correspondiente
        referencias[base_referencia].append(foto_con_ruta)

    # Escribimos el archivo CSV
    with open('fotos_referencias.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['reference', 'image'])  # Cabecera del CSV

        # Escribimos cada referencia con sus fotos agrupadas
        for referencia, fotos_list in referencias.items():
            writer.writerow([referencia, ';'.join(fotos_list)])

def main():
    """Función principal que ejecuta todas las tareas necesarias."""
    crear_directorio_destino()
    descomprimir_archivos_zip()
    mover_imagenes()
    eliminar_subdirectorios_vacios()
    generar_csv_rutas()
    print("Proceso completado. Todas las imágenes se han movido al directorio:", DIRECTORIO_DESTINO)
    print("Archivo CSV con rutas generado exitosamente.")


if __name__ == "__main__":
    main()