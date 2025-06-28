#!/bin/bash

# conf_pines.sh

# 	Un script que vuelve a configurar los pines
# a como los necesito.

# 	Se tiene el pin numero 18 del puerto 8 (P8) de la BBB,
# identificado como GPIO_65, usado para conectar un buzzer.
#
# 	Usaremos aqui comandos a mano para poner su direccion
# 'out', pues hay que mandar voltaje de salida al buzzer.
#
# 	Tambien haremos que se active una resistencia pull up
# poniendo la opcion 'gpio_pu', aunque como funciona el timbre
# podemos ponerla en opcion 'gpio' y ya esta
#
#	Entonces, si queremos activar el buzzer, se le debe
# pasar valor 1 al fichero 'value' de /sys/class/gpio/gpio64/.
# Y si queremos desactivarlo le pasamos el valor 0


# 	NOTA: El estado inicial del pin 18 (gpio, out) se configurara
# en el programa principal del proyecto con Adafruit. Se hace para
# minimizar la cantidad de mensajes en la terminal que aparecen al
# usar config-pin.

#config-pin p8.18 gpio # No necesitamos una resistencia pull up/down aqui
#config-pin p8.18 gpio_pu
#config-pin p8.18 gpio_pd

#echo out > /sys/class/gpio/gpio65/direction

echo 0 > /sys/class/gpio/gpio65/value
#echo 1 > /sys/class/gpio/gpio65/value
