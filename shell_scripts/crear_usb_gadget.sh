#! /bin/bash

# ******************************************************************************
# Nombre: crear_usb_gadget.sh
#
# Descripcion:
#
# 	* Script que configura la BeagleBone Black para que se 
# comporte como un teclado USB al conectarse mediante ese cable
# a un equipo host (un PC). 
#
# 	- Mas informacion sobre los pasos a seguir en:
#
#	https://www.kernel.org/doc/Documentation/usb/gadget_configfs.txt

# 	Nota: Supuestamente el ".auto" era un sufijo de versiones antiguas del
# kernel. Segun el enlace ...
#
# https://processors.wiki.ti.com/index.php/UsbgeneralpageLinuxCore
#
# 	Nota2: Se debe ejecutar el script en modo superusuario para su
# funcionamiento correcto.
# ******************************************************************************


sleep 1 

PTH='/sys/kernel/config/usb_gadget/BB_como_teclado_usb'
PTH_MRD="$(pwd)"/shell_scripts/my_report_desc

# Creacion directorio donde va el gadget/dispositivo
mkdir $PTH

# 	Nota: Lo anterior crea toda la estructura de ficheros/directorios del
# gadget/dispositivo. Los 'atributos', que son los ficheros generados, tendran
# contenido generico (ej.: idProduct tendra dentro "0x0000"). Faltara ademas
# crear el contenido de los directorios "configs", "functions" y "strings"

# Datos de identificador vendedor y producto
echo 0xa4ac > $PTH/idVendor
echo 0x0525 > $PTH/idProduct

# Crear directorio para el idioma (0x409 : Ingles de EEUU)
mkdir -p $PTH/strings/0x409

# Crear 'atributos' (ficheros) siguientes en ../strings/0x409
echo 1 > $PTH/strings/0x409/serialnumber
echo ULL > $PTH/strings/0x409/manufacturer
echo TECLADO-VIRTUAL-USB > $PTH/strings/0x409/product

# ------------------------------------------------------------------------------

# Ahora las configuraciones, solo una, "conf.1" aqui.
mkdir -p $PTH/configs/conf.1
mkdir -p $PTH/configs/conf.1/strings/0x409 # Cadenas/idioma de la config.

echo "Conf 1" > $PTH/configs/conf.1/strings/0x409/configuration
echo 120 > $PTH/configs/conf.1/MaxPower

# ------------------------------------------------------------------------------

# La parte de las funciones.

# 	Nota: Nos basamos en las fuentes/documentación encontradas ...
#
# https://www.kernel.org/doc/Documentation/ABI/testing/configfs-usb-gadget-hid
#
# y
#
#https://github.com/torvalds/linux/blob/master/Documentation/ABI/testing/configfs-usb-gadget-hid
#
#	En:
#
# https://android.googlesource.com/kernel/common/+/523e6d7f3186/Documentation/usb/gadget-testing.txt
#
# 	nos indican que la funcion 'hid' la provee el modulo "usb_f_hid.ko", pero no
# parece estar disponible en el BB (aun asi el gadget en las pruebas funciona
# aparentemente sin problemas)
#	Tambien nos indican que el protocolo y la subclase es '1', el report_desc
# es el que pondremos ahi a partir del fichero 'my_report_desc' y la longitud
# informe sera 8. 

mkdir -p $PTH/functions/hid.usb0

echo 1 > $PTH/functions/hid.usb0/protocol
echo 1 > $PTH/functions/hid.usb0/subclass
echo 8 > $PTH/functions/hid.usb0/report_length

cat $PTH_MRD > $PTH/functions/hid.usb0/report_desc

# ------------------------------------------------------------------------------

# Asociando funciones a configuraciones

ln -s $PTH/functions/hid.usb0 $PTH/configs/conf.1

# ------------------------------------------------------------------------------

# Activando el gadget

# 	Hay que ligar tal gadget a un UDC disponible para que funcione. Los UDC
# disponibles se encuentran en /sys/class/udc. En el caso del BB el unico
# disponible es "musb-hdrc.0" y usaremos ese.

# 	Nota: 'g_multi' suele usar el mismo UDC (musb-hdrc.0) que vamos a usar
# nosotros en nuestro gadget. Si no ponemos el contenido de su fichero 'UDC'
# vacio (/sys/kernel/config/usb_gadget/g_multi/UDC) no nos permitira llenar
# el fichero 'UDC' de nuestro gadget con 'musb-hdrc.0'; nos lo bloqueara.

echo "" > /sys/kernel/config/usb_gadget/g_multi/UDC

echo musb-hdrc.0 > $PTH/UDC

sleep 5

chmod 777 /dev/hidg0

