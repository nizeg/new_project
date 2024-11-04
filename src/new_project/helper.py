import os
from dotenv import load_dotenv

def load_env():
    """
    Load environment variables from a .env file into the system environment.
    This function uses the python-dotenv library to read a .env file located 
    in the project root directory.
    """
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print("Environment variables loaded successfully.")
    else:
        print("No .env file found. Ensure your environment variables are set properly.")

# Example of usage
load_env()
