import json

def read_credentials(file):
    with open(file) as f:
        data = json.load(f)
    return [(item['username'], item['password']) for item in data]
