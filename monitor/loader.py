import json
import os


from monitor.logger import log
from monitor.validator import validate_device

CONFIG_PATH = "assets/devices.json"


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

        if validate_device(device):
            validated_devices.append(device)
            
    log(
        f"Validated {len(validated_devices)} devices",
        level="INFO"
    )

    return validated_devices
