
#!/usr/bin/python3

# Nombre: tablas_conversion.py


# Descripción.
#
#   * Uso de constantes y funciones. Su información guardada en tuplas como
# tablas de conversión. Estas tablas suplen las funcionalidades de ...
#
#       - Como convertir un caracter a un codigo de caracter para
#       el lcd.
#
#       - Convertir el codigo de caracter del lcd a un Key_code para
#       el teclado usb.

import pdb
import time



# - Generación de los Key Codes -
# ==============================================================================
# ==============================================================================

#   Generación de una espera variable asociada a un elemento
# de una tabla de conversión.
#.....................
def espera2(x):
    time.sleep(x)
#.....................

K_ESPERA2 = espera2  # Se ejecuta escribiendo K_ESPERA2(x)

NADA = 0x00

# Teclas de control.
#   NOTA: Si queremos hacer que se presionen mas de uno a la vez
# usar el operador +.
#   EJ. Tener pulsado CTRL + ALT a la vez: LCTRL + LSHIFT. Su
# su contenido sera 0x01 + 0x02 = 0x03 (3)
#   EJ. Pulsado RMETA + LALT: 0x80 + 0x04 = 0x84 (132)
#
#   NOTA2 (IMPORTANTE): Al menos en el S.O. usado (Kubuntu),
# y con un teclado con solo la tecla windows izquierda (LMETA),
# resulta que LMETA y RMETA no funcionan exactamente igual.
#   Usaremos LMETA como una pulsacion sin combinacion de ninguna
# otra tecla (abre la miniventana de inicio) y RMETA se usara
# para combinacion de ella con otras teclas.
#
#   NOTA3 (IMPORTANTE): A la hora de mandar informacion a /dev/hidg0,
# cuando hacemos las operaciones de combinar mas de una tecla de control,
# si vamos a usar la tecla RMETA, a no ser que se deba combinar con ALTGR
# lo correcto es usar la teclas Control/Shift/Alt izquierdas, porque
# cuando hacemos las operaciones de suma de Key_Codes aparecen datos
# adicionales que arruinan el resultado. es mas dificil corregir esto
# si cuando usamos RMETA el resto de teclas en combinacion son tambien
# de la parte derecha.
LCTRL  = 0x01
LSHIFT = 0x02
LALT   = 0x04
LMETA  = 0x08
RCTRL  = 0x10
RSHIFT = 0x20
RALT   = 0x40
RMETA  = 0x80


#   Cada una de las teclas tiene su key_code correspondiente, fruto
# de colocar consecutivamente cada uno de los 8 bytes como expresion
# 'unicode' a partir de valores hexadecimales y valores enteros por
# medio de la funcion 'chr()'

K_SUELTA = (chr(NADA) * 8) # Simulación de soltar la tecla pulsada.


K_LCTRL  = chr(LCTRL)  + (chr(NADA) * 7)
K_LSHIFT = chr(LSHIFT) + (chr(NADA) * 7)
K_LALT   = chr(LALT)   + (chr(NADA) * 7)
K_LMETA  = chr(LMETA)  + (chr(NADA) * 7)
K_RCTRL  = chr(RCTRL)  + (chr(NADA) * 7)
K_RSHIFT = chr(RSHIFT) + (chr(NADA) * 7)
K_RALT   = chr(RALT)   + (chr(NADA) * 7)
K_RMETA  = chr(RMETA)  + (chr(NADA) * 7)


K_A_MAY =  chr(LSHIFT) + chr(NADA) + chr(4)  + (chr(NADA) * 5)
K_A_MIN =  chr(NADA)   + chr(NADA) + chr(4)  + (chr(NADA) * 5)
K_B_MAY =  chr(LSHIFT) + chr(NADA) + chr(5)  + (chr(NADA) * 5)
K_B_MIN =  chr(NADA)   + chr(NADA) + chr(5)  + (chr(NADA) * 5)
K_C_MAY =  chr(LSHIFT) + chr(NADA) + chr(6)  + (chr(NADA) * 5)
K_C_MIN =  chr(NADA)   + chr(NADA) + chr(6)  + (chr(NADA) * 5)
K_D_MAY =  chr(LSHIFT) + chr(NADA) + chr(7)  + (chr(NADA) * 5)
K_D_MIN =  chr(NADA)   + chr(NADA) + chr(7)  + (chr(NADA) * 5)
K_E_MAY =  chr(LSHIFT) + chr(NADA) + chr(8)  + (chr(NADA) * 5)
K_E_MIN =  chr(NADA)   + chr(NADA) + chr(8)  + (chr(NADA) * 5)
K_F_MAY =  chr(LSHIFT) + chr(NADA) + chr(9)  + (chr(NADA) * 5)
K_F_MIN =  chr(NADA)   + chr(NADA) + chr(9)  + (chr(NADA) * 5)
K_G_MAY =  chr(LSHIFT) + chr(NADA) + chr(10) + (chr(NADA) * 5)
K_G_MIN =  chr(NADA)   + chr(NADA) + chr(10) + (chr(NADA) * 5)
K_H_MAY =  chr(LSHIFT) + chr(NADA) + chr(11) + (chr(NADA) * 5)
K_H_MIN =  chr(NADA)   + chr(NADA) + chr(11) + (chr(NADA) * 5)
K_I_MAY =  chr(LSHIFT) + chr(NADA) + chr(12) + (chr(NADA) * 5)
K_I_MIN =  chr(NADA)   + chr(NADA) + chr(12) + (chr(NADA) * 5)
K_J_MAY =  chr(LSHIFT) + chr(NADA) + chr(13) + (chr(NADA) * 5)
K_J_MIN =  chr(NADA)   + chr(NADA) + chr(13) + (chr(NADA) * 5)
K_K_MAY =  chr(LSHIFT) + chr(NADA) + chr(14) + (chr(NADA) * 5)
K_K_MIN =  chr(NADA)   + chr(NADA) + chr(14) + (chr(NADA) * 5)
K_L_MAY =  chr(LSHIFT) + chr(NADA) + chr(15) + (chr(NADA) * 5)
K_L_MIN =  chr(NADA)   + chr(NADA) + chr(15) + (chr(NADA) * 5)
K_M_MAY =  chr(LSHIFT) + chr(NADA) + chr(16) + (chr(NADA) * 5)
K_M_MIN =  chr(NADA)   + chr(NADA) + chr(16) + (chr(NADA) * 5)
K_N_MAY =  chr(LSHIFT) + chr(NADA) + chr(17) + (chr(NADA) * 5)
K_N_MIN =  chr(NADA)   + chr(NADA) + chr(17) + (chr(NADA) * 5)
K_NN_MAY = chr(LSHIFT) + chr(NADA) + chr(51) + (chr(NADA) * 5)
K_NN_MIN = chr(NADA)   + chr(NADA) + chr(51) + (chr(NADA) * 5)
K_O_MAY =  chr(LSHIFT) + chr(NADA) + chr(18) + (chr(NADA) * 5)
K_O_MIN =  chr(NADA)   + chr(NADA) + chr(18) + (chr(NADA) * 5)
K_P_MAY =  chr(LSHIFT) + chr(NADA) + chr(19) + (chr(NADA) * 5)
K_P_MIN =  chr(NADA)   + chr(NADA) + chr(19) + (chr(NADA) * 5)
K_Q_MAY =  chr(LSHIFT) + chr(NADA) + chr(20) + (chr(NADA) * 5)
K_Q_MIN =  chr(NADA)   + chr(NADA) + chr(20) + (chr(NADA) * 5)
K_R_MAY =  chr(LSHIFT) + chr(NADA) + chr(21) + (chr(NADA) * 5)
K_R_MIN =  chr(NADA)   + chr(NADA) + chr(21) + (chr(NADA) * 5)
K_S_MAY =  chr(LSHIFT) + chr(NADA) + chr(22) + (chr(NADA) * 5)
K_S_MIN =  chr(NADA)   + chr(NADA) + chr(22) + (chr(NADA) * 5)
K_T_MAY =  chr(LSHIFT) + chr(NADA) + chr(23) + (chr(NADA) * 5)
K_T_MIN =  chr(NADA)   + chr(NADA) + chr(23) + (chr(NADA) * 5)
K_U_MAY =  chr(LSHIFT) + chr(NADA) + chr(24) + (chr(NADA) * 5)
K_U_MIN =  chr(NADA)   + chr(NADA) + chr(24) + (chr(NADA) * 5)
K_V_MAY =  chr(LSHIFT) + chr(NADA) + chr(25) + (chr(NADA) * 5)
K_V_MIN =  chr(NADA)   + chr(NADA) + chr(25) + (chr(NADA) * 5)
K_W_MAY =  chr(LSHIFT) + chr(NADA) + chr(26) + (chr(NADA) * 5)
K_W_MIN =  chr(NADA)   + chr(NADA) + chr(26) + (chr(NADA) * 5)
K_X_MAY =  chr(LSHIFT) + chr(NADA) + chr(27) + (chr(NADA) * 5)
K_X_MIN =  chr(NADA)   + chr(NADA) + chr(27) + (chr(NADA) * 5)
K_Y_MAY =  chr(LSHIFT) + chr(NADA) + chr(28) + (chr(NADA) * 5)
K_Y_MIN =  chr(NADA)   + chr(NADA) + chr(28) + (chr(NADA) * 5)
K_Z_MAY =  chr(LSHIFT) + chr(NADA) + chr(29) + (chr(NADA) * 5)
K_Z_MIN =  chr(NADA)   + chr(NADA) + chr(29) + (chr(NADA) * 5)


K_1       = chr(NADA)   + chr(NADA) + chr(30) + (chr(NADA) * 5)
K_ADMIRA  = chr(LSHIFT) + chr(NADA) + chr(30) + (chr(NADA) * 5)
K_BARRA   = chr(RALT)   + chr(NADA) + chr(30) + (chr(NADA) * 5)
K_2       = chr(NADA)   + chr(NADA) + chr(31) + (chr(NADA) * 5)
K_COM_DOB = chr(LSHIFT) + chr(NADA) + chr(31) + (chr(NADA) * 5)
K_ARROBA  = chr(RALT)   + chr(NADA) + chr(31) + (chr(NADA) * 5)
K_3       = chr(NADA)   + chr(NADA) + chr(32) + (chr(NADA) * 5)
K_ALMOHA  = chr(RALT)   + chr(NADA) + chr(32) + (chr(NADA) * 5)
K_4       = chr(NADA)   + chr(NADA) + chr(33) + (chr(NADA) * 5)
K_DOLAR   = chr(LSHIFT) + chr(NADA) + chr(33) + (chr(NADA) * 5)
K_TILDE   = chr(RALT)   + chr(NADA) + chr(33) + (chr(NADA) * 5)
K_5       = chr(NADA)   + chr(NADA) + chr(34) + (chr(NADA) * 5)
K_PORCE   = chr(LSHIFT) + chr(NADA) + chr(34) + (chr(NADA) * 5)
K_6       = chr(NADA)   + chr(NADA) + chr(35) + (chr(NADA) * 5)
K_AMPER   = chr(LSHIFT) + chr(NADA) + chr(35) + (chr(NADA) * 5)
K_7       = chr(NADA)   + chr(NADA) + chr(36) + (chr(NADA) * 5)
K_BARRAD  = chr(LSHIFT) + chr(NADA) + chr(36) + (chr(NADA) * 5)
K_LLAVEA  = chr(RALT)   + chr(NADA) + chr(36) + (chr(NADA) * 5)
K_8       = chr(NADA)   + chr(NADA) + chr(37) + (chr(NADA) * 5)
K_PARENA  = chr(LSHIFT) + chr(NADA) + chr(37) + (chr(NADA) * 5)
K_CORCHA  = chr(RALT)   + chr(NADA) + chr(37) + (chr(NADA) * 5)
K_9       = chr(NADA)   + chr(NADA) + chr(38) + (chr(NADA) * 5)
K_PARENC  = chr(LSHIFT) + chr(NADA) + chr(38) + (chr(NADA) * 5)
K_CORCHC  = chr(RALT)   + chr(NADA) + chr(38) + (chr(NADA) * 5)
K_0       = chr(NADA)   + chr(NADA) + chr(39) + (chr(NADA) * 5)
K_IGUAL   = chr(LSHIFT) + chr(NADA) + chr(39) + (chr(NADA) * 5)
K_LLAVEC  = chr(RALT)   + chr(NADA) + chr(39) + (chr(NADA) * 5)
K_ENTER   = chr(NADA)   + chr(NADA) + chr(40) + (chr(NADA) * 5)
K_BCKSP   = chr(NADA)   + chr(NADA) + chr(42) + (chr(NADA) * 5)
K_SPACE   = chr(NADA)   + chr(NADA) + chr(44) + (chr(NADA) * 5)
K_COM_SIM = chr(NADA)   + chr(NADA) + chr(45) + (chr(NADA) * 5)
K_INTERRO = chr(LSHIFT) + chr(NADA) + chr(45) + (chr(NADA) * 5)
K_BARRAI  = chr(RALT)   + chr(NADA) + chr(45) + (chr(NADA) * 5)
K_CAPUCHO = chr(LSHIFT) + chr(NADA) + chr(47) + (chr(NADA) * 5)
K_MAS     = chr(NADA)   + chr(NADA) + chr(48) + (chr(NADA) * 5)
K_MUL     = chr(LSHIFT) + chr(NADA) + chr(48) + (chr(NADA) * 5)
K_COMA    = chr(NADA)   + chr(NADA) + chr(54) + (chr(NADA) * 5)
K_PCOM    = chr(LSHIFT) + chr(NADA) + chr(54) + (chr(NADA) * 5)
K_PUNTO   = chr(NADA)   + chr(NADA) + chr(55) + (chr(NADA) * 5)
K_DPUNT   = chr(LSHIFT) + chr(NADA) + chr(55) + (chr(NADA) * 5)
K_MEN     = chr(NADA)   + chr(NADA) + chr(56) + (chr(NADA) * 5)
K_GUION   = chr(NADA)   + chr(NADA) + chr(56) + (chr(NADA) * 5)
K_GUIONB  = chr(LSHIFT) + chr(NADA) + chr(56) + (chr(NADA) * 5)


K_F1  = chr(NADA) + chr(NADA) + chr(58) + (chr(NADA) * 5)
K_F2  = chr(NADA) + chr(NADA) + chr(59) + (chr(NADA) * 5)
K_F3  = chr(NADA) + chr(NADA) + chr(60) + (chr(NADA) * 5)
K_F4  = chr(NADA) + chr(NADA) + chr(61) + (chr(NADA) * 5)
K_F5  = chr(NADA) + chr(NADA) + chr(62) + (chr(NADA) * 5)
K_F6  = chr(NADA) + chr(NADA) + chr(63) + (chr(NADA) * 5)
K_F7  = chr(NADA) + chr(NADA) + chr(64) + (chr(NADA) * 5)
K_F8  = chr(NADA) + chr(NADA) + chr(65) + (chr(NADA) * 5)
K_F9  = chr(NADA) + chr(NADA) + chr(66) + (chr(NADA) * 5)
K_F10 = chr(NADA) + chr(NADA) + chr(67) + (chr(NADA) * 5)
K_F11 = chr(NADA) + chr(NADA) + chr(68) + (chr(NADA) * 5)
K_F12 = chr(NADA) + chr(NADA) + chr(69) + (chr(NADA) * 5)


K_MENOR = chr(NADA)   + chr(NADA) + chr(100) + (chr(NADA) * 5)
K_MAYOR = chr(LSHIFT) + chr(NADA) + chr(100) + (chr(NADA) * 5)

# ==============================================================================
# ==============================================================================



# - Tablas de conversión usadas -
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#   Equivalencia caracter<->codigo lcd. El codigo a mostrar en el lcd
# es la pos. que ocupa.
#......................
CARACTER_CODIGO_LCD = (
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    ' ',    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', '!',    '"',    '#',    '$',    '%',    '&',    "'",
    '(',    ')',    '*',    '+',    ',',    '-',    '.',    '/',
    '0',    '1',    '2',    '3',    '4',    '5',    '6',    '7',
    '8',    '9',    ':',    ';',    '<',    '=',    '>',    '?',
    '@',    'A',    'B',    'C',    'D',    'E',    'F',    'G',
    'H',    'I',    'J',    'K',    'L',    'M',    'N',    'O',
    'P',    'Q',    'R',    'S',    'T',    'U',    'V',    'W',
    'X',    'Y',    'Z',    '[',    'yen',  ']',    '^',    '_',
    '`',    'a',    'b',    'c',    'd',    'e',    'f',    'g',
    'h',    'i',    'j',    'k',    'l',    'm',    'n',    'o',
    'p',    'q',    'r',    's',    't',    'u',    'v',    'w',
    'x',    'y',    'z',    '{',    '|',    '}',    '->',   '<-',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'enhe', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada',
    'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'nada', 'blqe'
)
#......................

#   Equivalencia codigo lcd <-> codigo Key_code teclado USB de la 
# pantalla del teclado1-1.
#......................
CODIGO_LCD_KEY_CODE1_1 = ( 
    K_A_MIN,  K_B_MIN,   K_C_MIN,  K_D_MIN,  K_E_MIN,
    K_F_MIN,  K_G_MIN,   K_H_MIN,  K_I_MIN,  K_J_MIN,
    K_K_MIN,  K_L_MIN,   K_M_MIN,  K_N_MIN,  K_NN_MIN,
    K_O_MIN,  K_P_MIN,   K_Q_MIN,  K_R_MIN,  K_S_MIN,
    K_T_MIN,  K_U_MIN,   K_V_MIN,  K_W_MIN,  K_X_MIN,
    K_Y_MIN,  K_Z_MIN,   K_A_MAY,  K_B_MAY,  K_C_MAY,
    K_D_MAY,  K_E_MAY,   K_F_MAY,  K_G_MAY,  K_H_MAY,
    K_I_MAY,  K_J_MAY,   K_K_MAY,  K_L_MAY,  K_M_MAY,

    K_N_MAY,  K_NN_MAY,  K_O_MAY,  K_P_MAY,  K_Q_MAY,
    K_R_MAY,  K_S_MAY,   K_T_MAY,  K_U_MAY,  K_V_MAY,
    K_W_MAY,  K_X_MAY,   K_Y_MAY,  K_Z_MAY,  K_SPACE,
    K_0,      K_1,       K_2,      K_3,      K_4,
    K_5,      K_6,       K_7,      K_8,      K_9,
    K_ADMIRA, K_COM_DOB, K_ALMOHA, K_DOLAR,  K_PORCE,
    K_AMPER,  K_COM_SIM, K_PARENA, K_PARENC, K_MUL,
    K_MAS,    K_COMA,    K_MEN,    K_PUNTO,  K_BARRAD,
)
#......................

# NOTAS:
#
#   Para obtener el caracter '^' se necesita ejecutar dos
# veces el codigo, como si pulsaramos dos veces el boton
# en dicho caracter. Codigo 47 = 0x2f

#   Equivalencia codigo lcd <-> codigo Key_code teclado USB de la 
# pantalla del teclado1-2. También se usa para la parte del programa
# que necesita ejecutar los comandos.
#......................
CODIGO_LCD_KEY_CODE1_2 = ( 
    K_DPUNT,   K_PCOM,   K_MENOR,  K_IGUAL,  K_MAYOR,
    K_INTERRO, K_ARROBA, K_CORCHA, K_CORCHC, K_CAPUCHO,
    K_GUIONB,  K_LLAVEA, K_BARRA,  K_LLAVEC, K_ENTER,
    K_BCKSP,   K_BARRAI, K_SPACE,  K_SPACE,  K_SPACE,
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 

    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE 
)

#   Key Codes adicionales para la parte del programa que necesita
# ejecutar los comandos. Pantalla 2 para comandos.
#......................
CODIGO_KEY_CODE_COMANDOS2 = (
    K_DPUNT,   K_PCOM,   K_MENOR,  K_IGUAL,  K_MAYOR,
    K_INTERRO, K_ARROBA, K_CORCHA, K_CORCHC, K_CAPUCHO,
    K_GUIONB,  K_LLAVEA, K_BARRA,  K_LLAVEC, K_ENTER,
    K_BCKSP,   K_BARRAI, K_LCTRL,  K_LSHIFT, K_LALT,
    K_LMETA,   K_RCTRL,  K_RSHIFT, K_RALT,   K_RMETA, 
    K_F1,      K_F2,     K_F3,     K_F4,     K_F5, 
    K_F6,      K_F7,     K_F8,     K_F9,     K_F10, 
    K_F11,     K_F12,    K_ENTER,  K_BCKSP,  K_ESPERA2, 

    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE 
)
#......................

#   Equivalencia codigo lcd <-> codigo Key_code teclado USB para la
# pantalla de Login1.
#......................
CODIGO_LCD_KEY_CODE_LOGIN1 = (
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE,

    K_A_MIN,   K_B_MIN,  K_C_MIN,  K_D_MIN,  K_E_MIN,
    K_F_MIN,   K_G_MIN,  K_H_MIN,  K_I_MIN,  K_J_MIN,
    K_K_MIN,   K_L_MIN,  K_M_MIN,  K_N_MIN,  K_NN_MIN,
    K_O_MIN,   K_P_MIN,  K_Q_MIN,  K_R_MIN,  K_S_MIN,
    K_T_MIN,   K_U_MIN,  K_V_MIN,  K_W_MIN,  K_X_MIN,
    K_Y_MIN,   K_Z_MIN,  K_A_MAY,  K_B_MAY,  K_C_MAY,
    K_D_MAY,   K_E_MAY,  K_F_MAY,  K_G_MAY,  K_H_MAY,
    K_I_MAY,   K_J_MAY,  K_K_MAY,  K_ENTER,  K_BCKSP
)
#......................

#   Equivalencia codigo lcd <-> codigo Key_code teclado USB para la
# pantalla de Login2.
#......................
CODIGO_LCD_KEY_CODE_LOGIN2 = (
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE,

    K_L_MAY,   K_M_MAY,  K_N_MAY,  K_NN_MAY, K_O_MAY,
    K_P_MAY,   K_Q_MAY,  K_R_MAY,  K_S_MAY,  K_T_MAY,
    K_U_MAY,   K_V_MAY,  K_W_MAY,  K_X_MAY,  K_Y_MAY,
    K_Z_MAY,   K_SPACE,  K_0,      K_1,      K_2,   
    K_3,       K_4,      K_5,      K_6,      K_7,
    K_8,       K_9,      K_ADMIRA, K_COM_DOB,K_ALMOHA,
    K_DOLAR,   K_PORCE,  K_AMPER,  K_COM_SIM,K_PARENA,
    K_PARENC,  K_MUL,    K_MAS,    K_ENTER,  K_BCKSP
)
#......................

#   Equivalencia codigo lcd <-> codigo Key_code teclado USB para la
# pantalla de Login3.
#......................
CODIGO_LCD_KEY_CODE_LOGIN3 = (
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE, 
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE,

    K_COMA,    K_MEN,    K_PUNTO,  K_BARRAD, K_DPUNT,
    K_PCOM,    K_MENOR,  K_IGUAL,  K_MAYOR,  K_INTERRO,
    K_ARROBA,  K_CORCHA, K_CORCHC, K_CAPUCHO,K_GUIONB,
    K_LLAVEA,  K_BARRA,  K_LLAVEC, K_BARRAI, K_SPACE,
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE,
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE,
    K_SPACE,   K_SPACE,  K_SPACE,  K_SPACE,  K_SPACE,
    K_SPACE,   K_SPACE,  K_SPACE,  K_ENTER,  K_BCKSP
)
#......................

#   Equivalencias de los caracteres de esta tabla con los Key_Code
# de la tabla CODIGO_LCD_KEY_CODE1_1, representando la pantalla de
# teclado1-1. Necesario sobre todo para la ejecución de comandos.
#......................
CODIGO_CAR_KEY_CODE1 = (
    'a',     'b',     'c',     'd',     'e',
    'f',     'g',     'h',     'i',     'j',
    'k',     'l',     'm',     'n',     'ñ',
    'o',     'p',     'q',     'r',     's',
    't',     'u',     'v',     'w',     'x',
    'y',     'z',     'A',     'B',     'C',
    'D',     'E',     'F',     'G',     'H',
    'I',     'J',     'K',     'L',     'M',

    'N',     666,     'O',     'P',     'Q',
    'R',     'S',     'T',     'U',     'V',
    'W',     'X',     'Y',     'Z',     ' ',
    '0',     '1',     '2',     '3',     '4',
    '5',     '6',     '7',     '8',     '9',
    '!',     '"',     '#',     '$',     '%',
    '&',     '\'',    '(',     ')',     '*',
    '+',     ',',     '-',     '.',     '/'
)
#......................

#   NOTA: Usando el simbolo del euro, como caracter de escape.
# Se usa ese simbolo porque JSON no permite usar el caracter \
# mas una letra como codigo con significado propio, sino que se
# produce un error en la conversion a informacion a gestionar
# por python.

#   Equivalencias de los caracteres de esta tabla con los Key_Code
# de la tabla CODIGO_LCD_KEY_CODE1_2, representando la pantalla de
# teclado1-2 y la de comandos. Necesario sobre todo para la ejecución
# de comandos.
#......................
CODIGO_CAR_KEY_CODE2 = (
    ':',     ';',     '<',     '=',     '>',
    '?',     '@',     '[',     ']',     '^',
    '_',     '{',     '|',     '}',     999,
    333,     '\\',    '€c',    '€d',    '€g',
    '€h',    '€i',    '€j',    '€k',    '€l',
    '€m',    '€o',    '€p',    '€q',    '€s',
    '€w',    '€y',    '€z',    '€_',    '€-',
    '€.',    '€:',    '€;',    '€,',    '€<',

    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' '
)
#......................

#   Equivalencias de los caracteres de esta tabla con los Key_Code
# de la tabla CODIGO_LCD_KEY_CODE_LOGIN1, representando la pantalla de
# Login1. 
#......................
CODIGO_CAR_KEY_CODE_LOGIN1 = (
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',

    'a',     'b',     'c',     'd',     'e',
    'f',     'g',     'h',     'i',     'j',
    'k',     'l',     'm',     'n',     'ñ',
    'o',     'p',     'q',     'r',     's',
    't',     'u',     'v',     'w',     'x',
    'y',     'z',     'A',     'B',     'C',
    'D',     'E',     'F',     'G',     'H',
    'I',     'J',     'K',     '€;',    '€,'
)
#......................


#   Equivalencias de los caracteres de esta tabla con los Key_Code
# de la tabla CODIGO_LCD_KEY_CODE_LOGIN2, representando la pantalla de
# Login2. 
#......................
CODIGO_CAR_KEY_CODE_LOGIN2 = (
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',

    'L',     'M',     'N',     666,     'O',
    'P',     'Q',     'R',     'S',     'T',
    'U',     'V',     'W',     'X',     'Y',
    'Z',     ' ',     '0',     '1',     '2',
    '3',     '4',     '5',     '6',     '7',
    '8',     '9',     '!',     '"',     '#',
    '$',     '%',     '&',     '\'',    '(',
    ')',     '*',     '+',     '€;',    '€,'
)
#......................

#   Equivalencias de los caracteres de esta tabla con los Key_Code
# de la tabla CODIGO_LCD_KEY_CODE_LOGIN2, representando la pantalla de
# Login2. 
#......................
CODIGO_CAR_KEY_CODE_LOGIN3 = (
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',
    ' ',   ' ' ,  ' ',   ' ',   ' ',

    ',',     '-',     '.',     '/',     ':',
    ';',     '<',     '=',     '>',     '?',
    '@',     '[',     ']',     '^',     '_',
    '{',     '|',     '}',     '\\',    ' ',
    ' ',     ' ',     ' ',     ' ',     ' ',
    ' ',     ' ',     ' ',     ' ',     ' ',
    ' ',     ' ',     ' ',     ' ',     ' ',
    ' ',     ' ',     ' ',     '€;',    '€,'
)
#......................

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



"""
********************************************************************************
*             ANEXO. EQUIVALENCIAS DE CÓDIGOS/CARACTERES/KEY_CODES             *
********************************************************************************


    Equivalencias caracter->unicode del LCD.
    ----------------------------------------


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


"""

    Equivalencias caracter->key_code para los comandos.
    ---------------------------------------------------

    €c -> LCTRL      €m -> F1     €_ -> F9
    €d -> LSHIFT     €o -> F2     €- -> F10
    €g -> LALT       €p -> F3     €. -> F11
    €h -> LMETA      €q -> F4     €: -> F12
    €i -> RCTRL      €s -> F5     €; -> ENTER
    €j -> RSHIFT     €w -> F6     €, -> BACKSPACE
    €k -> RALT       €y -> F7     €< -> K_ESPERA2
    €l -> RMETA      €z -> F8     €= -> 


    \> -> \ ->      \ -> 
    \+ -> \ ->      \ -> 
    \* -> \ ->      \ -> 
    \@ -> \ ->      \ -> 
    \$ -> \ ->      \ -> 
    \( -> \ ->      \ -> 
    \) -> \ ->      \ -> 
    \| -> \ ->      \ -> 

"""

"""
# Codigo [1,1,1]
TECLADO1_LINEA1 = ("abcdefghijklmnhnopqrs")
TECLADO1_LINEA2 = ("tuvwxyzABCDEFGHIJKLM")
TECLADO1_LINEA3 = ("NhnOPQRSTUVWXYZ 01234")
TECLADO1_LINEA4 = ("56789!\"#$%&'()*+,-./")



# Codigo [1,1,2]
TECLADO2_LINEA1 = (":;<=>?@[]^_{|}-><-bl ") 
TECLADO2_LINEA2 = ("                    ") 
TECLADO2_LINEA3 = ("                    ") 
TECLADO2_LINEA4 = ("                   S") 
"""


"""

    Equivalencias caracter->key_code para los teclados.
    ---------------------------------------------------



    04 = \ 04 -> a|A      12 = \ 0c -> i|I      20 = \ 14 -> q|Q|@
    05 = \ 05 -> b|B      13 = \ 0d -> j|J      21 = \ 15 -> r|R
    06 = \ 06 -> c|C      14 = \ 0e -> k|K      22 = \ 16 -> s|S
    07 = \ 07 -> d|D      15 = \ 0f -> l|L      23 = \ 17 -> t|T
    08 = \ 08 -> e|E      16 = \ 10 -> m|M      24 = \ 18 -> u|U
    09 = \ 09 -> f|F      17 = \ 11 -> n|N      25 = \ 19 -> v|V
    10 = \ 0a -> g|G      18 = \ 12 -> o|O      26 = \ 1a -> w|W
    11 = \ 0b -> h|H      19 = \ 13 -> p|P      27 = \ 1b -> x|X


    28 = \ 1c -> y|Y      36 = \ 24 -> 7|/|{    44 = \ 2c -> SPACE
    29 = \ 1d -> z|Z      37 = \ 25 -> 8|(|[    45 = \ 2d -> '|?|\
    30 = \ 1e -> 1|!||    38 = \ 26 -> 9|)|]    46 = \ 2e -> INVERSO !?
    31 = \ 1f -> 2|"|@    39 = \ 27 -> 0|=|}    47 = \ 2f -> `|^|[
    32 = \ 20 -> 3|#      40 = \ 28 -> ENTER    48 = \ 30 -> +|*|]
    33 = \ 21 -> 4|$|~    41 = \ 29 -> ESCAPE   49 = \ 31 -> CEDILLA|}
    34 = \ 22 -> 5|%      42 = \ 2a -> DELETE   50 = \ 32 -> CEDILLA|}
    35 = \ 23 -> 6|&      43 = \ 2b -> TAB      51 = \ 33 -> enhe|enhe mayus


    52 = \ 34 -> {|       60 = \ 3c -> F3       68 = \ 44 -> F11
    53 = \ 35 -> \        61 = \ 3d -> F4       69 = \ 45 -> F12
    54 = \ 36 -> ,|;      62 = \ 3e -> F5       70 = \ 46 -> IMPPT
    55 = \ 37 -> .|:      63 = \ 3f -> F6       71 = \ 47 -> SCROLL LOCK
    56 = \ 38 -> -|_      64 = \ 40 -> F7       72 = \ 48 -> PAUSE BUTTON
    57 = \ 39 -> BLOQMAY  65 = \ 41 -> F8       73 = \ 49 -> INSERT
    58 = \ 3a -> F1       66 = \ 42 -> F9       74 = \ 4a -> HOME BUTTON
    59 = \ 3b -> F2       67 = \ 43 -> F10      75 = \ 4b -> PAGE UP


    84 = \ 54 -> /
    85 = \ 55 -> *
    86 = \ 56 -> -
    87 = \ 57 -> +
    88 = \ 58 -> ENTER


    100 = \ 64 -> <|>||
    100 = \ 65 -> RATON BOTON 1 | 2 | 3
"""

