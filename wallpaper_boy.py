__author__ = 'conrad'

from bs4 import BeautifulSoup
import requests
import urllib
import string
import random

# generates a random 6-character string used for naming images
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# connects to website containing wallpapers
user_agent = {'User-Agent': 'Mozilla/5.0'}
html = requests.get('http://www.reddit.com/r/wallpapers/top/', headers=user_agent).text
soup = BeautifulSoup(html)

# makes a list of all a href links
possible_links = soup.find_all('a')
full_list = ""
for link in possible_links:
    if link.has_attr('href'):
        full_list += link.attrs['href'] + "\n"
full_list = full_list.split('\n')

# makes a new list only containing direct links to the image
imgur_list = ""
for i in range(0, len(full_list)):
    if "http://i.imgur" in full_list[i]:
        imgur_list += full_list[i] + "\n"
imgur_list = imgur_list.split('\n')

# gets rid of duplicate links 
imgur_list2 = list(set(imgur_list))
imgur_list2.sort(key=imgur_list.index)

# saves the top 3 images
for i in range(0, 3):
    
    # set to my directory, makes sure to change to desired path
    urllib.urlretrieve(imgur_list2[i], ("/home/conrad/Pictures/wallpapers/bg" + id_generator()))
    print ("Saving picture " + str(i+1) + "...")
print "DONE"
