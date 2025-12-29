import re
from collections import defaultdict

THRESHOLD = 3

def analyze_log(file_path):
    failed_attempts = defaultdict(int)

    with open(file_path, "r") as file:
        for line in file:
            match = re.search(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

    return failed_attempts

def main():
    log_path = "logs/auth.log"
    results = analyze_log(log_path)

    print(" Failed Login Attempts by IP:\n")
    for ip, count in results.items():
        print(f"{ip} -> {count} attempts")

    print("\n Suspicious IPs:")
    for ip, count in results.items():
        if count >= THRESHOLD:
            print(f"{ip} ( {count} failed attempts )")

if __name__ == "__main__":
    main()
