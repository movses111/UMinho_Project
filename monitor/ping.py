import subprocess

def ping_host(host, threshold):
    # asking only one ping
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)

    # checking ping
    if result.returncode == 0:
        ## Latency
        try:
            time_str = result.stdout.split("time=")[1].split(" ms")[0]
            latency = float(time_str)
        except IndexError:
            return False, 0

        ## if latency exceeds the limit, it is an anomaly!!!
        if latency > threshold:
            return False, latency  # the latecy exceeds the limit
        return True, latency  # latency is OK!
    else:
        return False, 0 # the device dont answere