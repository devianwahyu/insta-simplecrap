from instagramy import InstagramUser
from prettytable import PrettyTable

username = input("\nEnter username: ")
session_id = input("Session id (optional): ")

user = InstagramUser(username, from_cache=True)

print("\nReturn:\n")

table = PrettyTable(["Username", user.username])

table.align = 'l'

table.add_row(["Fullname", user.fullname])
table.add_row(["Followers", user.number_of_followers])
table.add_row(["Followings", user.number_of_followings])
table.add_row(["Biography", user.biography])
table.add_row(["Verified", user.is_verified])
table.add_row(["Total Post", user.number_of_posts])
table.add_row(["Private", user.is_private])
table.add_row(["Website", user.website])

print(table)

post_table = PrettyTable(["Time", "Likes", "Comments", "Caption", "Url"])
post_table.align = 'l'

for p in user.posts:
    post_table.add_row([p.timestamp, p.likes, p.comments, p.caption, p.post_url])

print("This table only shown if user is not private")
print(post_table)