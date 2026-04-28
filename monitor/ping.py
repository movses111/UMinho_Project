import subprocess

def ping_host(host):
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True)
    return result.returncode == 0