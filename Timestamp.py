from datetime import datetime


def write_current_timestamp_to_file():
    """
    Writes the current timestamp to a file named 'timestamp.txt'.
    """
    # Get the current timestamp
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    file_name = "timestamp.txt"

    with open(file_name, 'w') as file:
        file.write(f"Current Timestamp: {current_timestamp}")

    print(f"Timestamp content {file_name}")


write_current_timestamp_to_file()



