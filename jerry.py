import json
import os
import random
import tracemalloc
from time import sleep

import discord
import discord.ext.commands
from discord.ext import commands
from discord.ui import View, Select
from requests import get

from modules.files import EXTENSION_DIR, DATABASE_PATH
from modules.stats import StatsMenu

# invite = "https://discord.com/api/oauth2/authorize?client_id=1006997696923574282&permissions=8&scope=bot"
key = "MTAwNjk5NzY5NjkyMzU3NDI4Mg.Gp2rIb.l0iIjVEDH16ef00AMmhwFGe2uFmKiaK6fHlbPE"
tracemalloc.start()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="jerry ", help_command=None, intents=intents)


# TODO: Move to rocket_league extension
@bot.command()
async def reactionrole(ctx):
	select = Select(
		min_values=0,
		max_values=3,
		options=[
			discord.SelectOption(
				label="Tournament Notifications",
				description="Pings you a certain amount of time before a tournament starts",
			),
			discord.SelectOption(
				label="Community Notifications",
				description="Pings you when something related to the server or team happens",
			),
			discord.SelectOption(
				label="Party Notifications",
				description="Pings you when someone is looking for a party",
			),
		],
	)

	async def my_callback(interaction):
		for i in select.values:
			if i == "Tournament Notifications":
				role = interaction.guild.get_role(1009552943621607444)
				await interaction.user.add_roles(role)
				await interaction.response.send_message("Role given", ephemeral=True)
			elif i == "Community Notifications":
				role = interaction.guild.get_role(1009553082381779034)
				await interaction.user.add_roles(role)
				await interaction.response.send_message("Role given", ephemeral=True)
			elif i == "Party Notifications":
				role = interaction.guild.get_role(1009552979923308625)
				await interaction.user.add_roles(role)
				await interaction.response.send_message("Role given", ephemeral=True)
		if "Tournament Notifications" in select.values:
			role = interaction.guild.get_role(1009552943621607444)
			await interaction.user.add_roles(role)
		if "Community Notifications" in select.values:
			role = interaction.guild.get_role(1009553082381779034)
			await interaction.user.add_roles(role)
		if "Party Notifications" in select.values:
			role = interaction.guild.get_role(1009552979923308625)
			await interaction.user.add_roles(role)

	select.callback = my_callback
	view = View()
	view.add_item(select)
	await ctx.send("Reaction Role Menu", view=view)


# TODO: Move to rocket_league extension
@bot.command()
async def party(ctx: commands.Context):
	await ctx.send(f"{ctx.message.author.display_name} is looking for a party")


# TODO: Move to rocket_league extension
@bot.command()
async def tournaments(ctx: commands.Context, alerts, *args):
	if len(args) > int(alerts):
		await ctx.send(
			"Error. Number or arguments was greater than number of expected arguments"
		)
	elif len(args) < int(alerts):
		await ctx.send(
			"Error. Number or arguments was lesser than number of expected arguments"
		)
	elif len(args) == int(alerts):
		await ctx.send("Setting up alerts...")
		sleep(5)
		channel = bot.get_channel(1006638350184222740)


@bot.event
async def on_ready():
	await bot.change_presence(
		activity=discord.Activity(
			type=discord.ActivityType.watching,
			name="Stats for Slayers"
		)
	)
	print("Virtual Assistant is up and running")


@bot.event
async def on_message(message):
	await bot.process_commands(message)


@bot.event
async def on_member_join(member: discord.Member):
	channel = bot.get_channel(1006376115461443644)
	role = discord.utils.get(member.guild.roles, name="Unregistered Member")
	await channel.send(f"Welcome {member.mention}")
	await member.add_roles(role)


@bot.event
async def on_member_leave(member):
	channel = bot.get_channel(1006376115461443644)
	await channel.send(f"Goodbye {member.name}")


# TODO: Find out what this does
@bot.command()
async def update(ctx: commands.Context, message):
	# TODO: Is requests.get correct?
	role = get(ctx.guild.roles, 1010353081638211584)
	if role in ctx.author.roles:
		await ctx.message.delete()
		channel = bot.get_channel(1010268844557873172)
		await channel.send(message)
	else:
		await ctx.send("You cannot do that since you're not a bot developer")


@bot.command()
async def intro(ctx: commands.Context):
	await ctx.send(
		"My name is Jerry. I am the official manager of Slayers. "
		"My job is to make sure that I can help them with whatever they need so that they can focus on their gaming. "
		"I can do many things such as pull their live ranks, remind them of tournaments, and even get transcripts of their calls. "
		"To see what else I can do, just ask me for my help menu."
	)


@bot.command()
async def poke(ctx: commands.Context):
	responses = ["Ouch!", "I'm awake!", "Wha'dyou do that for?", "Hey!"]
	await ctx.send(random.choice(responses))


@bot.event
async def setup_hook():
	# Ensure the database is present
	if not os.path.isfile(DATABASE_PATH):
		with open(DATABASE_PATH, "x") as database:
			data = {"info": {}, "aliases": {}}
			database.write(json.dumps(data))

	# For persistent menus
	bot.add_view(StatsMenu())

	# Load extensions
	for _, _, file_names in os.walk(EXTENSION_DIR):
		for file_name in file_names:
			if file_name.endswith(".py"):
				await bot.load_extension(f"extensions.{file_name[:-3]}")


bot.run(key)
