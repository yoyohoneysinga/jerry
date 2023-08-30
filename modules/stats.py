import json
import time

import discord
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tabulate import tabulate
from webdriver_manager.chrome import ChromeDriverManager

from modules.files import DATABASE_PATH


class StatManager:
	@classmethod
	def get_stats(cls, user, platform):
		results = []
		try:
			driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
			url = f"https://rocketleague.tracker.network/rocket-league/profile/{platform}/{user}/overview"
			driver.get(url)
			time.sleep(3)
			a = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]",
			)
			b = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/div[2]",
			)
			c = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/div[2]",
			)
			d = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div[2]",
			)
			e = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[2]/div[2]",
			)
			f = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[2]/div[2]",
			)
			g = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[2]/div[2]",
			)
			h = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[2]/div[2]",
			)
			i = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div",
			)
			j = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div[2]/div[1]/div",
			)
			k = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div[2]/div[1]/div",
			)
			l = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[3]/div/div[2]/div[1]/div",
			)
			m = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[3]/div/div[2]/div[1]/div",
			)
			n = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[3]/div/div[2]/div[1]/div",
			)
			o = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[3]/div/div[2]/div[1]/div",
			)
			p = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[3]/div/div[2]/div[1]/div",
			)
			q = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[6]/div[2]",
			)
			r = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[6]/div[2]",
			)
			s = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[6]/div[2]",
			)
			t = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[6]/div[2]",
			)
			u = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[6]/div[2]",
			)
			v = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[6]/div[2]",
			)
			w = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[6]/div[2]",
			)
			x = driver.find_element(
				"xpath",
				"/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[6]/div[2]",
			)
			temp = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x]
			for i in temp:
				print(f"Before: {i}")
				i = i.text
				i = i.replace("WinStrk", "+")
				i = i.replace("LossStrk", "-")
				i = i.replace("  ", " ")
				i = cls.minimize(i)
				print(f"After {i}")
				print()
				results.append(i)
		except:
			driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
			url = f"https://rocketleague.tracker.network/rocket-league/profile/{platform}/{user}/overview"
			driver.get(url)
			time.sleep(3)
			a = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]",
			)
			b = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/div[2]",
			)
			c = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/div[2]",
			)
			d = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div[2]",
			)
			e = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[2]/div[2]",
			)
			f = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[2]/div[2]",
			)
			g = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[2]/div[2]",
			)
			h = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[2]/div[2]",
			)
			i = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div",
			)
			j = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div[2]/div[1]/div",
			)
			k = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div[2]/div[1]/div",
			)
			l = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[3]/div/div[2]/div[1]/div",
			)
			m = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[3]/div/div[2]/div[1]/div",
			)
			n = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[3]/div/div[2]/div[1]/div",
			)
			o = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[3]/div/div[2]/div[1]/div",
			)
			p = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[3]/div/div[2]/div[1]/div",
			)
			q = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[6]/div[2]",
			)
			r = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[6]/div[2]",
			)
			s = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[6]/div[2]",
			)
			t = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]/td[6]/div[2]",
			)
			u = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[6]/td[6]/div[2]",
			)
			v = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[6]/div[2]",
			)
			w = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]/td[6]/div[2]",
			)
			x = driver.find_element(
				"xpath",
				"/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[6]/div[2]",
			)
			temp = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x]
			for i in temp:
				print(f"Before: {i}")
				i = i.text
				i = i.replace("WinStrk", "+")
				i = i.replace("LossStrk", "-")
				i = i.replace("  ", " ")
				i = cls.minimize(i)
				print(f"After {i}")
				print()
				results.append(i)
		return results

	@classmethod
	def minimize(cls, string: str):
		replacements = {
			"Supersonic Legend": "SSL",
			"Grand Champion": "GC",
			"Champion": "C",
			"Diamond": "D",
			"Platinum": "P",
			"Gold": "G",
			"Silver": "S",
			"Bronze": "B",
			"Division": "D",
			"I": 1,
			"II": 2,
			"III": 3,
			"IV": 4,
		}

		for snippet, replacement in replacements.items():
			if snippet in string:
				string = string.replace(snippet, replacement)

		string = string.replace(" ", "")
		return string

	@classmethod
	def statistics(cls, user, platform):
		stats = cls.get_stats(user, platform)
		data = [
			["Ranked Duel 1v1", stats[0], stats[8], stats[16]],
			["Ranked Doubles 2v2", stats[1], stats[9], stats[17]],
			["Ranked Standard 3v3", stats[2], stats[10], stats[18]],
			["Hoops", stats[3], stats[11], stats[19]],
			["Rumble", stats[4], stats[12], stats[20]],
			["Dropshot", stats[5], stats[13], stats[21]],
			["Snowday", stats[6], stats[14], stats[22]],
			["Tournament Matches", stats[7], stats[15], "N/A"],
		]
		df = pd.DataFrame(data, columns=["Gamemode", "Rank", "MMR", "Streak"])
		return tabulate(df, headers="keys", tablefmt="fancy_grid")

	@classmethod
	def average_rank(cls, list1):
		total = 0
		rank2num = {
			"Bronze I Division I": 1,
			"Bronze I Division II": 2,
			"Bronze I Division III": 3,
			"Bronze I Division IV": 4,
			"Bronze II Division I": 5,
			"Bronze II Division II": 6,
			"Bronze II Division III": 7,
			"Bronze II Division IV": 8,
			"Bronze III Division I": 9,
			"Bronze III Division II": 10,
			"Bronze III Division III": 11,
			"Bronze III Division IV": 12,
			"Silver I Division I": 13,
			"Silver I Division II": 14,
			"Silver I Division III": 15,
			"Silver I Division IV": 16,
			"Silver II Division I": 17,
			"Silver II Division II": 18,
			"Silver II Division III": 19,
			"Silver II Division IV": 20,
			"Silver III Division I": 21,
			"Silver III Division II": 22,
			"Silver III Division III": 23,
			"Silver III Division IV": 24,
			"Gold I Division I": 25,
			"Gold I Division II": 26,
			"Gold I Division III": 27,
			"Gold I Division IV": 28,
			"Gold II Division I": 29,
			"Gold II Division II": 30,
			"Gold II Division III": 31,
			"Gold II Division IV": 32,
			"Gold III Division I": 33,
			"Gold III Division II": 34,
			"Gold III Division III": 35,
			"Gold III Division IV": 36,
			"Platinum I Division I": 37,
			"Platinum I Division II": 38,
			"Platinum I Division III": 39,
			"Platinum I Division IV": 40,
			"Platinum II Division I": 41,
			"Platinum II Division II": 42,
			"Platinum II Division III": 43,
			"Platinum II Division IV": 44,
			"Platinum III Division I": 45,
			"Platinum III Division II": 46,
			"Platinum III Division III": 47,
			"Platinum III Division IV": 48,
			"Diamond I Division I": 49,
			"Diamond I Division II": 50,
			"Diamond I Division III": 51,
			"Diamond I Division IV": 52,
			"Diamond II Division I": 53,
			"Diamond II Division II": 54,
			"Diamond II Division III": 55,
			"Diamond II Division IV": 56,
			"Diamond III Division I": 57,
			"Diamond III Division II": 58,
			"Diamond III Division III": 59,
			"Diamond III Division IV": 60,
			"Champion I Division I": 61,
			"Champion I Division II": 62,
			"Champion I Division III": 63,
			"Champion I Division IV": 64,
			"Champion II Division I": 65,
			"Champion II Division II": 66,
			"Champion II Division III": 67,
			"Champion II Division IV": 68,
			"Champion III Division I": 69,
			"Champion III Division II": 70,
			"Champion III Division III": 71,
			"Champion III Division IV": 72,
			"Grand Champion I Division I": 73,
			"Grand Champion I Division II": 74,
			"Grand Champion I Division III": 75,
			"Grand Champion I Division IV": 76,
			"Grand Champion II Division I": 77,
			"Grand Champion II Division II": 78,
			"Grand Champion II Division III": 79,
			"Grand Champion II Division IV": 80,
			"Grand Champion III Division I": 81,
			"Grand Champion III Division II": 82,
			"Grand Champion III Division III": 83,
			"Grand Champion III Division IV": 84,
			"Supersonic Legend I Division I": 85,
		}
		for i in list1:
			total += rank2num[i]
		total = round(float(total) / 7.0)
		rank = [k for k, v in rank2num.items() if v == total]
		return rank

	@classmethod
	def average_mmr(cls, list1):
		total = 0
		for i in list1:
			total += int(i)
		mmr = total / 7
		mmr = int(round(mmr))
		return mmr

	@classmethod
	def get_average(cls, user, platform):
		stats = cls.get_stats(user, platform)
		rank = cls.average_rank(stats[:7])
		mmr = cls.average_mmr(stats[8:-1])
		return f"Average Rank: {rank[0]}\nAverage MMR: {mmr}"

	# TODO: Find out what this method does, and make a better name for it
	@classmethod
	def edit_statistics(cls, user, platform, cols, rows):
		stats = cls.get_stats(user, platform)

		data = [
			["Ranked Duel 1v1", stats[0], stats[8], stats[16]],
			["Ranked Doubles 2v2", stats[1], stats[9], stats[17]],
			["Ranked Standard 3v3", stats[2], stats[10], stats[18]],
			["Hoops", stats[3], stats[11], stats[19]],
			["Rumble", stats[4], stats[12], stats[20]],
			["Dropshot", stats[5], stats[13], stats[21]],
			["Snowday", stats[6], stats[14], stats[22]],
			["Tournament Matches", stats[7], stats[15], "N/A"],
		]
		df = pd.DataFrame(data, columns=["Gamemode", "Rank", "MMR", "Streak"])
		a = []
		cols2 = ["Gamemode", "Rank", "MMR", "Streak"]
		rows2 = [
			"Ranked Duel 1v1",
			"Ranked Doubles 2v2",
			"Ranked Standard 3v3",
			"Hoops",
			"Rumble",
			"Dropshot",
			"Snowday",
			"Tournament Matches",
		]
		cols = list(set(cols2) - set(cols))
		rows = list(set(rows2) - set(rows))
		for i in cols:
			a.append(i)
		df = df.drop(labels=a, axis=1)
		# df = df[~df['Gamemode'].isin(rows)] # Exact Matches
		for i in rows:
			df = df[~df.Gamemode.str.contains(i)]  # String in
		return tabulate(df, headers="keys", tablefmt="fancy_grid")


# Stats Menu
class StatsMenu(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)

		self.rows = []
		self.cols = []

		self.add_item(StatsSelection(self.rows, self.cols, row=1))
		self.add_item(GamemodeSelection(self.rows, self.cols, row=2))
		self.add_item(StatsConfirmButton(self.rows, self.cols, row=3))


class StatsSelection(discord.ui.Select):
	"""
	Dropdown select class for stats
	"""

	def __init__(self, rows: list, cols: list, row: int | None = None):
		self.rows = rows
		self.cols = cols

		options = [
			discord.SelectOption(
				label="All",
				description="Load rank, MMR, and streak for selected gamemode(s)",
			),
			discord.SelectOption(
				label="Rank", description="Load rank for selected gamemode(s)"
			),
			discord.SelectOption(
				label="MMR", description="Load MMR for selected gamemode(s)"
			),
			discord.SelectOption(
				label="Streak", description="Load streak for selected gamemode(s)"
			),
		]
		super().__init__(
			placeholder="Select stats",
			min_values=1,
			max_values=3,
			options=options,
			custom_id="menu:stats",
			row=row,
		)

	async def callback(self, interaction: discord.Interaction):
		# Uses list slicing to set the values of self.cols to ["Gamemode"]
		self.cols[:] = ["Gamemode"]
		for i in self.values:
			if i == "All":
				self.cols.append("Rank")
				self.cols.append("MMR")
				self.cols.append("Streak")
			else:
				self.cols.append(i)
		await interaction.response.send_message("Settings saved", ephemeral=True)


class GamemodeSelection(discord.ui.Select):
	"""
	Dropdown select class for Rocket League gamemodes
	"""

	def __init__(self, rows: list, cols: list, row: int | None = None):
		self.rows = rows
		self.cols = cols

		options = [
			discord.SelectOption(label="All", description="Loads stats for all modes"),
			discord.SelectOption(
				label="Competitive Modes",
				description="Loads stats for all competitive modes",
			),
			discord.SelectOption(
				label="Extra Modes", description="Loads stats for all extra modes"
			),
			discord.SelectOption(
				label="Ranked Duel 1v1", description="Loads stats for 1v1"
			),
			discord.SelectOption(
				label="Ranked Doubles 2v2", description="Loads stats for 2v2"
			),
			discord.SelectOption(
				label="Ranked Standard 3v3", description="Loads stats for 3v3"
			),
			discord.SelectOption(label="Hoops", description="Loads stats for Hoops"),
			discord.SelectOption(label="Rumble", description="Loads stats for Rumble"),
			discord.SelectOption(
				label="Dropshot", description="Loads stats for Dropshot"
			),
			discord.SelectOption(
				label="Snowday", description="Loads stats for Snowday"
			),
			discord.SelectOption(
				label="Tournament Matches",
				description="Loads stats for Tournament Matches",
			),
		]
		super().__init__(
			placeholder="Select gamemodes",
			min_values=1,
			max_values=7,
			options=options,
			custom_id="menu:gamemodes",
			row=row,
		)

	async def callback(self, interaction: discord.Interaction):
		self.rows[:] = []
		for i in self.values:
			if i == "All":
				self.rows.append("Ranked Duel 1v1")
				self.rows.append("Ranked Doubles 2v2")
				self.rows.append("Ranked Standard 3v3")
				self.rows.append("Hoops")
				self.rows.append("Rumble")
				self.rows.append("Dropshot")
				self.rows.append("Snowday")
				self.rows.append("Tournament Matches")
			elif i == "Competitive Modes":
				self.rows.append("Ranked Duel 1v1")
				self.rows.append("Ranked Doubles 2v2")
				self.rows.append("Ranked Standard 3v3")
			elif i == "Extra Modes":
				self.rows.append("Hoops")
				self.rows.append("Rumble")
				self.rows.append("Dropshot")
				self.rows.append("Snowday")
			else:
				self.rows.append(i)
		await interaction.response.send_message("Settings saved", ephemeral=True)


class StatsConfirmButton(discord.ui.Button):
	def __init__(self, rows: list, cols: list, row: int | None = None):
		super().__init__(label="Confirm Selections", style=discord.ButtonStyle.green, custom_id="menu:confirm", row=row)

		self.rows = rows
		self.cols = cols

	async def callback(self, interaction: discord.Interaction):
		# await interaction.response.send_message("Settings saved")

		# TODO: Test to make sure this works
		self.style = discord.ButtonStyle.grey

		await interaction.response.defer()  # TODO: Find out what defer() means
		await interaction.followup.send("Loading Stats...", ephemeral=True)

		with open(DATABASE_PATH) as file:
			data = json.load(file)

		user = interaction.user.name
		if user in data["info"]:
			result = StatManager.edit_statistics(data["info"]["name"], data["info"]["platform"], self.cols, self.rows)
			await interaction.followup.send(f"```\n{result}\n```")
		else:
			await interaction.followup.send("You are not registered!")
