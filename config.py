import os

# Load token from file
def get_token():
    with open('token.txt', 'r') as f:
        return f.read().strip()

TOKEN = get_token()
PREFIX = '$'
OFFICIAL_ROLE_ID = 1502826407926169790  # Replace with your actual role ID
