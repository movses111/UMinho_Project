def detect_anomaly(previous, current):
    if previous == "UDP" and current == "DOWN":
        return "ALERT: Host went DOWN"
        
        if previous == "OPEN" and current == "CLOSED":
            return "ALERT: Port closed"

            return None