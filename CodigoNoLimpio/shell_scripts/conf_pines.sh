#!/bin/bash

# conf_pines.sh

# 	Un script que vuelve a configurar los pines
# a como los necesito.


# Configuracion de P9_17 y P9_18 que cada vez que
# apaga la placa pierde  su configuracion I2C.
# ..............................................................................
# ..............................................................................

config-pin p9.17 i2c
config-pin p9.18 i2c



# Configuracion de 6 botones fisicos
# ..............................................................................
# ..............................................................................

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
