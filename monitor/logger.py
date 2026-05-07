from datetime import datetime

LOG_LEVEL_STDOUT = True
LOG_LEVEL_FILE = True

LOG_FILE_PATH = "logs/logs.txt"


def get_timestamp():
    return datetime.utcnow().isoformat() + "Z"


def log(message, level="INFO"):

    timestamp = get_timestamp()

    formatted_message = f"{timestamp} [{level}] {message}"

    # console output
    if LOG_LEVEL_STDOUT:
        print(formatted_message)

    # file output
    if LOG_LEVEL_FILE:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(formatted_message + "\n")