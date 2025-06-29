#!/bin/bash

# ******************************************************************************
# Nombre: lista_ips.sh
#
# Descripcion:
#
# 	* Obtiene la lista de IPs activas del sistema junto con la interfaz
# asociada. Esos datos cribados se guardan en el fichero ips_activas.txt
#
# Parte sacado de:
#
# https://serverfault.com/questions/930142/display-only-the-network-interfaces-which-has-the-ip-address-using-ip-command#
# ******************************************************************************

PTH="$(pwd)"/shell_scripts


# Comando dividido en 3 lineas
ip -4 -brief address show up | \
       	awk '{gsub("/", " "); print $3 " " $1}' > \
	$PTH/ips_activas.txt
