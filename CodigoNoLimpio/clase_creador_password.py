
# Nombre: clase_creador_password.py

#   Descripcion: Va guardando los caracteres que seran la contrasenha
# a usar y tiene metodos para devolverla y borrarla. 

import pdb
import time

from tablas_conversion import CODIGO_CAR_KEY_CODE_LOGIN1, \
                              CODIGO_CAR_KEY_CODE_LOGIN2, \
                              CODIGO_CAR_KEY_CODE_LOGIN3

class Creador_password():
    def __init__(self):
        self.password = ""
        self.devolver_password = False

    # Convertir posicion de pantalla lcd a la de la tabla de conversion.
    # --------------------------------------------------------------------------
    def conversion_posicion(self, pos):
        posicion = pos

        if   posicion in range(64, 84):
            posicion = posicion - 44
        elif posicion in range(20, 40):
            posicion = posicion + 20
        elif posicion in range(84, 104):
            posicion = posicion - 24

        return posicion
    #   Busca caracter en la tabla de conversion y lo incorpora en
    # la contrasenha, si el booleano es False.
    # --------------------------------------------------------------------------
    def nuevo_caracter(self, pos, cod_pantalla):
        caracter = ""

        posicion = self.conversion_posicion(pos)

        print("Posicion generador password es: ", posicion)

        if self.devolver_password == False:
            if   cod_pantalla == (1,3,1):
                caracter = CODIGO_CAR_KEY_CODE_LOGIN1[posicion]
            elif cod_pantalla == (1,3,2):
                caracter = CODIGO_CAR_KEY_CODE_LOGIN2[posicion]
            elif cod_pantalla == (1,3,3):
                caracter = CODIGO_CAR_KEY_CODE_LOGIN3[posicion]

            #breakpoint()

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


    # Elimina el password.
    # --------------------------------------------------------------------------
    def borrar_password(self):
        self.password = ""
        self.devolver_password = False


    # Envia contrasenha.
    # --------------------------------------------------------------------------
    def get_password(self):
        if self.devolver_password == False:
            return -1
        else:
            return self.password

    # Obtener estado password (se ha pulsado ENTER o no
    # --------------------------------------------------------------------------
    def get_password_completo(self):
        return self.devolver_password



