# Script para Descargar Archivos desde Enlaces

Este script en Python permite descargar archivos desde una lista de enlaces que se encuentran en un archivo de texto. El script elimina automáticamente los enlaces duplicados, evitando así la descarga repetida de los mismos archivos.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalado Python y el módulo `requests`. Puedes instalar `requests` usando el siguiente comando:

```bash
pip install requests
```

## Uso 
Crea/edite un archivo de texto llamado `enlaces.txt` en el mismo directorio que el script. Cada enlace debe estar en una línea separada. Por ejemplo:

```bash
https://example.com/archivo1.pdf
https://example.com/archivo2.zip
https://example.com/archivo3.jpg
```

## Ejecuta el script desde la línea de comandos:

```bash
python3 procesar_pdfs.py
```

## Notas
- Los archivos se descargarán en una carpeta llamada `descargados scripts`, que se creará automáticamente si no existe.
- Si un enlace no se puede descargar, se mostrará un mensaje de error en la consola.
- Asegúrate de tener los permisos necesarios para descargar los archivos desde los enlaces proporcionados.
=======
# Automatizaciones
Scripts para automatizar descargas de PDFs y otras tareas.

