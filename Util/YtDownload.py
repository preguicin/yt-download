import subprocess, shlex

ytDLPRequest = "yt-dlp -x -f bestaudio "
ytURL = "https://www.youtube.com/watch?v="

def downloadCall(videosIdArray):
    index = 0
    limit = len(videosIdArray)
    while index < limit:
        subProcessString = shlex.split(ytDLPRequest + ytURL + videosIdArray[index]);
        p = subprocess.Popen(subProcessString)
        index += 1
    