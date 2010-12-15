#!/usr/bin/env python
#
# This script will decode an "encrypted" TDS7 password string capture, 
# presumably from a packet capture.  Wireshark will decode these for you
# but this is useful if:
# a) you don't have access to wireshark
# b) you want to understand how the password is encrypted in TDS7
#
import sys

hexstr = sys.argv[1]
key = 165	# hex 0xa5 converted to int
a = hexstr.split()
xorstr = ''

print 'hex int xor bin    msb lsb    nbin     ti c'

for b in a:
	print b,
	# convert the hex to int as it does not have leading 0x
	i = int(b, 16)
	print i,
	
	# xor with the key
	x = i ^ key	
	print x,

	# convert to hex
	#y = hex(x)
	#xorstr += y

	# now convert to binary and perform bit manipulation
	#bits = bin(x)
	bits = "{0:08b}".format(x)
	print bits,

	msb = bits[:4]
	lsb = bits[-4:]

	print msb,
	print lsb,

	nbin = lsb + msb
	print nbin,

	# generate unicode character
	ti = int(nbin, 2)
	print ti,

	c = "{0:c}".format(ti)
	print c

	# append to xorstr
	xorstr += c

print 'TDS password: %s' % xorstr
