import os

file_path = './hero_data.db'

try:
    os.remove(file_path)
    print(f"Successfully deleted {file_path}")
except Exception as e:
    print(f"Error occurred while deleting {file_path}: {e}")