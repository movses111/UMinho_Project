from monitor.loader import load_devices
from monitor.ping import ping_host
from monitor.port_check import check_port
from monitor.logger import log
from monitor.anomaly import detect_anomaly

log("System initialized", level="INFO")

devices = load_devices()

log(
    f"Loaded {len(devices)} devices",
    level="INFO"
)

previous_latencies = {} # save previous latencies

for device in devices:
    
    alias = device["alias"]
    ip = device["ip"]
    threshold = device["latency_threshold"]

    log(
        f"Checking {alias} ({ip})",
        level="INFO"
    )

    is_alive, current_latency = ping_host(ip, threshold)
    if is_alive:
        print(f"Ping: OK! Latency: {current_latency} ms")
        log(f"{alias} ({ip}) is alive", level="INFO")

        # finding anomalies
        if ip in previous_latencies:
            anomaly = detect_anomaly(previous_latencies[ip], current_latency)
            if anomaly:
                print(anomaly)
                log(anomaly)
        previous_latencies[ip] = current_latency # save the previous latencies in list


    else:

        print("Ping: FAILED!")
        log(
            f"{alias} ({ip}) is down",
            level="ERROR"
        )

    for port in[22, 80, 443]:
        
        status = check_port(ip, port)
        
        log(
            f"{alias} ({ip}) port {port} -> "
            f"{'OPEN' if status else 'CLOSED'}",
            level="DEBUG"
            )
            