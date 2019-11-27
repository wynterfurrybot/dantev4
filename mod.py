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
