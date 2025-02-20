import os

# Get the absolute path of the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

# Construct the full path to the text file
file_path = os.path.join(script_dir, 'API_KEY.txt')
print(file_path)

# Open the file and read its content
with open(file_path, 'r') as file:
    content = file.read().strip()  # .strip() removes any extra whitespace/newlines

print(content)
