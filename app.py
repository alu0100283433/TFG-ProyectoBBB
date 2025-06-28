#!/usr/bin/python3

# Nombre: pruebas_clase_lcd6.py
# Nombre: cargador_pantallas_lcd6.py

#   Haciendo pruebas para cargar las pantallas en el lcd y que
# funcionen de forma interactuable. Esto va a implicar que
# habra que configurar el comportamiento al presionar los botones
# reales para cada pantalla (mas personalizacion de que se hace
# en cada pantalla.
#
# Llamarlo "cargador de pantallas a lcd" o algo asi?



# Para usar la shell en python3
import subprocess

# Para usar los botones de la electronica instalada.
import os
import pdb
import Adafruit_BBIO.GPIO as GPIO
import time
import glob # Verificacion de existencia de ficheros.

import clase_lcd
import clase_gestor_pantallas
import clase_enviar_teclas
import clase_creador_password
import buzzers

import utilidades

# ............................
RUTA_SHELL = utilidades.ejecuta_pwd() + '/shell_scripts/'

F_CONF_PINES    = RUTA_SHELL + 'conf_pines.sh'
F_CREAR_GADGET  = RUTA_SHELL + 'crear_usb_gadget.sh' 
F_BORRAR_GADGET = RUTA_SHELL + 'elimi_usb_gadget.sh' 
F_HIDG0 = '/dev/hidg0'
# ............................

# Password de superusuario para los comandos.
pswd = "" # Intento de variable global


#   Ejecucion del shell script para poner los conectores
# (Modo i2c, modo in)
#subprocess.run(['sh', './conf_pines.sh']) 
subprocess.run(['sh', F_CONF_PINES]) 

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

# Configuracion del pin del buzzer
GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW) 


# Inicializacion objeto clase lcd.
lcd = clase_lcd.Lcd()
lcd.modificar_BCD(1,0,1) # Sin cursor '_'
lcd.clear()

# ----

#   NOTA: TODO A LO MEJOR CREAR UNA CLASE 'UTILIDADES' CON ESTAS FUNCIONES
# QUE VOY HACIENDO PARA GESTIONAR TODO ESTO Y SE ENCARGUE DE DISTINTAS
# COSAS (IMPRIMIR EN EL LCD, GESTIONAR UN ARBOL DE CURSORES DEPENDIENDO
# DE LA PANTALLA Y DE LA OPCION, EL MOVIMIENTO DEL MISMO, ETC. TODO



# ==============================================================================
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


# ==============================================================================
def existe_hidg0():
    existe = False

    coincidencias = glob.glob(F_HIDG0)
    
    if len(coincidencias) != 0:
        existe = True

    return existe


# ==============================================================================
def ejecutar_accion(gp):


    global pswd
    #pswd = "temppwd€;"

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
                # Pantalla usar password
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                print("Pantalla usar password")


                # Datos necesarios de pantalla actual de comandos.
                cod_pant = cod_pantalla
                pantalla = gp.get_pantalla_actual()

                if existe_hidg0():
                    # NOTA: Enviamos la linea entera de comandos de un golpe.
                    # Necesario porque las combinaciones de teclas se deben
                    # escribir a /dev/hidg0 de golpe en un mismo key code report
                    #cod_pan_act = pantalla.get_codigo()

                    #escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_pan_act)
                    #escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_p_com)

                    #breakpoint()

                    escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_pant)
                    error = escritor_teclas.enviar_linea(pswd) 
                    print("Perrito caliente")

                    #breakpoint()

                    # Pantalla cable usb no conectado
                    if error: 
                        gp.entrar_subpantalla(4)
                        pantalla = gp.get_pantalla_actual()
                        imprimir_menu_en_lcd(pantalla, True)

                        buzzers.sonar_S_buzzer2_2()

                        print("Deberia el buzzer pitar usb no conec.")

                    else:
                        pos_act = gp.get_charlcd_pos_pantalla_actual()
                else:
                    # Pantalla BBB no es teclado
                    gp.entrar_subpantalla(1)
                    pantalla = gp.get_pantalla_actual()
                    imprimir_menu_en_lcd(pantalla, True)

                    buzzers.sonar_S_buzzer3_3()

                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            elif cod_pantalla[0] == 1:
                # Pantalla teclado
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                print("Pantalla usar password")
                gp.entrar_subpantalla(1)
                pantalla = gp.get_pantalla_actual()
                imprimir_menu_en_lcd(pantalla, True)
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            #gp.entrar_subpantalla(1)
            #pantalla = gp.get_pantalla_actual()
            #imprimir_menu_en_lcd(pantalla, True)

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
            print("- Pos. actual: ", pos_actual)

            pantalla = gp.get_pantalla_actual()
            cod_pan_act = pantalla.get_codigo()

            escritor_teclas = clase_enviar_teclas.Enviar_teclas(cod_pan_act)
            error = escritor_teclas.enviar_tecla(pos_actual)

            #breakpoint() 

            if error: # Cable usb no conectado
                gp.entrar_subpantalla(2)
                pantalla = gp.get_pantalla_actual()
                imprimir_menu_en_lcd(pantalla, True)

                buzzers.sonar_S_buzzer2_2()
            else:
                pos_act = gp.get_charlcd_pos_pantalla_actual()
                print("+ Pos. lcd actual: ", pos_act)
        else: # ERROR SI /dev/hidg0 no existe
            gp.entrar_subpantalla(3)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)
            
            buzzers.sonar_S_buzzer3_3()


    # Crear contrasenha, teclados.
    # ..........................................................................
    elif cod_pantalla[0] == 1 and cod_pantalla[1] == 3:
        pantalla = gp.get_pantalla_actual()
        cod_pan_act = pantalla.get_codigo()


        generador_password.nuevo_caracter(pos_actual, cod_pan_act)

        #   Si se pulso ENTER en algun momento quiere decir que se escribio
        # una contrasenha a exportar. Almacenarla aqui como global y decirle
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

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        usb_conectado  = True
        bbb_es_teclado = True

        # Datos necesarios de pantalla actual de comandos.
        #cod_p_com = cod_pantalla
        #pan_com   = gp.get_pantalla_actual()

        print()
        print("Problemas comandos. Codigo p. act.: ", cod_pantalla)
        print("\tCodigo opcion1: ", pantalla.get_pantalla_opcion1())
        print("\tCodigo opcion2: ", pantalla.get_pantalla_opcion2())
        print("\tCodigo opcion3: ", pantalla.get_pantalla_opcion3())
        print("\tCodigo opcion4: ", pantalla.get_pantalla_opcion4())
        print()

        #breakpoint()

        # Datos de la pantalla de comandos actual para retornar
        cod_p_com = cod_pantalla
        pan_com   = gp.get_pantalla_actual()


        # Llamar a pantalla de 'comando en proceso'
        gp.entrar_subpantalla(3)
        pantalla = gp.get_pantalla_actual()
        imprimir_menu_en_lcd(pantalla, True)

        print()
        print("Yendo a (1): ", pantalla.get_codigo())
        print("Y pantalla superior: ", pantalla.get_pantalla_nivel_anterior())
        print()

        #time.sleep(1)

        # TODO PERO CONFIGURAR LA PANTALLA DEL COMANDO EN PROCESO PARA TODO
        # TODO LA PANTALLA DE NIVEL SUPERIOR SEA LA PANTALLA DE COMAN- TODO
        # TODO DE LA QUE VENIMOS, CARGARLA PERO NO MOSTRARLA           TODO
        pantalla = gp.get_pantalla_actual()
        pantalla.set_pantalla_nivel_anterior(cod_p_com)
        gp.salir_subpantalla()
        pantalla = gp.get_pantalla_actual()


        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


        if existe_hidg0():

            #pantalla = gp.get_pantalla_actual()
            lineas= []

            if   pos_actual == 19:
                #lineas = pantalla.get_linea1()
                lineas = pan_com.get_linea1()
            elif pos_actual == 83:
                #lineas = pantalla.get_linea2()
                lineas = pan_com.get_linea2()
            elif pos_actual == 39:
                #lineas = pantalla.get_linea3()
                lineas = pan_com.get_linea3()
            elif pos_actual == 103: #lineas = pantalla.get_linea4()
                lineas = pan_com.get_linea4()

            lineas.pop(0)

            #breakpoint()


            for linea in lineas:
                # NOTA: Enviamos la linea entera de comandos de un golpe.
                # Necesario porque las combinaciones de teclas se deben
                # escribir a /dev/hidg0 de golpe en un mismo key code report
                #cod_pan_act = pantalla.get_codigo()

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
            #time.sleep(1.3)
            gp.entrar_subpantalla(4)
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)

            buzzers.sonar_A_buzzer1()

            #   Antes de volver a los comandos confirmar salir
            # de esta pantalla actual.
            # TODO NO. MEJOR PONER UNA ESPERA DE UN PAR DE SEGUNDOS TODO
            # TODO Y SALIR AUTOMATICAMENTE PORQUE NO ESTA SIENDO    TODO
            # TODO MUY PRECISO Y TERMINA SALIENDO A LA PAG PPAL     TODO
            """
            continua = True
            while continua:
                #if (GPIO.input("P8_12")) == 0:
                if (GPIO.event_detected("P8_12")):
                    continua = False
            #time.sleep(1.3)
            """
            time.sleep(1.0)

            # Restaurar a la pantalla de comandos original.
            #gp.set_pantalla_actual(pan_com)
            #pantalla = gp.get_pantalla_actual()
            #imprimir_menu_en_lcd(pantalla, True)

            pantalla = gp.get_pantalla_actual()
            pantalla.set_pantalla_nivel_anterior(cod_p_com)
            gp.salir_subpantalla()
            pantalla = gp.get_pantalla_actual()
            imprimir_menu_en_lcd(pantalla, True)

        # Datos necesarios de pantalla actual de comandos.
        #cod_p_com = cod_pantalla
        #pan_com   = gp.get_pantalla_actual()



# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


continuar = True

# Creando objeto gestionador de contraseñas.
generador_password = clase_creador_password.Creador_password()

# Generando el menu ppal en el lcd y colocando el cursor.
gestor_pantallas = clase_gestor_pantallas.Gestor_pantallas()

pantalla_actual = gestor_pantallas.get_pantalla_actual()
imprimir_menu_en_lcd(pantalla_actual, True)
lcd.cursor_a(pantalla_actual.get_pos_actual_cursor())

#   Uso de GPIO para evitar que se envie continuamente senhales
# a la BBB al pulsar un boton si este se queda trabado o
# pulsado continuamente, salvo los botones que hacen de
# izquierda o derecha, para poder recorrer los teclados mas
# rapidamente.
#   No esta libre de problemas: Ralentiza a veces la ejecucion
# del programa, sobre todo al salir a los menus principales
# da la sensacion como si generara dicha pantalla dos veces.
#   Una alternativa es crear una funcion callback y colocarla
# su llamada como tercer argumento de GPIO.add_event_detect().
# El problema resulta ser que la ejecucion del programa se
# ralentiza demasiado, tanto, que se puede ver como se escribe
# cada pantalla caracter a caracter.
#GPIO.add_event_detect("P8_7",  GPIO.RISING)
GPIO.add_event_detect("P8_7",  GPIO.FALLING)
GPIO.add_event_detect("P8_8",  GPIO.FALLING)
GPIO.add_event_detect("P8_9",  GPIO.FALLING)
GPIO.add_event_detect("P8_10", GPIO.FALLING)
GPIO.add_event_detect("P8_11", GPIO.FALLING)
GPIO.add_event_detect("P8_12", GPIO.FALLING)

#   Hacer pitar el buzzer para indicar que el programa esta cargado
# y listo para ser usado.
buzzers.sonar_A_buzzer1_1()

# Para suavizar un poco la respuesta de los botones junto con time.sleep()
estado_arriba    = 1
estado_abajo     = 1
estado_izquierda = 1
estado_derecha   = 1
estado_entrar    = 1
estado_salir     = 1

while continuar == True:
    time.sleep(0.01)

    # Pulsado el boton 1. Izquierda.
    #if (GPIO.input("P8_7") == 0):
    if (GPIO.event_detected("P8_7")):
        if estado_izquierda == 1: # Suavizando la respuesta del boton
            print()
            print("* Boton 1. Izquierda")

            #time.sleep(0.01)
            cambio_p = gestor_pantallas.mover_cursor_uno_izquierda()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)
            #time.sleep(0.01)

            estado_izquierda = 0
        else:
            estado_izquierda = 1

        #time.sleep(0.13)
    # Pulsado el boton 2. Derecha.
    #elif (GPIO.input("P8_8") == 0):
    elif (GPIO.event_detected("P8_8")):
        if estado_derecha == 1: # Suavizando la respuesta del boton
            print()
            print("* Boton 2. Derecha")

            #time.sleep(0.01)
            cambio_p = gestor_pantallas.mover_cursor_uno_derecha()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)
            #time.sleep(0.01)

            estado_derecha = 0
        else:
            estado_derecha = 1

        #time.sleep(0.13)
    # Pulsado el boton 3. Arriba. 
    #elif (GPIO.input("P8_9") == 0):
    elif (GPIO.event_detected("P8_9")):
        if estado_arriba == 1: # Suavizando la respuesta del boton
            print()
            print("* Boton 3. Arriba")

            #time.sleep(0.13)
            #time.sleep(0.01)

            cambio_p = gestor_pantallas.mover_cursor_uno_arriba()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)

            estado_arriba = 0
        else:
            estado_arriba = 1

        #time.sleep(0.13)
        #time.sleep(0.01)

        #time.sleep(0.80)
    # Pulsado el boton 4. Abajo. 
    #elif (GPIO.input("P8_10") == 0):
    elif (GPIO.event_detected("P8_10")):
        if estado_abajo == 1: # Suavizando la respuesta del boton
            print()
            print("* Boton 4. Abajo")

            #time.sleep(0.13)
            #time.sleep(0.01)

            cambio_p = gestor_pantallas.mover_cursor_uno_abajo()
            imprimir_menu_en_lcd(gestor_pantallas.get_pantalla_actual(), cambio_p)

            estado_abajo = 0
        else:
            estado_abajo = 1

        #time.sleep(0.13)
        #time.sleep(0.01)

        #time.sleep(0.80)
    # Pulsado el boton 5. Aceptar/Entrar
    #elif (GPIO.input("P8_11") == 0):
    elif (GPIO.event_detected("P8_11")):
        if estado_entrar == 1: # Suavizando la respuesta del boton
            print()
            print("* Boton 5. Aceptar/Entrar")

            #time.sleep(0.01)
            ejecutar_accion(gestor_pantallas)
            #time.sleep(0.01)

            estado_entrar = 0
        else:
            estado_entrar = 1

        #time.sleep(0.13)
    # Pulsado el boton 6. Cancelar/Salir 
    #elif (GPIO.input("P8_12") == 0):
    elif (GPIO.event_detected("P8_12")):
        if estado_salir == 1: # Suavizando la respuesta del boton
            print()
            print("* Boton 6. Cancelar/Salir")

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

        #time.sleep(0.13)

# Limpiar todo
GPIO.cleanup()
