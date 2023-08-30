import asyncio

import discord
from discord.ext import commands

from modules.youtube import ytdl, ffmpeg_options


class YTDLSource(discord.PCMVolumeTransformer):
	def __init__(self, source, *, data, volume=0.5):
		super().__init__(source, volume)
		self.data = data
		self.title = data.get("title")
		self.url = data.get("url")

	@classmethod
	async def from_url(cls, url, *, loop=None, stream=False):
		loop = loop or asyncio.get_event_loop()
		data = await loop.run_in_executor(
			None, lambda: ytdl.extract_info(url, download=not stream)
		)
		if "entries" in data:
			# take first item from a playlist
			data = data["entries"][0]
		filename = data["url"] if stream else ytdl.prepare_filename(data)
		return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


# Radio Menu
class Radio(discord.ui.View):
	def __init__(self, bot: commands.Bot):
		super().__init__(timeout=None)

		self.bot = bot

	@discord.ui.button(label="Intense", style=discord.ButtonStyle.red, emoji="🔥")
	async def intense_callback(self, interaction, button):
		await interaction.response.send_message(f"Playing some intense music")
		url = "https://www.youtube.com/watch?v=7tNtU5XFwrU"
		player = await YTDLSource.from_url(
			url, loop=interaction.client.loop, stream=True
		)
		interaction.guild.voice_client.play(
			player, after=lambda e: print(f"Player error: {e}") if e else None
		)
		await self.bot.change_presence(
			activity=discord.Activity(
				type=discord.ActivityType.listening, name="Gaming Music"
			)
		)

	@discord.ui.button(label="Chill", style=discord.ButtonStyle.blurple, emoji="🧊")
	async def chill_callback(self, interaction, button):
		await interaction.response.send_message(f"Playing some chill music")
		url = "https://www.youtube.com/watch?v=jfKfPfyJRdk"
		player = await YTDLSource.from_url(
			url, loop=interaction.client.loop, stream=True
		)
		interaction.guild.voice_client.play(
			player, after=lambda e: print(f"Player error: {e}") if e else None
		)
		await self.bot.change_presence(
			activity=discord.Activity(type=discord.ActivityType.listening, name="Lofi")
		)
