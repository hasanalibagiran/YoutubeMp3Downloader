import youtube_dl

def download():
    video_url = input("Enter youtube url:")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url= video_url,
        download=False
        )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format' : 'bestaudio/best',
        'keepvideo' : False,
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
        'outtmp1' : filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl :
        ydl.download([video_info['webpage_url']])
    print("{} download process has started ".format(video_info['title']))

if __name__ == '__main__':
    download()
