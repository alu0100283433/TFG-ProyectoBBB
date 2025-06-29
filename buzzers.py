#!/usr/bin/python3

# ******************************************************************************
# Nombre: buzzers.py
#
# Descripcion: 
#
#   *Varias funciones que hacen sonar los buzzers con sonidos distintos.
# ******************************************************************************

import time
import subprocess
import Adafruit_BBIO.GPIO as GPIO

import utilidades

# =========================================================================
RUTA_SCRIPTS_BUZZERS = utilidades.ejecuta_pwd() + '/shell_scripts/'


F_BUZZER_APAGADO     = RUTA_SCRIPTS_BUZZERS + 'apagar_buzzer.sh'
F_BUZZER_ENCENDIDO   = RUTA_SCRIPTS_BUZZERS +'encender_buzzer.sh'
# =========================================================================


"""
********************************************************************************
*   - Los buzzers se pueden usar mediante shell scripts o con Adafruit GPIO -  *
********************************************************************************
*                                                                              *
*   -Las diferencias estan en:                                                 *
*                                                                              *
*       + Con Adafruit es mas limpio, no muestra mensajes de en que modo       *
*   se acaba de configurar el pin de la Beaglebone por la terminal, pero       *
*   es mas lento y esto no permite pitidos mas personalizados.                 *
*                                                                              *
*       + Con shell scripts se pueden hacer pitidos mas rapidos, logrando      *
*   pitidos mas variados. Lo malo es eso: Mensajes continuos cada vez          *
*   que se cambian los valores.                                                *
*                                                                              *
*   Nota: El buzzer esta conectado al pin 18 de P8, siendo GPIO_65. Para       *
* que pite configuramos ese pin como salida, sin resistencias internas y       *
* le pasamos valor alto (HIGH o 1), luego lo volvemos a configurar pero        *
* pasandole entonces un valor bajo (Low o 0) para que deje de pitar.           *
********************************************************************************
"""



# Funciones
# ==============================================================================
# ==============================================================================

# - Usando Adafruit GPIO. 'A' de Adafruit - 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 1
def sonar_A_buzzer1():
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 1-1
def sonar_A_buzzer1_1():
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    time.sleep(0.85)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 2
def sonar_A_buzzer2():
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 3
def sonar_A_buzzer3():
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 3-2
def sonar_A_buzzer3_2():
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 4
def sonar_A_buzzer4():
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.HIGH)
    GPIO.setup("P8_18", GPIO.OUT, GPIO.PUD_OFF, GPIO.LOW)


# - Usando shell scripts. 'S' de shell script - 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 2 V
def sonar_S_buzzer2():
    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.10)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.30)

    subprocess.run(['sh', F_BUZZER_APAGADO])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 2-2 
def sonar_S_buzzer2_2():
    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.10)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.10)

    subprocess.run(['sh', F_BUZZER_APAGADO])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 3 V
def sonar_S_buzzer3():
    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.10)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.10)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.30)

    subprocess.run(['sh', F_BUZZER_APAGADO])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 3-2
def sonar_S_buzzer3_2():
    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.7)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.1)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.1)

    subprocess.run(['sh', F_BUZZER_APAGADO])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hacer pitar el buzzer/zumbador/timbre. Tipo 3-3
def sonar_S_buzzer3_3():
    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.1)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.7)

    subprocess.run(['sh', F_BUZZER_APAGADO])

    subprocess.run(['sh', F_BUZZER_ENCENDIDO])
    time.sleep(0.1)

    subprocess.run(['sh', F_BUZZER_APAGADO])

# ==============================================================================
# ==============================================================================
