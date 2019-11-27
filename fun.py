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
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has hugged themselves! \n\nWhat a loner.."
            embed.set_thumbnail(url = "https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "glomp"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Glomp!", description = "<@" + str(msg.author.id) + "> has flopped on top of <@" + str(member.id) + ">!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has glomped themselves! \n\nWhat a loner.."
            embed.set_thumbnail(url = "https://d.facdn.net/art/zaezar/1502813432/1502813432.zaezar_glomp.png")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "cookie"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Cooooooooookieesss!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cookie!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://cdn.shopify.com/s/files/1/0043/8471/8938/products/154360576926714891_812x.jpg?v=1555127662")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "lick"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Slurp!", description = "<@" + str(msg.author.id) + "> has licked <@" + str(member.id) + ">, giving them a bath!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has gieven themselves a bath!"
            embed.set_thumbnail(url = "https://t2.ea.ltmcdn.com/en/images/0/7/5/why_do_cats_lick_each_other_2570_600_square.jpg")
            await msg.channel.send(embed = embed)
