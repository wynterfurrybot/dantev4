import discord
from datetime import datetime
from discord.utils import get
async def msg(message, x, p, self):
    msg = x
    hasperms = False

    cmd = message.split()
    validcommands = [p + "hackban", p + "ban", p + "kick", p + "mute", p + "warn", p+ "clear", p+"unmute", p+ "approve"]

    if not cmd[0].lower() in validcommands:
        return

    if message.startswith(p + "hackban"):
        if msg.author.guild_permissions.ban_members:
            hasperms = True

        if not hasperms:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
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
        if msg.author.guild_permissions.ban_members:
            hasperms = True

        if not hasperms:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return

        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        if not x.mentions:
            await x.delete()
            params = message.split()
            for users in params:
                if users == "!ban":
                    print("no user")
                else:
                    user = await self.fetch_user(int(users))
                    if user.id == msg.author.id:
                        return
                    embed = discord.Embed(title = "Ban!", description = "<@" + str(msg.author.id) + "> has banned <@" + str(user.id) + ">!\n" + message , color=0x00ff00)
                    await user.send("You have been banned from " + msg.guild.name + "\nThe reasoning can be found below: \n\n" + message)
                    await msg.guild.ban(user)
                    embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
                    await channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Ban!", description = "<@" + str(msg.author.id) + "> has banned <@" + str(member.id) + ">!\n" + message , color=0x00ff00)
            if member.id == msg.author.id:
                return
            await member.send("You have been banned from " + msg.guild.name)
            await msg.guild.ban(member)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)

    if message.startswith(p + "clear"):
        if msg.author.guild_permissions.kick_members:
            hasperms = True

        if hasperms == False:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
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
        if msg.author.guild_permissions.kick_members:
            hasperms = True

        if hasperms == False:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        if not x.mentions:
            await x.delete()
            params = message.split()
            for users in params:
                if users == "!kick":
                    print("no user")
                else:
                    user = await self.fetch_user(int(users))
                    if user.id == msg.author.id:
                        return
                    embed = discord.Embed(title = "Kick!", description = "<@" + str(msg.author.id) + "> has kicked <@" + str(user.id) + ">!\n" + message , color=0x00ff00)
                    await user.send("You have been kicked from " + msg.guild.name)
                    await msg.guild.kick(user)
                    embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
                    await channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Kick!", description = "<@" + str(msg.author.id) + "> has kicked <@" + str(member.id) + ">! \n\n**" + message + "**" , color=0x00ff00)
            if member.id == msg.author.id:
                return
            await member.send("You have been kicked from " + msg.guild.name + "\nThe reasoning can be found below: \n\n" + message)
            await msg.guild.kick(member)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)

    if message.startswith(p + "approve"):
        if msg.author.guild_permissions.kick_members:
            hasperms = True

        if hasperms == False:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        if not x.mentions:
            await x.delete()
            params = message.split()
            for users in params:
                if users == "!approve":
                    print("no user")
                else:
                    user = x.guild.get_member(int(users))
                    role = get(x.guild.roles, name="New Floof")
                    await user.remove_roles(role)
                    role = get(x.guild.roles, name="Verified Floof")
                    await user.add_roles(role)
                    await x.channel.send("Approved")

        for member in x.mentions:
            role = get(x.guild.roles, name="New Floof")
            await member.remove_roles(role)
            role = get(x.guild.roles, name="Verified Floof")
            await member.add_roles(role)
            await x.channel.send("Approved")


    if message.startswith(p + "warn"):
        if msg.author.guild_permissions.kick_members:
            hasperms = True

        if hasperms == False:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        if not x.mentions:
            await x.delete()
            params = message.split()
            for users in params:
                if users == "!warn":
                    print("no user")
                else:
                    user = await self.fetch_user(int(users))
                    if user.id == msg.author.id:
                        return
                    embed = discord.Embed(title = "Warn!", description = "<@" + str(msg.author.id) + "> has warned <@" + str(user.id) + ">!\n" + message , color=0x00ff00)
                    await user.send("You have been warned on " + msg.guild.name + "\nThe reasoning can be found below: \n\n" + message)
                    embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
                    await channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Warn!", description = "<@" + str(msg.author.id) + "> has warned <@" + str(member.id) + ">! \n\n**" + message + "**", color=0x00ff00)
            if member.id == msg.author.id:
                return
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await member.send("You have been warned on " + msg.guild.name + "\nThe reasoning can be found below: \n\n" + message)
            await channel.send(embed = embed)

    if message.startswith(p + "mute"):
        if msg.author.guild_permissions.kick_members:
            hasperms = True

        if hasperms == False:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        if not x.mentions:
            await x.delete()
            params = message.split()
            for users in params:
                if users == "!mute":
                    print("no user")
                else:
                    user = x.guild.get_member(int(users))
                    if user.id == msg.author.id:
                        return
                    embed = discord.Embed(title = "Mute!", description = "<@" + str(msg.author.id) + "> has muted <@" + str(user.id) + ">!\n" + message , color=0x00ff00)
                    if x.guild.id == 725201209358549012:
                        role = get(x.guild.roles, name="Verified Floof")
                        await user.remove_roles(role)
                    role = get(x.guild.roles, name="Muted")
                    await user.add_roles(role)
                    await user.send("You have been muted on " + msg.guild.name + "\nThe reasoning can be found below: \n\n" + message)
                    embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
                    await channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Muted!", description = "<@" + str(msg.author.id) + "> has muted <@" + str(member.id) + ">! \n\n**" + message + "**", color=0x00ff00)
            if member.id == msg.author.id:
                return
            if x.guild.id == 725201209358549012:
                role = get(x.guild.roles, name="Verified Floof")
                await member.remove_roles(role)
            role = get(member.guild.roles, name="Muted")
            await member.add_roles(role)
            await member.send("You have been muted on " + msg.guild.name + "\nThe reasoning can be found below: \n\n" + message)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)

    if message.startswith(p + "unmute"):
        if msg.author.guild_permissions.kick_members:
            hasperms = True

        if hasperms == False:
            embed = discord.Embed(title = "No Permissions!", description = "You do not have permission to run " + message + " in " + msg.guild.name, color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        channel = get(x.guild.channels, name="case_logs", type=discord.ChannelType.text)
        if not x.mentions:
            await x.delete()
            params = message.split()
            for users in params:
                if users == "!unmute":
                    print("no user")
                else:
                    user = x.guild.get_member(int(users))
                    if user.id == msg.author.id:
                        return
                    embed = discord.Embed(title = "Unmute!", description = "<@" + str(msg.author.id) + "> has unmuted <@" + str(user.id) + ">!\n" + message , color=0x00ff00)
                    if x.guild.id == 725201209358549012:
                        role = get(x.guild.roles, name="Verified Floof")
                        await user.add_roles(role)
                    role = get(x.guild.roles, name="Muted")
                    await user.remove_roles(role)
                    await user.send("You have been now been unmuted on " + msg.guild.name)
                    embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
                    await channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Unmuted!", description = "<@" + str(msg.author.id) + "> has unmuted <@" + str(member.id) + ">! \n\n**" + message + "**", color=0x00ff00)
            if member.id == msg.author.id:
                return
            role = get(member.guild.roles, name="Muted")
            if x.guild.id == 725201209358549012:
                role = get(x.guild.roles, name="Verified Floof")
                await user.add_roles(role)
            await member.remove_roles(role)
            await member.send("You have now been unmuted on " + msg.guild.name)
            embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
            await channel.send(embed = embed)
