import csv
import os
import re

# Función para limpiar y normalizar los códigos
def limpiar_codigos(codigo):
    # Remover espacios en blanco al inicio y al final
    codigo = codigo.strip()
    
    # Expresión regular para detectar números con comas decimales
    regex_coma_decimal = re.compile(r'(\d+),(\d+)')
    
    # Reemplazar comas decimales por puntos
    codigo = re.sub(regex_coma_decimal, r'\1.\2', codigo)
    
    # Separar por ", " o espacio y devolver como una lista
    if ', ' in codigo:
        return [c.strip() for c in codigo.split(',')]
    else:
        return [c.strip() for c in codigo.split()]

# Función para validar los códigos
def validar_codigo(codigo):
    # Validar longitud mínima de 3 caracteres
    if len(codigo) < 3:
        return False
    return True

# Archivos de entrada y salida
input_file = 'entrada.csv'  # Nombre del archivo de entrada
output_file = 'codigos_limpios.csv'  # Nombre descriptivo para el archivo de salida
excepciones_file = 'excepciones.txt'  # Archivo para registrar excepciones

# Verificar si el archivo de entrada existe
if not os.path.exists(input_file):
    print("Error: El archivo 'entrada.csv' no se encuentra.")
else:
    # Leer el archivo de entrada y procesar los datos
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile, open(excepciones_file, mode='w', encoding='utf-8') as excepciones_outfile:
        
        reader = csv.reader(infile, delimiter=';')  # El delimitador de entrada es ';'
        writer = csv.writer(outfile, delimiter='|')  # El delimitador de salida es '|'

        # Procesar cada fila en el archivo de entrada
        for row in reader:
            referencia = row[0]  # Primer elemento de la fila es la referencia
            codigos_alternativos = limpiar_codigos(row[1])  # Limpiar los códigos alternativos
            
            # Filtrar y validar los códigos alternativos
            codigos_validos = []
            
            for codigo in codigos_alternativos:
                if validar_codigo(codigo):
                    codigos_validos.append(codigo)
                else:
                    # Registrar excepción con referencia y código no válido
                    excepciones_outfile.write("{} - {}: No cumple con la longitud mínima de 3 caracteres\n".format(referencia, codigo))

            # Unir los códigos alternativos usando ';' y escribir en el archivo de salida solo si hay códigos válidos
            if codigos_validos:
                writer.writerow([referencia, ';'.join(codigos_validos)])  # Escribir la referencia y los códigos alternativos

    print('El archivo {} ha sido creado con éxito.'.format(output_file))
    print('El archivo {} ha sido creado con las excepciones registradas.'.format(excepciones_file))
