import os
from dotenv import load_dotenv

load_dotenv()

FAILURE_THRESHOLD = int(os.getenv("FAILURE_THRESHOLD", 5))
TIME_WINDOW_SECONDS = int(os.getenv("TIME_WINDOW_SECONDS", 60))
BLOCK_DURATION_SECONDS = int(os.getenv("BLOCK_DURATION_SECONDS", 300))
CREDENTIAL_STUFFING_THRESHOLD = int(os.getenv("CREDENTIAL_STUFFING_THRESHOLD", 5))
LOG_FILE = os.getenv("LOG_FILE", "logs/authguard.log")
