#!/bin/python

import sys
import re

iface = "bond0"

try:
        bond = open('/proc/net/bonding/%s' % iface).read()
except IOError:
        print("ERROR: Invalid interface {}".format(iface))


# Parse and output
active = 'NONE'
Link = 'NONE'
slaves = ''
state = 'OK'
links = ''
bond_status = ''
for line in bond.splitlines():
        i = re.match('^Currently Active Slave: (.*)', line)
        if i:
                active = i.groups()[0]

        print(i)

        i = re.match('^Slave Interface: (.*)', line)
        if i:
                s = i.groups()[0]
                slaves += ', %s' % s
        print(i)
#        i = re.match('^Link Failure Count: (.*)', line)
#        if i:
#                l = i.groups()[0]
#                links += ', %s' % l

        i = re.match('^MII Status: (.*)', line)
        if i:
                s = i.groups()[0]
                if slaves == '':
                        bond_status = s
                else:
                        slaves += ' %s' % s
                if s != 'up':
                        state = 'FAULT'
        print(i)
