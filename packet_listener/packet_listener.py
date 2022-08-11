import scapy.all as scapy
from scapy.layers import http


def listen_packets(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets)

def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

listen_packets("eth0")
