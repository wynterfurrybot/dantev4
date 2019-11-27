import discord
import importlib

from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        prefix = "!"
        message.content = message.content.lower()
        fun = __import__("fun")
        await fun.msg(str(message.content), message, prefix, self)
        info = __import__("info")
        await info.msg(str(message.content), message, prefix, self)
        mod = __import__("mod")
        await mod.msg(str(message.content), message, prefix, self)
        #nsfw = __import__("nsfw.py")
        if not message.author.bot:
            if message.content.startswith("!"):
                await message.delete()

client = MyClient()
client.run('MYTOKEN')
