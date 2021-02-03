from __init__ import app
import requests
import shutil # to save it locally
import json
from client_id import client_id as clientID, client_secret as secret
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pystray import MenuItem as item
import pystray
print('pleaseineedhelp')
def action():
    pass
def create_image():
    # Generate an image and draw a pattern
#     image = Image.new('RGB', (width, height), color1)
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", size= (50,50), color = (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("arial.ttf", 20)
    # get a drawing context
    SCO = ImageDraw.Draw(txt)

    # draw text, half opacity
    SCO.text((10,10), "ScO", font=fnt, fill=(255,255,255,128))

    return SCO
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
    form = SubmissionForm(request.form)
    if request.method =='POST' and form.validate():
        authcode = get_tokens(auth_info)
        style ={
            'authcode': authcode,
            'background': form.background.data,
            'size': form.size.data,
            'color': form.color.data
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