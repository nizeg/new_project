import sys
import os

# Function to load environment variables
# helper.py

import os

def load_env(env_file='/Users/nize/Documents/Coding/new_project/.env'):
    print("Inside load_env function")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Checking if {env_file} exists: {os.path.exists(env_file)}")

    if os.path.exists(env_file):
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        try:
                            key, value = line.split('=', 1)
                            os.environ[key.strip()] = value.strip()
                        except ValueError:
                            print(f"Skipping malformed line: {line}")
            print("Environment variables loaded.")
        except Exception as e:
            print(f"Error loading environment file: {str(e)}")
    else:
        print(f"{env_file} file not found.")

# Example usage
load_env()
