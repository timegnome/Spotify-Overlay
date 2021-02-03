import json
import requests
print('imdyingheere')
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
