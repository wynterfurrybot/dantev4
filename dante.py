import discord
import importlib

from discord.ext import commands

channels = [725776681159098408, 728691486115233804, 738967638964830341, 725566843766571112, 732288159060328529, 739199815627440232, 730887667491012720, 729753696199508088]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        prefix = "!"
        staff = False
        message.content = message.content.lower()
        if 'dark' in message.content and 'cute' in message.content:
            await message.delete()
        if message.guild.id == 725201209358549012:
            for role in message.author.roles:
                if role.id  == 739727880799518741:
                    staff = True
            if 'discord.gg' in message.content:
                if staff == True:
                    return
                if message.channel.id in channels:
                    return
                await message.channel.send("<@" + str(message.author.id) + "> Please do not promote your server here! \n\nIf you're looking to partner, please check <#729753696199508088>")
                await message.delete()
        mentions = message.mentions
        if len(mentions) > 3:
            if not message.author.bot:
                if message.content.startswith("!"):
                    await message.delete()
                    await message.channel.send("<@" + str(message.author.id) + "> Too many mentions!")
                    return
        fun = __import__("fun")
        await fun.msg(str(message.content), message, prefix, self)
        info = __import__("info")
        await info.msg(str(message.content), message, prefix, self)
        mod = __import__("mod")
        await mod.msg(str(message.content), message, prefix, self)
        christmas = __import__("christmas")
        await christmas.msg(str(message.content), message, prefix, self)
        food = __import__("foodanddrink")
        await food.msg(str(message.content), message, prefix, self)
        nsfw = __import__("nsfw")
        await nsfw.msg(str(message.content), message, prefix, self)
        if not message.author.bot:
            if message.content.startswith("!"):
                await message.delete()

client = MyClient()
client.run('YourTokenHere')
