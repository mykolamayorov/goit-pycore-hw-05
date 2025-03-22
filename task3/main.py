import sys
from collections import Counter

# Function to parse a log line and return a dictionary with components
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}


# Function to load logs from a file and parse each line
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"File {file_path} not found.")  # Handle file not found error
        sys.exit()
    except Exception as e:
        print(f"Error reading the file: {e}")  # Handle other exceptions
        sys.exit()
    return logs

# Function to filter logs by a specific level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]

# Function to count logs by logging level
def count_logs_by_level(logs: list) -> dict:
    level_counts = Counter(log["level"] for log in logs)
    return dict(level_counts)


# Function to display log counts in a readable table format
def display_log_counts(counts: dict):
    print(f"{'Log Level':<15}| {'Count'}")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{level:<15}| {count}")

# Main function to execute the script logic
def main():
    if len(sys.argv) < 2:
        print("Please provide the log file path.")  # Check if file path is provided
        sys.exit()

    log_file_path = sys.argv[1]  # Get the log file path from command line arguments
    
    # Load logs from the file
    logs = load_logs(log_file_path)

    # Count logs by level
    counts = count_logs_by_level(logs)
    
    # Display the log counts
    display_log_counts(counts)
    
    # If a log level is specified, filter logs by the level
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        logs = filter_logs_by_level(logs, level)

        # Display details of logs for the specified level
        print(f"\nLog details for level '{level}':")
        for log in logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    

if __name__ == "__main__":
    main()