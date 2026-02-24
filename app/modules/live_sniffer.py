from scapy.all import sniff
import pandas as pd

captured_packets = []

def process_packet(pkt):
    if pkt.haslayer("IP"):
        packet_info = {
            "src_ip": pkt["IP"].src,
            "dst_ip": pkt["IP"].dst,
            "protocol": pkt["IP"].proto,
            "packet_length": len(pkt)
        }
        captured_packets.append(packet_info)

def start_sniffing(packet_count=100):
    sniff(prn=process_packet, count=packet_count)
    return pd.DataFrame(captured_packets)