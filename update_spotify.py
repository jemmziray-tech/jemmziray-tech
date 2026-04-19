import os
import base64
import urllib.request
import urllib.parse
import json
import re

# 1. Grab secrets from GitHub Actions environment
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
refresh_token = os.environ.get('SPOTIFY_REFRESH_TOKEN')

# 2. Authenticate and get a fresh Access Token
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()
token_url = 'https://accounts.spotify.com/api/token'

headers = {
    'Authorization': f'Basic {b64_auth_str}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = urllib.parse.urlencode({
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
}).encode()

try:
    # Fetch Access Token
    req = urllib.request.Request(token_url, data=data, headers=headers)
    with urllib.request.urlopen(req) as response:
        access_token = json.loads(response.read().decode())['access_token']

    # 3. Check what song is currently playing
    playing_url = 'https://api.spotify.com/v1/me/player/currently-playing'
    req = urllib.request.Request(playing_url, headers={'Authorization': f'Bearer {access_token}'})
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 204: # 204 means nothing is playing
                playing_text = "🎧 *Not playing anything right now*"
            else:
                track_data = json.loads(response.read().decode())
                if track_data.get('is_playing') and track_data.get('item'):
                    artist = track_data['item']['artists'][0]['name']
                    song = track_data['item']['name']
                    playing_text = f"🎧 Now Playing: **{song}** by **{artist}**"
                else:
                    playing_text = "🎧 *Not playing anything right now*"
    except urllib.error.HTTPError:
        playing_text = "🎧 *Not playing anything right now*"
        
    # 4. Inject the text directly into your README
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        
    # Find the hidden markers and replace the text between them
    new_readme = re.sub(
        r'.*?',
        f'\n{playing_text}\n',
        readme,
        flags=re.DOTALL
    )
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
        
    print(f"Successfully updated README with: {playing_text}")

except Exception as e:
    print(f"Failed to update Spotify status. Error: {e}")
