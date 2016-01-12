import requests
from requests_oauthlib import OAuth1
import time
import random
from sense_hat import SenseHat

tw_oauth_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
tw_url = 'https://api.twitter.com/1.1/search/tweets.json?q='
tw_tag = 'bernie'
tw_key = 'xBqDJAoiO5zeF1uFdzKt9S6s0'
tw_secret = 'jGeo8KyHHhtVoaEyCGo6c1WSAjBRvtsfmFC86YjiTR8PZ3kCHu'
tw_auth = OAuth1(tw_key, tw_secret)

sense = SenseHat()
sense.clear()
orientation = sense.get_orientation_degrees()
#print("pitch: {pitch}, roll: {roll}, yaw: {yaw}".format(**orientation))
roll = sense.orientation.get('roll')
#print(roll)
if roll < 90:
    sense.set_rotation(90)


def random_rgb():
    random_r = random.randint(51,153)
    random_g = random.randint(51,153)
    random_b = random.randint(51,153)
    random_color = (random_r, random_g, random_b)
    #print(random_color)
    return random_color

def auth_display_tweets():
	return requests.get(tw_oauth_url, auth=tw_auth)

def display_tweets():
	r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=stuart_wagner&count=100', auth=tw_auth)
	for tweet in r.json():
	  	#print(tweet['text'])
  		sense.show_message(tweet['text'], scroll_speed=.1, text_colour=random_rgb())

display_tweets()
