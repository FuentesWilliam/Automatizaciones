# -*- coding: utf-8 -*-

import os
import shutil
import hashlib
import mimetypes

# Configuración de los directorios
input_dir = './descargas'  # Cambia esto a la ruta donde están tus PDFs
output_dir = './subir'  # Cambia esto a donde quieras guardar los archivos con hash

# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Archivo de salida para las consultas SQL
output_file = 'presta_sql_inserts.txt'

# Crear o vaciar el archivo de salida si ya existe
with open(output_file, 'w') as f:
    f.write('')

# Función para calcular el hash del nombre del archivo
def calcular_hash(nombre_archivo):
    """Calcula el hash MD5 del nombre del archivo."""
    hash_obj = hashlib.md5(nombre_archivo.encode())
    return hash_obj.hexdigest()

# Preparar la lista de archivos y sus datos para la base de datos
attachments = []

for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):  # Asegurarse de que solo se procesen archivos PDF
        original_name = filename
        hash_name = calcular_hash(original_name)
        
        # Obtener el tipo MIME del archivo
        mime_type, _ = mimetypes.guess_type(original_name)
        if mime_type is None:
            mime_type = 'application/pdf'  # Asumimos que es un PDF si no se detecta
        
        # Tamaño del archivo en bytes
        file_size = os.path.getsize(os.path.join(input_dir, original_name))

        # Guardar los datos del archivo en la lista
        attachments.append({
            'original_name': original_name,
            'hash_name': hash_name,
            'mime_type': mime_type,
            'file_size': file_size,
        })
        
        # Copiar el archivo con el hash (sin extensión) al directorio de salida
        hash_file_path = os.path.join(output_dir, hash_name)  # Ruta del archivo con hash
        shutil.copy(os.path.join(input_dir, original_name), hash_file_path)  # Copiar el archivo original

# Solicitar el id_attachment inicial al usuario
id_attachment_start = int(input("Introduce el id_attachment inicial: "))

# Generar las consultas SQL en el formato solicitado
with open(output_file, 'a') as f:
    # *** Generar UNA sola consulta para ps_attachment ***
    attachment_values = []
    for attachment in attachments:
        # Agregar valores a la lista en el formato deseado
        attachment_values.append(
            "('{hash_name}', '{original_name}', '{mime_type}', {file_size})".format(
                hash_name=attachment['hash_name'],
                original_name=attachment['original_name'],
                mime_type=attachment['mime_type'],
                file_size=attachment['file_size']
            )
        )

    # Generar la consulta para ps_attachment con todos los VALUES
    insert_attachment = (
        "INSERT INTO ps_attachment (file, file_name, mime, file_size) "
        "VALUES " + ', '.join(attachment_values) + ";\n"
    )
    
    # Escribir la consulta en el archivo
    f.write(insert_attachment)

    # *** Generar UNA sola consulta para ps_attachment_lang ***
    lang_values = []
    for i, attachment in enumerate(attachments):
        # Calcular el id_attachment para cada archivo
        id_attachment = id_attachment_start + i
        lang_values.append(
            "({id_attachment}, 1, 'PDF', NULL)".format(id_attachment=id_attachment)
        )

    # Generar la consulta para ps_attachment_lang con todos los VALUES
    insert_attachment_lang = (
        "INSERT INTO ps_attachment_lang (id_attachment, id_lang, name, description) "
        "VALUES " + ', '.join(lang_values) + ";\n"
    )
    
    # Escribir la consulta en el archivo
    f.write(insert_attachment_lang)

print("Archivos copiados y consultas SQL generadas con éxito.")