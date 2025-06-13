def validate_ip(ip):
    parts = ip.split(".")
    return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
