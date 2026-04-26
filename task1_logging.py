import hashlib
import json
import time

log_file = "logs.json"

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def load_logs():
    try:
        with open(log_file, "r") as f:
            return json.load(f)
    except:
        return []

def save_logs(logs):
    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

def add_log(event_type, description):
    logs = load_logs()
    timestamp = str(time.time())
    prev_hash = logs[-1]["hash"] if logs else "0"

    data = timestamp + event_type + description + prev_hash
    current_hash = calculate_hash(data)

    log_entry = {
        "timestamp": timestamp,
        "event_type": event_type,
        "description": description,
        "prev_hash": prev_hash,
        "hash": current_hash
    }

    logs.append(log_entry)
    save_logs(logs)
    print("✅ Log added successfully!")

def verify_logs():
    logs = load_logs()

    if not logs:
        print("⚠️ No logs found.")
        return

    for i in range(len(logs)):
        curr = logs[i]

        expected_prev_hash = "0" if i == 0 else logs[i-1]["hash"]

        if curr["prev_hash"] != expected_prev_hash:
            print(f"❌ Tampering detected at log {i+1}: Chain broken!")
            return

        data = curr["timestamp"] + curr["event_type"] + curr["description"] + curr["prev_hash"]
        recalculated_hash = calculate_hash(data)

        if curr["hash"] != recalculated_hash:
            print(f"❌ Data modified at log {i+1}!")
            return

    print("✅ All logs are secure and intact!")

while True:
    print("\n=== Tamper-Evident Logging System ===")
    print("1. Add Log")
    print("2. Verify Logs")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event = input("Enter event type: ")
        description = input("Enter description: ")
        add_log(event, description)

    elif choice == "2":
        verify_logs()

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")