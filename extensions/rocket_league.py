import json

import discord
from discord.ext import commands
from discord.ui import View

from modules.files import DATABASE_PATH
from modules.rocket_league import RegisterButton


class RocketLeagueCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def register(self, ctx: commands.Context):
		view = View()
		view.add_item(RegisterButton(self.bot))
		await ctx.send("Registration Menu", view=view)

	@commands.command()
	async def profile(self, ctx, arg=None, member: discord.Member = None):
		# TODO: Find out how kwargs work in discord, and modify method if needed

		if member is None:
			member = ctx.message.author

		with open(DATABASE_PATH) as file:
			data = json.load(file)

		member_name = member.name
		if member_name in data["info"]:
			if arg is None:
				pass
			else:
				get_info = arg.lower()

				if get_info == "name":
					await ctx.send(f"{member_name}'s name is {data['info']['name']}")
				elif get_info == "username":
					await ctx.send(f"{member_name}'s username is {data['info']['username']}")
				elif get_info == "club":
					await ctx.send(f"{member_name} is current signed with {data['info']['prefix']}{data['info']['club']}")
				elif get_info == "mic":
					if data['info']['mic'] == "Yes":
						await ctx.send(f"{member_name} has a mic")
					elif data['info']['mic'] == "No":
						await ctx.send(f"{member_name} does not have a mic")
				elif get_info == "alias":
					await ctx.send(f"{member_name}'s alias is {data['info']['alias']}")
				elif get_info == "id":
					await ctx.send(f"{member_name}'s id is {data['info']['id']}")
				elif get_info == "platform":
					await ctx.send(f"{member_name}'s platform is {data['info']['platform']}")
				elif get_info == "style":
					await ctx.send(f"{member_name}'s style is {data['info']['style']}")
				elif get_info == "personality":
					await ctx.send(f"{member_name}'s personality is {data['info']['personality']}")
		else:
			await ctx.send(f"{member_name} is not registered!")


async def setup(bot: commands.Bot):
	await bot.add_cog(RocketLeagueCog(bot))
