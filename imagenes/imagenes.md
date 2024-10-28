# Script de Procesamiento de Imágenes

Este script de Python está diseñado para descomprimir archivos ZIP, mover imágenes a un directorio específico, y generar un archivo CSV que agrupa las imágenes por referencia. Es ideal para gestionar imágenes de productos o cualquier otro tipo de archivo que necesite ser organizado.

## Requisitos

- Python 3.5 o superior
- Módulos de Python: `os`, `zipfile`, `shutil`, `csv`, `collections`

## Estructura del Script

El script está dividido en varias funciones, cada una responsable de una tarea específica:

### Funciones

- **`crear_directorio_destino`**: Crea el directorio de destino si no existe.
- **`descomprimir_archivos_zip`**: Descomprime todos los archivos ZIP en el directorio de trabajo y elimina los ZIP después de la descompresión.
- **`mover_imagenes`**: Mueve todas las imágenes (`.jpg`, `.jpeg`, `.png`) a un directorio de destino, renombrando los archivos en caso de conflicto.
- **`eliminar_subdirectorios_vacios`**: Elimina los subdirectorios vacíos en el directorio de destino.
- **`generar_csv_rutas`**: Genera un archivo CSV que contiene las rutas de las imágenes movidas, agrupadas por referencia.

## Uso

1. Coloca todos los archivos ZIP en el mismo directorio donde se encuentra el script o especifica el directorio en la variable `DIRECTORIO_ZIP`.
2. Ejecuta el script:
   ```bash
   python nombre_del_archivo.py
   ```
3. El script creará un directorio llamado `imagenes` y moverá todas las imágenes allí.
4. Se generará un archivo `fotos_referencias.csv` que contendrá las referencias y rutas de las imágenes.

## Ejemplo de Archivo CSV

El archivo `fotos_referencias.csv` tendrá un formato como el siguiente:

| reference   | image                                                      |
|-------------|------------------------------------------------------------|
| producto_1  | https://uniontecnica.vrweb.cl/producto1.jpg;https://uniontecnica.vrweb.cl/producto1_1.jpg |
| producto_2  | https://uniontecnica.vrweb.cl/producto2.jpg              |

## Notas

- Asegúrate de tener permisos de lectura y escritura en los directorios que estás utilizando.
- Si el directorio de destino ya contiene imágenes con el mismo nombre, se renombrarán automáticamente para evitar conflictos.