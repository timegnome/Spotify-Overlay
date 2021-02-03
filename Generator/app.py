import time
import os, sys
from os import environ
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process
from forms import SubmissionForm
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# from authentication import *
# from codegenerator import *
import json
import requests
print('imdyingheere')
# from __init__ import app
import requests
import shutil # to save it locally
import json
from client_id import client_id as clientID, client_secret as secret
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pystray import MenuItem as item
import pystray
print('pleaseineedhelp')

# Start Application 
# Start Selenium Browser
# request address for user sign-in
# Login to Spotify
# Redirect to Local URL
# Get User's Features Selection
# Get User's tokens and Permissions
# Request for the users current playing song
# Grab the current playing songs uri
# Parse the uri for playist or song code
# Request Image of Code
# Create Directory for Image
# Store Image of Code
# Update Image on new song
# Kill Program and remove memory leaks
# Create tray icon for exit
# Login to Spotify
# Get Users tokens and Permissions
# Request for the users current playing song
# scope:user-read-currently-playing
# get an image
def action():
    pass
def create_image():
    for root, dirs, files in os.walk(os.getcwd()):
        if 'icon.jpg' in files:
            txt = Image.open(files)
            return txt
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", size= (50,50), color = (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("arial.ttf", 20)
    # get a drawing context
    SCO = ImageDraw.Draw(txt)

    # draw text, half opacity
    SCO.text((10,10), "ScO", font=fnt, fill=(255,255,255,128))

    return txt
# Create permission prompt and feature choices for the image
def get_permission(browser):
    url = 'https://accounts.spotify.com/authorize'
    header = {
        'client_id': clientID,
        'response_type': 'code',
        'redirect_uri': 'http://localhost:5500/login',
        'state': 't1i2m3e4g5n6o7m8e',
        'scope': 'user-read-currently-playing',
        'show_dialog': 'false'}
    req = requests.get(url,header)
    browser.visit(req.url)
def get_tokens():
    request_body = json.dumps({
        "client_id" : clientID,
        "client_secret": secret
    })
    query = f"https://accounts.spotify.com/api/token"
    response = requests.post(
    query,
    data = request_body,
    headers= {
        "grant_Type":'authorization_code',
        "Authorization":auth_info,
        "redirect_uri" : 'http://localhost:5500/login'
        }
    )
    if response.status_code == 200:
        OAth_tokens= response.json()
        # Grab the current playing songs uri
        try:
            return OAth_tokens
        except:
            return None 
    
def get_spotify_song_info(style):
    request_body = json.dumps({
        "market" : 'US',
        "additional_types": 'track'
    })
    query = f"https://api.spotify.com/v1/me/player/currently-playing"
    response = requests.post(
    query,
    data = request_body,
    headers= {
        "Content-Type":"application/json",
        "Authorization":f"Bearer {OAuth_tokens['access_token']}"
        }
    )
    if response.status_code == 200:
        response_json= response.json()
        # Grab the current playing songs uri
        try:
            song = {'uri':response_json['item']['uri'],
            'name':response_json['item']['name'],
            'background':style['background'],
            'size':style['size'],
            'color':style['color']}
        except:
            song = {'uri':response_json['item'][0]['uri'],
            'name':response_json['item']['name'],
            'background':style['background'],
            'size':style['size'],
            'color':style['color']}
    return song
    # Parse the uri for playist or song code if needed or if null
def get_spotify_code_image(song):
    url = f"https://scannables.scdn.co/uri/plain\
          /jpeg/{song['color']}/{song['background']}/{song['size']}/{song['uri']}"
    response = requests.get(url, stream=True)
    # # print(response.status_code)
    # test = Image.open(BytesIO(response))
    if response.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        response.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open('spotify_code.jpeg','wb') as f:
            shutil.copyfileobj(response.raw, f)

        print('Image sucessfully Downloaded: ','spotify_code.jpeg')
    else:
        print('Image Couldn\'t be retreived')
@app.route('/login')
def get_login(browser):
    auth_info = request.args.get('code')
    state = request.args.get('state')
    if state != 't1i2m3e4g5n6o7m8e':
        return 404
    if code:
        return render_template(
            'login.html',
            state = state,
            code = auth_info,
        year = datetime.now().year
        )
    else:
        return render_template(
            'login.html',
            state = state,
            code = auth_info,
            year = datetime.now().year
        )
@app.route('/features', methods = ['GET', 'POST'])
def get_features():
    if request.method =='POST' and form.validate():
        authcode = get_tokens(auth_info)
        style ={
            'authcode': authcode,
            'background': form.background.data,
            'size': form.size.data,
            'color' : form.color.data
        }
        return render_template(
            'completed.html',
            year = datetime.now().year
        )
    else:
        return render_template(
            'features.html',
            form = form,
            year = datetime.now().year
        )
def endprogram(icon):
    icon.stop()
    exit()
 #   Global Variables
auth_info= ''
OAth_tokens = {}
if __name__ == "__main__":
#     Create system tray icon to be able to terminate program without
#     using the kill cmd or task manager
    image = create_image()
    menu = (item('Info', lambda: icon.stop()), item('Exit', lambda : endprogram(icon)))
    icon = pystray.Icon("ScO", image, "ScO Menu", menu)
    icon.run()
#     Setup server thread for the local flask app
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5500'))
    except ValueError:
        PORT = 5500
    server = Process(target=app.run(HOST, PORT))
    server.start()
    
#     Start browser for the request redirects and url displayed
    executable_path = {"executable_path": ChromeDriverManager().install()}
    brws = Browser('chrome', **executable_path, headless=False)
    
#     Get the permissions from the user sending the requests and redirect
#     to be shown on the browser
    get_permission(brws)
#     Retrieve the authentication and refresh tokens
    OAuth_tokens = get_tokens(auth_info)
#     Get the features the user would like to have on their image
    features = get_features(brws)
#     remove resources
    brws.close()
#     terminate server once done with the user requests
    server.terminate()
    server.join()