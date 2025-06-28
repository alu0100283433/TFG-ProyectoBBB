
# ******************************************************************************
# Nombre: clase_creador_password.py

# Descripcion:
#
#   * Va guardando los caracteres que serán la contraseña a usar y tiene
# métodos para devolverla y borrarla. 
#   * La contraseña se crea desde una opción de menú de la aplicación y
# sólo se almacenará mientras la aplicación esté en ejecución.
#   * Se uso es mandarse/ejecutarse directamente cuando se necesite (por
# ejemplo cuando es necesario la contraseña para ejecutar un comando)
# ******************************************************************************


import pdb
import time


from tablas_conversion import CODIGO_CAR_KEY_CODE_PSW1, \
                              CODIGO_CAR_KEY_CODE_PSW2, \
                              CODIGO_CAR_KEY_CODE_PSW3



#.....................
class Creador_password():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Constructor
    def __init__(self):
        self.password = ""
        self.devolver_password = False


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Convertir posicion de pantalla lcd a la de la tabla de conversion.
    def conversion_posicion(self, pos):
        posicion = pos

        if   posicion in range(64, 84):
            posicion = posicion - 44
        elif posicion in range(20, 40):
            posicion = posicion + 20
        elif posicion in range(84, 104):
            posicion = posicion - 24

        return posicion


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Busca un caracter en la tabla de conversion y lo incorpora en
    # la contraseña, si el booleano es False.
    def nuevo_caracter(self, pos, cod_pantalla):
        caracter = ""

        posicion = self.conversion_posicion(pos)


        if self.devolver_password == False:
            if   cod_pantalla == (1,3,1):
                caracter = CODIGO_CAR_KEY_CODE_PSW1[posicion]
            elif cod_pantalla == (1,3,2):
                caracter = CODIGO_CAR_KEY_CODE_PSW2[posicion]
            elif cod_pantalla == (1,3,3):
                caracter = CODIGO_CAR_KEY_CODE_PSW3[posicion]

            # Identificar si es ENTER o no.
            if caracter == "€;":
                # Solo permitir un ENTER en la cadena
                if self.devolver_password == False:
                    self.password = self.password + caracter
                    self.devolver_password = True
            # Identificar si es BACKSPACE o no.
            elif caracter == '€,':
                self.password = self.password[:-1]
            else:
                self.password = self.password + caracter


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Elimina el password.
    def borrar_password(self):
        self.password = ""
        self.devolver_password = False


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Envia la contraseña.
    def get_password(self):
        if self.devolver_password == False:
            return -1
        else:
            return self.password

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Obtener el estado del password ( si se ha pulsado ENTER o no)
    def get_password_completo(self):
        return self.devolver_password
#.....................



