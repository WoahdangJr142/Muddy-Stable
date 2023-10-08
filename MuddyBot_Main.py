import discord
import os
import sys
import subprocess
import random
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=';', intents=intents)
intents.message_content = True
load_dotenv()

bot.help_command=None

bot_owner = [621481279132663828]
power_users = []

#Startup confirmation message
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! Version {discord.__version__}')

#Command not recognized handling
@bot.event
async def on_command_error(ctx, error):
    print(f"Error in command {ctx.command}: {error}")
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply(f"Sorry, I don't recognize that command. Type `{bot.command_prefix}help` for a list of available commands.")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"Command on cooldown. Try again in {error.retry_after:.2f} seconds.")


# Basic ping command. Responds with "Pong! <Latency in ms>"
@bot.command()
@commands.cooldown(3, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.reply('Pong! `{0} ms`'.format(round(bot.latency * 1000, 2)))


# Gracefully restarts the bot
@bot.command()
async def restart(ctx):
    # Check if the user invoking the command is in the allowed list
    if ctx.author.id in bot_owner or ctx.author.id in power_users:
        await ctx.reply('Restarting...')
        subprocess.Popen(['python', 'restart_bot.py'])  # Start the restart script
        await bot.close()  # Close the bot gracefully
    else:
        await ctx.reply('You do not have permission to restart the bot.')

#Safely stops the bot
@bot.command()
async def stop(ctx):
    if ctx.author.id in bot_owner or ctx.author.id in power_users:
        await ctx.reply("Shutting Down")
        await bot.close()
        await sys.exit()
    else:
        await ctx.reply("You do not have permission to shut down the bot.")

#Send a list of all commands !!MUST MANUALLY EDIT!!
@bot.command()
@commands.cooldown(3, 5, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description="Gives you a list of all commands and what they do, as well as any arguments that can be given.",
        color=discord.Color.green()
    )

    embed.add_field(name="Help :question:", value=f"```{bot.command_prefix}help\nGives you this message.```", inline=False)
    embed.add_field(name="Ping :signal_strength:", value=f"```{bot.command_prefix}ping\nSends a message containing the response time in ms.```", inline=False)
    embed.add_field(name="Important Links :link:", value=f"```{bot.command_prefix}links\nGives different invite links with various functions.```", inline=False)
    embed.add_field(name="Kill :skull:", value=f"```{bot.command_prefix}kill\nKill a user with a random death message.\nargs: user```", inline=False)

    await ctx.reply(embed=embed)

#Send an invite to Watermelon Province
@bot.command()
async def links(ctx):
    embed = discord.Embed(
        title="**Important Links**",
        color=discord.Color.red()
    )
    embed.add_field(name="**Bot Invite**", value="[Limited permissions](https://discord.com/api/oauth2/authorize?client_id=809491842621505607&permissions=39859447654720&scope=bot)\n[Full Permissions](https://discord.com/api/oauth2/authorize?client_id=809491842621505607&permissions=8&scope=bot)", inline=False)
    embed.add_field(name="**Server Invite**", value="[Watermelon Province](https://dsc.gg/WaPro)", inline=False)
    embed.add_field(name="**The Chromatic Empire**", value="[Website](https://chromatic.zone)\n[Discord](https://discord.gg/Hb4gtWseBb)\n[Wiki](https://wiki.pxls.space/index.php?title=Chromatic_Empire)\n[Reddit](https://www.reddit.com/r/chromatic/)\n[Twitter/X](https://twitter.com/chromaticzone)\n[Bluesky](https://bsky.app/profile/chromatic.zone)", inline=False)
    embed.add_field(name="**Misc**", value="[Github](https://github.com/WoahdangJr142/MuddyBot/tree/main)")

    await ctx.reply(embed=embed)

@bot.command()
@commands.cooldown(3, 5, commands.BucketType.user)
async def kill(ctx, user: discord.Member = None):
    rand_kill_lst = [
    "<@USER> picked a fight with buddy and brought down the wrath of ChE upon themselves",
    "<@USER> mocked Rizzy - big mistake",
    f"The pxls mods found <@USER>'s {random.randrange(1, 51)} alts",
    "<@USER> posted cringe and got banned :nerd: :nerd:",
    f"<@USER> didn't place {random.randrange(1, 21)}.{random.randrange(1, 10)}k pixels by the end of the canvas",
    "Uh oh, looks like <@USER> forgot to place for opcellog",
    "<@USER> drank too much pineapple juice",
    "<@USER> took a whiff of Liam's socks and dropped dead on the spot",
    "<@USER> stopped placing for the Chromatic Empire",
    "Turns out <@USER> didn't post in #buddy-chain today...",
    "<@USER> got taken out by NSIA agents. Wait, did you hear anything?",
    "<@USER> unfollowed @chromatic.zone on [Bluesky](https://bsky.app/profile/chromatic.zone)",
    f"<@USER> got stabbed in a back alley by {ctx.author.mention}",
    f"<@USER> got shot by {ctx.author.mention}'s seventh bullet from their six-shooter",
    "<@USER> got blinded by the new moon :new_moon:",
    "<@USER> griefed the Minecraft server and got banned",
    "<@USER> didn't join the Clash of Clans clan",
    "<@USER> didn't join the Clash Royale clan",
    "<@USER> didn't join the Roblox Group",
    "<@USER> hasn't registered their pxls account with ChromaBot",
    "<@USER> didn't participate in ChE Game Night",
    "<@USER> posted a meme in #general",
    "<@USER> isn't a part of Watermelon Province",
    f"Oops! In {ctx.author.mention}'s attempt to kill <@USER>, they slipped on a banana peel and was dead before hitting the ground",
    f"Oops! {ctx.author.mention} forgot which drink they poisoned and drank the wrong one",
    f"Zamn, it looks like {ctx.author.mention} dropped the dynamite at their own feet"
]
    
    if user is None:
        await ctx.reply("Please mention a valid user to kill.")
    elif user == ctx.author:
        await ctx.reply("You can't kill yourself!")
    else:
        rand_kill = random.choice(rand_kill_lst)
        rand_kill_mention = rand_kill.replace("<@USER>", f"{user.mention}")
        embed = discord.Embed(
            #description=f"**{user.mention} has been killed by {ctx.author.mention}!**",
            color = discord.Color.greyple()
        )
        embed.add_field(name="", value=rand_kill_mention, inline=False)
        
        await ctx.reply(embed=embed)

#@bot.command()
#async def test(ctx):
#    await ctx.reply(f"<@USER> didn't place {random.randrange(1, 21)}.{random.randrange(1, 10)}k pixels by the end of the canvas")

bot.run(os.getenv("token_main"))
