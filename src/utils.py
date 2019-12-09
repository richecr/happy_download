import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestvideo+audio/best',
    'noplaylist' : True,
    'progress_hooks': [my_hook]
}

def download_video(url):
    print(url)
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        print(e)
        pass

def tratar_url(url):
    url_test = url.split("https://youtu.be/")
    if (len(url_test) == 1):
        return url
    elif (len(url_test) == 2):
        url_ = "https://www.youtube.com/watch?v="+url_test[1]+"&feature=youtu.be"
        return url_