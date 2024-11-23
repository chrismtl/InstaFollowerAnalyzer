import json
import os

# Paths to JSON files in Insta folder
insta_folder = "Insta"
followers_file = os.path.join(insta_folder, "followers.json")
following_file = os.path.join(insta_folder, "following.json")

# Load the JSON files
with open(followers_file, "r", encoding="utf-8") as f:
    insta_followers_data = json.load(f)
with open(following_file, "r", encoding="utf-8") as f:
    insta_following_data = json.load(f)

# Extract the "value" fields from the nested structure with error handling
def extract_followers_values(data):
    values = []
    for entry in data:
        # Access "string_list_data" list within each dictionary
        string_list = entry.get("string_list_data", [])
        for string_entry in string_list:
            # Extract the "value" field
            if "value" in string_entry:
                values.append(string_entry["value"])
    return values

def extract_following_values(data):
    values = []
    data = data.get("relationships_following", [])
    for entry in data:
        # Access "string_list_data" list within each dictionary
        string_list = entry.get("string_list_data", [])
        for string_entry in string_list:
            # Extract the "value" field
            if "value" in string_entry:
                values.append(string_entry["value"])
    return values


def followers():
    return extract_followers_values(insta_followers_data)

def following():
    return extract_following_values(insta_following_data)