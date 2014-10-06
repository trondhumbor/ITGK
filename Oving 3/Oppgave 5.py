import urllib.parse as urlparse

baseShortUrl = "youtu.be/"

def shortify(video):
    #Python burde VIRKELIG lage en bedre standardmodul for URLparsing

    parsed = urlparse.urlparse(video)
    
    # urlparse.parse_qsl() returnerer et array med tupler
    # Det er lettere å operere på en dict, så vi omformer
    # det til et dict, og henter ut "v"-parameteret
    getParams = dict(urlparse.parse_qsl(parsed.query))
    return baseShortUrl + getParams["v"]

if __name__ == "__main__":
    videoer = [
        "http://www.youtube.com/watch?v=-840keiiFDE&t=1m40s",
        "http://www.youtube.com/watch?v=GpNSip5gyKo",
        "http://www.youtube.com/watch?v=sXX5drqRD9s",
        "http://www.youtube.com/watch?v=ZFngtBIxRPk",
        "http://www.youtube.com/watch?v=OZBWfyYtYQY",
        "http://www.youtube.com/watch?v=7LKHpM1UeDA"
    ]

    for video in videoer:
        print(shortify(video))