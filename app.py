#!/usr/bin/python3

# ******************************************************************************
# Nombre: app.py
#
#   Descripcion: 
#
#   * Script principal de la aplicación, desde donde se pone en marcha ésta y
# manda a ejecutar el resto (carga de pantallas, operaciones, ...).
#   * Configura el estado de los pines a usar en la BeagleBone con la
# biblioteca de Adafruit y vigila cuando los botones físicos se pulsan
# ******************************************************************************


import time
import pdb

# Para usar la shell en python3
import subprocess

# Para usar los botones de la electronica instalada.
import os
import Adafruit_BBIO.GPIO as GPIO
import glob # Verificacion de existencia de ficheros.

import clase_lcd
import clase_gestor_pantallas
import clase_enviar_teclas
import clase_creador_password
import buzzers

import utilidades


# ==============================================================================
RUTA_SHELL = utilidades.ejecuta_pwd() + '/shell_scripts/'

F_CONF_PINES    = RUTA_SHELL + 'conf_pines.sh'
F_CREAR_GADGET  = RUTA_SHELL + 'crear_usb_gadget.sh' 
F_BORRAR_GADGET = RUTA_SHELL + 'elimi_usb_gadget.sh' 
F_HIDG0 = '/dev/hidg0'
# ==============================================================================


# Password de superusuario para los comandos.
pswd = ""


# Informacion de biblioteca Adafruit GPIO en:
#
# https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/GPIO.html
#
# Implementacion/activacion de los botones.
#   NOTA: Distintos con Adafruit. En el shell script
# es P8_07, aqui es P8_7 y lo mismo con el 8 y el 9
GPIO.setup("P8_7", GPIO.IN, GPIO.PUD_UP)
GPIO.setup("P8_8", GPIO.IN, GPIO.PUD_UP)
GPIO.setup("P8_9", GPIO.IN, GPIO.PUD_UP)
GPIO.setup("P8_10", GPIO.IN, GPIO.PUD_UP)
GPIO.setup("P8_11", GPIO.IN, GPIO.PUD_UP)
GPIO.setup("P8_12", GPIO.IN, GPIO.PUD_UP)

#   Alternativa a usar Adafruit: Ejecucion mediante un shell script
# (Modo i2c, modo in)
#subprocess.run(['sh', F_CONF_PINES]) 

# Configuracion del pin del buzzer
GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW) 



# Funciones
# ==============================================================================
# ==============================================================================

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def imprimir_menu_en_lcd(pantalla_actual, cp):

    if cp == True:
        lcd.clear()

        for cod in (pantalla_actual).get_linea1_lcd():
            lcd.escribir_caracter(cod)
        lcd.cursor_a(64) # Mover cursor a principio 2a linea
        for cod in (pantalla_actual).get_linea2_lcd():
            lcd.escribir_caracter(cod)
        lcd.cursor_a(20) # Mover cursor a principio 3a linea
        for cod in (pantalla_actual).get_linea3_lcd():
            lcd.escribir_caracter(cod)
        lcd.cursor_a(84) # Mover cursor a principio 4a linea
        for cod in (pantalla_actual).get_linea4_lcd():
            lcd.escribir_caracter(cod)

    lcd.cursor_a(pantalla_actual.get_pos_actual_cursor())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def existe_hidg0():
    existe = False

    coincidencias = glob.glob(F_HIDG0)
    
    if len(coincidencias) != 0:
        existe = True

    return existe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Ejecuta una acción según el botón físico pulsado, la pos. del cursor y la
# pantalla.
def ejecutar_accion(gp):

    global pswd

    pantalla     = gp.get_pantalla_actual()
    cod_pantalla = pantalla.get_codigo()
    pos_actual   = pantalla.get_pos_actual_cursor()

    # Pantallas ppales.
    # ..........................................................................
    if   (
            cod_pantalla == (1,0,0) or
            cod_pantalla == (2,0,0) or
            cod_pantalla == (3,0,0) 
         ):
        if   (pos_actual == 82):
            if   cod_pantalla[0] == 3: 
                # Entrar pantalla IPs
                gp.borrar_pantallas_ips()
                gp.crear_pantallas_ips()

                gp.entrar_subpantalla(1)
                pantalla = gp.get_pantalla_actual()
                imprimir_menu_en_lcd(pantalla, True)
            elif cod_pantalla[0] == 2:
                # - Pantalla usar password
                # Datos necesarios de pantalla actual de comandos.
                cod_pant = cod_pantalla
                pantalla = gp.get_pantalla_actual()

                if existe_hidg0():
                    # NOTA: Enviamos la linea entera de comandos de un golpe.
                    # Necesario porque las combinaciones de teclas se deben
                    # escribir a /dev/hidg0 de golpe en un mismo key code report
                    escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_pant)
                    error = escritor_teclas.enviar_linea(pswd) 

                    # Pantalla cable usb no conectado
                    if error: 
                        gp.entrar_subpantalla(4)
                        pantalla = gp.get_pantalla_actual()
                        imprimir_menu_en_lcd(pantalla, True)

                        buzzers.sonar_S_buzzer2_2()
                    else:
                        pos_act = gp.get_charlcd_pos_pantalla_actual()
                else:
                    # Pantalla BBB no es teclado
                    gp.entrar_subpantalla(1)
                    pantalla = gp.get_pantalla_actual()
                    imprimir_menu_en_lcd(pantalla, True)

                    buzzers.sonar_S_buzzer3_3()
            elif cod_pantalla[0] == 1:
                # - Pantalla teclado
                gp.entrar_subpantalla(1)
                pantalla = gp.get_pantalla_actual()
                imprimir_menu_en_lcd(pantalla, True)
        elif (pos_actual == 38):
            if cod_pantalla[0] == 1: 
                # Entrar pantalla comandos
                gp.borrar_pantallas_comandos()
                gp.crear_pantallas_comandos()

            gp.entrar_subpantalla(2)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)

            if cod_pantalla[0] == 2: 
                # Crear gadget
                subprocess.run(['sudo', 'sh', F_CREAR_GADGET])
                time.sleep(5)

                gp.mover_siguiente_pantalla()
                pantalla = gp.get_pantalla_actual()
                imprimir_menu_en_lcd(pantalla, True)

                buzzers.sonar_S_buzzer3_2()

            if cod_pantalla[0] == 3: 
                # Reiniciar BBB
                subprocess.run(['sudo', 'reboot'])

        elif (pos_actual == 102):
            gp.entrar_subpantalla(3)

            if cod_pantalla[0] == 2: 
                # Borrar gadget
                subprocess.run(['sudo', 'sh', F_BORRAR_GADGET])

            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)

            if cod_pantalla[0] == 3: 
                # Apagar BBB
                subprocess.run(['sudo', 'poweroff'])

    # Teclado 1 y 2
    # ..........................................................................
    elif cod_pantalla == (1,1,1) or cod_pantalla == (1,1,2):
        if existe_hidg0():
            # Conversor pos a caracter
            # O conversor a codigo KEY_CODE
            pantalla = gp.get_pantalla_actual()
            cod_pan_act = pantalla.get_codigo()

            escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_pan_act)
            error = escritor_teclas.enviar_tecla(pos_actual)

            if error: # Cable usb no conectado
                gp.entrar_subpantalla(2)
                pantalla = gp.get_pantalla_actual()
                imprimir_menu_en_lcd(pantalla, True)

                buzzers.sonar_S_buzzer2_2()
            else:
                pos_act = gp.get_charlcd_pos_pantalla_actual()
        else: # Error si /dev/hidg0 no existe
            gp.entrar_subpantalla(3)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)
            
            buzzers.sonar_S_buzzer3_3()

    # Crear contraseña, teclados.
    # ..........................................................................
    elif cod_pantalla[0] == 1 and cod_pantalla[1] == 3:
        pantalla = gp.get_pantalla_actual()
        cod_pan_act = pantalla.get_codigo()

        generador_password.nuevo_caracter(pos_actual, cod_pan_act)

        #   Si se pulso ENTER en algun momento quiere decir que se escribió
        # una contraseña a exportar. Almacenarla aqui como global y decirle
        # al objeto que crea los password que vacie el que tenia guardado.
        # Tambien ir a una pantalla que muestre que el password se creo y
        # volver despues a una pantalla de las principales.
        if generador_password.get_password_completo() == True:
            pswd = generador_password.get_password()
            #breakpoint()
            generador_password.borrar_password()

            # A pantalla de 'password generado'
            gp.entrar_subpantalla(1)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)


            continua = True
            while continua:
                if (GPIO.input("P8_12")) == 0:
                    continua = False

    # Pantallas comandos
    # ..........................................................................
    elif (cod_pantalla[0] == 1) and (cod_pantalla[1] == 2):
        usb_conectado  = True
        bbb_es_teclado = True

        # Datos necesarios de pantalla actual de comandos.
        # Datos de la pantalla de comandos actual para retornar
        cod_p_com = cod_pantalla
        pan_com   = gp.get_pantalla_actual()

        # Llamar a pantalla de 'comando en proceso'
        gp.entrar_subpantalla(3)
        pantalla = gp.get_pantalla_actual()
        imprimir_menu_en_lcd(pantalla, True)

        #   Configuramos la pantalla del comando en proceso y preparamos
        # la pantalla de comandos del que se viene para cargarla de nuevo
        # al dar a cancelar.
        pantalla = gp.get_pantalla_actual()
        pantalla.set_pantalla_nivel_anterior(cod_p_com)
        gp.salir_subpantalla()
        pantalla = gp.get_pantalla_actual()

        if existe_hidg0():
            lineas= []

            if   pos_actual == 19:
                lineas = pan_com.get_linea1()
            elif pos_actual == 83:
                lineas = pan_com.get_linea2()
            elif pos_actual == 39:
                lineas = pan_com.get_linea3()
            elif pos_actual == 103:
                lineas = pan_com.get_linea4()

            lineas.pop(0)


            for linea in lineas:
                # NOTA: Enviamos la linea entera de comandos de un golpe.
                # Necesario porque las combinaciones de teclas se deben
                # escribir a /dev/hidg0 de golpe en un mismo key code report
                escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_p_com)
                error = escritor_teclas.enviar_linea(linea) 

                # Pantalla cable usb no conectado
                if error: 
                    gp.entrar_subpantalla(2)
                    pantalla = gp.get_pantalla_actual()
                    imprimir_menu_en_lcd(pantalla, True)

                    buzzers.sonar_S_buzzer2_2()

                    usb_conectado = False

            time.sleep(0.3)
        else:
            # Pantalla BBB no es teclado
            gp.entrar_subpantalla(1)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)

            buzzers.sonar_S_buzzer3_3()

            bbb_es_teclado = False

        # Pantalla comando ejecutado
        if (usb_conectado == True) and (bbb_es_teclado == True):
            gp.entrar_subpantalla(4)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)

            buzzers.sonar_A_buzzer1()

            time.sleep(1.0)

            # Restaurar a la pantalla de comandos original.
            pantalla = gp.get_pantalla_actual()
            pantalla.set_pantalla_nivel_anterior(cod_p_com)
            gp.salir_subpantalla()
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)
# ==============================================================================
# ==============================================================================


#                            - Programa principal -
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

continuar = True

# Inicializacion objeto clase lcd.
lcd = clase_lcd.Lcd()
lcd.modificar_BCD(1,0,1) # Sin cursor '_'
lcd.clear()

# Creando objeto gestionador de contraseñas.
generador_password = clase_creador_password.Creador_password()

# Generando el menu ppal en el lcd y colocando el cursor.
gestor_pantallas = clase_gestor_pantallas.Gestor_pantallas()

pantalla_actual = gestor_pantallas.get_pantalla_actual()
imprimir_menu_en_lcd(pantalla_actual, True)
lcd.cursor_a(pantalla_actual.get_pos_actual_cursor())

"""
#   Uso de funciones de Adafruit para evitar casos donde
# los botones físicos se queden bloqueados, emitiendo
# continuamente una señal a la BBB. Con esto sólo se
# considerará una señal si se pulsa y se suelta el
# botón.
#   No esta libre de problemas: Ralentiza a veces la ejecucion
# del programa, sobre todo al salir a los menus principales
# da la sensacion como si generara dicha pantalla dos veces.
#   Una alternativa es crear una funcion callback y colocarla
# su llamada como tercer argumento de GPIO.add_event_detect().
# Pero a su vez produce el problema de que la ejecucion del
# programa se ralentiza demasiado, tanto, que se puede ver como
# se escribe cada pantalla caracter a caracter.
"""
GPIO.add_event_detect("P8_7",  GPIO.FALLING)
GPIO.add_event_detect("P8_8",  GPIO.FALLING)
GPIO.add_event_detect("P8_9",  GPIO.FALLING)
GPIO.add_event_detect("P8_10", GPIO.FALLING)
GPIO.add_event_detect("P8_11", GPIO.FALLING)
GPIO.add_event_detect("P8_12", GPIO.FALLING)

# Pitido para indicar que el programa esta cargado y listo.
buzzers.sonar_A_buzzer1_1()

# Para suavizar un poco la respuesta de los botones junto con time.sleep()
estado_arriba    = 1
estado_abajo     = 1
estado_izquierda = 1
estado_derecha   = 1
estado_entrar    = 1
estado_salir     = 1

# Bucle principal del programa.
while continuar == True:
    time.sleep(0.01)

    # Pulsado el boton 1. Izquierda.
    if (GPIO.event_detected("P8_7")):
        if estado_izquierda == 1: # Suavizando la respuesta del boton
            cambio_p = gestor_pantallas.mover_cursor_uno_izquierda()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)

            estado_izquierda = 0
        else:
            estado_izquierda = 1
    # Pulsado el boton 2. Derecha.
    elif (GPIO.event_detected("P8_8")):
        if estado_derecha == 1: # Suavizando la respuesta del boton
            cambio_p = gestor_pantallas.mover_cursor_uno_derecha()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)

            estado_derecha = 0
        else:
            estado_derecha = 1
    # Pulsado el boton 3. Arriba. 
    elif (GPIO.event_detected("P8_9")):
        if estado_arriba == 1: # Suavizando la respuesta del boton
            cambio_p = gestor_pantallas.mover_cursor_uno_arriba()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)

            estado_arriba = 0
        else:
            estado_arriba = 1
    # Pulsado el boton 4. Abajo. 
    elif (GPIO.event_detected("P8_10")):
        if estado_abajo == 1: # Suavizando la respuesta del boton
            cambio_p = gestor_pantallas.mover_cursor_uno_abajo()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)

            estado_abajo = 0
        else:
            estado_abajo = 1
    # Pulsado el boton 5. Aceptar/Entrar
    elif (GPIO.event_detected("P8_11")):
        if estado_entrar == 1: # Suavizando la respuesta del boton
            #print()
            #print("* Boton 5. Aceptar/Entrar")

            ejecutar_accion(gestor_pantallas)

            estado_entrar = 0
        else:
            estado_entrar = 1
    # Pulsado el boton 6. Cancelar/Salir 
    elif (GPIO.event_detected("P8_12")):
        if estado_salir == 1: # Suavizando la respuesta del boton
            time.sleep(0.01)
            pantalla = gestor_pantallas.get_pantalla_actual()
            cod_pantalla = pantalla.get_codigo()

            # Borrar contrasenha almacenada en el generador de contrasenhas
            if cod_pantalla[0] == 1 and cod_pantalla[1] == 3:
                generador_password.borrar_password()

            gestor_pantallas.salir_subpantalla()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), True)
            time.sleep(0.01)

            estado_salir = 0
        else:
            estado_salir = 1

# Limpiar todo
GPIO.cleanup()
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
