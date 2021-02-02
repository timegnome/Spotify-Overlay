import json
import os, sys
from os import environ
from client_id import client_id as clientID
from datetime import datetime
from flask import Flask, render_template, request, redirect
# from FlaskApp.forms import SubmissionForm

app = Flask(__name__)

# Construct the HTTP request header
url = 'https://accounts.spotify.com/authorize'
header = {
    'client_id': clientID,
    'response_type': 'code',
    'redirect_uri': 'https://localhost:5500',
    'state': 't1i2m3e4g5n6o7m8e',
    'scope': 'user-read-currently-playing',
    'show_dialog': 'false'}

#     'Authorization': ('Bearer ' + MOVIE_KEY)}

# Main app page/route

# create_image()
@app.route('/')
@app.route('/home')
def home():
    return render_template (
        'index.html'
    )


@app.route('/login', methods =['GET','POST'])
@app.route('/login?code=<code>&state=t1i2m3e4g5n6o7m8e', methods =['GET','POST'])
# @app.route('/login?code=<code>')
def login(code = '', state =''):
    return  render_template(
        'login.html',
        form= form
    )

# @app.route('/mldeployRating',  methods = ['GET', 'POST'])
# def rating():
#     form = SubmissionForm(request.form)
    
#     # Form has been submitted
#     if request.method == 'POST' and form.validate():
#         # Plug in the data into a dictionary object
#         # -data from the input form
#         data = {
#             "Inputs": {
#                 "input1": {
#                     "ColumnNames":[
#                                     "Genres",
#                                     "Production Companies",
#                                     "Production Countries",
#                                     "New Key",
#                                     "Percent_Profit",
#                                     "Good_Movie"
#                                     ],
#                                     "Values": [
#                                     [
#                                         f'{form.genres.data}',
#                                         f'{form.prodComp.data}',
#                                         f'{form.prodCont.data}',
#                                         f'{form.new_Key.data}',
#                                         form.percent_Profit.data,
#                                         'A'
#                                     ]
#                                 ]
#                 }
#             },
#             "GlobalParameters": {}
#         }

#         # Serialize the input data into json string
#         body = str.encode(json.dumps(data))
#         # print(body)
#         # Formulate the request
#         req = urllib.request.Request(MOVIE_URL, body, HEADERS1)
        
#         # Send this request to the AML service and render the results on page
#         try:
#             response = urllib.request.urlopen(req)
#             #print(response)
#             respdata = response.read()
#             result = json.loads(str(respdata, 'utf-8'))
#             return render_template(
#                 'mldeployRating.html',
#                 year = datetime.now().year,
#                 result = result
#         # An HTTP error
#         except urllib.error.HTTPError as err:
#             result = "The request failed with status code: " + str(err.code)
#             return render_template (
#                 'mldeployRating.html',
#                 title = 'There was an error',
#                 year = datetime.now().year,
#                 result = result
    
#     # Serve up the input form
#     return render_template (
#         'ratingform.html',
#         form = form,
#         year = datetime.now().year,
#     )
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5500'))
    except ValueError:
        PORT = 5500
    app.run(HOST, PORT)