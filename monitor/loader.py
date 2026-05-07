import json
import os
import ipaddress

from monitor.logger import log

CONFIG_PATH = "assets/devices.json"

REQUIRED_FIELDS = [
    "id",
    "alias",
    "ip",
    "check_interval",
    "latency_threshold"
]


def is_valid_ip(ip):

    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False


def load_devices():

    if not os.path.exists(CONFIG_PATH):

        log(
            "devices.json file not found",
            level="ERROR"
        )

        return []

    try:

        with open(CONFIG_PATH) as f:
            devices = json.load(f)

    except json.JSONDecodeError:

        log(
            "Invalid JSON format",
            level="ERROR"
        )

        return []

    validated_devices = []

    for device in devices:

        missing_fields = []

        for field in REQUIRED_FIELDS:
        
            if field not in device:
                missing_fields.append(field)
        
        if missing_fields:

            log(
                f"Device missing fields: "
                f"{missing_fields}",
                level="WARNING"
            )
        
            continue

        if not is_valid_ip(device["ip"]):

            log(
                f"Invalid IP address: "
                f"{device['ip']}",
                level="WARINIG"
            )
        
            continue

        validated_devices.append(device)

    log(
        f"Validated {len(validated_devices)} devices",
        level="INFO"
    )

    return validated_devices
