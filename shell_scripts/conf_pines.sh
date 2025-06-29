#!/bin/bash

# ******************************************************************************
# Nombre: conf_pines.sh
#
# Descripcion:
#
# 	* Un script que configurar los pines como se necesitan para la
# aplicación, los I2C para el LCD y los GPIO para los botones.
#
# 	* Esto es porque cada vez que se reinicia la BeagleBone, la
# configuración se resetea a una por defecto distinta a la necesaria.
# ******************************************************************************


# Configuración de los pines I2C para el LCD
# ..............................................................................
config-pin p9.17 i2c
config-pin p9.18 i2c


# NOTA:
#
# 	Si no sabemos que valor de p8.xx (su identificador) debe
# llevar cada conexion gpio, ir a:
#
# 	/sys/class/gpio/gpioxx/label
#
# 	donde xx corresponde al numero de conexion gpio del 
# pueto p8. Alli, en ese fichero debe esta el valor.
#	Asi, el identificador/etiqueta de gpio66 es "P8_07"
# y por tanto hay que escribir "p8.07" aqui abajo.


# Configuracion de 6 botones fisicos que usan GPIO
# ..............................................................................
# B. Izquierdo
echo in > /sys/class/gpio/gpio66/direction
config-pin p8.07 gpio_pu
# B. Derecho
echo in > /sys/class/gpio/gpio67/direction
config-pin p8.08 gpio_pu
# B. Arriba
echo in > /sys/class/gpio/gpio69/direction
config-pin p8.09 gpio_pu
# B. Abajo
echo in > /sys/class/gpio/gpio68/direction
config-pin p8.10 gpio_pu

# B. Aceptar/Intro
echo in > /sys/class/gpio/gpio45/direction
config-pin p8.11 gpio_pu
# B. Cancelar/Salir
echo in > /sys/class/gpio/gpio44/direction
config-pin p8.12 gpio_pu
