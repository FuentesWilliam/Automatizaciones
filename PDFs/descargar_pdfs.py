 
import os
import requests

# Archivo que contiene los enlaces
archivo_enlaces = 'enlaces.txt'

# Directorio donde se guardarán los PDFs
carpeta_descargas = './descargas'

# Función para descargar un PDF desde una URL
def descargar_archivo(url):
    """
    Descarga cualquier archivo desde una URL y lo guarda en un directorio.

    :param url: La URL del archivo.
    :param output_dir: Directorio donde guardar el archivo.
    :return: Ruta completa del archivo descargado.
    """
    try:
        # Crear el directorio si no existe
        if not os.path.exists(carpeta_descargas):
            os.makedirs(carpeta_descargas)

        # Obtener el nombre del archivo desde el enlace
        nombre_archivo = url.split('/')[-1]
        ruta_archivo = os.path.join(carpeta_descargas, nombre_archivo)

        # Descargar el archivo
        print('Descargando {}...'.format(url))
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verificar si hubo algún error

        # Guardar el contenido del PDF en un archivo local
        with open(ruta_archivo, 'wb') as f:
            f.write(respuesta.content)

        # Guardar el archivo
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)

        #print('Archivo descargado: {}'.format(ruta_archivo))
    except requests.exceptions.RequestException as e:
        print("Error al descargar {}: {}".format(url, e))

# Leer los enlaces desde el archivo de texto, eliminando duplicados
def obtener_enlaces_sin_duplicados(archivo_enlaces):
    with open(archivo_enlaces, 'r') as f:
        # Usamos un conjunto (set) para eliminar automáticamente duplicados
        enlaces_unicos = set(enlace.strip() for enlace in f if enlace.strip())
    return enlaces_unicos

# Obtener los enlaces sin duplicados
enlaces_unicos = obtener_enlaces_sin_duplicados(archivo_enlaces)

# Descargar los archivos correspondientes a cada enlace único
for enlace in enlaces_unicos:
    descargar_archivo(enlace)

print("Descarga completada.")