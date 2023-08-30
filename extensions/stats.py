import json

from discord.ext import commands

from modules.files import DATABASE_PATH
from modules.stats import StatsMenu, StatManager


class StatsCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def average(self, ctx: commands.Context):
		with open(DATABASE_PATH) as file:
			data = json.load(file)

		author_name = ctx.message.author.name

		if author_name in data["info"]:
			name = data["info"][author_name]
			platform = data["info"]["platform"]

			print(name)
			print(platform)
			await ctx.send(f"Loading average...")
			await ctx.send(StatManager.get_average(name, platform))

		else:
			await ctx.send("You are not registered!")

	@commands.command()
	async def stats(self, ctx: commands.Context):
		with open(DATABASE_PATH) as file:
			data = json.load(file)

		author_name = ctx.message.author.name

		if author_name in data["info"]:
			name = data["info"][author_name]
			platform = data["info"]["platform"]

			print(name)
			print(platform)
			await ctx.send(f"Loading stats...")
			await ctx.send(f"```\n{StatManager.statistics(name, platform)}\n```")

		else:
			await ctx.send("You are not registered!")

	@commands.command()
	async def menu(self, ctx):
		await ctx.send(f"Menu for {ctx.message.author.name}", view=StatsMenu())


async def setup(bot: commands.Bot):
	await bot.add_cog(StatsCog(bot))
