import os
import read_insta as m0
import read_inspect as m1

os.system('cls')

DATA_SOURCE = 1 # 0: Insta Data Download    1: Inspect element copy

followers = []
following = []

if DATA_SOURCE:
    print("Analyzing data from inspector")
    followers = m1.followers()
    following = m1.following()
else:
    print("Analyzing data from instagram")
    followers = m0.followers()
    following = m0.following()

# Verify followers/following count
print(f"Followers: {len(followers)}")
print(f"Following: {len(following)}\n")

# Print following that are not in followers
not_following_back = [user for user in following if user not in followers]
print(f"Found {len(not_following_back)} that don't follow you back:")

display = ""
while not(display in ["Y","y","N","n"]):
    display = input("Do you want to display the list? (Y/N): ")
if display in ['Y','y']:
    for user in not_following_back:
        print(user)