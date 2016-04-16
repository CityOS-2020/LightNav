import bluetooth
import time

ARDUINO_ADDR = '98:23:31:90:02:70'
ARDUINO_NAME = 'LiGhTpAtH'

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((ARDUINO_ADDR, 1))

def sock_readln(sock):
    ln = ''
    while True:
        ch = sock.recv(1)
        if ch != '\n':
            ln += ch
        else:
            break
    return ln

while True:
    sock.sendall("BTR.HIGH 13\n")
    print sock_readln(sock)
    time.sleep(1)
    sock.sendall("BTR.LOW 13\n")
    print sock_readln(sock)
    time.sleep(1)
    

