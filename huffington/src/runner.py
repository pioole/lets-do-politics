# python3
import requests

SCRAP_ROUNDS = 400
ACCESS_TOKEN = 'EAACEdEose0cBAF6ehmh1XBl2uZChtnTTziDzWZCMZBkYzD36VR1gZAOwgDQyzZCPgEnIbg9EW7q3Uh12NI0oXu4HA6tE5S8UKkYZAr9c08Y3eHGFgSrDM7eCLIYHnD0pCQMODQJZAlqsHPX19NzJRdTWVmv4TA38WgUK0o5U7CWnwZDZD'


r = requests.get('https://graph.facebook.com/HuffingtonPost/posts', params={'access_token': ACCESS_TOKEN})

trumps = 0
hillarys = 0
posts = 0
comments = 0
dates = set()


def archive_comment(msg, date):
    global trumps, hillarys
    if 'hilary' in msg.lower():
        hillarys += 1
        dates.add(date)
    if 'trump' in msg.lower():
        trumps += 1
        dates.add(date)


def scrap_post(post):
    global posts, comments
    posts += 1
    try:
        comments_list = post['comments']['data']
        for comment in comments_list:
            comments += 1
            msg = comment['message']
            archive_comment(msg, comment['created_time'])
    except KeyError:
        print('no comments')


try:
    for x in range(0, SCRAP_ROUNDS):
        for post in r.json()['data']:
            scrap_post(post)
        print('iter: {} min: {} max: {} trumps: {} hillarys: {} comments: {} posts: {}'.format(x, min(dates), max(dates), trumps, hillarys, comments, posts))
        url = r.json()['paging']['next']
        r = requests.get(url, params={'access_token': ACCESS_TOKEN})
except KeyError:
    print('min: {} max: {} trumps: {} hillarys: {} comments: {} posts: {}'.format(min(dates), max(dates), trumps, hillarys, comments, posts))




