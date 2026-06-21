# AuthGuard – Login Attack Detection Service

AuthGuard is a lightweight backend service built with Flask, designed to detect and respond to suspicious login activity such as brute-force attacks and credential stuffing. It uses time-windowed tracking and IP-based analysis to identify abnormal behavior in authentication flows.

This project is intended as a practical demonstration of detection engineering concepts and secure application design.

---

## Overview

Authentication endpoints are a common target for automated attacks. AuthGuard introduces a simple detection layer that monitors failed login attempts and flags potentially malicious activity based on frequency and timing patterns.

The system is intentionally minimal and focuses on clarity of logic rather than production-scale infrastructure.

---

## Features

- Detects brute-force attempts using configurable thresholds
- Tracks failed login attempts per IP address
- Applies time-window-based analysis for anomaly detection
- Returns alerts when suspicious behavior is identified
- Modular detection logic for easy extension

---

## Architecture

The application is composed of two main components:

- `app.py` – Handles HTTP requests and simulates an authentication endpoint
- `detector.py` – Implements detection logic for tracking and flagging suspicious activity

All detection is performed in-memory for simplicity.

---

## How It Works

1. Each login attempt is recorded along with the originating IP address
2. Failed attempts are tracked within a defined time window
3. If the number of failed attempts exceeds a threshold, the IP is flagged
4. Flagged requests receive a blocked response

This approach mimics basic rate-limiting and behavioral detection strategies used in real systems.

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

## Running the Application

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Example Request

Send a login request using cURL:

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username":"admin","password":"incorrect"}'
```

### Example Response

```json
{
  "success": false
}
```

After repeated failed login attempts exceeding the configured threshold, the service will return:

```json
{
  "alert": "Brute-force detected"
}
```
