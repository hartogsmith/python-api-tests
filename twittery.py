import requests
from requests_oauthlib import OAuth1
import time
import random
from sense_hat import SenseHat

# app credentials in file untracked by git
import twittery_cred
from twittery_cred import tw_key, tw_secret

tw_oauth_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
tw_timeline_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
tw_user = 'stuart_wagner'
tw_quantity = '100'
tw_url = 'https://api.twitter.com/1.1/search/tweets.json?q='
tw_tag = 'bernie'
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
	r = requests.get(tw_timeline_url + '?screen_name= '+ tw_user + '&count=' + tw_quantity, auth=tw_auth)
	for tweet in r.json():
	  	#print(tweet['text'])
  		sense.show_message(tweet['text'], scroll_speed=.1, text_colour=random_rgb())

display_tweets()
