#!/usr/bin/env python3
#
# Convert the decimal notations of the IP list to usable IP addresses
# List can be found at https://download.ip2location.com/lite/IP2LOCATION-LITE-DB1.CSV.ZIP
#

import sys
import socket
import struct
import csv

if len(sys.argv) > 1:
    # print(sys.argv[1])
    # print(socket.inet_ntoa(struct.pack('!L', int(sys.argv[1]))))
    with open(sys.argv[1], "r") as csvFile:
        reader = csv.reader(csvFile)
        for line in reader:
            # print(line)
            from_ip = int(line[0])
            to = int(line[1])
            
            while from_ip <= to:
                # print(from_ip)
                print(socket.inet_ntoa(struct.pack('!L', from_ip)))
                from_ip += 1
else:
    print('Usage: ' + sys.argv[0] + ' [integer-ip]')

exit(0)