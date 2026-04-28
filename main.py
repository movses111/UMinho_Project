from monitor.ping import ping_host
from monitor.port_check import check_port
from monitor.logger import log

host = input("Enter IP: ")

if ping_host(host):
    print("Ping: OK!")
    log(f"{host} is alive!")
else:
    print("Ping: FAILED!")
    log(f"{host} is down!")

for port in [22, 80, 443]:
    status = check_port(host, port)
    print(f"Port {port}: {'OPEN' if status else 'CLOSED'}")
    log(f"{host}:{port} -> {'OPEN' if status else 'CLOSED'}")

