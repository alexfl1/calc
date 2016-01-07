#!/usr/bin/python3
import sys
import re
from netaddr import *

#print (sys.argv[1])
# https://pythonhosted.org/netaddr/tutorial_01.html

IP = sys.argv[1]

i = IPAddress(IP)

print (i.bin)
