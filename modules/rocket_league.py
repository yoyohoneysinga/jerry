import asyncio
import json

import discord
from discord.ext import commands
from discord.ui import Button

from modules.files import DATABASE_PATH


class RegisterButton(Button):
	def __init__(self, bot: commands.Bot):
		super().__init__(label="Start Registration", style=discord.ButtonStyle.green)

		self.bot = bot

	async def callback(self, interaction: discord.Interaction):
		user = interaction.user
		channel = await user.create_dm()

		def check(message):
			return isinstance(message.channel, discord.channel.DMChannel) and message.author == user

		user_info = {}

		await interaction.response.send_message("Starting registration")
		async with channel.typing():
			# Register preamble
			await user.send("Welcome to the registration menu")
			await asyncio.sleep(1)
			await user.send("I just have to ask you some basic questions so this shouldn't take too long")
			await asyncio.sleep(1)

			# Username
			await user.send("What is your in game username?")
			username: discord.Message = await self.bot.wait_for("message", check=check)
			user_info["username"] = username.content
			await asyncio.sleep(1)

			# Club info
			await user.send("Are you part of a club (Y/N)?")
			is_club: discord.Message = await self.bot.wait_for("message", check=check)

			await asyncio.sleep(1)

			# No club
			if "n" in is_club.content.lower():
				user_info["club"] = "None"
				user_info["prefix"] = "None"

			# Part of club
			else:
				await user.send("Enter the name of the club. This is case sensitive so enter it exactly as it is shown inside of Rocket League")
				club: discord.Message = await self.bot.wait_for("message", check=check)
				user_info["club"] = club.content

				await asyncio.sleep(1)

				await user.send("Enter the club prefix without the brackets")
				prefix: discord.Message = await self.bot.wait_for("message", check=check)
				user_info["prefix"] = f"[{prefix.content.upper()}]"
				await user.edit(nick=f"{user_info['prefix']}{user.name}")

				await asyncio.sleep(1)

			# Mic info
			await user.send("Do you have a microphone (Y/N)?")
			mic: discord.Message = await self.bot.wait_for("message", check=check)

			await asyncio.sleep(1)

			# No mic
			if "n" in mic.content.lower():
				user_info["mic"] = "No"
				user_info["alias"] = "None"

			# Has mic
			else:
				user_info["mic"] = "Yes"

				await user.send("When comming or in voice call, what do you preferred to be called? For example yoyohoneysinga prefers to be called simply yoyo.")
				alias: discord.Message = await self.bot.wait_for("message", check=check)

				user_info["alias"] = alias.content

				await asyncio.sleep(1)

			# Platform
			await user.send("What is your main platform (epic, steam, xbl, psn)?")
			platform: discord.Message = await self.bot.wait_for("message", check=check)
			user_info["platform"] = platform.content.lower()

			await asyncio.sleep(1)

			# Playstyle info
			await user.send("What is your playstyle (Passive, Passive-Aggressive, Aggressive)?")
			playstyle: discord.Message = await self.bot.wait_for("message", check=check)
			user_info["style"] = playstyle.content

			await asyncio.sleep(1)

			await user.send("How would you describe yourself (Mechanical, Neutral, Rotational)?")
			personality: discord.Message = await self.bot.wait_for("message", check=check)
			user_info["personality"] = personality.content

			await asyncio.sleep(1)

			# End
			await user.send("All done! Thank you for your time")

			user_info["id"] = user.id

		# Modify roles to Registered Member
		registered_member_role = discord.utils.get(user.server.roles, name="Registered Member")
		unregistered_member_role = discord.utils.get(user.server.roles, name="Unregistered Member")
		await user.add_roles(registered_member_role)
		await user.remove_roles(unregistered_member_role)

		# Write to database
		with open(DATABASE_PATH) as file:
			data = json.load(file)

			data["info"][user.name] = user_info

			# For lookup with alias
			if not user_info["alias"] == "None":
				data["aliases"][user_info["alias"]] = user.name
