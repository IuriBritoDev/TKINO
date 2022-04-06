import serial.tools.list_ports
from Controller import controleSerial


def BuscaPortas():

    ports = serial.tools.list_ports.comports()
    return ports

def ConectaPortaUSB(connectPort):

    ser = serial.Serial(connectPort, baudrate = 9600, timeout = 1)
    
    controleSerial.ser = ser
   