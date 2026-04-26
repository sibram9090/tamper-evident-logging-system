# tamper-evident-logging-system
A Python-based tamper-evident logging system using SHA-256 hash chaining.
# Tamper-Evident Logging System

A Python-based cybersecurity project that ensures log integrity using SHA-256 hash chaining.

## Features
- Secure log creation
- SHA-256 hash generation
- Hash chaining between log entries
- Tamper detection and integrity verification

## Technologies Used
- Python 3
- hashlib
- JSON

## How It Works
Each log entry contains:
- Timestamp
- Event type
- Description
- Previous log hash
- Current log hash

If any log entry is modified, the system immediately detects the change during verification.

## Usage
1. Run the script:
   python task1_logging.py

2. Choose an option:
   - Add Log
   - Verify Logs
   - Exit

## Sample Use Cases
- Security event logging
- Audit trail protection
- Forensic evidence integrity
- SOC analyst training

## Author
Sibr<img width="825" height="328" alt="Tamper" src="https://github.com/user-attachments/assets/41b71a7b-994c-40ff-a2ad-2686d071dffa" />

am
