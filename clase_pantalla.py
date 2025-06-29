
# ******************************************************************************
# Nombre: clase_pantalla.py


# Descripción:

# - Codigos para construir menus en el LCD.
#
#   * La clase Pantalla recibe los datos que conforman una pantalla en el LCD,
# bien como ficheros JSON, bien como ficheros txt. Estos datos se transforman
# en otros datos que permiten escribirlos y mostrarlos en el display LCD.
#   * Tambien contiene codigos descriptores de las pantallas y de las
# pantallas adyacentes, y datos de las posiciones en las que los
# cursores pueden moverse en la pantalla.
#   * Se establecerán códigos únicos para cada pantalla y a cuáles otras
# pantallas se podrán transicionar desde ellas.
# ******************************************************************************


import pdb

import tablas_conversion



#.....................
class Pantalla:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Constructor
    def __init__(self, *args):


        if (len(args) == 0): # Cuando extraemos de JSON
            self.codigo = (0,0,0)

            self.nombre_codigo = "P0_0_0"
            self.nombre_pantalla = ""

            self.tipo = ""

            self.linea1 = ""
            self.linea2 = ""
            self.linea3 = ""
            self.linea4 = ""

            self.pantalla_siguiente       = (0,0,0) # Codigo pantalla siguiente.
            self.pantalla_anterior        = (0,0,0) # Codigo pantalla anterior.
            self.pantalla_nivel_anterior  = (0,0,0) # Codigo nivel anterior.

            # Las posibles pantallas a entrar desde la pantalla actual
            self.pantalla_opcion1 = (0,0,0)
            self.pantalla_opcion2 = (0,0,0)
            self.pantalla_opcion3 = (0,0,0)
            self.pantalla_opcion4 = (0,0,0)

            self.pos_validas = (0,0,0) # Pos. permitidas en pantalla (0 = todas)

            self.pos_actual_cursor = 0

        else: # Cuando extraemos IPs de un txt
            self.codigo = args[0][0]

            self.linea1 = args[0][1]
            self.linea2 = args[0][2]
            self.linea3 = args[0][3]
            self.linea4 = args[0][4]

            self.linea1_ascii = self.conversor_texto_a_ascii(self.linea1)
            self.linea2_ascii = self.conversor_texto_a_ascii(self.linea2)
            self.linea3_ascii = self.conversor_texto_a_ascii(self.linea3)
            self.linea4_ascii = self.conversor_texto_a_ascii(self.linea4)

            self.linea1_lcd = self.conversor_ascii_a_lcd(self.linea1_ascii)
            self.linea2_lcd = self.conversor_ascii_a_lcd(self.linea2_ascii)
            self.linea3_lcd = self.conversor_ascii_a_lcd(self.linea3_ascii)
            self.linea4_lcd = self.conversor_ascii_a_lcd(self.linea4_ascii)

            self.pantalla_siguiente       = (0,0,0) # Codigo pantalla siguiente.
            self.pantalla_anterior        = (0,0,0) # Codigo pantalla anterior.
            self.pantalla_nivel_anterior  = (0,0,0) # Codigo nivel anterior.

            self.tipo = ""

            # Las posibles pantallas a entrar desde la pantalla actual
            self.pantalla_opcion1 = (0,0,0)
            self.pantalla_opcion2 = (0,0,0)
            self.pantalla_opcion3 = (0,0,0)
            self.pantalla_opcion4 = (0,0,0)

            #self.cursores = (0,0,0) # Pos. permitidas en pantalla (0 = todas)
            self.pos_validas = (0,0,0) # Pos. permitidas en pantalla (0 = todas)

            self.pos_actual_cursor = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Convierte el texto de una linea de pantalla en una serie de
    # caracteres ascii separados como una lista.
    def conversor_texto_a_ascii(self, linea):
        lista_caracteres = []
        aux_lista1 = []
        aux_lista2 = []
    
        contador = 0
    
        # Paso a lista auxiliar.
        for c in linea:
            aux_lista1.append(c)
    
    
        # Conversion de 'hn' a enhes y las flechas si las hubiera
        while len(aux_lista1) > 0:
            aux_c1 = aux_lista1.pop(0)
    
            if   aux_c1 == "h":
                aux_c2 = aux_lista1.pop(0)
    
                if aux_c2 == "n":
                    aux_lista2.append("enhe")
                else:
                    aux_lista2.append(aux_c1)
                    aux_lista2.append(aux_c2)
            elif aux_c1 == "-":
                aux_c2 = aux_lista1.pop(0)
    
                if aux_c2 == ">":
                    aux_lista2.append("->")
                else:
                    aux_lista2.append(aux_c1)
                    aux_lista2.append(aux_c2)
            elif aux_c1 == "<":
                aux_c2 = aux_lista1.pop(0)
    
                if aux_c2 == "-":
                    aux_lista2.append("<-")
                else:
                    aux_lista2.append(aux_c1)
                    aux_lista2.append(aux_c2)
            elif aux_c1 == "b":
                aux_c2 = aux_lista1.pop(0)
    
                if aux_c2 == "l":
                    aux_lista2.append("blqe")
                else:
                    aux_lista2.append(aux_c1)
                    aux_lista2.append(aux_c2)
            else:
                aux_lista2.append(aux_c1)

    
        #   Quedarse con los 20 primeros caracteres de la lista, que es
        # el tamaño máximo de caracteres en una línea del LCD.
        for c in aux_lista2: 
            lista_caracteres.append(c)
            contador = contador + 1
    
            if contador == 20:
                break

    
        return lista_caracteres

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Convierte los caracteres ascii de una linea en sus codigos
    # correspondientes para escribirse y mostrarse en el lcd.
    def conversor_ascii_a_lcd(self, linea):
        pantalla_codigo_lcd = []
    
        for c in linea:
            try:
                indice = tablas_conversion.CARACTER_CODIGO_LCD.index(c)
            except ValueError:
                print("Caracter pasado sin equivalencia en la tabla de conversion.")
                print("Saliendo del programa. Error 1.")
                sys.exit(1)
    
            pantalla_codigo_lcd.append(indice)

        return pantalla_codigo_lcd

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def mostrar_pantalla_texto(self):
        print(self.linea1)
        print(self.linea2)
        print(self.linea3)
        print(self.linea4)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def mostrar_pantalla_ascii(self):
        print(self.linea1_ascii)
        print(self.linea2_ascii)
        print(self.linea3_ascii)
        print(self.linea4_ascii)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def mostrar_pantalla_lcd(self):
        print(self.linea1_lcd)
        print(self.linea2_lcd)
        print(self.linea3_lcd)
        print(self.linea4_lcd)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_codigo(self,codigo):
        self.codigo = codigo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_codigo(self):
        codigo = self.codigo

        return codigo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_nombre_codigo(self,nombre_codigo):
        self.nombe_codigo = nombre_codigo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_nombre_codigo(self):
        nombre_codigo = self.nombre_codigo

        return nombre_codigo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_nombre_pantalla(self,nombre_pantalla):
        self.nombre_pantalla = nombre_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_nombre_pantalla(self):
        nombre_pantalla = self.nombre_pantalla

        return nombre_pantalla

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_siguiente(self, pantalla_s):
        self.pantalla_siguiente = pantalla_s

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_siguiente(self):
        pantalla_s = self.pantalla_siguiente

        return pantalla_s

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_anterior(self, pantalla_a):
        self.pantalla_anterior = pantalla_a

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_anterior(self):
        pantalla_a = self.pantalla_anterior

        return pantalla_a

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_nivel_anterior(self, pantalla_na):
        self.pantalla_nivel_anterior = pantalla_na

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_nivel_anterior(self):
        pantalla_na = self.pantalla_nivel_anterior

        return pantalla_na

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_opcion1(self, pantalla_o1):
        self.pantalla_opcion1 = pantalla_o1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_opcion1(self):
        o1 = self.pantalla_opcion1

        return o1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_opcion2(self, pantalla_o2):
        self.pantalla_opcion2 = pantalla_o2

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_opcion2(self):
        o2 = self.pantalla_opcion2

        return o2

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_opcion3(self, pantalla_o3):
        self.pantalla_opcion3 = pantalla_o3

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_opcion3(self):
        o3 = self.pantalla_opcion3

        return o3

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pantalla_opcion4(self, pantalla_o4):
        self.pantalla_opcion4 = pantalla_o4

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pantalla_opcion4(self):
        o4 = self.pantalla_opcion4

        return o4

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pos_validas(self, pos_validas):
        self.pos_validas = pos_validas 

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pos_validas(self):
        pos_validas = self.pos_validas

        return pos_validas

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea1_lcd(self):
        l1 = self.linea1_lcd

        return l1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea2_lcd(self):
        l2 = self.linea2_lcd

        return l2

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea3_lcd(self):
        l3 = self.linea3_lcd

        return l3

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea4_lcd(self):
        l4 = self.linea4_lcd

        return l4

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_pos_actual_cursor(self, pac):
        self.pos_actual_cursor = pac

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_pos_actual_cursor(self):
        pac = self.pos_actual_cursor

        return pac

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_tipo(self, tipo):
        self.tipo = tipo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_tipo(self):
        return self.tipo

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea1(self):
        if isinstance(self.linea1, str):
            l1 = self.linea1
        elif isinstance(self.linea1, list):
            l1 = self.linea1.copy()

        return l1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea2(self):
        if isinstance(self.linea2, str):
            l2 = self.linea2
        elif isinstance(self.linea2, list):
            l2 = self.linea2.copy()

        return l2

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea3(self):
        if isinstance(self.linea3, str):
            l3 = self.linea3
        elif isinstance(self.linea3, list):
            l3 = self.linea3.copy()

        return l3

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_linea4(self):
        if isinstance(self.linea4, str):
            l4 = self.linea4
        elif isinstance(self.linea4, list):
            l4 = self.linea4.copy()

        return l4

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_linea1(self, linea1):
        self.linea1 = linea1

        if type(linea1) == list:
            linea1 = linea1[0]
            
        self.linea1_ascii = self.conversor_texto_a_ascii(linea1)
        self.linea1_lcd = self.conversor_ascii_a_lcd(self.linea1_ascii)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_linea2(self, linea2):
        self.linea2 = linea2

        if type(linea2) == list:
            linea2 = linea2[0]

        self.linea2_ascii = self.conversor_texto_a_ascii(linea2)
        self.linea2_lcd = self.conversor_ascii_a_lcd(self.linea2_ascii)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_linea3(self, linea3):
        self.linea3 = linea3

        if type(linea3) == list:
            linea3 = linea3[0]

        self.linea3_ascii = self.conversor_texto_a_ascii(linea3)
        self.linea3_lcd = self.conversor_ascii_a_lcd(self.linea3_ascii)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def set_linea4(self, linea4):
        self.linea4 = linea4

        if type(linea4) == list:
            linea4 = linea4[0]

        self.linea4_ascii = self.conversor_texto_a_ascii(linea4)
        self.linea4_lcd = self.conversor_ascii_a_lcd(self.linea4_ascii)
#.....................



"""

********************************************************************************
*                                    ANEXO.                                    *
********************************************************************************

    Equivalencias caracter->unicode.
    --------------------------------


    Espacio = 16


    0 = 48      ! = 33      + = 43      : = 58      [ = 91      { = 123
    1 = 49      " = 34      , = 44      ; = 59      ] = 93      | = 124
    2 = 50      # = 35      - = 45      < = 60      ^ = 94      } = 125
    3 = 51      $ = 36      . = 46      = = 61      _ = 95      -> = 126
    4 = 52      % = 37      / = 47      > = 62                  <- = 127
    5 = 53      & = 38                  ? = 63
    6 = 54      ' = 39                  @ = 64
    7 = 55      ( = 40                                          bloque = 255
    8 = 56      ) = 41
    9 = 57      * = 42                                          enhe = 238
    

    A = 65      K = 75      U = 85
    B = 66      L = 76      V = 86
    C = 67      M = 77      W = 87
    D = 68      N = 78      X = 88
    E = 69      O = 79      Y = 89
    F = 70      P = 80      Z = 90
    G = 71      Q = 81
    H = 72      R = 82
    I = 73      S = 83
    J = 74      T = 84


    a = 97      k = 107     u = 117
    b = 98      l = 108     v = 118
    c = 99      m = 109     w = 119
    d = 100     n = 110     x = 120
    e = 101     o = 111     y = 121
    f = 102     p = 112     z = 122
    g = 103     q = 113
    h = 104     r = 114
    i = 105     s = 115
    j = 106     t = 116

"""
