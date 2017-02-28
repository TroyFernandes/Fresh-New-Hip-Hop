from flask import Flask
from flask_ask import Ask, statement, question,session
import json
import logging
import requests
import time
import re
import unidecode

app = Flask(__name__)
ask = Ask(app, "/fresh_new_hip_hop")
favArtists = ["ADD FAVOURITE ARTISTS SEPERATED WITH A COMMA"]
#Dictionary order is [Artist]:[link]
links = {}

#Uncomment lines below to enable logging 
#log = logging.getLogger()
#log .addHandler(logging.StreamHandler())
#log.setLevel(logging.DEBUG)
#logging.getLogger("flask_ask").setLevel(logging.DEBUG)


#add reddit username and password to access reddit api
def get_headlines(withArtist):
    user_pass_dict = {'user':'USERNAME',
                      'passwd': 'PASSWORD',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent':'Fresh New Hip Hop'})
    sess.post('http://www.reddit.com/api/login',data=user_pass_dict)
    time.sleep(1)
    url = 'https://www.reddit.com/r/hiphopheads/.json?limit=100'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    links.clear()
    for listing in data['data']['children']:
        if '[FRESH]' in listing['data']['title']:
            if withArtist == 0:
                titles.append(unidecode.unidecode(listing['data']['title'].replace('[FRESH]','')))
                links[listing['data']['title']] = listing['data']['url']
            else:
                if any(favouriteArtists in listing['data']['title'] for favouriteArtists in favArtists):
                    titles.append(unidecode.unidecode(listing['data']['title'].replace('[FRESH]','')))
                    links[listing['data']['title']] = listing['data']['url']
                         
    titles = '... ... ... next up ... '.join([i for i in titles])
    return titles


@app.route('/')
def homepage():
    return "hi"

@ask.launch
def start_skill():
    welcome_message = "Hello! you wanna know whats fresh on r/hiphopheads?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines(0)
    headline_msg = 'The newest tracks today are {}'.format(headlines)
    return question(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "Ok... bye"
    return statement(bye_text)

@ask.intent("FavouriteArtists")
def get_favourite_artists():
    headlines = get_headlines(1)
    headline_msg = 'The newest tracks from your favourite artists today are {}'.format(headlines)
    return question(headline_msg)

@ask.intent("GetLinks")
def get_song_links(ArtistName):
    #v = list(links.values())
    for x in links:
        if ArtistName.lower() in x.lower():
           # print (x,links[x])
            return statement("Sending the link for {}".format(x)).simple_card(x,links[x])
        #else:
         #   return statement("I couldn't find any links for the artist {}".format(ArtistName))

if __name__ == '__main__':
    app.run(debug=True)