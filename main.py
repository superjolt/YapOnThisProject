import scratchattach as sa
import os
from dotenv import load_dotenv
import random

load_dotenv()

SESSION_ID = os.getenv("SESSION_ID") or (print("SESSION_ID is MISSING!")) or exit(1)
PROJECT_ID = "1193902598"

session = sa.login_by_id(SESSION_ID, username="superjolt")
project = session.connect_project(PROJECT_ID)
cloud = session.connect_cloud(PROJECT_ID)
client = cloud.requests()

@client.request
def get_comment():
    print(f"\nRecieved comment request from {client.get_requester()}")
    comments = list(project.comments())
    if comments:
        comment = random.choice(comments)
        print(f"\nSelected comment: {comment.content}, by {comment.author_name}")
        return [comment.author_name, comment.content]
    else:
        print("No comments found.")
        return ["error", "No comments found! Comment something!"]

@client.event
def on_ready():
    print("Request handler is running") 

client.start(thread=True)

if __name__ == "__main__":
    while True:
        # your entire script logic goes here
        pass