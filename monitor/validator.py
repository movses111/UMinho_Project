import ipaddress


from monitor.logger import log

REQUIRED_FIELDS = [
    "id",
    "alias",
    "ip",
    "check_interval",
    "latency_threshold"
]


def validate_required_fields(device):

    missing_fields = []

    for field in REQUIRED_FIELDS:

        if field not in device:
            missing_fields.append(field)

    if missing_fields:
        
        log(
            f"Missing required fields: {missing_fields}",
            level="WARNING"
        )
        return False
    
    return True


def validate_ip(ip):

    try:
        ipaddress.ip_address(ip)
        return True
    
    except ValueError:

        log(
            f"Invalid IP address: {ip}",
            level="WARNING"
        )

        return False
    

def validate_numeric_fields(device):

    numeric_fields = [
        "check_interval",
        "latency_threshold"
    ]

    for field in numeric_fields:

        if not isinstance(device[field], int):

            log(
                f"{field} must be integer",
                level="WARNING"
            )

            return False
        
    return True


def validate_device(device):

    return all([
        validate_required_fields(device),
        validate_ip(device["ip"]),
        validate_numeric_fields(device)
    ])