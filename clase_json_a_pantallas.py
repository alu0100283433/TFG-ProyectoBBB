
# ******************************************************************************
# Nombre: clase_json_a_pantallas.py
#
#   Descripcion: 
#
#       * Abre y carga el fichero JSON con los datos de las pantallas,
# convierte estos en objetos de tipo pantalla y los guarda en una lista
# de las mismas para ser enviadas facilmente a otro sitios (otros objetos,
# por ejemplo)
# ******************************************************************************

import pdb
import json

import clase_pantalla
import utilidades


#.....................
class Json_a_pantallas:

    # =========================================================================
    RUTA_DIR_JSON = utilidades.ejecuta_pwd() + '/ficheros_json/'

    RUTA_JSON = RUTA_DIR_JSON + "/pantallas.json"
    RUTA_COMANDOS_JSON = RUTA_DIR_JSON + "/pantallas_comandos.json"
    # =========================================================================

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Constructor
    def __init__(self, json_a_abrir):

        self.fichero_a_abrir = json_a_abrir

        self.lista_pantallas = []

        self.abrir_leer_json()

        if self.fichero_a_abrir == "pantallas": # Ajuste numeracion
            self.ajustar_ppales()

        self.conversion_a_pantallas()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Abre el Json de pantallas de comandos o el del resto de pantallas.
    def abrir_leer_json(self):

        if self.fichero_a_abrir == "pantallas":
            fichero = self.RUTA_JSON
        elif self.fichero_a_abrir == "comandos":
            fichero = self.RUTA_COMANDOS_JSON

        with open(fichero, 'r') as fj:
            self.lista_datos_json = json.load(fj)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Ajusta el titulo de las pantallas principales para que ponga el
    # numero de pagina y las totales.
    def ajustar_ppales(self):
        p_ppales_totales = 0
        tam_linea = 20

        for i in range(0, len(self.lista_datos_json)):
            p_actual = self.lista_datos_json[i]

            if p_actual["codigo_p"][1] == 0 and p_actual["codigo_p"][2] == 0:
                p_ppales_totales = p_ppales_totales + 1

        for i in range(0, len(self.lista_datos_json)):
            p_actual = self.lista_datos_json[i]

            if p_actual["codigo_p"][1] == 0 and p_actual["codigo_p"][2] == 0:
                codigo_p = p_actual["codigo_p"]
                linea1   = p_actual["linea1"]

                linea1 = (linea1.partition('('))[0]

                linea1 = linea1 + '(' + str(codigo_p[0]) + '/' + \
                         str(p_ppales_totales) + ')'

                while len(linea1) < 20:
                    linea1 = linea1 + ' '

                self.lista_datos_json[i]["linea1"] = linea1


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Guarda en una lista de objetos pantalla datos de cada pantalla del Json
    def conversion_a_pantallas(self):

        for json_p in self.lista_datos_json:
            aux_p = clase_pantalla.Pantalla()

            aux_p.set_codigo(tuple(json_p["codigo_p"]))
            aux_p.set_nombre_codigo(json_p["nombre_codigo"])
            aux_p.set_nombre_pantalla(json_p["nombre_p"])

            aux_p.set_pantalla_siguiente(tuple(json_p["siguiente_p"]))
            aux_p.set_pantalla_anterior(tuple(json_p["anterior_p"]))
            aux_p.set_pantalla_nivel_anterior(tuple(json_p["nivel_anterior_p"]))

            aux_p.set_pos_validas(tuple(json_p["posiciones_validas"]))
            aux_p.set_pos_actual_cursor(json_p["posicion_cursor_actual"])

            aux_p.set_tipo(json_p["tipo"])

            aux_p.set_linea1(json_p["linea1"])
            aux_p.set_linea2(json_p["linea2"])
            aux_p.set_linea3(json_p["linea3"])
            aux_p.set_linea4(json_p["linea4"])

            aux_p.set_pantalla_opcion1(tuple(json_p["opcion1_p"]))
            aux_p.set_pantalla_opcion2(tuple(json_p["opcion2_p"]))
            aux_p.set_pantalla_opcion3(tuple(json_p["opcion3_p"]))
            aux_p.set_pantalla_opcion4(tuple(json_p["opcion4_p"]))

            self.lista_pantallas.append(aux_p)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_lista_pantallas(self):
        copia_lista_pantallas = self.lista_pantallas.copy()

        return copia_lista_pantallas
#.....................

