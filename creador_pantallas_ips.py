
# ******************************************************************************
# Nombre: creador_pantallas_ips.py
#
#   Descripcion: 
#
#       * Generador de pantallas con listas de IPs activas en el dispositivo.
# Estas pantallas se formatearan para poder ser cargadas en el lcd.
# ******************************************************************************

import pdb
import subprocess

import clase_pantalla
import utilidades


#.....................
class Creador_pantallas_ips:

    # =========================================================================
    RUTA_SHELL = utilidades.ejecuta_pwd() + '/shell_scripts/'

    F_LISTA_IPS = RUTA_SHELL + 'lista_ips.sh'
    F_IPS = RUTA_SHELL + 'ips_activas.txt'
    # =========================================================================


    LINEA1_PANTALLA = ("  LISTA   IPs   X   ")
    CIFRA1_C = 3
    CIFRA2_C = 1
    cifra3_c = 1
    C_PANT1_IPS     = (3,1,2)
    C_PANT_NIV_ANT  = (3,0,0)
    C_PANT_OPCIONES = (0,0,0)
    POS_VALIDAS     = (6000,6000,6000,6000)
    CURSOR_PANTALLA = 103
    TIPO = "Pantalla"


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Constructor
    def __init__(self):
        #   NOTA: Los atributos fuera de los metodos se comportan
        # como variables/atributos de clase, compartidos con todas las
        # instancia creadas
        #   La creacion de variables con prefijo 'self' en el constructor
        # hace que se 'transformen' en atributos de la instancia de clase
        # al crear el objeto
        self.lista_pantallas = []
        self.lista_objetos_pantalla = []

        self.crear_lista_pantallas()
        self.crear_objetos_pantalla()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def crear_lista_pantallas(self):
        aux_pantalla = []
        numero_linea = 0
        numero_pantalla = 1
        
        repetir = True

        subprocess.run(['sh', self.F_LISTA_IPS])

        f_ips = open(self.F_IPS, 'r')
        
        while repetir:
            l_lista_ips = f_ips.readline()
        
            if (l_lista_ips):
                l_lista_ips = self.tratar_linea_ips(l_lista_ips)

                if numero_linea == 0:
                    l1 = self.LINEA1_PANTALLA.replace("X", str(numero_pantalla))
                    numero_pantalla = numero_pantalla + 1
                    aux_pantalla.append(l1)
                    numero_linea = numero_linea + 1
        
                # Forzar añadir espacios por la derecha hasta tam. 20
                aux_pantalla.append("{:<20}".format(l_lista_ips))
                numero_linea = numero_linea + 1
        
                if numero_linea == 4:
                    numero_linea = 0

                    self.cifra3_c = self.cifra3_c + 1

                    codigo = (
                            self.CIFRA1_C,
                            self.CIFRA2_C,
                            self.cifra3_c
                            )

                    self.lista_pantallas.append(
                            ((codigo),
                            aux_pantalla[0],
                            aux_pantalla[1],
                            aux_pantalla[2],
                            aux_pantalla[3]
                            ))

                    aux_pantalla = []
            else:

                num_lin = len(aux_pantalla)

                if num_lin != 0:

                    while num_lin < 4:
                        aux_pantalla.append("{:<20}".format(""))
                        num_lin = num_lin + 1

                    self.cifra3_c = self.cifra3_c + 1

                    codigo = (
                            self.CIFRA1_C,
                            self.CIFRA2_C,
                            self.cifra3_c
                            )

                    self.lista_pantallas.append(
                            ((codigo),
                            aux_pantalla[0],
                            aux_pantalla[1],
                            aux_pantalla[2],
                            aux_pantalla[3]
                            ))

                repetir = False
        
        f_ips.close()
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def tratar_linea_ips(self, linea):
        linea_tratada = linea.rsplit("\n")[0]
    
        if (len(linea_tratada) < 20):
            dif = 20 - len(linea_tratada)
            linea_tratada + (" " * dif)
    
        return linea_tratada

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def crear_objetos_pantalla(self):

        cod_primer = (self.lista_pantallas[0])[0]  # Codigo pri pant.
        cod_ultimo = (self.lista_pantallas[-1])[0] # Codigo ult pant.

        for p in self.lista_pantallas:

            cod_actual = p[0]  # Codigo pantalla actual.

            pantalla = clase_pantalla.Pantalla(p)

            if len(self.lista_pantallas) == 1: # Solo 1 pantalla a crear.
                pantalla.set_pantalla_siguiente(cod_primer)
                pantalla.set_pantalla_anterior(cod_primer)
            else: # > 1 pantalla a crear.
                ca3_sig = cod_actual[-1] # Mod. codigo sig. pantalla
                ca3_sig = ca3_sig + 1

                ca3_ant = cod_actual[-1] # Mod. codigo ant. pantalla
                ca3_ant = ca3_ant - 1

                aux_c = list(cod_actual)
                aux_c[-1] = ca3_sig
                aux_sig = tuple(aux_c)

                aux_c = list(cod_actual)
                aux_c[-1] = ca3_ant
                aux_ant = tuple(aux_c)

                if cod_actual == cod_primer:   # Es primera pantalla

                    pantalla.set_pantalla_siguiente(aux_sig)
                    pantalla.set_pantalla_anterior(cod_ultimo)

                elif cod_actual == cod_ultimo: # Es ultima pantalla

                    pantalla.set_pantalla_siguiente(cod_primer)
                    pantalla.set_pantalla_anterior(aux_ant)

                else:                          # Ni primera ni ultima pantalla
                    pantalla.set_pantalla_siguiente(aux_sig)
                    pantalla.set_pantalla_anterior(aux_ant)

            pantalla.set_tipo(self.TIPO)

            pantalla.set_pantalla_nivel_anterior(self.C_PANT_NIV_ANT)
            pantalla.set_pos_validas(self.POS_VALIDAS)
            pantalla.set_pos_actual_cursor(self.CURSOR_PANTALLA)
            pantalla.set_pantalla_opcion1(self.C_PANT_OPCIONES)
            pantalla.set_pantalla_opcion2(self.C_PANT_OPCIONES)
            pantalla.set_pantalla_opcion3(self.C_PANT_OPCIONES)
            pantalla.set_pantalla_opcion4(self.C_PANT_OPCIONES)
            

            self.lista_objetos_pantalla.append(pantalla)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_objetos_pantalla(self):
        lop = self.lista_objetos_pantalla
        return lop
#.....................

