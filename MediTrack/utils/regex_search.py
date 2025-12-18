import re

def search(pattern, data):
    regex = re.compile(pattern, re.IGNORECASE)
    return [d for d in data if regex.search(d)]
