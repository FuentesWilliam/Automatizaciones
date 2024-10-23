# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse

# Archivo de entrada con las referencias de productos y URLs
input_file = 'referencias_productos.txt'  # Archivo que contiene las referencias de productos y las URLs de los PDFs
# Archivo de asociaciones nombre_pdf -> hash generado por el script anterior
hash_file = 'nombre_pdf_hash.txt'

# Archivo de salida para las consultas SQL
output_sql = 'insert_product_attachment .txt'

# Leer el archivo con las asociaciones nombre_pdf -> hash
hash_dict = {}

with open(hash_file, 'r') as f_hash:
    for line in f_hash:
        nombre_pdf, hash_name = line.strip().split(';')  # Dividir por punto y coma
        hash_dict[nombre_pdf] = hash_name

# Función para extraer el nombre del PDF de la URL
def extraer_nombre_pdf(url):
    """Extrae el nombre del archivo PDF desde la URL, quitando cualquier variable de consulta"""
    parsed_url = urlparse(url)
    # Obtiene la parte final de la ruta, que debería ser el nombre del archivo
    nombre_pdf = os.path.basename(parsed_url.path)
    # Asegurarnos de eliminar cualquier parámetro como ?v=...
    nombre_pdf = nombre_pdf.split('?')[0]
    return nombre_pdf

# Leer el archivo de referencias de productos y URLs de PDFs
referencias = []

with open(input_file, 'r') as f_referencias:
    for line in f_referencias:
        referencia_producto, url_pdf = line.strip().split(';')  # Dividir por punto y coma
        nombre_pdf = extraer_nombre_pdf(url_pdf)  # Extraer el nombre del PDF de la URL
        referencias.append((referencia_producto, nombre_pdf))

# Generar las consultas SQL en el formato solicitado
with open(output_sql, 'w') as f_sql:
    # Lista para acumular las consultas
    product_attachment_values = []

    for referencia, nombre_pdf in referencias:
        # Buscar el hash correspondiente en el diccionario hash_dict
        hash_name = hash_dict.get(nombre_pdf)

        if hash_name:
            # Crear la consulta SQL para insertar en ps_product_attachment
            product_attachment_values.append(
                "('{referencia}', '{hash_name}')".format(
                    referencia=referencia,
                    hash_name=hash_name
                )
            )
        else:
            print("Advertencia: No se encontró hash para el PDF {}".format(nombre_pdf))

    # Escribir la consulta para ps_product_attachment
    if product_attachment_values:
        insert_product_attachment = (
            "INSERT INTO ps_product_attachment (id_product, id_attachment) "
            "VALUES " + ', '.join(product_attachment_values) + ";\n"
        )
        f_sql.write(insert_product_attachment)

print("Consultas SQL generadas correctamente en", output_sql)
