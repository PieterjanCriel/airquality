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
        self.serial = serial.Serial(device, baudrate=9600)
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
        checksum = float(data_hex[30]*256 + data_hex[31])
        if debug: print data
        n = 2
        sum = int('42',16) + int('4d',16)
        for i in range(0, len(data)-4, n):
            sum += int(data[i],16)
        if debug: print sum
            if debug: print checksum
        if sum == checksum:
            print "data correct"
	
    def read_data(self):
        data = self.serial.read(30)
        data_hex=data.encode('hex')
        if debug: self.vertify_data(data_hex)

        data1 = float(data_hex[4]*256 + data_hex[5])
        data2 = float(data_hex[6]*256 + data_hex[7])
        data3 = float(data_hex[8]*256 + data_hex[9])
        data4 = float(data_hex[10]*256 + data_hex[11])
        data5 = float(data_hex[12]*256 + data_hex[13])
        data6 = float(data_hex[14]*256 + data_hex[15])
        data7 = float(data_hex[16]*256 + data_hex[17])
        data8 = float(data_hex[18]*256 + data_hex[19])
        data9 = float(data_hex[20]*256 + data_hex[21])
        data10 = float(data_hex[22]*256 + data_hex[23])
        data11 = float(data_hex[24]*256 + data_hex[25])
        data12 = float(data_hex[26]*256 + data_hex[27])
        data13 = float(data_hex[28]*256 + data_hex[29])

        if debug: print "data1: "+str(data1)
        if debug: print "data2: "+str(data2)
        if debug: print "data3: "+str(data3)
        if debug: print "data4: "+str(data4)
        if debug: print "data5: "+str(data5)
        if debug: print "data6: "+str(data6)
        if debug: print "data7: "+str(data7)
        if debug: print "data8: "+str(data8)
        if debug: print "data9: "+str(data9)
        if debug: print "data10: "+str(data10)
        if debug: print "data11: "+str(data11)
        if debug: print "data12: "+str(data12)
        if debug: print "data13: "+str(data13)

        data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12]

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
            pmdata=air.read("/dev/ttyAMA0")
        except: 
            next
        if pmdata != 0:
            print pmdata
            break
