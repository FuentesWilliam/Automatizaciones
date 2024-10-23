import csv
from datetime import datetime
import os

# Función para limpiar el texto de tildes
def limpiar_texto(texto):
    # Remover tildes y caracteres no deseados
    texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    texto = texto.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    return texto

# Archivos de entrada y salida
input_file = 'codigos_limpios.csv'  # Nombre del archivo limpio de entrada
hoy = datetime.now().strftime("%m-%d")

# Verificar si el archivo de entrada existe
if not os.path.exists(input_file):
    print("Error: El archivo 'codigos_limpios.csv' no se encuentra. Asegúrate de ejecutar primero el script de limpieza.")
else:
    # Pedir al usuario el texto a incluir en el archivo de PrestaShop
    texto_prestashop = input("Introduce el texto que se usará en PrestaShop (ej. 'Código OEM'): ")
    texto_prestashop_limpio = limpiar_texto(texto_prestashop)

    # Crear el nombre del archivo para PrestaShop
    prestashop_file = 'prestashop_import-{}-{}.csv'.format(hoy, texto_prestashop_limpio)

    # Intentar leer el archivo de entrada y procesar los datos
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile, open(prestashop_file, mode='w', newline='', encoding='utf-8') as prestashop_outfile:
            
            reader = csv.reader(infile, delimiter='|')  # El delimitador de entrada es '|'
            prestashop_writer = csv.writer(prestashop_outfile, delimiter='|')  # Usamos '|' como delimitador para salida

            # Procesar cada fila en el archivo limpio
            for row in reader:
                referencia = row[0]  # Primer elemento de la fila es la referencia
                codigos_alternativos = row[1].split(';')  # Separar los códigos alternativos

                # Crear la línea de PrestaShop concatenando los códigos alternativos con el texto dado y el índice
                linea_prestashop = ";".join("{}:{}:{}".format(texto_prestashop, codigo, i + 1) for i, codigo in enumerate(codigos_alternativos))

                # Escribir la referencia y los códigos formateados en el archivo
                prestashop_writer.writerow([referencia, linea_prestashop])

        print('El archivo {} ha sido creado para importar en PrestaShop.'.format(prestashop_file))

    except Exception as e:
        print("Se produjo un error: {}".format(e))
