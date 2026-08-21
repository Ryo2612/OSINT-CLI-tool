
import sys
import socket

from modules.dns_lookup import get_dns_records
from modules.http_info import get_http_info 
from modules.ip_info import get_ip_info
if len(sys.argv) != 2:
    print("Usage: python3 src/osint.py <domain>")
    sys.exit(1)

target = sys.argv[1]

print("Target:", target)

try:
    ip_address = socket.gethostbyname(target)
    print("IP Address:", ip_address)
    ip_data = get_ip_info(ip_address)
    if ip_data:
            print("\nIP Information")
            print("-------------------------")
            print("IP:", ip_data.get("ip"))
            print("ASN:", ip_data.get("asn"))
            print("Organisation:", ip_data.get("as_name"))
            print("Country:", ip_data.get("country"))
except socket.gaierror:
    print("Could not resolve domain.")

print("\nMX Records:")
mx_records = get_dns_records(target, "MX")

for record in mx_records:
    print(record)

print("\nNS Records:")
ns_records = get_dns_records(target, "NS")

for record in ns_records:
    print(record)

print("\nTXT Records:")
txt_records = get_dns_records(target, "TXT")

for record in txt_records:
    print(record)

print("\nAAAA Records:")
aaaa_records = get_dns_records(target, "AAAA")

for record in aaaa_records:
    print(record)

print("\nHTTP status:")
get_http_info(target)
