# utils/colors.py — Terminal Colors by Faizan™
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

    @staticmethod
    def success(msg):
        return f"{Colors.OKGREEN}[+] {msg}{Colors.ENDC}"

    @staticmethod
    def info(msg):
        return f"{Colors.OKCYAN}[~] {msg}{Colors.ENDC}"

    @staticmethod
    def warning(msg):
        return f"{Colors.WARNING}[!] {msg}{Colors.ENDC}"

    @staticmethod
    def error(msg):
        return f"{Colors.FAIL}[X] {msg}{Colors.ENDC}"
