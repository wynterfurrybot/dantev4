import discord
from datetime import datetime
from discord.utils import get
async def msg(message, x, p, self):
    msg = x
    hasperms = False

    if msg.author.guild_permissions.kick_members:
        hasperms = True

    if hasperms == False:
        return

    if message.startswith(p + "hackban"):
        if not msg.author.guild_permissions.ban_members:
            hasperms = False
        if not hasperms:
            return
        params = message.split()
        bannedusers = 0
        for users in params:
            if users == "!hackban":
                print("no user")
            else:
                bannedusers = bannedusers +1
                print(users)
                user = await self.fetch_user(int(users))
                await msg.guild.ban(user)
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        embed = discord.Embed(title = "Ban!", description = "<@" + str(msg.author.id) + "> has hackbanned " + str(bannedusers) + " users!\n" + message , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        await channel.send(embed = embed)

    if message.startswith(p + "ban"):
        if not msg.author.guild_permissions.ban_members:
            hasperms = False
        if not hasperms:
            return
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Ban!", description = "<@" + str(msg.author.id) + "> has banned <@" + str(member.id) + ">!\n" + message , color=0x00ff00)
            if member.id == msg.author.id:
                return
            await msg.guild.ban(member)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)

    if message.startswith(p + "clear"):
        mess = message.split(" ")
        mess[1] = int(mess[1]) + 1
        if int(mess[1]) > 100:
            mess[1] = 100
        if int(mess[1]) < 2:
            mess[1] = 2
        await msg.channel.purge(limit= int(mess[1]))
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        await channel.send(str(mess[1]) + " messages removed from #" + msg.channel.name)

    if message.startswith(p + "kick"):
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Kick!", description = "<@" + str(msg.author.id) + "> has kicked <@" + str(member.id) + ">! \n\n**" + message + "**" , color=0x00ff00)
            if member.id == msg.author.id:
                return
            await msg.guild.kick(member)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)

    if message.startswith(p + "warn"):
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Warn!", description = "<@" + str(msg.author.id) + "> has warned <@" + str(member.id) + ">! \n\n**" + message + "**", color=0x00ff00)
            if member.id == msg.author.id:
                return
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)


    if message.startswith(p + "mute"):
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Muted!", description = "<@" + str(msg.author.id) + "> has muted <@" + str(member.id) + ">! \n\n**" + message + "**", color=0x00ff00)
            if member.id == msg.author.id:
                return
            role = get(member.guild.roles, name="Muted")
            await member.add_roles(role)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)
