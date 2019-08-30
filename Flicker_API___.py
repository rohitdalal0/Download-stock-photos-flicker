import requests
from urllib.request import urlretrieve
import json,os

api = '<your api_key>'
secret = '<secret_key>' # optional

# Input from user
search = str(input('Describe photo: '))
page = str(input('On which page you wanna land: '))
list_of_photos = str(input('How many photos you wanna: '))
size = str(input('Size of photos (example: android, tablet, pc):'))
# This url to get img id only
url = 'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key= <Your api_key> &tags={}&page={}&per_page={}&format=json&nojsoncallback=1'.format(search,page,list_of_photos)

# Stored all img-id and their img-name in one list
req = requests.get(url).json()['photos']['photo']
img_id = [req[i]['id'] for i in range(int(list_of_photos))]
title = [req[i]['title'] for i in range(int(list_of_photos))]

# Get img url
size_No = 0
for i in range(len(img_id)):
    img_url_api = 'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key= <your api_key> &photo_id=%s&format=json&nojsoncallback=1' % img_id[i]
    img_url = requests.get(img_url_api).json()['sizes']['size']
    
    # Ger size of photos by user
    if size == 'android':
        size_No = 4
    elif size == 'tablet' or 'tab' or 't':
        size_No = 6
    elif size == 'pc' or 'desktop' or 'computer' or 'c':
        size_No = 8
    else:
        size_No = 8
    sizing = img_url[size_No]['source']  # max len(8)

    # creating folder to store images
    if os.path.isdir('c:\\users\\abc\\Desktop\\flicker'):
        os.chdir('c:\\users\\abc\\Desktop\\flicker')
    else:
        os.mkdir('c:\\users\\abc\\Desktop\\flicker')
        os.chdir('c:\\users\\abc\\Desktop\\flicker')

    print('Downloading >>>>>>> %s' % sizing)
    urlretrieve(sizing, '%s.jpg' % title[i])
