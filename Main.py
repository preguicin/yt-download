import sys

from Util import Utils
from Util import YtDownload
from googleapiclient.discovery import build

#Util 
youTubeApiKey = "Your API Key Here"
videosIdArray = []

def main() -> int:
    #Your Playlist URL Here
    url = "https://www.youtube.com/playlist?list=PLKpm9P9iFOXqPrFu9QbaJ0D-qczYW8fXI"
    playlistId = Utils.parseListURL(url)
    youtube = build("youtube","v3",developerKey=youTubeApiKey)
    videosIdArray = Utils.videosArray(youtube, playlistId)

    #Download videos part
    YtDownload.downloadCall(videosIdArray)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
