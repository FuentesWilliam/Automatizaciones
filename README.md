# Automatizaciones

Este repositorio contiene scripts para automatizar la descarga de PDFs y otras tareas relacionadas con PrestaShop.

## Script para Descargar Archivos desde Enlaces

Este script en Python permite descargar archivos desde una lista de enlaces que se encuentran en un archivo de texto. El script elimina automáticamente los enlaces duplicados, evitando así la descarga repetida de los mismos archivos.

### Requisitos

Antes de ejecutar el script, asegúrate de tener instalado Python y el módulo `requests`. Puedes instalar `requests` usando el siguiente comando:

```bash
pip install requests
```

### Uso 

1. Crea/edita un archivo de texto llamado `enlaces.txt` en el mismo directorio que el script. Cada enlace debe estar en una línea separada. Por ejemplo:

    ```bash
    https://example.com/archivo1.pdf
    https://example.com/archivo2.zip
    https://example.com/archivo3.jpg
    ```

2. Ejecuta el script desde la línea de comandos:

    ```bash
    python3 descargar_archivos.py
    ```

### Notas

- Los archivos se descargarán en una carpeta llamada `descargados`, que se creará automáticamente si no existe.
- Si un enlace no se puede descargar, se mostrará un mensaje de error en la consola.
- Asegúrate de tener los permisos necesarios para descargar los archivos desde los enlaces proporcionados.

## Script para Procesar PDFs

Este script en Python permite procesar archivos PDF descargados, generando consultas SQL para insertar registros en las tablas `ps_attachment` y `ps_attachment_lang` de PrestaShop. Los archivos se copian a un directorio específico y se les asigna un hash en lugar de su nombre original.

### Uso 

1. Asegúrate de que los archivos PDF estén en el directorio `./descargas`.
2. Ejecuta el script desde la línea de comandos:

    ```bash
    python3 procesar_pdfs.py
    ```

3. Cuando se te solicite, introduce el `id_attachment` inicial (por ejemplo, 22).

### Notas

- Los archivos procesados se copiarán en el directorio `./subir` con un nombre de archivo basado en un hash MD5 del nombre original.
- Se generará un archivo `presta_sql_inserts.txt` que contendrá las consultas SQL para insertar los archivos en la base de datos de PrestaShop.
- Asegúrate de que la estructura de la base de datos en PrestaShop sea la correcta y de tener los permisos necesarios para realizar inserciones.

### Ejemplo de Salida

El archivo `presta_sql_inserts.txt` tendrá un formato similar al siguiente:

```sql
INSERT INTO ps_attachment (file, file_name, mime, file_size) 
VALUES 
('hash1', 'archivo1.pdf', 'application/pdf', 12345),
('hash2', 'archivo2.pdf', 'application/pdf', 23456),
('hash3', 'archivo3.pdf', 'application/pdf', 34567);

INSERT INTO ps_attachment_lang (id_attachment, id_lang, name, description) 
VALUES 
(22, 1, 'PDF', NULL),
(23, 1, 'PDF', NULL),
(24, 1, 'PDF', NULL);
```

Este archivo es fundamental para agregar los archivos PDF a la base de datos de PrestaShop de manera eficiente.