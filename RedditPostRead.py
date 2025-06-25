import praw

# Set up Reddit API client (replace values with your own)
reddit = praw.Reddit(
    client_id="YNWHsRhGN56JVQ-nb8Hbow",
    client_secret="yeBhVTuAfW6zmgqLFebIZHdr3HTwbA",
    user_agent="testscript by /u/False_Use_2621"
)

# URL of a Reddit post (can be any public post)
url = "https://www.reddit.com/r/learnprogramming/comments/1lgnh60/what_have_you_been_working_on_recently_june_21/"
submission = reddit.submission(url=url)

print("Title:", submission.title)
print("Score:", submission.score)
print("Author:", submission.author)
print("Text:", submission.selftext)

print("\nTop 5 comments:")
submission.comments.replace_more(limit=0)
for comment in submission.comments[:5]:
    print(f"- {comment.body[:100]}")
