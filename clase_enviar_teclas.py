
# Nombre: clase_enviar_teclas.py

#   Recepcion de posiciones del teclado del lcd y envio de la
# senhal por el cable USB simulando un teclado virtual. Para
# su funcionamiento debe estar disponible /dev/hidg0 tras
# ejecutar el script que convierte la BeagleBone Black en un
# teclado USB

#   Equivalencias de posicion de la pantalla del teclado (el
# caracter ahi mostrado) con su correspondencia como KEY_CODE
# para el HID montado como teclado virtual USB que es la BBB

# Informacion de enviar informes a /dev/hidg0 sacado de:
#
# https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-send-reports/

import pdb
import time

"""
from tablas_conversion import CODIGO_LCD_KEY_CODE1_1, \
                              CODIGO_LCD_KEY_CODE1_2, \
                              CODIGO_CAR_KEY_CODE1, \
                              CODIGO_CAR_KEY_CODE2, \
                              CODIGO_KEY_CODE_COMANDOS2, \
                              CODIGO_LCD_KEY_CODE_LOGIN1, \
                              CODIGO_LCD_KEY_CODE_LOGIN2, \
                              CODIGO_LCD_KEY_CODE_LOGIN3, \
                              CODIGO_CAR_KEY_CODE_LOGIN1, \
                              CODIGO_CAR_KEY_CODE_LOGIN2, \
                              CODIGO_CAR_KEY_CODE_LOGIN3, \
                              K_SUELTA, K_CAPUCHO, K_LCTRL, K_LSHIFT, \
                              K_LALT, K_LMETA, K_RCTRL, K_RSHIFT, \
                              K_RALT, K_RMETA, K_F1, K_F2, K_F3, \
                              K_F4, K_F5, K_F6, K_F7, K_F8, K_F9, K_F10, \
                              K_F11, K_F12, K_ENTER, K_BCKSP, K_ESPERA2, \
                              K_SPACE
"""

from tablas_conversion import CODIGO_LCD_KEY_CODE1_1, \
                              CODIGO_LCD_KEY_CODE1_2, \
                              CODIGO_CAR_KEY_CODE1, \
                              CODIGO_CAR_KEY_CODE2, \
                              CODIGO_KEY_CODE_COMANDOS2, \
                              CODIGO_LCD_KEY_CODE_PSW1, \
                              CODIGO_LCD_KEY_CODE_PSW2, \
                              CODIGO_LCD_KEY_CODE_PSW3, \
                              CODIGO_CAR_KEY_CODE_PSW1, \
                              CODIGO_CAR_KEY_CODE_PSW2, \
                              CODIGO_CAR_KEY_CODE_PSW3, \
                              K_SUELTA, K_CAPUCHO, K_LCTRL, K_LSHIFT, \
                              K_LALT, K_LMETA, K_RCTRL, K_RSHIFT, \
                              K_RALT, K_RMETA, K_F1, K_F2, K_F3, \
                              K_F4, K_F5, K_F6, K_F7, K_F8, K_F9, K_F10, \
                              K_F11, K_F12, K_ENTER, K_BCKSP, K_ESPERA2, \
                              K_SPACE

class Enviar_teclas():


    # Constructor
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, c_p):
        self.posicion = -1
        #self.key_code = -1
        self.key_report = -1
        self.codigo_pantalla = c_p

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_posicion_tabla_conversion(self): # Cambio pos. lcd a tabla conv.
        pos_v = self.posicion

        if   pos_v in range(64,84):
            pos_v = pos_v - 44
        elif pos_v in range(20,40):
            pos_v = pos_v + 20 
        elif pos_v in range(84,104):
            pos_v = pos_v - 24

        return pos_v

    #   Metodo que busca el key code de un caracter pasado buscandolo en una
    # tabla de conversion
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def obtener_key_code_caracter(self):
        contador = 0
        posicion_kc1 = -1
        posicion_kc2 = -1


        # 1ro: obtener posicion tablas conversion caracteres
        for i in CODIGO_CAR_KEY_CODE1:
            if (self.caracter == CODIGO_CAR_KEY_CODE1[contador]):
                #posicion_kc1 = i
                posicion_kc1 = contador
                break

            contador = contador + 1

        contador = 0

        for i in CODIGO_CAR_KEY_CODE2:
            if (self.caracter == CODIGO_CAR_KEY_CODE2[contador]):
                #posicion_kc2 = i
                posicion_kc2 = contador
                break

            contador = contador + 1

        #breakpoint()

        # 2do: Ir a la tabla de conversion de los key_codes y extraer el pedido.
        if posicion_kc1 != -1:
            return CODIGO_LCD_KEY_CODE1_1[posicion_kc1]
        elif posicion_kc2 != -1:
            #breakpoint()
            #return CODIGO_LCD_KEY_CODE1_2[posicion_kc2]
            return CODIGO_KEY_CODE_COMANDOS2[posicion_kc2] # Para teclas control
        else:
            return CODIGO_LCD_KEY_CODE1_2[40] # Espacio



    # Obtencion del key_code_report listo para escribirlo en un medio
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def conversion_posicion_key_code(self):
        #breakpoint()
        if   self.codigo_pantalla == (1,1,1):
            #self.key_code = CODIGO_LCD_KEY_CODE1_1.index(self.posicion)
            posi = self.get_posicion_tabla_conversion()
            #self.key_report = CODIGO_LCD_KEY_CODE1_1[self.posicion]
            self.key_report = CODIGO_LCD_KEY_CODE1_1[posi]
        elif self.codigo_pantalla == (1,1,2):
            #self.key_code = CODIGO_LCD_KEY_CODE1_2.index(self.posicion)
            posi = self.get_posicion_tabla_conversion()
            #self.key_report = CODIGO_LCD_KEY_CODE1_2[self.posicion]
            self.key_report = CODIGO_LCD_KEY_CODE1_2[posi]
        elif self.codigo_pantalla == (1,3,1): # Pantallas login
            posi = self.get_posicion_tabla_conversion()
            #self.key_report = CODIGO_LCD_KEY_CODE_LOGIN1[posi]
            self.key_report = CODIGO_LCD_KEY_CODE_PSW1[posi]
        elif self.codigo_pantalla == (1,3,2):
            posi = self.get_posicion_tabla_conversion()
            #self.key_report = CODIGO_LCD_KEY_CODE_LOGIN2[posi]
            self.key_report = CODIGO_LCD_KEY_CODE_PSW2[posi]
        elif self.codigo_pantalla == (1,3,3):
            posi = self.get_posicion_tabla_conversion()
            #self.key_report = CODIGO_LCD_KEY_CODE_LOGIN3[posi]
            self.key_report = CODIGO_LCD_KEY_CODE_PSW3[posi]
        elif (self.codigo_pantalla[0] == 1) and (self.codigo_pantalla[1] == 2):
            self.key_report = self.obtener_key_code_caracter()


    #   Tras obtener el key_code report de la tecla, mandarlo a /dev/hidg0
    # y que escriba el teclado virtual.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def escritura_key_press_report(self):
        error = False

        with open('/dev/hidg0', 'rb+') as char_dev: # character device
            # Codificacion por defecto: UTF-8

            try:
                if (self.key_report == K_CAPUCHO):
                    char_dev.write(self.key_report.encode()) 
                    char_dev.write(K_SUELTA.encode())
                    char_dev.write(self.key_report.encode()) 
                    char_dev.write(K_SUELTA.encode())
                    char_dev.close()
                else:
                    char_dev.write(self.key_report.encode()) 
                    char_dev.write(K_SUELTA.encode())
                    char_dev.close()
            except BrokenPipeError:
                #print("Error. Cable no conectado")
                error = True

        return error

    #   Metodo gestion de operaciones a hacer para escribir una tecla en
    # un medio. -> Metodo general para teclas
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def enviar_tecla(self, pos): # Al 'pulsar' una tecla en el teclado
        self.posicion = pos

        self.conversion_posicion_key_code()

        error = self.escritura_key_press_report()

        return error

    #   Metodo gestion de operaciones  a hacer para escribir un caracter
    # pasado en un medio. -> Metodo general para caracteres
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def enviar_caracter(self, caracter): # Escribir el caracter enviado
        self.caracter = caracter 

        self.conversion_posicion_key_code()

        error = self.escritura_key_press_report()

        return error


    #   Al simular secuencias de escape con '€' se deben asociar con el caracter
    # necesario (definidos en las tablas de conversion) que corresponderan a 
    # una tecla de control o Fx.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def lista_caracteres_asociados(self, lista_linea):
        l_c_a = []

        while (len(lista_linea) > 0):
            aux_caracter = lista_linea.pop(0)

            if aux_caracter == '€':
                if len(lista_linea) > 0:
                    aux_caracter = aux_caracter + lista_linea.pop(0)
                else:
                    aux_caracter = ' '

            l_c_a.append(aux_caracter)


        return l_c_a.copy()


    #   Recorrer la lista de caracteres asociados y formar una lista con los
    # KEY_CODES de cada caracter/caracteres de escape.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def l_c_a_a_Key_Codes_Login(self, lca):

        lista_KC = []
        aux_KC = 0

        #for c in range(0, len(lca)):
        for c in lca:
            contador = 0
            posicion_kc1 = -1
            posicion_kc2 = -1
            posicion_kc3 = -1


            # 1ro: obtener posicion tablas conversion caracteres
            #for i in CODIGO_CAR_KEY_CODE_LOGIN1:
            for i in CODIGO_CAR_KEY_CODE_PSW1:
                #if (c == CODIGO_CAR_KEY_CODE_LOGIN1[contador]):
                if (c == CODIGO_CAR_KEY_CODE_PSW1[contador]):
                    posicion_kc1 = contador
                    break

                contador = contador + 1

            contador = 0


            #for i in CODIGO_CAR_KEY_CODE_LOGIN2:
            for i in CODIGO_CAR_KEY_CODE_PSW2:
                #if (c == CODIGO_CAR_KEY_CODE_LOGIN2[contador]):
                if (c == CODIGO_CAR_KEY_CODE_PSW2[contador]):
                    posicion_kc2 = contador
                    break

                contador = contador + 1

            contador = 0


            #for i in CODIGO_CAR_KEY_CODE_LOGIN3:
            for i in CODIGO_CAR_KEY_CODE_PSW3:
                #if (c == CODIGO_CAR_KEY_CODE_LOGIN3[contador]):
                if (c == CODIGO_CAR_KEY_CODE_PSW3[contador]):
                    posicion_kc3 = contador
                    break

                contador = contador + 1


            #breakpoint()

            # 2do: Ir a la tabla de conversion de los key_codes y extraer el pedido.
            if posicion_kc1 != -1:
                #aux_KC =  CODIGO_LCD_KEY_CODE_LOGIN1[posicion_kc1]
                aux_KC =  CODIGO_LCD_KEY_CODE_PSW1[posicion_kc1]
            elif posicion_kc2 != -1:
                #aux_KC = CODIGO_LCD_KEY_CODE_LOGIN2[posicion_kc2] 
                aux_KC = CODIGO_LCD_KEY_CODE_PSW2[posicion_kc2] 
            elif posicion_kc3 != -1:
                #aux_KC = CODIGO_LCD_KEY_CODE_LOGIN3[posicion_kc3] 
                aux_KC = CODIGO_LCD_KEY_CODE_PSW3[posicion_kc3] 
            else:
                #aux_KC = CODIGO_LCD_KEY_CODE1_2[40] # Espacio
                #aux_KC =  CODIGO_LCD_KEY_CODE_LOGIN1[0] # Espacio
                aux_KC =  CODIGO_LCD_KEY_CODE_PSW1[0] # Espacio

            lista_KC.append(aux_KC)

        #breakpoint()

        return lista_KC.copy()


    #   Recorrer la lista de caracteres asociados y formar una lista con los
    # KEY_CODES de cada caracter/caracteres de escape.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def l_c_a_a_Key_Codes(self, lca):

        lista_KC = []
        aux_KC = 0

        #for c in range(0, len(lca)):
        for c in lca:
            contador = 0
            posicion_kc1 = -1
            posicion_kc2 = -1


            # 1ro: obtener posicion tablas conversion caracteres
            for i in CODIGO_CAR_KEY_CODE1:
                if (c == CODIGO_CAR_KEY_CODE1[contador]):
                    posicion_kc1 = contador
                    break

                contador = contador + 1

            contador = 0

            #breakpoint()

            #for i in CODIGO_CAR_KEY_CODE2:
            for i in CODIGO_CAR_KEY_CODE2:
                if (c == CODIGO_CAR_KEY_CODE2[contador]):
                    posicion_kc2 = contador
                    break

                contador = contador + 1

            #breakpoint()


            # 2do: Ir a la tabla de conversion de los key_codes y extraer el pedido.
            if posicion_kc1 != -1:
                aux_KC =  CODIGO_LCD_KEY_CODE1_1[posicion_kc1]
            elif posicion_kc2 != -1:
                #breakpoint()
                aux_KC = CODIGO_KEY_CODE_COMANDOS2[posicion_kc2] # Para teclas control
            else:
                aux_KC = CODIGO_LCD_KEY_CODE1_2[40] # Espacio

            lista_KC.append(aux_KC)

        #breakpoint()

        return lista_KC.copy()
            

    #   Como los key codes estan ya como strings, para sumar dos hay que hacer
    # varias operaciones intermedias, operaciones hechas en este metodo.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def suma_string_de_bytes(self, key_code_string1, key_code_string2):

        #breakpoint()

        resultado_bytes = -1

        # Proceso:
        # 1) De string a byte
        kc_byte1 = key_code_string1.encode("utf-8")
        kc_byte2 = key_code_string2.encode("utf-8")

        #   Problema: Cada vez que se encuentre en el string
        # un 'valor' byte algo mayor de \0x7f va a anhadir
        # justo antes de este un byte \xc2 en el resultado de
        # aplicar .encode("uft-8"). Esto nos descuadra los
        # calculos y revienta las operaciones. Habra que tratar
        # los bytes resultantes y eliminarles todos los valores
        # \xc2.
        #   El problema es al intentar usar la tecla RMETA o
        # RMETA con otras teclas de control, generando un byte
        # como de error antes del byte de las teclas de control
        # en el key_code
        if len(kc_byte1) > 8:
                aux_limpia = list(kc_byte1)
                #aux_limpia.pop(0)
                aux_limpia = [i for i in aux_limpia if i < 194]
                kc_byte1 = bytes(aux_limpia)
        if len(kc_byte2) > 8:
                aux_limpia = list(kc_byte2)
                #aux_limpia.pop(0)
                aux_limpia = [i for i in aux_limpia if i < 194]
                kc_byte2 = bytes(aux_limpia)

        # 2) Sumar cada byte individual y montarlo en una variable.
        #for el in range(0, 8):
        for i in range(0, len(kc_byte1)):
            aux = kc_byte1[i] + kc_byte2[i]

            if resultado_bytes == -1:
                resultado_bytes = aux.to_bytes(1, 'big')
            else:
                resultado_bytes = resultado_bytes +  aux.to_bytes(1, 'big')

        #breakpoint()

        resultado_final = -1

        # 3) El resultado en bytes convertirlo en un string
        for elem in range(0, len(resultado_bytes)):
            if resultado_final == -1:
                resultado_final = chr(resultado_bytes[elem])
            else:
                resultado_final = resultado_final + chr(resultado_bytes[elem])

        #breakpoint()
        #resultado_final = resultado_bytes.decode("utf-8")

        return resultado_final

    #   Gestiona la escritura de los Key Codes a /dev/hidg0. Recibe una lista
    # con todos los Key Codes a presionar pero gestiona los casos en los que
    # hay teclas de control o F1-12
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def escritura_linea_key_press_report(self, linea_KC):
        num_escrituras = 0
        error = False
        envio_KC = -1

        #breakpoint()

        #with open('/dev/hidg0', 'rb+') as char_dev: # character device
        # Codificacion por defecto: UTF-8
        # ===============================
        while (len(linea_KC) > 0):
            aux_KC = linea_KC.pop(0)

            # Si es una tecla de control la actual
            if (
                aux_KC == K_LCTRL  or
                aux_KC == K_LSHIFT or
                aux_KC == K_LALT   or
                #aux_KC == K_LMETA or # RMETA no funciona igual que LMETA
                aux_KC == K_RCTRL or
                aux_KC == K_RSHIFT or
                aux_KC == K_RALT or
                aux_KC == K_RMETA
               ):
                # Si no hubo teclas de control en espera previas
                #if envio_KC != -1: 
                if envio_KC == -1: 
                    # Es la 1ra tecla de control que se da 
                    envio_KC = aux_KC # Es la 1ra tecla control
                # Si hubo teclas de control en espera previas
                else:
                    # TODO TODO
                    # Problema: Los valores ya son string y no puede
                    # hacerse una suma de los bytes a nivel individual:
                    # Hay que hacer un tratamiento previo
                    # Solucion: metodo suma_string_de_bytes

                    # Unir la tecla/s de control previa con la actual
                    #envio_KC = envio_KC + aux_KC 
                    #breakpoint()
                    envio_KC = self.suma_string_de_bytes(envio_KC, aux_KC)
            # Si no es una tecla de control la actual
            else:
                # Si no hubo teclas de control previas
                #if envio_KC != -1:
                if envio_KC == -1:
                    envio_KC = aux_KC
                # Si hubo teclas de control previas
                else:
                    # TODO TODO
                    #envio_KC = envio_KC + aux_KC
                    #breakpoint()
                    envio_KC = self.suma_string_de_bytes(envio_KC, aux_KC)
                    #breakpoint()
                # Y por fin mandar a escribir la tecla/combinacion
                try:
                    #if (aux_KC  == K_CAPUCHO):
                    if (envio_KC  == K_CAPUCHO):
                        with open('/dev/hidg0', 'rb+') as char_dev: # character device
                            #char_dev.write(aux_KC.encode()) 
                            char_dev.write(envio_KC.encode()) 
                            char_dev.write(K_SUELTA.encode())
                            #char_dev.write(aux_KC.encode()) 
                            char_dev.write(envio_KC.encode()) 
                            char_dev.write(K_SUELTA.encode())

                            num_escrituras = num_escrituras + 1

                            #time.sleep(0.1)
                            char_dev.close()

                        envio_KC = -1
                    elif (envio_KC == K_ESPERA2):
                        K_ESPERA2(2)
                        envio_KC = -1
                    else:
                        #breakpoint()
                        with open('/dev/hidg0', 'rb+') as char_dev: # character device
                            #breakpoint()
                            # Eliminar bytes de error si uso RMETA
                            envio_KC_cod = envio_KC.encode()
                            envio_KC_cod = [i for i in envio_KC_cod if i < 194]
                            envio_KC_cod = bytes(envio_KC_cod)
                            #char_dev.write(aux_KC.encode()) 
                            char_dev.write(envio_KC_cod) 
                            char_dev.write(K_SUELTA.encode())

                            num_escrituras = num_escrituras + 1

                            #time.sleep(0.1)
                            char_dev.close()

                        envio_KC = -1

                except BrokenPipeError:
                    #print("Error. Cable no conectado")
                    char_dev.close()
                    error = True

        # ===============================

        print("Numero de escrituras fueron:", num_escrituras)

        return error


    #   Metodo que recibe y trata una linea de comandos que fueron extraidos
    # de la pantalla de comandos cargada de un JSON.
    #   Se usa porque si usamos combinaciones de caracteres para definir teclas
    # de control o Fx la linea entera debe ser tratada a la vez, pues las
    # combinaciones de teclas con una o varias teclas de control mas un caracter
    # deben ser enviadas de golpe a /dev/hidg0, no pueden ser enviadas una a una.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def enviar_linea(self, linea):
        self.linea = linea 

        # linea a lista de caracteres
        lista_linea = list(linea)

        # lista de caracteres a lista de caracters asociados
        # (p.e.: '€', 'c' = '€c'
        lista_c_a = self.lista_caracteres_asociados(lista_linea)

        #breakpoint()
        
        if self.codigo_pantalla == (2,0,0):
            print()
            # lista de caracteres asociados a lista de KEY_CODES password
            lista_c_a_KC = self.l_c_a_a_Key_Codes_Login(lista_c_a)
        else:
            # lista de caracteres asociados a lista de KEY_CODES
            lista_c_a_KC = self.l_c_a_a_Key_Codes(lista_c_a)

        #breakpoint()

        # escritura de los KEY_CODES en un KEY_PRESS REPORT
        error = self.escritura_linea_key_press_report(lista_c_a_KC)


        return error

    # Borrar todos los caracteres enviados de login cuando no se hace un ENTER.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def limpiar_enviado(self):
        # lista de caracteres asociados a lista de  KEY_CODES
        #lista_c_a_KC = self.l_c_a_a_Key_Codes(lista_c_a)
        lista_c_a_KC = [K_BCKSP] * 100

        #breakpoint()

        # escritura de los KEY_CODES en un KEY_PRESS REPORT
        error = self.escritura_linea_key_press_report(lista_c_a_KC)


        return error
