import os
import base64
import urllib.request
import urllib.parse
import urllib.error
import json

# Grab secrets
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
refresh_token = os.environ.get('SPOTIFY_REFRESH_TOKEN')

# Authenticate
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
    req = urllib.request.Request(token_url, data=data, headers=headers)
    with urllib.request.urlopen(req) as response:
        access_token = json.loads(response.read().decode())['access_token']

    # Get playing song
    playing_url = 'https://api.spotify.com/v1/me/player/currently-playing'
    req = urllib.request.Request(playing_url, headers={'Authorization': f'Bearer {access_token}'})
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 204:
                playing_text = "🎧 *Not playing anything right now*"
            else:
                track_data = json.loads(response.read().decode())
                if track_data.get('is_playing') and track_data.get('item'):
                    item = track_data['item']
                    item_type = track_data.get('currently_playing_type')
                    
                    if item_type == 'episode':
                        title = item.get('name', 'Unknown Podcast')
                        creator = item.get('show', {}).get('name', 'Unknown Show')
                    else:
                        title = item.get('name', 'Unknown Song')
                        creator = item.get('artists', [{'name': 'Unknown Artist'}])[0].get('name', 'Unknown Artist')
                        
                    playing_text = f"🎧 Now Playing: **{title}** by **{creator}**"
                else:
                    playing_text = "🎧 *Not playing anything right now*"
                    
    except urllib.error.HTTPError as e:
        print(f"Spotify API Error: {e.read().decode()}")
        playing_text = "🎧 *Not playing anything right now*"
        
    # THE STRING-SPLIT METHOD (Immune to formatting bugs)
    with open('README.md', 'r', encoding='utf-8') as f:
        text = f.read()
        
    start_tag = ''
    end_tag = ''
    
    if start_tag in text and end_tag in text:
        # Chop the text into pieces and rebuild it perfectly
        before = text.split(start_tag)[0]
        after = text.split(end_tag)[1]
        
        new_text = before + start_tag + '\n' + playing_text + '\n' + end_tag + after
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Successfully updated README with: {playing_text}")
    else:
        print("SAFETY LOCK: Markers not found. File untouched.")

except Exception as e:
    print(f"Failed to update Spotify status. Error: {repr(e)}")
