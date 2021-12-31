from Google import Create_Service

## Edit This Information
playlistId_Source = 'PLa2--cmNqUF6bm5F5Bk2740Fo8NTlCBTI'
delChannelName = "Chris Hallbeck"

CLIENT_SECRET_FILE  =  'client_secret_7.json'
API_NAME  =  'youtube'
API_VERSION  =  'v3'
SCOPES  = ['https://www.googleapis.com/auth/youtube']

service =  Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

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
    if video['snippet']['videoOwnerChannelTitle'] == delChannelName:
        print("Deleting Video by: " + video['snippet']['videoOwnerChannelTitle'])
        service.playlistItems().delete(id=video['id']).execute()
