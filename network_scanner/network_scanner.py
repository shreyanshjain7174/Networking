import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = broadcast / arp_request
    answered, unanswered = scapy.srp(arp, timeout=1)
    print(answered.summary())

scan("192.168.187.1/24")
