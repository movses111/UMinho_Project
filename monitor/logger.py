def log(message):
    
    with open("logs/logs.txt", "a") as f:
        f.write(message + "\n")