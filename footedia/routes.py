from footedia import footedia
from flask import render_template
from flask import request
import os
import praw
from prawcore import (Authorizer, DeviceIDAuthorizer, ReadOnlyAuthorizer,
                      Redirect, Requestor, ScriptAuthorizer,
                      TrustedAuthenticator, UntrustedAuthenticator, session)


@footedia.route('/')
@footedia.route('/index')
def index():
    title = "Footedia!"
    return render_template('index.html', title=title)

@footedia.route('/playerdetail')
def playerdetail():
    playername = request.args.get('player')
    reddit_username = os.getenv('reddit_username_first')
    reddit_pw = os.getenv('reddit_pw_first')
    reddit = praw.Reddit(client_id='eTSh9ULVWNEcYA',
                         client_secret='9FmmnV1eIkSzgcKMe3EzZDSC7YE',
                         password=reddit_pw,
                         user_agent='sample_user_agent',
                         username=reddit_username)
    subreddit = reddit.subreddit('soccer')
    player_submissions = []
    for submission in subreddit.top(limit=200):
        if submission.title.find(playername) == -1:
            continue

        player_submissions.append(submission)

    return render_template('get_playerdetails.html', player_submissions=player_submissions)






