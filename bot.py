import praw
import config
import time
import os

# Defines bot_login, which logs the bot into reddit with data sourced from config.py
def bot_login():
	print ""
	print "Logging in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Automatic Text Submission Replier v0.1")
	print ""
	print "Logged in at:"
	print time.time()
	print ""

	return r

def diagnostics():
	print "--------------------------------------------------"
	print ""
	print "Current reply template:"
	print ""
	print reply_text
	print ""
	print "--------------------------------------------------"
	print ""
	print "Current posts replied to:"
	print ""
	print posts_replied_to
	print ""

	return diagnostics

# Defines run_bot, which performs submission scanning and replying
def run_bot(r, posts_replied_to):
	print "--------------------------------------------------"
	print ""
	print "Scanning 10 submissions at:"
	print time.time()
	print ""
	
	# Scans 10 newest submissions in the subreddit given in config.py for blacklisted words and adds submission.id to posts_replied_to
	for submission in r.subreddit(config.subreddit).new(limit=10):
		for i in blacklist:
			if i in submission.title and submission.id not in posts_replied_to and submission.author != r.user.me():
				print "String with blacklisted words found in submission title. ID: " + submission.id
				
				posts_replied_to.append(submission.id)
				
				with open ("posts_replied_to.txt", "a") as f:
					f.write(submission.id + "\n")	
				
				print "Added submission ID to posts_replied_to.txt. ID: " + submission.id
				print time.time()
				print ""
	
	# Scans 10 newest submissions in the subreddit given in config.py for keywords and replies to the submission and adds submission.id to posts_replied_to
	for submission in r.subreddit(config.subreddit).new(limit=10):
		for i in keywords:
			if i in submission.title and submission.id not in posts_replied_to and submission.author != r.user.me():
				print "String with \"request\" found in submission title. ID: " + submission.id
				submission.reply(reply_text)
				print "Replied to submission ID: " + submission.id
				
				posts_replied_to.append(submission.id)
				
				with open ("posts_replied_to.txt", "a") as f:
					f.write(submission.id + "\n")	
				
				print "Added submission ID to posts_replied_to.txt. ID: " + submission.id
				print time.time()
				print ""
		
	#Notifies completion of operations
	print ""
	print "Operations complete at:"
	print time.time()
	print ""

	#Sleeps to prevent server overloading and to space replies
	print "Sleeping..."
	time.sleep(config.sleep_time)

# Defines get_saved_posts, which extracts threads which have already been posted to, source from posts_replied_to.txt
def get_saved_posts():
	if not os.path.isfile("posts_replied_to.txt"):
		posts_replied_to = []
	else:
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = filter(None, posts_replied_to)

	return posts_replied_to

# Defines reply_template, which is the template for the reply comment, sourced from reply_text.txt
def reply_template():
	if not os.path.isfile("reply_text.txt"):
		reply_text = []
	else:
		with open("reply_text.txt", "r") as f:
			reply_text = f.read()
			reply_text = reply_text
			reply_text = filter(None, reply_text)

	return reply_text

r = bot_login()
posts_replied_to = get_saved_posts()
reply_text = reply_template()
ts = time.time()
diagnostics = diagnostics()
keywords = {'keyword1', 'keyword2', 'keyword3'}
blacklist = {'keyword1', 'keyword2', 'keyword3'}

# Loops refreshing posts_replied_to and run_bot
while True:
	posts_replied_to = get_saved_posts()
	run_bot(r, posts_replied_to)