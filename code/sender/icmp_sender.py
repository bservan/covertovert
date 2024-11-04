import scapy

# Implement your ICMP sender here
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send
import socket


def icmp_sender(dest_ip: str):
    """
    Sends ICMP packets to destination IP address.

    Args:
        dest_ip (str): IP address of destination to send ICMP packets.

    This method sends ICMP packets with time to live (TTL) value of 1.
    """
    icmp_packet = IP(dst=dest_ip, ttl=1) / ICMP()
    send(icmp_packet, verbose=False)
    print("ICMP packet sent to " + dest_ip)

def main():
    """
    Main sender method.

    Gets 'receiver' host and sends ICMP packet to that host.
    """
    dst_ip = socket.gethostbyname("receiver")
    icmp_sender(dest_ip=dst_ip)


if __name__ == "__main__":
    main()
