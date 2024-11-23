# InstaFollowerAnalyzer
Tired of having loads of followers that don't follow you back? Get the list here

Steps:
There are two possible methods for doing this, you choose which one you prefer:

Method 0: Classic method, takes less than 10 minutes, involves more clicks but is simple
Method 1: Faster but more complex (you just have to search for the list in the tab inspector)

Method 0:
1. Go to instagram.com and login
2. Go to you profile
3. Click the settings icon (top-right)
4. Click on Privacy and Security
5. Go to the Meta Account Center
6. Go to your Data and autorisations
7. Click  Download your data
8. Choose your account
9. Click Select your info
10. On the Contact section choose Following and Followers and click next
11. Choose Download on device
12. Change the format from HTML to JSON
13. Change quality from Medium to Low

Once ready place the files followers(_1).json and following.json in the insta folder and simply run insta_stats.py

Method 1:
1. Go to instagram.com
2. Go to your followers list
3. Scroll down to the bottom of the list (VERY IMPORTANT)
4. Press f12
5. Click on the mouse icon top left of the inspect page to select an element of the page
6. Once clicked, click on the picture of a random user in your list of followers (This will lead you to the html element linked to the profile picture)
7. Pass your mouse on every element from bottom to top, starting from the profile pic element you just selected
8. Stop at the furthest element that selects the entire list of followers (find the div containing every followers)
9. Right click on the parent div -> Copy -> Copy elements inside
 This will copy the html code for all the followers being displayed, which includes their username.
 Now simply paste this code in Insta/followers.txt and do the same for the following list and run insta_stats.py
