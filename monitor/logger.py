import os

from datetime import datetime

LOG_LEVEL_STDOUT = True
LOG_LEVEL_FILE = True

LOG_FILE_PATH = "logs/app.log"


def get_timestamp():

    return (
        datetime.utcnow()
        .replace(microsecond=0)
        .isoformat() + "Z"
    )


def format_log(level, message):

    return (
        f"{get_timestamp()} "
        f"[{level}] "
        f"{message}"
    )
    

def write_to_file(message):
        
        os.makedirs(
            "logs",
            exist_ok=True
        )

        try:

            with open(LOG_FILE_PATH, "a") as file:
                
                file.write(message + "\n")

        except OSError as error:

            print(
                f"[LOGGER ERROR] "
                f"{error}"
            )


def log(message, level="INFO"):

    formatted_message = format_log(
        level,
        message
    )

    if LOG_LEVEL_STDOUT:
        print(formatted_message)

    if LOG_LEVEL_FILE:
        write_to_file(formatted_message)