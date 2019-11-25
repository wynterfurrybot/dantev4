import discord
async def msg(message, x, p, self):
    msg = x

    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!
    if message == p + "ping":
        embed = discord.Embed(title = "Pong!", description = '___Took {0}'.format(round(self.latency, 1)) + "ms___" , color=0x00ff00)
        await msg.channel.send(embed = embed)

    if message == "f":
        await msg.channel.send("<@" + str(msg.author.id) + "> has paid respects")

    if message.startswith(p + "hug"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hug!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a hug!" , color=0x00ff00)
            embed.set_image(url = "https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "cookie"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Cooooooooookieesss!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cookie!" , color=0x00ff00)
            embed.set_image(url = "https://cdn.shopify.com/s/files/1/0043/8471/8938/products/154360576926714891_812x.jpg?v=1555127662")
            await msg.channel.send(embed = embed)
