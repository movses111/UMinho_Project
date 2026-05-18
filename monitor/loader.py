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

    except FileNotFoundError:

        log(
            "Configuration file missing",
            level="ERROR"
        )

        return [] 

    except json.JSONDecodeError as error:

        log(
            "Invalid JSON format: {error}",
            level="ERROR"
        )

        return []
    
    except PermissionError:

        log(
            "Permission denied while "
            "reading devices.json",
            level="ERROR"
        )

        return []
    
    except Exception as error:

        log(
            f"Unexpected loader error: "
            f"{error}",
            level="ERROR"
        )

        return []


    validated_devices = []

    for device in devices:

        try:

            if validate_device(device):
                validated_devices.append(device)

        except KeyError as error:

            log(
                f"Missing device ket: "
                f"{error}",
                level="WARNING"
            )

        except Exception as error:

            log(
                f"Device validation error: "
                f"{error}",
                level="WARNING"
            )
            
    log(
        f"Validated "
        f"{len(validated_devices)} devices",
        level="INFO"
    )

    return validated_devices
