import discord
import requests
import youtube_dl
from discord.ext import commands
from discord.ui import Button, View

from modules.music import Radio, YTDLSource
from modules.youtube import ytdl_format_options


class MusicCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def radio(self, ctx: commands.Context):
		channel = ctx.channel.id
		vc = ctx.author.voice.channel
		if channel != 1010268755202412604:
			await ctx.message.delete()
			await ctx.send("This command doesn't belong here", ephemeral=True)
		else:
			if ctx.voice_client is not None:
				return await ctx.voice_client.move_to(vc)
			await vc.connect()
			await ctx.send("What mood are you feeling?", view=Radio(self.bot))

	@commands.command()
	async def play(self, ctx: commands.Context, *arg):
		channel = ctx.channel.id
		if channel != 1010268755202412604:
			await ctx.message.delete()
			await ctx.send("This command doesn't belong here", ephemeral=True)
		else:
			with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
				try:
					requests.get(arg)
				except:
					video = ydl.extract_info(f"ytsearch:{arg}", download=False)["entries"][
						0
					]
				else:
					video = ydl.extract_info(arg, download=False)
			channel = ctx.author.voice.channel
			if ctx.voice_client is not None:
				return await ctx.voice_client.move_to(channel)
			await channel.connect()
			url = video["webpage_url"]
			title = video["title"]
			player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
			ctx.voice_client.play(
				player, after=lambda e: print(f"Player error: {e}") if e else None
			)
			await ctx.send(f"Now playing: {title}")
			await self.bot.change_presence(
				activity=discord.Activity(type=discord.ActivityType.listening, name=title)
			)

	@commands.command()
	async def playing(self, ctx: commands.Context):
		channel = ctx.channel.id
		if channel != 1010268755202412604:
			await ctx.message.delete()
			await ctx.send("This command doesn't belong here", ephemeral=True)
		else:
			arg = [s for s in self.bot.guilds][0].get_member(self.bot.user.id).activity.name
			arg2 = [s for s in self.bot.guilds][0].get_member(self.bot.user.id).activity.type
			if "watching" in arg2:
				await ctx.send("No song is playing")
			else:
				with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
					try:
						requests.get(arg)
					except:
						video = ydl.extract_info(f"ytsearch:{arg}", download=False)[
							"entries"
						][0]
					else:
						video = ydl.extract_info(arg, download=False)
				title = video["title"]
				link = video["webpage_url"]
				button = Button(
					label=f"Click here", style=discord.ButtonStyle.link, url=link
				)
				view = View()
				view.add_item(button)
				await ctx.send(f"Check out {title} with the link below!")
				await ctx.send("", view=view)

	@commands.command()
	async def volume(self, ctx: commands.Context, volume: int):
		channel = ctx.channel.id
		if channel != 1010268755202412604:
			await ctx.message.delete()
			await ctx.send("This command doesn't belong here", ephemeral=True)
		else:
			if ctx.voice_client is None:
				return await ctx.send("Not connected to a voice channel.")
			ctx.voice_client.source.volume = volume / 100
			await ctx.send(f"Changed volume to {volume}%")

	@commands.command()
	async def stop(self, ctx: commands.Context):
		channel = ctx.channel.id
		if channel != 1010268755202412604:
			await ctx.message.delete()
			await ctx.send("This command doesn't belong here", ephemeral=True)
		else:
			await ctx.voice_client.disconnect()

		@self.radio.before_invoke
		async def ensure_voice(ctx):
			if ctx.voice_client is None:
				if ctx.author.voice:
					await ctx.author.voice.channel.connect()
				else:
					await ctx.send("You are not connected to a voice channel.")
					raise commands.CommandError("Author not connected to a voice channel.")
			elif ctx.voice_client.is_playing():
				ctx.voice_client.stop()
			await self.bot.change_presence(
				activity=discord.Activity(
					type=discord.ActivityType.watching, name="Stats for Slayers"
				)
			)


async def setup(bot: commands.Bot):
	await bot.add_cog(MusicCog(bot))
