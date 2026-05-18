import os

from datetime import datetime

LOG_LEVEL_STDOUT = True
LOG_LEVEL_FILE = True

LOG_FILE_PATH = "logs/app.log"


def get_timestamp():

    return (
        datetime.utcnow()
        .isoformat() + "Z"
    )


def log(message, level="INFO"):

    timestamp = get_timestamp()

    formatted_message = (
        f"{timestamp} "
        f"[{level}] "
        f"{message}"
    )
    # console output
    if LOG_LEVEL_STDOUT:
        print(formatted_message)

    # file output
    if LOG_LEVEL_FILE:

        os.makedirs(
            "logs",
            exist_ok=True
        )

        try:

            with open(LOG_FILE_PATH, "a") as f:
                f.write(
                    formatted_message + "\n"
                )

        except OSError as error:

            print(
                f"[LOGGER ERROR] "
                f"{error}"
            )