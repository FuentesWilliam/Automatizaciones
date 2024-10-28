import re
import os

# Rutas de los archivos dentro del directorio 'ignore'
archivo_produccion = "ignore/lista_img.txt"
archivo_nuevas = "ignore/nuevas_img.txt"
archivo_resultado = "ignore/coincidencias.txt"

# Crear el directorio 'ignore' si no existe
if not os.path.exists("ignore"):
    os.makedirs("ignore")

# Función para leer referencias y eliminar sufijos como "-2" y extensiones como ".jpg" o ".png"
def leer_archivo_limpio(nombre_archivo):
    referencias = set()
    with open(nombre_archivo, 'r') as file:
        for line in file:
            # Eliminar espacios y saltos de línea
            referencia = line.strip()
            # Remover sufijos (-2, -3, etc.) y extensiones (.jpg, .png) usando una expresión regular
            referencia_limpia = re.sub(r'-\d+(\.jpg|\.png)$|(\.jpg|\.png)$', '', referencia, flags=re.IGNORECASE)
            referencias.add(referencia_limpia)
    return referencias

# Cargar y mostrar referencias de ambos archivos para verificar la lectura y limpieza
referencias_produccion = leer_archivo_limpio(archivo_produccion)
referencias_nuevas = leer_archivo_limpio(archivo_nuevas)

# Comparar referencias y mostrar las coincidencias
productos_en_ambas_listas = referencias_nuevas.intersection(referencias_produccion)
print("\nProductos en ambas listas:")
print(productos_en_ambas_listas)

# Guardar los resultados en un archivo dentro de 'ignore'
with open(archivo_resultado, 'w') as resultado_file:
    resultado_file.write("Productos en ambas listas:\n")
    for producto in productos_en_ambas_listas:
        resultado_file.write("{}\n".format(producto))

print("El archivo 'coincidencias.txt' ha sido creado en el directorio 'ignore'.")
