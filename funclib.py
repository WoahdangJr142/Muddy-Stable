import discord
import random

def operation_embed(ctx, role, message, operation_type=None, template_link=None, image=None):
    embed=discord.Embed(
        title="Military Operation!",
        color = discord.Color.dark_gold()
    )
    if image is not None:
        embed.set_thumbnail(url=image)
    embed.add_field(name="Template Link", value=template_link, inline=False)
    embed.add_field(name=f"{operation_type}", value=f"{message}", inline=False)
    return embed


def random_emoji():
    rand_emoji_list=[
        '<:mikuddy:1034491405411827783>',
        '<:muddy:1017260706384588881>',
        '<:rizzy:1156237117471588383>',
        '<:buddy:957635711870316634>',
        '<:buddydrip:980532836262101062>',
        '<:buggy:999127555405783070>',
        'https://media.discordapp.net/attachments/954714002217398345/1158444261226852373/ezgif-3-8d760c9895.gif?ex=651c44ca&is=651af34a&hm=67657ad4379643ab079837a6b5403bc46b6937d3e1bf75b904dfa78f84c11b3f&',
        '<:boi:957675700742144090>',
        '<:bubbly:1040357807830093824>',
        '<:bahamabuddy:988181032434012210>',
        '<:fella~1:1119261067911114834>',
        '<:grubbyGun1:997215219153653892><:grubbyGun2:997215226179104788>',
        '<:guy:970318484242309181>',
        '<:hot_buddy:1019977604427685939>',
        '<:jollyBuddy:1049690540813328385>',
        '<:kruddy:1053142956556701786>',
        '<:metty:1055163919188103218>',
        '<:mikuddy:1034491405411827783>',
        '<:mate~1:1053797959743053864>',
        '<:nyuddy:1057463244773671042>',
        '<:Pallycursed:958807997503660062>',
        '<:luiddy:1143995706017849504>',
        '<:tuddycursed:991718123797495828>'
    ]
    emoji=random.choice(rand_emoji_list)
    return emoji


def create_embed(
        title=None, description=None, url=None, colour=None, 
        timestamp=None, author_name=None, author_url=None, 
        author_icon=None, footer_text=None, footer_icon=None, 
        thumbnail=None, image=None, fields=None):
    
    embed = disnake.Embed(
        title=title,
        description=description,
        url=url,
        colour=colour or disnake.Colour.default(),
        timestamp=timestamp,
    )

    if author_name:
        embed.set_author(name=author_name, url=author_url, icon_url=author_icon)

    if footer_text:
        embed.set_footer(text=footer_text, icon_url=footer_icon)

    if thumbnail:
        if isinstance(thumbnail, str):
            embed.set_thumbnail(url=thumbnail)
        elif isinstance(thumbnail, io.BytesIO):
            embed.set_thumbnail(file=disnake.File(thumbnail, filename='thumbnail.png'))

    if image:
        if isinstance(image, str):
            embed.set_image(url=image)
        elif isinstance(image, io.BytesIO):
            embed.set_image(file=disnake.File(image, filename='image.png'))

    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

    return embed