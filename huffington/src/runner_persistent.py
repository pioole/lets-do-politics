import os
os.environ["DJANGO_SETTINGS_MODULE"] = "djangoormsettings"  # this must be done before importing any django modules

import django
django.setup()

import requests
import time
from src.models import Comment

SCRAP_ROUNDS = 400
ACCESS_TOKEN = 'EAACEdEose0cBAFwZADhBhqsZBcrl4gTieARKMjZAVUrZAcu4KuxNmQ0lZB9JQcCz8cOqbis48uvugjyOiTQgnSxlFGJUHl8AISM8TapiovWRLfF1c57Jbe2DzOTYqWEZAAX4W7C4eo8Xi5dRZC5bwvyOdZBLHedCxRxRvfkqZCLc3SgZDZD'


r = requests.get('https://graph.facebook.com/HuffingtonPost/posts', params={'access_token': ACCESS_TOKEN})

trumps = 0
hillarys = 0
posts = 0
comments = 0
dates = set()


def archive_comment(msg, date, author, id):
    global trumps, hillarys
    if 'hilary' in msg.lower():
        hillarys += 1
        dates.add(date)
    if 'trump' in msg.lower():
        trumps += 1
        dates.add(date)
    date_parsed = time.strptime(date, '%Y-%m-%dT%H:%M:%S+0000')
    comment = Comment(author=author, text=msg, date=time.strftime('%Y-%m-%d', date_parsed), fb_graph_api_id=id)
    comment.save()



def scrap_post(post):
    global posts, comments
    posts += 1
    try:
        comments_list = post['comments']['data']
        for comment in comments_list:
            comments += 1
            msg = comment['message']
            archive_comment(msg, comment['created_time'], comment['from']['name'], comment['id'])
    except KeyError:
        print 'no comments'


try:
    for x in range(0, SCRAP_ROUNDS):
        for post in r.json()['data']:
            scrap_post(post)
        print 'iter: {} min: {} max: {} trumps: {} hillarys: {} comments: {} posts: {}'.format(x, min(dates), max(dates), trumps, hillarys, comments, posts)
        url = r.json()['paging']['next']
        r = requests.get(url, params={'access_token': ACCESS_TOKEN})
except KeyError:
    print 'min: {} max: {} trumps: {} hillarys: {} comments: {} posts: {}'.format(min(dates), max(dates), trumps, hillarys, comments, posts)




