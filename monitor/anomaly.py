def detect_anomaly(previous_latency, current_latency):
    if previous_latency > 100 and current_latency > 100:
        return f"ALERT: Hight Latency detected ({current_latency} ms)"       
    return None