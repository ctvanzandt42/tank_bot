from info import bot
from info import me

subreddit = bot.subreddit('memphisgrizzlies')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    author = comment.author
    if 'tank' in text.lower():
        if author is me:
            message = "*TANK COMMANDER u/{0}!!!!!!!* ^Beep ^^Boop".format(author)

            comment.reply(message)
