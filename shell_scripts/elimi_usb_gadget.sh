#! /bin/bash

# elimi_usb_gadget.sh

# 	Script de desactivacion y eliminacion del gadget usb creado en el
# script "crear_usb_gadget.sh" (un teclado virtual mediante la conexion
# usb del BB).
#
# 	- Mas informacion sobre los pasos a seguir en:
#
#	https://www.kernel.org/doc/Documentation/usb/gadget_configfs.txt

PTH='/sys/kernel/config/usb_gadget/BB_como_teclado_usb'


# ------------------------------------------------------------------------------

# Desactivando el gadget/dispositivo

echo "" > $PTH/UDC

# 	Activando el 'g_multi' para que tome el mando y funcione la conexion USB
# como puerto Ethernet/alimentacion de BB/almacenamiento/... (conf. original)
echo musb-hdrc.0 > /sys/kernel/config/usb_gadget/g_multi/UDC

# ------------------------------------------------------------------------------

# Limpiando ...

# 	configuraciones ...

# 		eliminando el enlace de la funcion en la configuracion.
rm $PTH/configs/conf.1/hid.usb0

# 		eliminando los directorios de 'string'
rmdir $PTH/configs/conf.1/strings/0x409
#rm -R $PTH/configs/conf.1/strings/0x409

#		eliminando los directorios de la config. 'conf.1'
rmdir $PTH/configs/conf.1

# 	funciones ...

rmdir $PTH/functions/hid.usb0

# 	cadenas (y sus idiomas) ...
rmdir $PTH/strings/0x409

# 	y por ultimo el propio gadget ...
rmdir $PTH

# 	NOTA IMPORTANTE: "... functions modules are not unloaded ..."
# Creo que hay que descargar los modulos cargados cuando se creo el
# gadget. Habra que descargarlos (con modprobe?. Recordar que 'lsmod'
# creo que mostraba la lista de modulos cargados, por si es necesario.

# 	NOTA 1: Parece funcionar perfectamente y sin problemas.
#
# 	NOTA 2: No veo, por ahora, un cambio en el numero de modulos
# cargados con "lsmod" tras crear el gadget. Asi que no parece que
# haya que buscar y descargar ningun modulo cuando creemos y borremos
# el gadget creado.

