

#   Clase que gestiona las operaciones posibles sobre
# un LCD con microcontrolador LCMI1602 usando conexionado
# I2C.


import time
import pdb

# Para manejar operaciones de escritura y otras instrucciones  en el LCD 
import smbus as smb


# Nanosegundos, para las operaciones en 'escritura'
tiempoBase = 0.000001 

#   El tiempo de espera para 'Return home', que se ve en la pagina
# 24 del Datasheet del HD44780
esperCmds = 0.00152

class Lcd:


    def __init__(self):

        self.bus = smb.SMBus(1)

        time.sleep(0.015)

        """
            Proceso de inicializacion del HD44780 en modo 4-bits.
         Pagina 46 Datasheet del HD44780.
        """

        #1a instruccion.
        self.escritura_modo4bits((0b0011_0000 | (1 << 3)))
        time.sleep(0.0041)

        #2a instruccion.
        self.escritura_modo4bits(0b0011_0000 | (1 << 3))
        time.sleep(0.0001)

        #3a instruccion.
        self.escritura_modo4bits(0b0011_0000 | (1 << 3))
        time.sleep(esperCmds)

        #4a instruccion.
        self.escritura_modo4bits(0b0010_0000 | (1 << 3))
        time.sleep(esperCmds)

        #5a y 6a instruccion.
        self.escritura_modo4bits(0b0010_0000 | (1 << 3))
        self.escritura_modo4bits(0b1100_0000 | (1 << 3))
        time.sleep(esperCmds)

        #7a y 8a instruccion.
        self.escritura_modo4bits(0b0000_0000 | (1 << 3))
        self.escritura_modo4bits(0b1000_0000 | (1 << 3))
        time.sleep(esperCmds)

        #9a y 10a instruccion.
        self.escritura_modo4bits(0b0000_0000 | (1 << 3))
        self.escritura_modo4bits(0b0001_0000 | (1 << 3))
        time.sleep(esperCmds)

        #11a y 12a instruccion.
        self.escritura_modo4bits(0b0000_0000 | (1 << 3))
        self.escritura_modo4bits(0b0110_0000 | (1 << 3))
        time.sleep(esperCmds)


    # Para el modo 4bits. Instrucciones/comandos
    def dos_nibbles_instruccion(self, byte):
        # Instruccion: RS y R/W a 0. Dejando la retroiluminacion encendida.
        # 4BMS del byte recibido al nibble1 (n1)
        # 4bms del byte recibido al nibble2 (n2)
        n1 =  (byte & 0xF0) | (1 << 3)         # nibble 1
        n2 =  ((byte & 0x0F) << 4) | (1 << 3)  # nibble 2

        self.escritura_modo4bits(n1)
        self.escritura_modo4bits(n2)


    # Para el modo 4bits. Operacion escritura caracter al LCD
    def dos_nibbles_escritura(self, byte):
        # Escritura: RS a 1, R/W a 0. Retro. a 1.
        n1 =  (byte & 0xF0) | (1 << 3) | 1         # nibble 1
        n2 =  ((byte & 0x0F) << 4) | (1 << 3) | 1  # nibble 2

        self.escritura_modo4bits(n1)
        self.escritura_modo4bits(n2)


    #   Simulacion del ciclo de Escritura pag.58 datasheet HD44780
    # Obligatorio a simular de esta manera para escribir en el LCD.
    def escritura_modo4bits(self, contenido):
        #   NOTA: La operacion de escritura al LCD ocurre,
        # automaticamente, en el periodo de tiempo cuando
        # el flanco alto del bit 'E' empieza a bajar tras
        # la 3a operacion de '.write_byte()' aqui.

        self.bus.write_byte(0x27, contenido)
        time.sleep(tiempoBase * 40)

        # Bit Enable activado (3bms)
        self.bus.write_byte(0x27, contenido | (1 << 2))
        time.sleep(tiempoBase * 230)

        # Bit Enable desactivado(3bms)
        self.bus.write_byte(0x27, contenido & ~(1 << 2))
        time.sleep(tiempoBase * 10)


    def modificar_BCD(self, b: int,  c: int, d: int):
        instruccion = 0b0000_1000

        # Activar/desactivar b-c-d
        # d: El display/LCD. Apagado no muestra nada.
        #
        # c: Un cursor ('_') en la pos. actual del LCD.
        #
        # b: Un parpadeo (blink) en la pos. actual del LCD.
        if d == 1:
            instruccion = instruccion | (1 << 2)
        if c == 1:
            instruccion = instruccion | (1 << 1)
        if b == 1:
            instruccion = instruccion | 1

        self.dos_nibbles_instruccion(instruccion)


    def escribir_caracter(self, caracter): # Escribir caracter a LCD
        self.dos_nibbles_escritura(caracter)


    def cursor_a_izda(self):
        instruccion = 0b0001_0000

        self.dos_nibbles_instruccion(instruccion)


    def cursor_a_drca(self):
        instruccion = 0b0001_0100

        self.dos_nibbles_instruccion(instruccion)


    def cursor_a(self, posicion: int):
        # Usa "Set DDRAM address"
        instruccion = 0b1000_0000 | posicion

        self.dos_nibbles_instruccion(instruccion)


    def home(self):
        instruccion = 0b0000_0010

        self.dos_nibbles_instruccion(instruccion)


    def clear(self):
        instruccion = 0b0000_0001

        self.dos_nibbles_instruccion(instruccion)
