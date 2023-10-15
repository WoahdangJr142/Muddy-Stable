import discord
import os
import sys
import subprocess
import random
import validators
from dotenv import load_dotenv
from discord.ext import commands
from discord import default_permissions
from discord.ext import tasks


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

load_dotenv()

bot.help_command=None

bot_owner = [621481279132663828]
power_users = [839138084712873984, 313264660826685440, 398912653491437573]


#Startup confirmation message
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! Version {discord.__version__}')
    muddy_chain.start()


@bot.event
async def on_guild_join(guild):
    print(f'Joined a new guild: {guild.name} (ID: `{guild.id}`)')


@bot.event
async def on_guild_remove(guild):
    print(f'Removed from a guild: {guild.name} (ID: {guild.id})')


@bot.event
async def on_command_error(ctx, error):
    print(f"Error in command {ctx.command}: {error}")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"Command on cooldown. Try again in {error.retry_after:.2f} seconds.")


# Basic ping command. Responds with "Pong! <Latency in ms>"
@bot.slash_command(description="Returns the average ping in ms of the bot.")
@commands.cooldown(3, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.respond('Pong! `{0} ms`'.format(round(bot.latency * 1000, 2)))


# Gracefully restarts the bot
@bot.slash_command(description="Restart the bot")
async def restart(ctx) -> None:
    # Check if the user invoking the command is in the allowed list
    if ctx.author.id in bot_owner or ctx.author.id in power_users:
        await ctx.respond('Restarting...', ephemeral=True)
        subprocess.Popen(['python', 'restart_bot.py'])  # Start the restart script
        await bot.close()  # Close the bot gracefully
    else:
        await ctx.respond('You do not have permission to restart the bot.', ephemeral=True)

#Safely stops the bot
@bot.slash_command()
async def stop(ctx):
    if ctx.author.id in bot_owner or ctx.author.id in power_users:
        await ctx.respond("Shutting Down", ephemeral=True)
        await bot.close()
        await sys.exit()
    else:
        await ctx.respond("You do not have permission to shut down the bot.", ephemeral=True)


'''
#Send a list of all commands !!MUST MANUALLY EDIT!!
@bot.slash_command(description="Gives you a list of all commands and what they do, as well as any arguments that can be given.")
@commands.cooldown(3, 5, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description="A list of all commands and what they do, as well as any arguments that can be given.",
        color=discord.Color.green()
    )

    embed.add_field(name="Help :question:", value=f"```{bot.command_prefix}help\nGives you this message.```", inline=False)
    embed.add_field(name="Ping :signal_strength:", value=f"```{bot.command_prefix}ping\nSends a message containing the response time in ms.```", inline=False)
    embed.add_field(name="Important Links :link:", value=f"```{bot.command_prefix}links\nGives different invite links with various functions.```", inline=False)
    embed.add_field(name="Kill :skull:", value=f"```{bot.command_prefix}kill\nKill a user with a random death message.\nargs: user```", inline=False)

    await ctx.respond(embed=embed)
'''


@bot.slash_command(description="A list of important links.")
async def links(ctx):
    embed = discord.Embed(
        title="**Important Links**",
        color=discord.Color.red()
    )
    embed.add_field(name="**Bot Invite**", value="[Limited permissions](https://discord.com/api/oauth2/authorize?client_id=809491842621505607&permissions=39859447654720&scope=bot)\n[Full Permissions](https://discord.com/api/oauth2/authorize?client_id=809491842621505607&permissions=8&scope=bot)", inline=False)
    embed.add_field(name="**Server Invite**", value="[Watermelon Province](https://dsc.gg/WaPro)", inline=False)
    embed.add_field(name="**The Chromatic Empire**", value="[Website](https://chromatic.zone)\n[Discord](https://discord.gg/Hb4gtWseBb)\n[Wiki](https://wiki.pxls.space/index.php?title=Chromatic_Empire)\n[Reddit](https://www.reddit.com/r/chromatic/)\n[Twitter/X](https://twitter.com/chromaticzone)\n[Bluesky](https://bsky.app/profile/chromatic.zone)", inline=False)
    embed.add_field(name="**Misc**", value="[Github](https://github.com/WoahdangJr142/MuddyBot/tree/main)")

    await ctx.respond(embed=embed)


@bot.slash_command(description="Kill the specified user")
@commands.cooldown(3, 5, commands.BucketType.user)
async def kill(ctx, user: discord.User):
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
    f"Oops! In {ctx.author.mention}'s attempt to kill <@USER>, they slipped on a banana peel and were dead before hitting the ground",
    f"Oops! {ctx.author.mention} forgot which drink they poisoned and drank the wrong one",
    f"Zamn, it looks like {ctx.author.mention} dropped the dynamite at their own feet"
]
    
    if user == ctx.author:
        await ctx.respond("You can't kill yourself!")
    else:
        rand_kill = random.choice(rand_kill_lst)
        rand_kill_mention = rand_kill.replace("<@USER>", f"{user.mention}")
        embed = discord.Embed(
            color = discord.Color.greyple()
        )
        embed.add_field(name="", value=rand_kill_mention, inline=False)
        
        await ctx.respond(embed=embed)


@bot.slash_command(description="DM all valid members for a military operation.")
async def operation(ctx, role: discord.Role, *, message, template_link, operation_type, image=None):
    successful = []
    failed = []
    should_send=True

    # Check if template_link and image are valid URLs
    if template_link and not validators.url(template_link):
        await ctx.respond(f"Invalid URL provided for template_link: {template_link}", ephemeral=True)
        should_send=False
        pass
    if image and not validators.url(image):
        await ctx.respond(f"Invalid URL provided for image: {image}", ephemeral=True)
        should_send=False
        pass

    embed=discord.Embed(
        title="Military Operation!",
        color = discord.Color.dark_gold()
    )
    if image is not None:
        embed.set_thumbnail(url=image)
    embed.add_field(name="Template Link", value=template_link, inline=False)
    embed.add_field(name=f"{operation_type}", value=f"{message}", inline=False)

    if should_send==True:
        if ctx.author.id in bot_owner or ctx.author.id in power_users:
            for member in role.members:
                if member.bot:# or member==ctx.author:
                    continue
                try:
                    await member.send(embed=embed)
                    successful.append(member.mention)
                except Exception as error:
                    print(error)
                    await ctx.author.send(f"Couldn't DM {member}.\nReason: {error}")
                    failed.append(member.mention)

            await ctx.respond(f'Success! "{message}" sent to {successful}.\nFailed to send to {failed}.\nPreview:', embed=embed, ephemeral=True)
        else:
            await ctx.respond("You do not have permission to run this command.", ephemeral=True)


@bot.slash_command(name="count_members_in_role")
async def count_members_in_role(ctx, role: discord.Role):
    count=0
    for member in role.members:
        count=count+1
    await ctx.respond(f"There are {count} members that have the role {role.mention}.", ephemeral=True)


@tasks.loop(hours=1)
async def muddy_chain():
    channel=bot.get_channel(983032616380940368)
    await channel.send("<:muddy:1017260706384588881>")


bot.run(os.getenv("token_main"))