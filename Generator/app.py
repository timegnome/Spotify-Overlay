import requests
import time
import os, sys
from os import environ
from flask import Flask, render_template, request, redirect
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process
from flask import Flask
from forms import SubmissionForm
from Generator.authentication import *
from Generator.codegenerator import *
#   Global Variables

app = Flask(__name__)
auth_info= ''
OAth_tokens = {}
if __name__ == "__main__":
#     Create system tray icon to be able to terminate program without
#     using the kill cmd or task manager
    image = create_image()
    menu = (item('Info', action), item('Exit', lambda : sys.exit()))
    icon = pystray.Icon("ScO", image, "ScO Menu", menu)
    icon.run()
    time.sleep(30)
    sys.exit()
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
#     Send request with auth info for the song request of the 
#     currently playing song if available
    song_info = get_spotify_song_info(features)
#     Get image of spotify code of the current song
    get_spotify_code_image(song_info)
#     start timer for the system
    start_time=time.perf_counter()
#     spotify_code = CreateSpotifyCode()
#         spotify_code.get_spotify_song_info(song_info)
#  loop through until system terminated
    while(true):
        if (start_time - time.perf_counter)%30 == 0:
            get_spotify_code_image(song_info)
        if (start_time - time.perf_counter)%3600 == 0:
            OAth_tokens = get_tokens(auth_info)
        