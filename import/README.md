### `README.md`

```markdown
# Limpieza y Exportación de Códigos para MySQL y PrestaShop

Este proyecto contiene scripts en Python para la limpieza y validación de códigos de productos alternativos, exportándolos a formatos adecuados para importación en MySQL y PrestaShop.

## Estructura de archivos

- `limpiar_datos.py`: Script para limpiar los datos de códigos de productos alternativos, validarlos y registrar excepciones.
- `exportar_codigos_formateados.py`: Script para generar un archivo `.csv` con los códigos formateados para su importación en PrestaShop.
- `entrada.csv`: Archivo de entrada con los datos crudos de los códigos.
- `codigos_limpios.csv`: Archivo de salida que contiene los códigos limpios y validados.
- `excepciones.txt`: Archivo donde se registran los códigos que no cumplen con las validaciones.

## Requisitos

- Python 3.x
- Librería estándar `csv`
- No se requiere ninguna dependencia adicional.

## Uso

### 1. Limpieza de datos con `limpiar_datos.py`

Este script procesa el archivo `entrada.csv` y realiza las siguientes tareas:
- Elimina espacios extra alrededor de los códigos.
- Reemplaza comas decimales por puntos.
- Separa los códigos por espacios o por `", "` (coma seguida de espacio).
- Valida que los códigos tengan al menos 3 caracteres.
- Registra las excepciones (códigos no válidos) en el archivo `excepciones.txt`.

#### Ejecutar:

```bash
python limpiar_datos.py
```

#### Archivos generados:
- `codigos_limpios.csv`: Códigos limpiados y validados, listos para su procesamiento posterior.
- `excepciones.txt`: Registro de códigos que no cumplen con las validaciones.

### 2. Exportación para PrestaShop con `exportar_codigos_formateados.py`

Este script toma el archivo `codigos_limpios.csv` generado por el primer script y crea un archivo `.csv` listo para ser importado en PrestaShop. Este archivo incluye un formato específico requerido por PrestaShop, donde los códigos se enumeran con un texto de prefijo y un índice incremental.

#### Ejecutar:

```bash
python exportar_codigos_formateados.py
```

El script pedirá que ingreses un nombre o prefijo para los códigos exportados. Generará un archivo `.csv` con el nombre que elijas.

#### Archivos generados:
- Un archivo `.csv` con los códigos formateados según las reglas de PrestaShop. El nombre incluirá el prefijo proporcionado por el usuario.

### Ejemplo de ejecución

#### Entrada (`entrada.csv`):
```
22130454 S;3,25514 3,18117;22223804
```

#### Salida (`codigos_limpios.csv`):
```
22130454|3.25514;3.18117;22223804
```

#### Salida (`archivo_prestashop.csv`):
```
22130454|Código OEM:3.25514:1;Código OEM:3.18117:2;Código OEM:22223804:3
```

## Manejo de errores

- Si los archivos `entrada.csv` o `codigos_limpios.csv` no se encuentran, el programa notificará el error y saldrá sin realizar cambios.
- Los códigos que no cumplen con la longitud mínima se registran en el archivo `excepciones.txt` junto con su referencia correspondiente.