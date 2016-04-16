from django.db import models

import bluetooth

ARDUINO_ADDR = '98:23:31:90:02:70'
ARDUINO_NAME = 'LiGhTpAtH'

sock = None


def sock_readln(sock):
    ln = ''
    while True:
        ch = sock.recv(1).decode("UTF-8")
        if ch != '\n':
            ln += ch
        else:
            break
    return ln


class LocationType(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    location_type = models.ForeignKey(LocationType)
    name = models.CharField(max_length=15)
    relay_no = models.IntegerField(default=4)
    relay_no_2 = models.IntegerField(default=0)
    map_url = models.CharField(max_length=100, blank=True, null=True)
    enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    display_seconds = models.IntegerField(default=30)
    active = models.BooleanField(default=False)
    btn_class = models.CharField(max_length=20, default='info')
    btn_icon = models.CharField(max_length=20, default='', blank=True)

    def __str__(self):
        return self.name

    def connect_sock(self, force=False):
        global sock
        if sock == None or force:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((ARDUINO_ADDR, 1))

    def turn_on_relay(self):
        self.connect_sock()

        while True:
            try:
                sock.sendall('BTR.HIGH %d\n' % self.relay_no)
                resp = sock_readln(sock).strip()
                break
            except:
                self.connect_sock(True)
        
        if resp != '+OK':
            print(resp)
        else:
            print("Turned on %d" % self.relay_no)

    def turn_off_relay(self):
        self.connect_sock()

        while True:
            try:
                sock.sendall('BTR.LOW %d\n' % self.relay_no)
                resp = sock_readln(sock).strip()
                break
            except:
                self.connect_sock(True)

        if resp != '+OK':
            print(resp)
        else:
            print("Turned off %d" % self.relay_no)


class NavigationAction(models.Model):
    location = models.ForeignKey(Location)
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location.name

