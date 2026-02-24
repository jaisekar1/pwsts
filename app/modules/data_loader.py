
import pandas as pd
from scapy.all import rdpcap

def load_pcap(file):
    packets = rdpcap(file)
    data = []
    for pkt in packets:
        if pkt.haslayer("IP"):
            data.append([
                pkt["IP"].src,
                pkt["IP"].dst,
                len(pkt),
                pkt["IP"].proto
            ])
    return pd.DataFrame(data, columns=["Source", "Destination", "Length", "Protocol"])
