import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ""

ytdl_format_options = {
	"format": "bestaudio/best",
	"outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
	"restrictfilenames": True,
	"noplaylist": True,
	"nocheckcertificate": True,
	"ignoreerrors": False,
	"logtostderr": False,
	"quiet": True,
	"no_warnings": True,
	"default_search": "auto",
	# bind to ipv4 since ipv6 addresses cause issues sometimes
	"source_address": "0.0.0.0",
}
ffmpeg_options = {
	"options": "-vn",
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
