from monitor.loader import load_devices
from monitor.ping import ping_host
from monitor.port_check import check_port
from monitor.logger import log
from monitor.anomaly import detect_anomaly

log("=" * 60, level="IFNO")
log("Monitoring Session Started", level="INFO")
log("=" * 60, level="INFO")

devices = load_devices()

log(
    f"Loaded {len(devices)} devices",
    level="INFO"
)

previous_latencies = {} # save previous latencies

for device in devices:
    log("." * 40, level="INFO")
    
    alias = device["alias"]
    ip = device["ip"]
    threshold = device["latency_threshold"]

    log(
        f"Checking {alias} ({ip})",
        level="INFO"
    )

    is_alive, current_latency = ping_host(
        ip,
        threshold
    )

    if is_alive:

        log(
            f"Device {alias} "
            f"{ip} responded in "
            f"{current_latency} ms",
            level="INFO"
        )

        # finding anomalies
        if ip in previous_latencies:

            anomaly = detect_anomaly(
                previous_latencies[ip],
                current_latency
            )

            if anomaly:

                log(
                    anomaly,
                    level="WARNING"
                )
                
        previous_latencies[ip] = current_latency # save the previous latencies in list
        
    else:
        
        log(
            f"{alias} ({ip}) is down",
            level="ERROR"
        )

    for port in[22, 80, 443]:
        
        status = check_port(ip, port)
        
        log(
            f"Port check "
            f"{alias} ({ip}) "
            f"port {port} -> "
            f"{'OPEN' if status else 'CLOSED'}",
            level="DEBUG"
        )

        log(
            "Monitoring cycle completed",
            level="INFO"
        )