import json
from monitor.ping import ping_host
from monitor.port_check import check_port
from monitor.logger import log

print("=== Network Monitoring System ===")

with open("assets/devices.json") as f:
    devices = json.load(f)

print(f"Loaded {len(devices)} devices.\n")

for device in devices:

    alias = device["alias"]
    ip = device["ip"]

    print(f"Checking {alias} ({ip})")

    if ping_host(ip):
        print("Ping: OK!")
        log(f"{alias} ({ip}) is alive")
    else:
        print("Ping: FAILED!")
        log(f"{alias} ({ip}) is down")

    for port in[22, 80, 443]:

        status = check_port(ip, port)

        print(f"Port {port}: {'OPEN' if status else 'CLOSED'}")

        log(
            f"{alias} ({ip}) port {port} -> "
            f"{'OPEN' if status else 'CLOSED'}"
        )

    print("-" * 40)
