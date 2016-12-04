# Idea from https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8#.pw7f1hqdb
from scapy.all import *

def buttonPushARP(pkt):
	if pkt[0][ARP].hwsrc == "44:65:0d:80:4e:0f":
		print 'Energizer!'
	else:
		#print pkt[0].show()
		print pkt[0][ARP].hwsrc
		print pkt[ARP].hwsrc
		#print pkt[0][Ether].src
		#print 'Not 44:65:0d:80:4e:0f'

def buttonPushIP(pkt):
	if pkt[1][IP].src == "10.0.0.4":
		print "Energizer!"
	else:
		#print pkt.show()
		print pkt[1][IP].src
#print sniff(prn=buttonPush, store=0, count=10)
sniff(prn=buttonPushIP, filter="ip", store=0)

