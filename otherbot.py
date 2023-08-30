from dadjokes import Dadjoke
import discord
from discord.ext import commands
import asyncio
from discord.ui import View
import youtube_dl

intents = discord.Intents.all()
intents.members = True


# Prefix
default_prefix = "?"


bot = commands.Bot(command_prefix=default_prefix, intents=intents)
bot.remove_command('help')


# Bot Start / Server List   

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Game(name=f"Over {len(bot.users)}  Members!"))
        print("Der Bot ist Jetzt Online")
        guild = bot.get_guild(1011034093661728878)
        channel = guild.get_channel(1011380519763709972)
        message = ("Bot wurde jetzt gestartet / oder ist schon 12 Stunden Online")
        await channel.send(message)
        channel = guild.get_channel(1011338455881621576)
        guilds = [g.name for g in bot.guilds]
        m = "**Serverlist:**\n\n"
        for i in guilds:
            guild = bot.get_guild(guild.id)
            m = m+i+": \n"
        message = await channel.fetch_message(1011378162631979139)
        await message.edit(content=m)
        await asyncio.sleep(43200)

# Prefix Command


@bot.command()
async def prefix(ctx):
    await ctx.send(f'prefix ist **{default_prefix}**')

# Ping


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000, 1)
    embed = discord.Embed(
        title='🏓 pong', description=f'**:robot: Bot Ping:**\n` {round(bot.latency * 1000)}ms`\n\n**:hourglass: Api Latency:**\n`{latency}ms`')
    embed.set_author(name=f'{ctx.author.name}',
                     icon_url=f'{ctx.author.avatar.url}')
    embed.set_footer(text=f'{ctx.guild.name}',
                     icon_url=f'{ctx.guild.icon.url}')
    await ctx.send(embed=embed)

# Bot Info


@bot.command()
async def botinfo(ctx):
    latency = round(bot.latency * 1000, 1)
    embed = discord.Embed()
    embed.add_field(name="❓ My Prefix is:",
                    value=f"{default_prefix}", inline=False)
    embed.add_field(name="🏓My Ping is:", value=f"{latency}ms")
    embed.add_field(name=" My Developer is:",
                    value=f"<@793887959287857173> | φully", inline=False)
    embed.add_field(name="My Owners are:",
                    value="<@956115149134106677> | REALTM", inline=False)

    embed.add_field(name="🧩 Server", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="👥 Member", value=f"{len(bot.users)}", inline=False)
    embed.set_author(name=f"{ctx.author.name}",
                     icon_url=f'{ctx.author.avatar.url}')
    embed.set_footer(text=f"{ctx.guild.name}",
                     icon_url=f"{ctx.guild.icon.url}")
    await ctx.send(embed=embed)


# Profil Bilder anzeigen (nur sich selber geht erst)
@bot.command(name='avatar', help='fetch avatar of a user')
async def dp(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar
    await ctx.send(userAvatar)

# command eingeben + text = der bot spucht text aus

# announce


@bot.command()
@commands.has_role(1011034393315385457)
async def announce(ctx, *, message=None):
    channel = bot.get_channel(1011306346689339513)
    a = ctx.author.mention
    m = message
    m = a+" \n"+m
    embed = discord.Embed(title=f"New Announcement from {ctx.author}", description=f'{m}')
    embed.set_thumbnail(url=ctx.author.avatar)
    await channel.send(embed=embed)
    await ctx.send("Nachricht Wurde versendet. <#1011306346689339513>")


# Bansystem


@bot.command()
@commands.has_role(1011034393315385457)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:  discord.Member, *, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "Kein Gutes Verhalten!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await member.ban(reason=reason)
    await ctx.send(f"{member} is banned!")

# Help


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="Help", description="Use ?Help <command> for extended information")

    em.add_field(name="Moderation", value="kick','ban,'announce','purge'")
    em.add_field(name="Fun", value="'Avatar'")

    await ctx.send(embed=em)

# Verify


class VerificationMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Click me to Verify', style=discord.ButtonStyle.green, custom_id='verificationmenu:green')
    async def verification(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(self.ctx.guild.roles, id=1011039530880610374)
        await interaction.response.send_message('Verified!', ephemeral=True)
        guild = bot.get_guild(1011034093661728878)
        role = discord.utils.get(guild.roles, name="♰・Member")
        await interaction.response.user.add_roles(role)


async def setup_hook(self) -> None:
    self.add_view(VerificationMenu())


@bot.command()
@commands.has_role(1011034393315385457)
async def verify(ctx: commands.Context):
    await ctx.send("Verification Menu", view=VerificationMenu())


@bot.command()
@commands.has_role(1011034393315385457)
async def nachricht(ctx):
    await ctx.send("nachricht wegen etwas")


@bot.command()
@commands.has_role(1011034393315385457)
async def setup(ctx):
    guild = bot.get_guild(ctx.guild.id)
    await guild.create_text_channel(name="Clan Member: "f"{ctx.guild.member_count}")


# Purge/Clear/Delete
@bot.command(aliases=['purge', 'delete'])
@commands.has_role(1011034393315385457)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 1000000):
    await ctx.channel.purge(limit=amount)
    await ctx.send("https://i.giphy.com/media/tlVLCzWwz8k36/200.gif")
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1011306868213289012)
    embed = discord.Embed(
        title="Welcome!", description=f"{member.mention} Just Joined")
    embed.set_thumbnail(url=member.avatar)
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1011306868213289012)
    embed = discord.Embed(
        title="Byee?!", description=f"{member.mention} is now out!")
    embed.set_thumbnail(url=member.avatar)
    await channel.send(embed=embed)


class reactionrolemenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        min_values=1,
        max_values=1,
        custom_id="reactionrolemenu:age",
        placeholder="Select Age",
        options=[
            discord.SelectOption(label="13-15"),
            discord.SelectOption(label="16+"),
        ],
    )
    async def callback(self, interaction, select):
        await interaction.response.send_message("Callback", ephemeral=True)
        thirteentofifteen = interaction.guild.get_role(1011576338991296572)
        sixteenplus = interaction.guild.get_role(1011576375825670174)
        for i in select.values:
            if i == "13-15":
                await interaction.user.add_roles(thirteentofifteen)
            elif i == "16+":
                await interaction.user.add_roles(sixteenplus)
        if "13-15" not in select.values:
            await interaction.user.remove_roles(thirteentofifteen)
        if "16+" not in select.values:
            await interaction.user.remove_roles(sixteenplus)
    @discord.ui.select(
        min_values=1,
        max_values=5,
        placeholder="Select Pings",
        custom_id="reactionrolemenu:pings",
        options=[
            discord.SelectOption(label="News"),
            discord.SelectOption(label="Giveaway"),
            discord.SelectOption(label="Youtube"),
            discord.SelectOption(label="Important"),
            discord.SelectOption(label="Question"),
        ],
    )
    async def callback2(self, interaction, select):
        await interaction.response.send_message("Callback2", ephemeral=True)
        news = interaction.guild.get_role(1011577326087196733)
        giveaway = interaction.guild.get_role(1011577329245487125)
        youtube = interaction.guild.get_role(1011577332198289448)
        important = interaction.guild.get_role(1011577616236544010)
        question = interaction.guild.get_role(1011578138314158102)
        list1 = [news, giveaway, youtube, important, question]
        for i in select.values:
            if i == "News":
                await interaction.user.add_roles(news)
            elif i == "Giveaway":
                await interaction.user.add_roles(giveaway)
            elif i == "Youtube":
                await interaction.user.add_roles(youtube)
            elif i == "Important":
                await interaction.user.add_roles(important)
            elif i == "Question":
                await interaction.user.add_roles(question)
        if "News" not in select.values:
            await interaction.user.remove_roles(news)
        if "Giveaway" not in select.values:
            await interaction.user.remove_roles(giveaway)
        if "Youtube" not in select.values:
            await interaction.user.remove_roles(youtube)
        if "Important" not in select.values:
            await interaction.user.remove_roles(important)
        if "Question" not in select.values:
            await interaction.user.remove_roles(question)
    # @discord.ui.select(
    #     min_values=1,
    #     max_values=5,
    #     placeholder="Select Platforms",
    #     custom_id="reactionrolemenu:platforms",
    #     options=[
    #         discord.SelectOption(label="PC"),
    #         discord.SelectOption(label="Handy"),
    #         discord.SelectOption(label="Switch"),
    #         discord.SelectOption(label="Xbox"),
    #         discord.SelectOption(label="Playstation"),
    #     ],
    # )
    # async def callback3(self, interaction, select):
    #     await interaction.response.send_message("Callback3", ephemeral=True)
    #     pc = interaction.guild.get_role(1011576798267588729)
    #     handy = interaction.guild.get_role(1011576799517491220)
    #     switch = interaction.guild.get_role(1011577110151827488)
    #     xbox = interaction.guild.get_role(1011577110827110430)
    #     playstation = interaction.guild.get_role(1011577111686959116)
    #     for i in select.values:
    #         if i == "PC":
    #             await interaction.user.add_roles(pc)
    #         elif i == "Handy":
    #             await interaction.user.add_roles(handy)
    #         elif i == "Switch":
    #             await interaction.user.add_roles(switch)
    #         elif i == "Xbox":
    #             await interaction.user.add_roles(xbox)
    #         elif i == "Playstation":
    #             await interaction.user.add_roles(playstation)
    #     if "PC" not in select.values:
    #         await interaction.user.remove_roles(pc)
    #     if "Handy" not in select.values:
    #         await interaction.user.remove_roles(handy)
    #     if "Switch" not in select.values:
    #         await interaction.user.remove_roles(switch)
    #     if "Xbox" not in select.values:
    #         await interaction.user.remove_roles(xbox)
    #     if "Playstation" not in select.values:
    #         await interaction.user.remove_roles(playstation)
    @discord.ui.select(
        min_values=1,
        max_values=5,
        placeholder="Select Games",
        custom_id="reactionrolemenu:games",
        options=[
            discord.SelectOption(label="Minecraft"),
            discord.SelectOption(label="Fortnite"),
            discord.SelectOption(label="Warzone"),
            discord.SelectOption(label="Fallguys"),
            discord.SelectOption(label="Other"),
        ],
    )
    async def callback4(self, interaction, select):
        await interaction.response.send_message("Callback4", ephemeral=True)
        minecraft = interaction.guild.get_role(1011576672182620183)
        fortnite = interaction.guild.get_role(1011576733784354867)
        warzone = interaction.guild.get_role(1011576792160673822)
        fallguys = interaction.guild.get_role(1011576796485005332)
        other_game = interaction.guild.get_role(1011576797185450067)
        for i in select.values:
            if i == "Minecraft":
                await interaction.user.add_roles(minecraft)
            elif i == "Fortnite":
                await interaction.user.add_roles(fortnite)
            elif i == "Warzone":
                await interaction.user.add_roles(warzone)
            elif i == "Fallguys":
                await interaction.user.add_roles(fallguys)
            elif i == "Other":
                await interaction.user.add_roles(other_game)
        if "Minecraft" not in select.values:
            await interaction.user.remove_roles(minecraft)
        if "Fortnite" not in select.values:
            await interaction.user.remove_roles(fortnite)
        if "Warzone" not in select.values:
            await interaction.user.remove_roles(warzone)
        if "Fallguys" not in select.values:
            await interaction.user.remove_roles(fallguys)
        if "Other" not in select.values:
            await interaction.user.remove_roles(other_game)
    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Select gender",
        custom_id="reactionrole:gender",
        options=[
            discord.SelectOption(label="Boy"),
            discord.SelectOption(label="Girl"),
        ],
    )
    async def callback5(self, interaction, select):
        await interaction.response.send_message("Callback5", ephemeral=True)
        boy = interaction.guild.get_role(1011576529244921856)
        girl = interaction.guild.get_role(1011576561205518407)
        for i in select.values:
            if i == "Boy":
                await interaction.user.add_roles(boy)
            elif i == "Girl":
                await interaction.user.add_roles(girl)
        if "Boy" not in select.values:
            await interaction.user.remove_roles(boy)
        if "Girl" not in select.values:
            await interaction.user.remove_roles(girl)
    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Select primary language",
        custom_id="reactionrolemenu:language",
        options=[
            discord.SelectOption(label="English"),
            discord.SelectOption(label="Deutsch"),
            discord.SelectOption(label="Other"),
        ],
    )
    async def callback6(self, interaction, select):
        await interaction.response.send_message("Callback6", ephemeral=True)
        deutsch = interaction.guild.get_role(1011578378454839356)
        english = interaction.guild.get_role(1011578430879436830)
        other_language = interaction.guild.get_role(1011578478639980594)
        for i in select.values:
            if i == "English":
                await interaction.user.add_roles(english)
            elif i == "Deutsch":
                await interaction.user.add_roles(deutsch)
            elif i == "Other":
                await interaction.user.add_roles(other_language)
        if "English" not in select.values:
            await interaction.user.remove_roles(english)
        if "Deutsch" not in select.values:
            await interaction.user.remove_roles(deutsch)
        if "Other" not in select.values:
            await interaction.user.remove_roles(other_language)

@bot.event
async def setup_hook(self) -> None:
    self.add_view(reactionrolemenu())

@bot.command()
async def reactionrole(ctx: commands.Context):
    await ctx.send("Select your roles", view=reactionrolemenu())


@bot.command()
async def joke(ctx):
    joke = Dadjoke()
    await ctx.send(joke.joke)


# Radio

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'playlist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    # bind to ipv4 since ipv6 addresses cause issues sometimes
    'source_address': '0.0.0.0',
}
ffmpeg_options = {
    'options': '-vn',
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(ctx, source, *, data, volume=0.5):
        super().__init__(source, volume)
        ctx.data = data
        ctx.title = data.get('title')
        ctx.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


@bot.command()
async def radio(ctx):
    channel_id = 1011308329391362150
    channel = bot.get_channel(channel_id)
    url = "https://youtube.com/playlist?list=PLO9vVSbHstT3b3PG8PoIyGQq1qqoTqaKH"
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect()
    await ctx.send("Starting radio")
    player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
    ctx.voice_client.play(player, after=lambda e: print(
        f'Player error: {e}') if e else None)


@bot.command()
async def volume(ctx, volume: int):
    channel = ctx.channel.id
    ctx.voice_client.source.volume = volume / 100
    await ctx.send(f"Changed volume to {volume}%")


@bot.command()
async def stop(ctx):
    await ctx.voice_client.disconnect()

class Menu(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Click me to Open Ticket", style=discord.ButtonStyle.red, custom_id="menu:ticket_button")
    async def callback(self, interaction, button):
        guild = bot.get_guild(1011034093661728878)
        owner = guild.get_role(1011034393315385457)
        admin = guild.get_role(1011034449523261620)
        dev = guild.get_role(1011367964622205019)
        ticket_category = discord.utils.get(guild.categories, name="Tickets")
        await interaction.response.send_message("Creating ticket...", ephemeral=True)
        ticket_created_embed = discord.Embed(
            title="Ticket Processed",
            description=f"Hey {interaction.user.name}! Thanks for opening a ticket with us today. Please be as descriptive as possible with your message. It may take some time for our team to get to your ticket but we promise, we will eventually get to it. We thank you in advance for your patience.",
        )
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True),
            guild.me: discord.PermissionOverwrite(view_channel=True),
            owner: discord.PermissionOverwrite(view_channel=True),
            admin: discord.PermissionOverwrite(view_channel=True),
            dev: discord.PermissionOverwrite(view_channel=True),
        }
        ticket = await ticket_category.create_text_channel(
            f"{interaction.user.name}-{interaction.user.discriminator}", overwrites=overwrites)
        await ticket.send(f"This is your ticket {interaction.user.mention}", embed=ticket_created_embed)

@bot.event
async def setup_hook():
    bot.add_view(Menu())

@bot.command()
async def ticket(ctx):
    view = Menu()
    await ctx.send("", view=view)

@bot.command()
async def close(ctx):
    guild = bot.get_guild(1011034093661728878)
    channel = ctx.message.channel
    category = discord.utils.get(guild.categories, name="Tickets")
    if channel in category.text_channels:
        await channel.delete()
    else:
        await ctx.send("Can't delete non-ticket channel", ephemeral=True)

@bot.command()
async def player(ctx, *, message):
    message = message
    await ctx.send(f'**{message}**')
    await ctx.send(f'https://gen.plancke.io/exp/{message}.png')



bot.run("OTc1MjAxODU3Mzg5NjIxMzY5.GzquQ6.4murCHRuPwORUih3L1iJw_IlyqZ3_YFZayFrtw")
