#!/bin/bash

# ******************************************************************************
# Nombre: encender_buzzer.sh
#
# Descripcion:
#
# 	* Activando directamente el buzzer conectado al pin numero 18 del
# puerto 8 (P8) de la BBB, identificado como GPIO_65.
#
#	* Entonces, si queremos activar el buzzer, se le debe
# pasar valor 1 al fichero 'value' de /sys/class/gpio/gpio64/
# (Y si queremos desactivarlo le pasamos el valor 0)
# ******************************************************************************


echo 1 > /sys/class/gpio/gpio65/value
