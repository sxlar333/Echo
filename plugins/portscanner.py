import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-ALT",
    9000: "Custom"
}


def scan_port(host, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        s.connect((host, port))
        return port
    except:
        return None
    finally:
        s.close()


def port_scan(host, ports):
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(host, p), ports)

    for result in results:
        if result:
            open_ports.append(result)

    return open_ports


def main():
    print("Simple Port Scanner\n")

    host = input("Target IP / Hostname: ").strip()

    port_input = input(
        "Ports (e.g. 22,80,443 or press Enter for common ports): "
    ).strip()

    if port_input:
        ports = [int(p) for p in port_input.split(",") if p.isdigit()]
    else:
        ports = list(COMMON_PORTS.keys())

    print("\nScanning...\n")

    open_ports = port_scan(host, ports)

    if not open_ports:
        print("No open ports found")
        return

    print("Open ports:")
    for port in open_ports:
        service = COMMON_PORTS.get(port, "Unknown")
        print(f"  {port}/tcp  {service}")


if __name__ == "__main__":
    main()
