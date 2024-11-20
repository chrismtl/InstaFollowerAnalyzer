import requests

# Replace with your access token
ACCESS_TOKEN = 'your_access_token'
USER_ID = 'your_user_id'  # Replace with your Instagram User ID
BASE_URL = 'https://graph.facebook.com/v17.0'

def get_followers():
    url = f'{BASE_URL}/{USER_ID}/followers?access_token={ACCESS_TOKEN}'
    response = requests.get(url)
    followers_data = response.json()
    print("Response:")
    print(followers_data)
    followers = {user['username'] for user in followers_data['data']}
    return followers

def get_following():
    url = f'{BASE_URL}/{USER_ID}/following?access_token={ACCESS_TOKEN}'
    response = requests.get(url)
    following_data = response.json()
    following = {user['username'] for user in following_data['data']}
    return following

def calculate_percentage_not_following_back():
    followers = get_followers()
    following = get_following()
    not_following_back = following - followers
    percentage = (len(not_following_back) / len(following)) * 100
    return percentage

if __name__ == "__main__":
    percentage_not_following_back = calculate_percentage_not_following_back()
    print(f"Percentage of people not following you back: {percentage_not_following_back:.2f}%")
