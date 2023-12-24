"""
This module suggests a spotify track from a playlist of sumitted songs by 
developers. (Issue #6)



It is called with /tunesuggest <genre>

The client-secret is used to fetch a token wich can be submitted to get the
playlist's content

"""
# Access to os environment variables
import os
import time
import requests
# API token and client secret
api_token = ""
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
"""
{
    "grant_type": "client_credential",
    "client_id": ,
    "client_secret": client_secret
    }
"""

# Fetching temporarily valid API access token with client ID and client secret



# Writing token into http authorization field
bearer_token = "Bearer " + api_token

# Defining http authorization field
headers = {"Authorization" : bearer_token}

# Debug output
print(headers)

# Get playlist json information with api token
response = requests.get(url="https://api.spotify.com/v1/playlists/23L8Koh7R29eOvA9ZBI9DN", headers=headers)
for track in response.json()['tracks']['items']:
    # Get album genres
    genre_api_response = requests.get(url=track['track']['artists'][0]['href'], headers=headers)
    artist = genre_api_response.json()
    genre = "unknown"
    if len(artist['genres']) > 0:
        genre = str(artist['genres'][0])
    print(str(artist['name']) + " -  " + str(track['track']['name']) + " (" + genre + ")")


def get_api_token(client_secret):
    """
    Returns API-Token gathered from the spotify Web API client-id and client-secret

    Both have to be saved in the environment variables:
    client-id       -> GP_SPOTIFY_CLIENT_ID
    client-secret:  -> GP_SPOTIFY_CLIENT_SECRET
    """
    # Setting URL
    url = "https://accounts.spotify.com/api/token"  

    # Setting application type field in http-header
    header_content_type ="Content-Type: application/x-www-form-urlencoded"

    # Setting http post request content
    https_data = "grant_type=client_credentials&client_id=&client_secret=" + client_secret  

    # Fetching http-request response
    response = requests.post(url=url, headers={"Content-Type" : "application/x-www-form-urlencoded"}, data = https_data)

    # Parsing token from http response json
    return response.json()["access_token"]    
    

def get_client_info():
    """
    Load spotify api client secret and it fom environment
    client_info = [<client id>,<client secret>]
    """
    client_info = [None, None]
    client_info[0] = os.environ.get('GP_SPOTIFY_CLIENT_ID')
    client_info[1] = os.environ.get('GP_SPOTIFY_CLIENT_SECRET')
    return client_info

def get_full_tracklist(client_info, playlist_id):
    """
    returns full tracklist
    """
    pass

def get_filtered_tracklist(genre):
    """
    returns filtered tracklist json:
    {
        "genre": <genre>,
        "tracks":[
            {
                "name": "song title",
                "artist": "artist name",
                "url": "spotify track url"
            }
        ]
    }
    """
    # Uses get_client_info and get_api_token
    
    # Fetch complete tracklist 
    tracklist = get_full_tracklist()

    # Filter logic

    pass

# Returns a formatted message with URL and other info on the suggested song
def get_suggestion(command):
    """
    Filters a defined playlist for song from the genre that is passed in /tunesuggest command

    """
    # Grab desired genre from command input
    genre = str(command).split(' ')

    # fetches the json list
    filtered_tracklist = get_filtered_tracklist(genre)

    # Returns a random item from the filtered track list
    return filtered_tracklist[tracks][i] 
