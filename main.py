import json
from monitor.ping import ping_host
from monitor.port_check import check_port
from monitor.logger import log
from monitor.anomaly import detect_anomaly

print("=== Network Monitoring System ===")

with open("assets/devices.json") as f:
    devices = json.load(f)

print(f"Loaded {len(devices)} devices.\n")

previous_latencies = {} # save previous latencies

for device in devices:

    alias = device["alias"]
    ip = device["ip"]
    threshold = device["latency_threshold"]

    print(f"Checking {alias} ({ip})")

    is_alive, current_latency = ping_host(ip, threshold)
    if is_alive:
        print("Ping: OK! Latency: {current_latency} ms")
        log(f"{alias} ({ip}) is alive")

        # finding anomalies
        if ip in previous_latencies:
            anomaly = detect_anomaly(previous_latencies[ip], current_latency)
            if anomaly:
                print(anomaly)
                log(anomaly)
        previous_latencies[ip] = current_latency # save the previous latencies in list


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
