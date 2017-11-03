# Reddit Automatic Text Submission Replier

Created by: ColonialDagger

The Reddit Automatic Text Submission Replier bot is a reddit bot that automatically parses and posts a given comment when certain keywords are present in the title of the 10 newest submissions in a given subreddit. This bot runs on Python 2.7 and is currently incomaptible with any version of Python 3.

---

## Prerequisites

This bot runs on Python 2.7. Before installing Python 2.7, install the required packages:

	$ sudo apt-get update

	$ sudo apt-get install build-essential checkinstall

	$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Download the most recent version of Python 2.7, replacing XXX with the most recent version of Python 2.7
(most recent version of Python 2.7 is 14 as of Nov 3 2017):

	$ cd /usr/src

	$ sudo wget https://www.python.org/ftp/python/2.7.XXX/Python-2.7.XXX.tgz

Extract the downloaded package with:

	$ sudo tar xzf Python-2.7.13.tgz

Compile the Python 2.7 source code on your system using altinstall (make altinstall is used to prevent replacing the default python binary file /usr/bin/python.):

	$ cd Python-2.7.13

	$ sudo ./configure

	$ sudo make altinstall

Check the latest version installed of Python:

	$ python2.7 -V

This bot also needs PRAW: The Python Reddit API Wrapper. Install PRAW:

	$ pip install praw

---

# Installation and Configuration

1. Install the bot by extracting all files to a directory of your choice.

2. Create an addon on www.reddit.com/prefs/apps while logged in to your bot account.

3. Configure config.py:

	A. Input your account username in quotes:
	
		username = "username_goes_here"
		
	B. Input your account password in quotes:
	
		password = "password_goes_here"
		
	C. Input your addon's client_id in quotes:
	
		client_id = "client_id_goes_here"
		
	D. Input your addon's client_secret in quotes:
	
		client_secret = "client_secret_token_goes_here"
		
	E. Input the subreddit you want your bot to operate on in apostrophes:
	
		subreddit = 'subreddit_goes_here'
		
	F. Input the time you want your bot to rest between cycles:
	
		sleep_time = number_in_seconds_goes_here
		
4. Input your comment into reply_text.txt, including all notations and formatting marks.

5. Configure bot.py.

	A. On line 117, input various whitelisted keywords in submission titles that you want to reply to. This input is case-sensitive.
	   
		keywords = {'keyword1', 'keyword2', 'keyword3'}
		
	B. On line 118, input various blacklisted keywords in submission titles that you do not want to reply to, regardless of whitelisted keywords detected in the submission's title. This input is case-sensitive.
	   
		blacklist = {'keyword1', 'keyword2', 'keyword3'}

---

# Usage

Run the bot using:

> python [directory-path]/bot.py

Stop the bot using CTRL+C.

---

# Licensing

This project is licensed under the MIT License - see the LICENSE.txt file for details.
