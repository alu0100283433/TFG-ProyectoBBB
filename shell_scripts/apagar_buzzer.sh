#!/bin/bash

# apagar_buzzer.sh

# 	Script que manda la señal de apagado al puerto GPIO
# correspondiente donde está conectado el buzzer del proyecto.

# 	Se tiene el pin numero 18 del puerto 8 (P8) de la BBB,
# identificado como GPIO_65, usado para conectar un buzzer.

# 	NOTA: El estado inicial del pin 18 (gpio, out) se configurara
# en el programa principal del proyecto con Adafruit. Se hace para
# minimizar la cantidad de mensajes en la terminal que aparecen al
# usar config-pin.


echo 0 > /sys/class/gpio/gpio65/value
