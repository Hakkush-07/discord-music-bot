import youtube_dl
import requests
import re
import json
import discord


class Audio:
    def __init__(self, query):
        self.query = query
        self.url, self.title = self.url_and_title()
        self.sound = self.get_audio()

    def get_audio(self):
        ydl_options = {
            "format": "best" + "audio",
            "no" + "playlist": "True",
            "quiet": "True",
            "geo_bypass_country": "us"
        }
        ffmpeg_options = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn"
        }
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(self.url, download=False)
        sound_url = info["formats"][0]["url"]
        return discord.FFmpegPCMAudio(sound_url, **ffmpeg_options)

    def url_and_title(self):
        search_results_url = f"https://www.youtube.com/results?search_query={'+'.join(self.query.split())}"
        video_id = re.findall(r"watch\?v=(\S{11})", requests.get(search_results_url).text)[0]
        url = "https://www.youtube.com/watch?v=" + video_id
        title = json.loads(requests.get(f"https://www.youtube.com/oembed?format=json&url={url}").text)["title"]
        return url, title
