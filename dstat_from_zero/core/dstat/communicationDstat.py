#!/usr/bin/env python

import time
import serial
from serial.tools import list_ports

import logging
from pkg_resources import parse_version

logger = logging.getLogger(__name__)
dstat_logger = logging.getLogger("{}.DSTAT".format(__name__))
exp_logger = logging.getLogger("{}.Experiment".format(__name__))



ser = serial.Serial('/dev/ttyACM0')  # open serial port
print("Connected to: " + ser.portstr)


ser.write(str.encode('!1\n'))
line = ser.readline().decode('ascii')
print(line)

time.sleep(.5)

ser.write(str.encode('V\n'))
line = ser.readline().decode('ascii')
print(line)

time.sleep(.5)
line = ser.readline().decode('ascii')
print(line)

time.sleep(.5)
line = ser.readline().decode('ascii')
print(line)

#
# for i in range(10):
#     if ser.readline().rstrip()=="@ACK 1":
#         ser.write('V\n')
#         if ser.readline().rstrip()=="@RCV 1":
#             break
#     else:
#         time.sleep(.5)
#         ser.reset_input_buffer()
#         ser.write('!1\n')
#         time.sleep(.1)
#
# for line in ser:
#     dstat_logger.info(line.decode('utf-8'))
#     if line.startswith('V'):
#         input = line.lstrip('V')
#     elif line.startswith("#"):
#         dstat_logger.info(line.lstrip().rstrip())
#     elif line.lstrip().startswith("@DONE"):
#         dstat_logger.debug(line.lstrip().rstrip())
#         ser.reset_input_buffer()
#         break

ser.close()             # close port
