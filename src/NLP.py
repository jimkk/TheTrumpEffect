import urllib.parse, urllib.request

def getSentiment(text):
    params = urllib.parse.urlencode({"text": text})
    f = urllib.request.urlopen("http://text-processing.com/api/sentiment/", bytearray(params, "ascii"))
    data = f.read()
    return data

def getPhrases(text):
    params = urllib.parse.urlencode({"text": text})
    f = urllib.request.urlopen("http://text-processing.com/api/phrases/", bytearray(params, "ascii"))
    data = f.read()
    return data
