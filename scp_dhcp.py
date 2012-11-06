#! /usr/bin/env python

from scapy.all import *
from pox.lib.addresses import *
from pox.lib.recoco import *
import struct


# Test code for Packing DHCP Packet

# This Program just send DHCP Discovcery and then
# according to the DHCP Offer packet replying from 
# a DHCP Server, it sends the DHCP Request Packet 
# and receive the DHCP Ack Packet.

# Date: 5 Sep, 2012
conf.checkIPaddr = False
hw1 = 0x00
hw2 = 0x21
hw3 = 0x9b
hw4 = 0xe3
hw5 = 0xae
hw6 = 0x00

# Build DHCP Discovery Packet
dhcp_disc = Ether(dst = "ff:ff:ff:ff:ff:ff")/\
			IP(src = "0.0.0.0", dst = "255.255.255.255")/\
			UDP(sport = 68, dport = 67)/\
			BOOTP()/\
			DHCP(options = [("message-type", "discover"), "end"])
			   
dhcp_disc[BOOTP].xid = 123456
hw = struct.pack('BBBBBB', hw1, hw2, hw3, hw4, hw5, hw6)
src_hw = EthAddr(hw).toStr()
dhcp_disc[Ether].src = src_hw
dhcp_disc[BOOTP].chaddr = hw
#while True:
print time
sendp(dhcp_disc, loop=1, inter=0.2)
