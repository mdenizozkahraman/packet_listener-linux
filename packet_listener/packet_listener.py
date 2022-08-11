import scapy.all as scapy
from scapy.layers import http



def listen_packets(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets)

def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

print("""
by mdo //-
                  _        _       _ _     _                            _ _                  
 _ __   __ _  ___| | _____| |_    | (_)___| |_ ___ _ __   ___ _ __     | (_)_ __  _   ___  __
| '_ \ / _` |/ __| |/ / _ \ __|   | | / __| __/ _ \ '_ \ / _ \ '__|____| | | '_ \| | | \ \/ /
| |_) | (_| | (__|   <  __/ |_    | | \__ \ ||  __/ | | |  __/ | |_____| | | | | | |_| |>  < 
| .__/ \__,_|\___|_|\_\___|\__|___|_|_|___/\__\___|_| |_|\___|_|       |_|_|_| |_|\__,_/_/\_\ 
|_|                          |_____|                                                         


""")

number = 0
a = "."

try:
    print("\rSniffing ... ")
    print()
    listen_packets("eth0")


except KeyboardInterrupt:
    print("\n Sniffing terminated!")


