#!/usr/bin/env python2
# -*- coding: utf-8-*-
"""
Created on Tue Apr 10 12:42:49 2018

@author: zp

Transfer can file to asc file.
"""


import binascii as ba
import time
import numpy as np
import os
import subprocess


def can2asc(can_file, asc_file):
    d = time.strptime(can_file.split(
        '/')[-1].split('.')[0].split('_')[1], "%Y%m%dT%H%M%S")
    tm_mon = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    wday = {0: 'Mon', 1: 'Tue', 2: 'Wed',
            3: 'Thur', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    date = wday[d[6]]+' '+tm_mon[d[1]]+' '+str(d[2])+' '+str(d[3])+':'+str(
        d[4])+':'+str(d[5])+' '+['am' if d[3] < 12 else 'pm'][0]+'  '+str(d[0])

    fileLen = os.path.getsize(can_file)
    if fileLen <= 1024:
        raise Exception("Incorrect File")

    if (fileLen-1024) % 13 != 0:
        raise Exception("Bad Format")

    NumMsg = (fileLen-1024) / 13

    dir_name = os.path.dirname(asc_file)
    if dir_name != '' and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(can_file) as f:
        asc = open(asc_file+".working", 'w')
        asc.writelines(['data'+' '+date+'\r\n', 'base hex timestamps absolute\r\n',
                        'internal events logged\r\n', '// version 8.5.0\r\n'])
        start_time = 0.000000

        for i in range(NumMsg):
            data = f.read(13)
            h = ba.b2a_hex(data)
            tm = start_time+300.0/(NumMsg)*i
            channel = int(h[0], 16)+1
            # CANid = '0000'+(hex(np.random.randint(16, 255)))[2:].upper()
            CANid = h[4:10]
            t = 'RX   d'
            length = h[1]
            message_data = str(h[10:12])
            for j in range(1,int(length)):
                message_data = message_data + ' ' + str(h[10+2*j:12+2*j])
            # message_data = str(h[10:12])+' '+str(h[12:14])+' '+str(h[14:16])+' '+str(
            #     h[16:18])+' '+str(h[18:20])+' '+str(h[20:22])+' '+str(h[22:24])+' '+str(h[24:26])
            tail = 'Length = 0 BitCount = 0 ID = %s' % int(h[4:10], 16)
            asc.writelines([str('%.6f' % tm), ' ', str(channel), '  ', CANid, '             ', t, ' ', str(
                length), ' ', message_data, ' ', tail, '\r\n'])

        asc.close()
        os.rename(asc_file+".working", asc_file)

    f.close()


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description='Convert ADAS Pandora CAN Log Data')
    parser.add_argument('-i', '--infile', help='Input file', required=True)
    parser.add_argument('-o', '--outfile', help='Output file', required=False)

    args = vars(parser.parse_args())

    infile = args['infile']
    outfile = args['outfile']
    if outfile is None:
        outfile = "/tmp/" + os.path.basename(infile).replace('.dat', '.asc')

    can2asc(infile, outfile)

