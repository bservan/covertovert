import scapy

# Implement your ICMP receiver here
from scapy.layers.inet import ICMP
from scapy.packet import Packet
from scapy.sendrecv import sniff


def icmp_receiver_callback(packet: Packet):
    """
    Callback method that captures and processes incoming ICMP packets

    Args:
        packet (Packet): incoming ICMP packet that is captured.

    This method checks whether the packet is an ICMP packet or not.
    If the packet is an ICMP packet, and it is an ICMP echo request (.type == 8),
    print the details of that packet.
    """
    if ICMP in packet and packet[ICMP].type == 8:
        packet.show()

def main():
    """
    Main receiver method.

    Sniffs the first incoming ICMP echo request and processes it by 'icmp_receiver_callback'.
    Then exits (only captures one packet by passing count=1).
    """
    sniff(filter="icmp", prn=icmp_receiver_callback, store=0, count=1)

if __name__ == "__main__":
    main()
