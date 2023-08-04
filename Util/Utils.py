def parseListURL(url) -> str:
    resultUrl = ""
    IsURLCorrect = False

    urlParts = url.split("&")
    for part in urlParts:
        if "list" in part:
            urlParts = part.split("=")
            IsURLCorrect = True
            break

    #To guarantee that the url is correct with a list element in it
    if IsURLCorrect == True:
        resultUrl = urlParts[1]
    else:
        raise Exception("Invalid URL Mate")
        
    return resultUrl

def videosArray(youtube, playlistId) -> []:
    index = 0
    videosIdArray = [] 

    #First ocurrence
    result = youtube.playlistItems().list(part="contentDetails", playlistId = playlistId, maxResults = 50).execute()
    tempArr = result["items"]

    for item in tempArr:
        videosIdArray.insert(index, item["contentDetails"]["videoId"])
        index += 1
    
    while result.get("nextPageToken") != None:
        result = youtube.playlistItems().list(part="contentDetails", playlistId = playlistId, pageToken = result["nextPageToken"], maxResults = 50).execute()
        tempArr = result["items"]

        for item in tempArr:
            videosIdArray.insert(index, item["contentDetails"]["videoId"])
            index+=1

    return videosIdArray