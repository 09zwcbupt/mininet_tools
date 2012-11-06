#! /usr/bin/env python

from scapy.all import *
import time

import os

conf.checkIPaddr = False

'''
ret = os.system("ifconfig eth0 promisc")
if ret != 0:
	print "______Error: Failed to enable promisc mode on interface, Please run the script with root permission______"
	exit()
'''

class ARP_test(object):
	def __init__(self):
		self.IP_list= []

	def statistics(self):
		packet = Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = "10.0.0.20")
		send_time = time.time()
		#ans_for_arp = srp(packet)
		srp(packet)
		#os.system("arping -I eth0 -c 1 10.108.147.237")
		receive_time = time.time()

		#ans_for_arp.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )

		#print send_time
		#print receive_time

		interval = receive_time - send_time
		interval = interval * 100

		print str(interval)+"\n"

class testing():
	tester = ARP_test()
	tester.statistics()
