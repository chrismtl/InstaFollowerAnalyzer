import os
import read_insta as m0
import read_inspect as m1
from datetime import datetime

# Clear the console (cross-platform)
os.system('cls' if os.name == 'nt' else 'clear')

# Data source selection
DATA_SOURCE = 0  # 0: Insta Data Download    1: Inspect element copy

followers = []
following = []

# Analyze data based on the selected source
if DATA_SOURCE:
    print("Analyzing data from inspector...")
    followers = m1.followers()
    following = m1.following()
else:
    print("Analyzing data from Instagram...")
    followers = m0.followers()
    following = m0.following()

# Verify followers/following count
print(f"\nFollowers: {len(followers)}")
print(f"Following: {len(following)}\n")

# Find and display users who don't follow you back
not_following_back = [user for user in following if user not in followers]
print(f"Found {len(not_following_back)} users who don't follow you back.")

# Prompt user to display the list
while True:
    display = input("Do you want to display the list? (Y/N): ").strip().upper()
    if display in ['Y', 'N']:
        break

if display == 'Y':
    print("\nUsers who don't follow you back:")
    for user in not_following_back:
        print(user)

# Prompt user to save the list to a file
while True:
    save = input("\nDo you want to save the list to a file? (Y/N): ").strip().upper()
    if save in ['Y', 'N']:
        break

if save == 'Y':
    # Create Results folder if it doesn't exist
    results_folder = "Results"
    os.makedirs(results_folder, exist_ok=True)

    # Generate filename with current date
    current_date = datetime.now().strftime("%d-%m-%y")
    filename = os.path.join(results_folder, f"no-follow-back-{current_date}.txt")

    # Save the list to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Users who don't follow you back:\n")
        for user in not_following_back:
            file.write(f"{user}\n")

    print(f"\nThe list has been saved to {filename}.")
