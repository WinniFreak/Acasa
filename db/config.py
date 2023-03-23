# Imports
import os
from pathlib import Path
import json

# Change the current working directory to the directory of the current script
os.chdir(Path(__file__).parent)

# Load config file
try:
    with open('config.json', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    print("Config file not found!")
    exit()

# Save DB file path in static variable
DB_FILE_PATH = config['DB_FILE_PATH']

