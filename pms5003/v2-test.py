#!/bin/python
import serial
import time
import sys
from struct import *
debug=1
# work for pms3003
# data structure: https://github.com/avaldebe/AQmon/blob/master/Documents/PMS3003_LOGOELE.pdf
# fix me: the format is different between /dev/ttyUSBX(USB to Serial) and /dev/ttyAMA0(GPIO RX)
#          ttyAMA0:0042 004d 0014 0022 0033
#          ttyUSB0:4d42 1400 2500 2f00

class g3sensor():
    def __init__(self):
        if debug: print "init"
	self.endian = sys.byteorder
    
    def conn_serial_port(self, device):
        if debug: print device
        self.serial = serial.Serial(device, baudrate=9600, parity=serial.parity, stopbits=serial.STOPBITS_ONE)
        if debug: print "conn ok"

    def check_keyword(self):
        if debug: print "check_keyword"
        while True:
            token = self.serial.read()
    	    token_hex=token.encode('hex')
    	    if debug: print token_hex
    	    if token_hex == '42':
    	        if debug: print "get 42"
    	        token2 = self.serial.read()
    	        token2_hex=token2.encode('hex')
    	        if debug: print token2_hex
    	        if token2_hex == '4d':
    	            if debug: print "get 4d"
                    return True
                elif token2_hex == '00': # fixme
                    if debug: print "get 00"
                    token3 = self.serial.read()
                    token3_hex=token3.encode('hex')
                    if token3_hex == '4d':
                        if debug: print "get 4d"
                        return True
		    
    def vertify_data(self, data):
        checksum = int(data_hex[30], 16) * 256 + int(data_hex[31], 16)
        if debug: print data
        n = 2
        sum = int('42',16) + int('4d',16)
        for i in range(0, len(data)-4, n):
            sum += int(data[i], 16)
        if debug: print sum
        if debug: print checksum
        if sum == checksum:
            print "data correct"
        else:
            print "data incorrect"
	
    def read_data(self):
        data = self.serial.read(30)
        data_hex=data.encode('hex')
        if debug: self.vertify_data(data_hex)
        data = []
        for i in range(0, len(data_hex), 2):
            data[i] = int(data_hex[i], 16) * 256 + int(data_hex[i+1], 16)
            if debug: print "data"+i+":"+str(data[i])

    	self.serial.close()
        return data

    def read(self, argv):
        tty=argv[0:]
        self.conn_serial_port(tty)
        if self.check_keyword() == True:
            self.data = self.read_data()
            if debug: print self.data
            return self.data

if __name__ == '__main__': 
    air=g3sensor()
    while True:
        pmdata=0
        try:
            pmdata=air.read("/dev/ttyS0")
        except: 
            next
        if pmdata != 0:
            print pmdata
            break
