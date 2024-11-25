#!/usr/bin/python3
import urllib.request

# URL to fetch
url = "https://alu-intranet.hbtn.io/status"

# Open the URL and fetch the content
with urllib.request.urlopen(url) as response:
    body = response.read()

# Decode the response body to UTF-8 (if it's in bytes) and print it with the required format
print(f"Body response:\n\t- {body.decode('utf-8')}")

