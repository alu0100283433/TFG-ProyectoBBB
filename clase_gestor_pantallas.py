
# ******************************************************************************
# Nombre: clase_gestor_pantallas.py
#
#   Descripcion: 
#
#       * Clase que gestiona todas las pantallas (objetos de esa clase). 
# Carga las mismas y se encarga de rotar las pantallas cuando se eligen
# las opciones necesarias.
#
# - Codigos de los cursores:
#
#   5000 = Pantalla no interactuable con cursores.
#   6000 = Otro tipo de pantalla no interactuable.
#   2000 = No tiene restricciones, se puede mover por toda la pantalla.
#   1000 = Posicion (linea del lcd) no permitida en la pantalla.
# ******************************************************************************

import pdb
import copy

import creador_pantallas_ips
import clase_json_a_pantallas


#.....................
class Gestor_pantallas:

    RANGO_LINEA1 = range(00,20) # Rango de cursores usables en pantalla lcd.
    RANGO_LINEA2 = range(64,84)
    RANGO_LINEA3 = range(20,40)
    RANGO_LINEA4 = range(84,104)

    RANGO_LINEAS = (RANGO_LINEA1, RANGO_LINEA2, RANGO_LINEA3, RANGO_LINEA4)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Constructor
    def __init__ (self):

        self.lista_pantallas = []

        j_a_p = clase_json_a_pantallas.Json_a_pantallas("pantallas")

        self.lista_pantallas = j_a_p.get_lista_pantallas()

        del j_a_p


        self.pantalla_actual   = self.lista_pantallas[0] # Copia ref.

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_c_pantalla_actual(self, cpa):
        self.pantalla_actual.set_codigo(cpa)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_c_pantalla_actual(self):
        return self.pantalla_actual.get_codigo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def mostrar_pantallas(self):
        for p in self.lista_pantallas:
            p.mostrar_pantalla_texto()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_indice_pantalla_actual(self):
        cpa = self.pantalla_actual.get_codigo()

        indice = 0

        for p in self.lista_pantallas:
            if cpa == p.get_codigo(): # Ordenar para comparar.
                break
            else:
                indice = indice + 1

        return indice

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_indice_codigo_pantalla(self, codigo):

        indice = -1 

        for pantalla in self.lista_pantallas:
            indice = indice + 1

            if codigo == pantalla.get_codigo(): # Ordenar para comparar.
                break

        return indice

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_actual(self, pantalla_nueva):
        indice = self.get_indice_pantalla_actual()

        self.lista_pantallas[indice] = pantalla_nueva
        self.pantalla_actual = pantalla_nueva

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_actual(self):
        return self.pantalla_actual 

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def mostrar_pantalla_actual(self):
        self.pantalla_actual.mostrar_pantalla_texto()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Mover una pos. arriba en pantallas tipo lista.
    def mover_cursor_uno_arriba_lista(self):
        cambiar_de_pantalla = False

        # Obtener cursor actual
        pantalla_aux = self.get_pantalla_actual()
        cursor_aux = pantalla_aux.get_pos_actual_cursor()

        #   Con la linea en donde esta el cursor, recorriendo continuamente
        # todo hasta encontrar la primera posicion valida.
        continuar = True

        #   Como se supone que es una pos valida, vamos a ver en
        # que linea está.
        lista_pos_validas = pantalla_aux.get_pos_validas()

        l_cursor_actual = 0

        for pos_linea in lista_pos_validas:
            if (cursor_aux == pos_linea):
                break
            else:
                l_cursor_actual = l_cursor_actual + 1


        while continuar == True:

            #   Si es linea 1 de la pantalla. Pasar a la anterior y a la 4
            if l_cursor_actual == 0:
                self.mover_anterior_pantalla()

                l_cursor_actual = 3

                pantalla_aux = self.get_pantalla_actual()

                lista_pos_validas = pantalla_aux.get_pos_validas()
                nuevo_cursor = lista_pos_validas[l_cursor_actual]
                self.pantalla_actual.set_pos_actual_cursor(nuevo_cursor)

                pantalla_aux = self.get_pantalla_actual()

                cursor_aux = pantalla_aux.get_pos_actual_cursor()

                cambiar_de_pantalla = True
            # Si son las linea 2-4, pasar a la anterior
            else:
                l_cursor_actual = l_cursor_actual - 1

                lista_pos_validas = pantalla_aux.get_pos_validas()
                nuevo_cursor = lista_pos_validas[l_cursor_actual]
                self.pantalla_actual.set_pos_actual_cursor(nuevo_cursor)

                pantalla_aux = self.get_pantalla_actual()
                cursor_aux = pantalla_aux.get_pos_actual_cursor()

            if l_cursor_actual == -1:
                l_cursor_actual = 3


            if cursor_aux != 1000: # Si hay pos. viable, terminar.
                continuar = False

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Mover una pos. arriba en pantallas tipo teclado.
    def mover_cursor_uno_arriba_teclado(self):
        cambiar_de_pantalla = False

        pantalla_aux = self.get_pantalla_actual()
        cursor_aux   = pantalla_aux.get_pos_actual_cursor()

        continuar = True

        # Bucle. Una posicion arriba cada vez
        while continuar == True:
            # Obtener linea del cursor actual
            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            # Segun linea actual mover a linea anterior 
            if l_cursor_actual == 0:
                self.mover_anterior_pantalla()
                cursor_aux = cursor_aux + 84
                cambiar_de_pantalla = True
            elif l_cursor_actual == 1:
                cursor_aux = cursor_aux - 64
            elif l_cursor_actual == 2:
                cursor_aux = cursor_aux + 44
            elif l_cursor_actual == 3:
                cursor_aux = cursor_aux - 64

            # Ajustar el cursor. Mover cursor a nueva pos.
            self.pantalla_actual.set_pos_actual_cursor(cursor_aux)

            # Obtener la lista de cursores por linea validos en
            # la nueva linea. Si la nueva linea es 1000, no es
            # una pos. valida, moverse una linea arriba/pantalla
            # anterior.

            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            aux_pos_lineas = self.pantalla_actual.get_pos_validas()

            if aux_pos_lineas[l_cursor_actual] != 1000:
                continuar = False

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Gestor de movimiento una pos. de cursor arriba segun tipo de pantalla
    def mover_cursor_uno_arriba(self): 
        cambiar_de_pantalla = False

        pantalla_aux = self.get_pantalla_actual()
        tipo_aux     = pantalla_aux.get_tipo()
        cursor_aux   = pantalla_aux.get_pos_actual_cursor()

        # Operacion por tipos de pantalla
        if   tipo_aux == "Lista":
            cambiar_de_pantalla = self.mover_cursor_uno_arriba_lista() 
        elif tipo_aux == "Pantalla":
            self.mover_anterior_pantalla()
            cambiar_de_pantalla = True
        elif tipo_aux == "Teclado" or tipo_aux == "Password":
            cambiar_de_pantalla = self.mover_cursor_uno_arriba_teclado()

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Mover una pos. abajo en pantallas tipo teclado.
    def mover_cursor_uno_abajo_lista(self):
        cambiar_de_pantalla = False

        # Obtener cursor actual
        pantalla_aux = self.get_pantalla_actual()
        cursor_aux = pantalla_aux.get_pos_actual_cursor()

        #   Con la linea en donde esta el cursor, recorriendo continuamente
        # todo hasta encontrar la primera posicion valida.
        continuar = True

        #   Suponemos pos. válida. Vemos en que línea está.
        lista_pos_validas = pantalla_aux.get_pos_validas()

        l_cursor_actual = 0

        for pos_linea in lista_pos_validas:
            if (cursor_aux == pos_linea):
                break
            else:
                l_cursor_actual = l_cursor_actual + 1

        while continuar == True:

            #   Si es linea 4 de la pantalla. Pasar a la siguiente y a linea 1
            if l_cursor_actual == 3:
                self.mover_siguiente_pantalla()

                l_cursor_actual = 0

                pantalla_aux = self.get_pantalla_actual()

                lista_pos_validas = pantalla_aux.get_pos_validas()
                nuevo_cursor = lista_pos_validas[l_cursor_actual]
                self.pantalla_actual.set_pos_actual_cursor(nuevo_cursor)

                pantalla_aux = self.get_pantalla_actual()

                cursor_aux = pantalla_aux.get_pos_actual_cursor()

                cambiar_de_pantalla = True
            # Si son las linea 1-3, pasar a la siguiente
            else:
                l_cursor_actual = l_cursor_actual + 1

                lista_pos_validas = pantalla_aux.get_pos_validas()
                nuevo_cursor = lista_pos_validas[l_cursor_actual]
                self.pantalla_actual.set_pos_actual_cursor(nuevo_cursor)

                pantalla_aux = self.get_pantalla_actual()
                cursor_aux = pantalla_aux.get_pos_actual_cursor()

            if l_cursor_actual == 4:
                l_cursor_actual = 0

            if cursor_aux != 1000: # Si hay pos. viable, terminar.
                continuar = False

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Mover una pos. abajo en pantallas tipo teclado.
    def mover_cursor_uno_abajo_teclado(self):
        cambiar_de_pantalla = False

        pantalla_aux = self.get_pantalla_actual()
        cursor_aux   = pantalla_aux.get_pos_actual_cursor()

        continuar = True

        # Bucle. Una posicion arriba cada vez
        while continuar == True:
            # Obtener linea del cursor actual
            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1


            # Segun linea actual mover a linea siguiente
            if l_cursor_actual == 0:
                cursor_aux = cursor_aux + 64
            elif l_cursor_actual == 1:
                cursor_aux = cursor_aux - 44
            elif l_cursor_actual == 2:
                cursor_aux = cursor_aux + 64
            elif l_cursor_actual == 3:
                self.mover_siguiente_pantalla()
                cursor_aux = cursor_aux - 84
                cambiar_de_pantalla = True

            # Ajustar el cursor. Mover cursor a nueva pos.
            self.pantalla_actual.set_pos_actual_cursor(cursor_aux)

            # Obtener la lista de cursores por linea validos en
            # la nueva linea. Porque si en la nueva linea su valor
            # es 1000 es que no es una posicion valida y hay que
            # volver a moverse una linea hacia arriba (o pantalla
            # anterior).

            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            aux_pos_lineas = self.pantalla_actual.get_pos_validas()

            if aux_pos_lineas[l_cursor_actual] != 1000:
                continuar = False

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Gestor de movimiento una posicion abajo segun el tipo de pantalla
    def mover_cursor_uno_abajo(self):
        cambiar_de_pantalla = False

        pantalla_aux = self.get_pantalla_actual()
        tipo_aux     = pantalla_aux.get_tipo()
        cursor_aux   = pantalla_aux.get_pos_actual_cursor()

        # Operacion por tipos de pantallas
        if tipo_aux == "Lista":
            cambiar_de_pantalla = self.mover_cursor_uno_abajo_lista()
        elif tipo_aux == "Pantalla":
            self.mover_siguiente_pantalla()
            cambiar_de_pantalla = True
        elif tipo_aux == "Teclado" or tipo_aux == "Password":
            cambiar_de_pantalla = self.mover_cursor_uno_abajo_teclado()

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Mover una pos. izquierda en pantallas tipo teclado
    def mover_cursor_uno_izquierda(self):
        cambiar_de_pantalla = False

        pantalla_aux = self.get_pantalla_actual()
        tipo_aux     = pantalla_aux.get_tipo()
        cursor_aux   = pantalla_aux.get_pos_actual_cursor()

        if tipo_aux != "Teclado" and tipo_aux != "Password":
            return cambiar_de_pantalla

        continuar = True

        # Bucle. Una posicion izquierda cada vez
        while continuar == True:
            # Obtener linea del cursor actual
            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            # Segun linea actual mover una pos. izquierda 
            if   cursor_aux == 0:
                self.mover_anterior_pantalla()
                cursor_aux = cursor_aux + 103 #P103
                cambiar_de_pantalla = True
            elif cursor_aux == 64:
                cursor_aux = cursor_aux - 45  #P19
            elif cursor_aux == 20:
                cursor_aux = cursor_aux + 63  #P83
            elif cursor_aux == 84:
                cursor_aux = cursor_aux - 45  #P39
            else:
                cursor_aux = cursor_aux - 1

            # Ajustar el cursor. Mover cursor a nueva pos.
            self.pantalla_actual.set_pos_actual_cursor(cursor_aux)

            # Obtener la lista de cursores por linea validos en
            # la nueva linea. Porque si en la nueva linea su valor
            # es 1000 es que no es una posicion valida y hay que
            # volver a moverse una posicion a la izquierda (o
            # pantalla anterior).

            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            aux_pos_lineas = self.pantalla_actual.get_pos_validas()

            if aux_pos_lineas[l_cursor_actual] != 1000:
                continuar = False

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Mover una pos. derecha en pantallas tipo teclado
    def mover_cursor_uno_derecha(self):
        cambiar_de_pantalla = False

        pantalla_aux = self.get_pantalla_actual()
        tipo_aux     = pantalla_aux.get_tipo()
        cursor_aux   = pantalla_aux.get_pos_actual_cursor()

        if tipo_aux != "Teclado" and tipo_aux != "Password":
            return cambiar_de_pantalla

        continuar = True

        # Bucle. Una posicion derecha cada vez
        while continuar == True:
            # Obtener linea del cursor actual
            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            # Segun linea actual mover una pos. derecha 
            if   cursor_aux == 19:
                cursor_aux = cursor_aux + 45  #P64
            elif cursor_aux == 83:
                cursor_aux = cursor_aux - 63  #P20
            elif cursor_aux == 39:
                cursor_aux = cursor_aux + 45  #P84
            elif cursor_aux == 103:
                self.mover_siguiente_pantalla()
                cursor_aux = cursor_aux - 103 #P0
                cambiar_de_pantalla = True
            else:
                cursor_aux = cursor_aux + 1

            # Ajustar el cursor. Mover cursor a nueva pos.
            self.pantalla_actual.set_pos_actual_cursor(cursor_aux)

            # Obtener la lista de cursores por linea validos en
            # la nueva linea. Porque si en la nueva linea su valor
            # es 1000 es que no es una posicion valida y hay que
            # volver a moverse una posicion a la derecha (o
            # pantalla siguiente).

            l_cursor_actual = 0

            for linea in self.RANGO_LINEAS:
                if (cursor_aux in linea):
                    break
                else:
                    l_cursor_actual = l_cursor_actual + 1

            aux_pos_lineas = self.pantalla_actual.get_pos_validas()

            if aux_pos_lineas[l_cursor_actual] != 1000:
                continuar = False

        return cambiar_de_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Pantalla siguiente de la actual 
    def mover_siguiente_pantalla(self): 
        codigo_sig = (self.pantalla_actual).get_pantalla_siguiente()

        indice = self.get_indice_codigo_pantalla(codigo_sig)

        self.pantalla_actual = self.lista_pantallas[indice]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Pantalla anterior de la actual
    def mover_anterior_pantalla(self): 
        codigo_ant = (self.pantalla_actual).get_pantalla_anterior()

        indice = self.get_indice_codigo_pantalla(codigo_ant)

        self.pantalla_actual = self.lista_pantallas[indice]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Entrar a una pantalla de opcion
    def entrar_subpantalla(self, opcion): 

        if   opcion == 1:
            codigo_opcion = self.pantalla_actual.get_pantalla_opcion1()
        elif opcion == 2:
            codigo_opcion = self.pantalla_actual.get_pantalla_opcion2()
        elif opcion == 3:
            codigo_opcion = self.pantalla_actual.get_pantalla_opcion3()
        elif opcion == 4:
            codigo_opcion = self.pantalla_actual.get_pantalla_opcion4()

        # Si la pantalla de opcion es una pantalla existente.
        if codigo_opcion != (0,0,0):
            # Obligatorio, a veces recibe listas en vez de tuplas
            if isinstance(codigo_opcion, list):
                codigo_opcion = tuple(codigo_opcion)

            indice = self.get_indice_codigo_pantalla(codigo_opcion)

            self.pantalla_actual = self.lista_pantallas[indice]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Salir de una pantalla de opcion
    def salir_subpantalla(self):  
        cna = self.pantalla_actual.get_pantalla_nivel_anterior()

        indice = self.get_indice_codigo_pantalla(cna)

        self.pantalla_actual = self.lista_pantallas[indice]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Borrar las pantallas con datos IPs
    def borrar_pantallas_ips(self): 
        cifra1 = 3
        cifra2 = 1

        lp_aux = [] # Lista pantallas aux

        for p in self.lista_pantallas:
            cod = p.get_codigo()

            if (cod[0] != cifra1) or (cod[1] != cifra2):
                lp_aux.append(p)

        self.lista_pantallas = lp_aux

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Crear (de nuevo o no) las pantallas IPs
    def crear_pantallas_ips(self): 
        pantallas_ips = creador_pantallas_ips.Creador_pantallas_ips()

        lista_p_ips = pantallas_ips.get_objetos_pantalla()

        lista_p_ips_copia = lista_p_ips.copy()

        for p in lista_p_ips_copia:
            aux = copy.deepcopy(p)
            self.lista_pantallas.append(aux)

        del pantallas_ips

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Borrar pantallas con datos comandos 
    def borrar_pantallas_comandos(self): 
        cifra1 = 1
        cifra2 = 2

        lp_aux = [] # Lista pantallas aux

        for p in self.lista_pantallas:
            cod = p.get_codigo()

            if (cod[0] != cifra1) or (cod[1] != cifra2):
                lp_aux.append(p)

        self.lista_pantallas = lp_aux

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Crear pantallas comandos 
    def crear_pantallas_comandos(self): 
        j_a_p = clase_json_a_pantallas.Json_a_pantallas("comandos")

        lista_p_comandos = j_a_p.get_lista_pantallas()

        lista_p_comandos_copia = lista_p_comandos.copy()

        del j_a_p

        #   Falta abrir la lista de pantallas de comandos y
        # ajustar los codigos de pantallas siguientes y anteriores
        # de cada una.
        num_p = len(lista_p_comandos)

        for posicion in range(0, num_p):
            if  posicion == (num_p - 1): # Ultimo
                a = num_p - 1
                s = 1
            elif posicion == 0: # Primero
                a = num_p
                s = 2
            else: # Resto
                a = posicion
                s = posicion + 2

            nuevo_c_ant = (1,2,a)
            nuevo_c_sig = (1,2,s)

            lista_p_comandos_copia[posicion].set_pantalla_anterior(nuevo_c_ant)
            lista_p_comandos_copia[posicion].set_pantalla_siguiente(nuevo_c_sig)

            lista_p_comandos_copia[posicion].set_pantalla_opcion1([1,1,0])
            lista_p_comandos_copia[posicion].set_pantalla_opcion2([1,1,-1])
            lista_p_comandos_copia[posicion].set_pantalla_opcion3([1,1,-2])
            lista_p_comandos_copia[posicion].set_pantalla_opcion4([1,1,-3])

        for p in lista_p_comandos_copia:
            aux = copy.deepcopy(p)
            self.lista_pantallas.append(aux)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pos_pantalla_actual(self):
        return (self.get_pantalla_actual()).get_pos_actual_cursor()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Obtener codigo caracter lcd
    def get_charlcd_pos_pantalla_actual(self): 

        pos_act = self.get_pos_pantalla_actual()

        if   (pos_act in self.RANGO_LINEA1):
            linea1 = self.pantalla_actual.get_linea1_lcd()

            char_lcd = linea1[pos_act]

        elif (pos_act in self.RANGO_LINEA2):
            linea2 = self.pantalla_actual.get_linea2_lcd()

            char_lcd = linea2[pos_act - 64]

        elif (pos_act in self.RANGO_LINEA3):
            linea3 = self.pantalla_actual.get_linea3_lcd()

            char_lcd = linea3[pos_act - 20]

        elif (pos_act in self.RANGO_LINEA4):
            linea4 = self.pantalla_actual.get_linea4_lcd()

            char_lcd = linea4[pos_act - 84]

        return char_lcd
#.....................

