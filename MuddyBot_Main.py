import discord
import os
import sys
import subprocess
import random
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()

bot = commands.Bot(command_prefix=';', intents=intents)
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
        await ctx.send(f"Sorry, I don't recognize that command. Type `{bot.command_prefix}help` for a list of available commands.")


# Basic ping command. Responds with "Pong! <Latency in ms>"
@bot.command()
async def ping(ctx):
    await ctx.channel.send('Pong! `{0} ms`'.format(round(bot.latency * 1000, 2)))


# Gracefully restarts the bot
@bot.command()
async def restart(ctx):
    # Check if the user invoking the command is in the allowed list
    if ctx.author.id in bot_owner or ctx.author.id in power_users:
        await ctx.send('Restarting...')
        subprocess.Popen(['python', 'restart_bot.py'])  # Start the restart script
        await bot.close()  # Close the bot gracefully
    else:
        await ctx.send('You do not have permission to restart the bot.')

#Safely stops the bot
@bot.command()
async def stop(ctx):
    if ctx.author.id in bot_owner or ctx.author.id in power_users:
        await ctx.channel.send("Shutting Down")
        await bot.close()
        await sys.exit()
    else:
        await ctx.channel.send("You do not have permission to shut down the bot.")

#Send a list of all commands !!MUST MANUALLY EDIT!!
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description="Gives you a list of all commands and what they do, as well as any arguments that can be given.",
        color=discord.Color.green()
    )

    embed.add_field(name="Help :question:", value=f"```{bot.command_prefix}help\nGives you this message.```", inline=False)
    embed.add_field(name="Ping :signal_strength:", value=f"```{bot.command_prefix}ping\nSends a message containing the response time in ms.```", inline=False)
    embed.add_field(name="Invite :desktop:", value=f"```{bot.command_prefix}invite\nGives different invite links with various functions.```", inline=False)
    embed.add_field(name="Kill :skull:", value=f"```{bot.command_prefix}kill\nKill a user with a random death message.\nargs: user```", inline=False)

    await ctx.channel.send(embed=embed)

#Send an invite to Watermelon Province
@bot.command()
async def invite(ctx):
    embed = discord.Embed(
        title="Invite the Bot or Join the Server!",
        color=discord.Color.red()
    )
    embed.add_field(name="Bot Invite", value="[Limited permissions](https://discord.com/api/oauth2/authorize?client_id=809491842621505607&permissions=39859447654720&scope=bot)\n[Full Permissions](https://discord.com/api/oauth2/authorize?client_id=809491842621505607&permissions=8&scope=bot)", inline=False)
    embed.add_field(name="Server Invite", value="[Watermelon Province](https://dsc.gg/WaPro)", inline=False)

    await ctx.channel.send(embed=embed)

@bot.command()
async def kill(ctx, user: discord.Member = None):
    rand_kill_lst = [
    "<@target> picked a fight with buddy and brought down the wrath of ChE upon themselves.",
    "<@target> mocked Rizzy. Big mistake.",
    f"The pxls mods found <@target>'s {random.randrange(1, 51)} alts.",
    "<@target> posted cringe and got banned :nerd: :nerd:",
    "<@target> didn't place 50k pixels by the end of the canvas.",
    "Uh oh, looks like target> forgot to place for opcellog.",
    "<@target> got Lainpilled.",
    "<@target> drank too much pineapple juice.",
    "<@target> took a whiff of Liam's socks and dropped dead on the spot.",
    "<@target> stopped placing for the Chromatic Empire.",
    "Turns out <@target> didn't post in https://discord.com/channels/954714002217398342/983032616380940368 today...",
    "<@target> got taken out by NSIA agents. Wait, did you hear anything?",
    "<@target> unfollowed @chromatic.zone on Bluesky.",
    f"<@target> got stabbed in a back ally by {ctx.author.mention}.",
    f"<@target> got shot by {ctx.author.mention}'s seventh bullet from their six-shooter.",
    "<@target> got blinded by the new moon. :new_moon:"
]
    
    if user is None:
        await ctx.send("Please mention a valid user to kill.")
    elif user == ctx.author:
        await ctx.send("You can't kill yourself!")
    else:
        rand_kill = random.choice(rand_kill_lst)
        rand_kill_mention = rand_kill.replace("<@target>", f"{user.mention}")
        embed = discord.Embed(
            description=f"{user.mention} has been killed by {ctx.author.mention}!",
            color = discord.Color.greyple()
        )
        embed.add_field(name="", value=rand_kill_mention, inline=False)
        
        await ctx.send(embed=embed)


bot.run(os.getenv("token_main"))  
