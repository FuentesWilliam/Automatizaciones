
```md
# Guía de Uso de Git

Esta guía cubre los comandos más utilizados en Git y cómo gestionar tus archivos de manera eficiente dentro de un repositorio.

## 1. Verificar el estado del repositorio

Este comando muestra el estado actual de los archivos en tu repositorio. Te indicará qué archivos han sido modificados, añadidos al área de staging o eliminados.

```bash
git status
```

## 2. Añadir archivos al área de staging

Cuando realizas cambios y quieres prepararlos para un commit, añades los archivos al área de staging con:

```bash
git add <ruta/del/archivo>
```

Si quieres añadir todos los archivos modificados al staging:

```bash
git add .
```

⚠**Nota:** Usar `git add .` puede agregar archivos no deseados. Si prefieres controlar más el proceso, añade los archivos uno por uno.

## 3. Ver los archivos añadidos al staging

Para ver los archivos que has añadido al área de staging y los cambios que serán incluidos en el commit:

```bash
git diff --staged
```

Este comando muestra las diferencias de los archivos que ya están en el staging con respecto al último commit. Si solo deseas ver la lista de archivos en staging, usa:

```bash
git status
```

Los archivos listados bajo "Changes to be committed" están en staging y serán incluidos en el próximo commit.

## 4. Confirmar los cambios (commit)

Una vez que los archivos estén en el área de staging, puedes realizar un commit, que guarda esos cambios en el historial del repositorio.

```bash
git commit -m "Descripción del commit"
```

El commit solo incluirá los archivos que han sido añadidos al área de staging. Los archivos modificados pero que no están en staging, así como los archivos no rastreados (untracked files), **no serán** incluidos en el commit.

## 5. Ver el historial de commits

Para ver el historial de commits realizados en el repositorio:

```bash
git log
```

Esto te muestra una lista detallada de commits, incluyendo sus mensajes y hashes únicos.

## 6. Ver las diferencias de los archivos

Para ver los cambios realizados en tus archivos comparados con la última versión confirmada:

```bash
git diff <ruta/del/archivo>
```

Si quieres ver los cambios que están en el staging (en preparación para commit):

```bash
git diff --staged
```

## 7. Restaurar archivos a su versión del último commit

Si modificaste un archivo y deseas restaurarlo a su versión en el último commit, puedes hacerlo con:

```bash
git checkout HEAD -- <ruta/del/archivo>
```

Por ejemplo, si modificaste `exportar_codigos_formateados.py` y quieres deshacer esos cambios:

```bash
git checkout HEAD -- import/exportar_codigos_formateados.py
```

## 8. Descartar cambios en el área de staging

Si añadiste archivos al área de staging y deseas sacarlos sin confirmar los cambios, puedes usar:

```bash
git restore --staged <ruta/del/archivo>
```

Esto moverá el archivo fuera del staging y no se incluirá en el commit.

## 9. Revertir un commit

Si necesitas deshacer un commit anterior sin perder el historial, puedes revertirlo con:

```bash
git revert <hash_del_commit>
```

Esto crea un nuevo commit que deshace los cambios del commit especificado.

## 10. Recuperar archivos eliminados accidentalmente

Si borraste un archivo y deseas restaurarlo a su versión en el último commit, usa:

```bash
git checkout HEAD -- <ruta/del/archivo>
```

Esto recuperará el archivo en cuestión sin modificar otros archivos.

## 11. Sincronizar cambios con un repositorio remoto

Para subir tus cambios confirmados a un repositorio remoto (como GitHub):

```bash
git push origin <nombre_de_la_rama>
```

Si deseas obtener los cambios más recientes del repositorio remoto y fusionarlos con tu rama actual:

```bash
git pull
```