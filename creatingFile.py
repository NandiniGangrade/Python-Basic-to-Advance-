import os
from datetime import datetime
import time

def create_test_file(directory_path):
    # Create a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # file_name = f"pythonDemo{timestamp}.py"
    file_name = input(f"Enter the File name :- ")
    file_path = os.path.join(directory_path, file_name)

    # Write some content to the file
    with open(file_path, 'w') as file:
        file.write("This is a test file.\n")

    print(f"New file '{file_name}' \ncreated at {datetime.now().strftime('%Y-%m-%d Current Time :-  %H:%M:%S')}")

# Replace '/path/to/your/directory' with the actual path to your directory
directory_to_monitor = 'C:/Users/Dell/PycharmProjects/pythonProject4'

# Create a test file in the specified directory
create_test_file(directory_to_monitor)
