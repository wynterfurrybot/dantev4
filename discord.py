import discord
import importlib

from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        prefix = "!"
        fun = __import__("fun")
        await fun.msg(str(message.content), message, prefix, self)
        info = __import__("info")
        await info.msg(str(message.content), message, prefix, self)
        #nsfw = __import__("nsfw.py")
        #roomservice = __import__("roomservice.py")

client = MyClient()
client.run('MyToken')
