import discord
from datetime import datetime
from discord.utils import get
async def msg(message, x, p, self):
    msg = x
    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!
    if message.startswith(p + "snowball"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Snowball!", description = "<@" + str(msg.author.id) + "> has thrown a snowball directly at <@" + str(member.id) + ">'s face!" , color=0x00ff00)
            if member.id == msg.author.id:
                return
            embed.set_thumbnail(url = "http://d.facdn.net/art/olypixandstuff/1265692624/1265692624.olypixandstuff_1263408058.sapphwolf_snowballfight2.png")
            await msg.channel.send(embed = embed)
