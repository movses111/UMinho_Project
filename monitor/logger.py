def log(message):
    with open("logs.txt", "a") as f:
        f.write(message + "\n")