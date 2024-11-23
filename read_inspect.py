import re

# Updated pattern for href="/username/"
pattern = r'href="/([^"]+)/"'

# Read the raw HTML files
followers_raw = ""
following_raw = ""

with open("Inspect/followers.txt", "r", encoding="utf-8") as file:
    followers_raw = file.read()
with open("Inspect/following.txt", "r", encoding="utf-8") as file:
    following_raw = file.read()

# Extract unique href content using the updated pattern
def followers():
    return list(set(re.findall(pattern, followers_raw)))

def following():
    return list(set(re.findall(pattern, following_raw)))