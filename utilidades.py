
#!/usr/bin/python3

# ******************************************************************************
# Nombre: utilidades.py
#
# Descripción: 
#
#   * Agrupación de diversas funciones para su uso en la aplicación.
#
# ******************************************************************************


import subprocess



# Funciones
# ==============================================================================
# ==============================================================================


#   Ejecución del comando 'pwd' en Python. Guardado y devolución del valor en
# una variable. Permite que se ejecute la aplicación independientemente del
# nombre y de la ruta del directorio padre.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ejecuta_pwd():
    cmd = 'pwd'

    # Ejecución del comando.
    #   - capture_output = True -> Guardar los resultados de salida
    #   - text = True -> Salida como texto utf-8
    res = subprocess.run(cmd, capture_output=True, text=True)
    ruta_actual = res.stdout[0:-1]

    return ruta_actual
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

