from collections import defaultdict
import time

FAILED_ATTEMPTS = defaultdict(list)

THRESHOLD = 5        # attempts
WINDOW = 60          # seconds

def log_attempt(ip, success):
    now = time.time()
    
    if not success:
        FAILED_ATTEMPTS[ip].append(now)

    # Remove old attempts
    FAILED_ATTEMPTS[ip] = [
        t for t in FAILED_ATTEMPTS[ip] if now - t < WINDOW
    ]

    return detect_attack(ip)

def detect_attack(ip):
    if len(FAILED_ATTEMPTS[ip]) >= THRESHOLD:
        return True
    return False
