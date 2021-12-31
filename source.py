from Google import Create_Service
# import pandas as pd

CLIENT_SECRET_FILE  =  'client_secret_7.json'
API_NAME  =  'youtube'
API_VERSION  =  'v3'
SCOPES  = ['https://www.googleapis.com/auth/youtube']

service =  Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


playlistId_Source = 'watch_later'

response = service.playlistItems().list(
    part='snippet',
    playlistId=playlistId_Source,
    maxResults=50
).execute()

playlistItems = response['items']
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.playlistItems().list(
        part='snippet',
        playlistId=playlistId_Source,
        maxResults=50,
        pageToken=nextPageToken
    ).execute()

    playlistItems.extend(response['items'])
    nextPageToken = response.get('nextPageToken')


for video in playlistItems: 
    print(video['id'])   
    if video['snippet']['videoOwnerChannelTitle'] == "Mark165":
        print("Deleting Video by: " + video['snippet']['videoOwnerChannelTitle'])
        service.playlistItems().delete(id=video['id']).execute()
