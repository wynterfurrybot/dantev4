import discord
from datetime import datetime
import pymysql.cursors
async def msg(message, x, p, self):
    msg = x
    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!
    if message == p + "info":
        embed = discord.Embed(title = "Info", description = 'Made by: Darkmane Arweinyd \nWith help by: Alex Malebogh \n\nPing: ___Took {0}'.format(round(self.latency, 1)) + "ms___" , color=0x00ff00)
        await msg.channel.send(embed = embed)

    if message.startswith(p + "s"):
        embed = discord.Embed(title=msg.guild.name, color=0x00ff00)
        embed.add_field(name="Owner", value=msg.guild.owner, inline=False)
        embed.add_field(name="Date of creation", value=msg.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Region", value=msg.guild.region, inline=False)
        embed.set_thumbnail(url = msg.guild.icon_url)
        await msg.channel.send(embed=embed)

    if message.startswith(p + "u"):
        for user in x.mentions:
            connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='password',
                                 db='dante',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT * FROM cases WHERE `userid`=%s"
                cursor.execute(sql, (user.id,))
                result = cursor.rowcount
                print(result)
                embed = discord.Embed(description = str(user.name) + "#" +str(user.discriminator) , color = 0x00ff00)
                embed.set_thumbnail(url = user.avatar_url)
                embed.add_field(name = "Name:", value = user.display_name, inline = True)
                embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = True)
                embed.add_field(name = "Date Joined:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = True)
                embed.add_field(name = "Strikes (All servers)", value = result, inline = True)
                await msg.channel.send(embed = embed)
