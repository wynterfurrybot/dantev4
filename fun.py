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

    if message == "x":
        await msg.channel.send("<@" + str(msg.author.id) + "> very much has doubts about this")

    if message == "make me a sandwich":
        await msg.channel.send("<@" + str(msg.author.id) + "> I can't... I have no condiments")

    if message == "what is the meaning of life?":
        await msg.channel.send("<@" + str(msg.author.id) + "> 42")

    if message == "kill yourself dante":
        await msg.channel.send("<@" + str(msg.author.id) + "> no u")

    if message.startswith(p + "hug"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hug!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a hug!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has hugged themselves! \n\nWhat a loner.."
            embed.set_thumbnail(url = "https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "cuddle"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hug!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a hug!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has hugged themselves! \n\nWhat a loner.."
            embed.set_thumbnail(url = "https://pm1.narvii.com/6362/398e5e2edeed52fc23d9e85cbbbbe6e5b3951635_hq.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "snuggle"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Snuggle!", description = "<@" + str(msg.author.id) + "> has snuggled <@" + str(member.id) + "> tightly!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has snuggled themselves! \n\nWhat a loner.."
            embed.set_thumbnail(url = "https://66.media.tumblr.com/e7cc512f3e136d610c0c0780e045dbe3/tumblr_p25tmi3fJg1wchqdto1_400.png")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "slap"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Trout Slap!", description = "<@" + str(msg.author.id) + "> slaps <@" + str(member.id) + "> around a bit with a wet trout!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has slapped themselves with a wet trout! \n\nWut?"
            embed.set_thumbnail(url = "https://i.pinimg.com/600x315/c7/eb/77/c7eb77dfaa7628a6c3438cd0139bcb78.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "nuzzle"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Nuzzle!", description = "<@" + str(msg.author.id) + "> has nuzzled <@" + str(member.id) + ">!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> attempts to nuzzle themselves! \n\nUhhhh..??"
            embed.set_thumbnail(url = "https://pm1.narvii.com/6427/42cdd0b2870e26482cd6907bce2edca12a82286c_hq.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "pat"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Pat!", description = "<@" + str(msg.author.id) + "> has pat <@" + str(member.id) + "> softly on the head!" , color=0x00ff00)
            if member.id == msg.author.id:
                return
            embed.set_thumbnail(url = "https://d.facdn.net/art/itsmekurisu/1550247117/1550247117.itsmekurisu_corrina.png")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "throwdict"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Do u even knowledge?", description = "<@" + str(msg.author.id) + "> has thrown a dictionary at <@" + str(member.id) + ">, landing softly on their head!" , color=0x00ff00)
            if member.id == msg.author.id:
                return
            embed.set_thumbnail(url = "https://i.imgur.com/n58IlmY.png")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "bap"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Bad furry!", description = "<@" + str(msg.author.id) + "> has bapped <@" + str(member.id) + "> on the nose with a newspaper!" , color=0x00ff00)
            if member.id == msg.author.id:
                return
            embed.set_thumbnail(url = "https://i.ytimg.com/vi/dNrwSeMY-bk/hqdefault.jpg")
            await msg.channel.send(embed = embed)

    if message == p + "rubs":
        embed = discord.Embed(title = "Belly rubs!", description = "<@" + str(msg.author.id) + "> demands belly rubs!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://cdn1.cloudcanvas.website/media/sites/119/2018/01/26063531/Belly-rub.jpg")
        await msg.channel.send(embed = embed)

    if message == p + "howl":
        embed = discord.Embed(title = "AwooooOooooo!", description = "<@" + str(msg.author.id) + "> has let out a big howl!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://d.facdn.net/art/windwo1f/1484617505/1484617505.windwo1f_wintie_s_howl.png")
        await msg.channel.send(embed = embed)

    if message == p + "growl":
        embed = discord.Embed(title = "A light growl was heard!", description = "<@" + str(msg.author.id) + "> has let out a growl!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://pm1.narvii.com/6219/8faceb03db01e5c8e64b87dc8fa6d3e18a08011e_hq.jpg")
        await msg.channel.send(embed = embed)

    if message.startswith(p + "boop"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Boop!", description = "<@" + str(msg.author.id) + "> has booped <@" + str(member.id) + ">!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has booped themselves.. now their nose hurts!"
            embed.set_thumbnail(url = "https://i.pinimg.com/originals/4c/02/bd/4c02bdb8056ef9bb3883f38eb59d4b8e.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "bite"):
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Bite!", description = "<@" + str(msg.author.id) + "> has nibbled at <@" + str(member.id) + ">'s ear!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has bit themselves.. now their hand hurts!"
            embed.set_thumbnail(url = "https://i.pinimg.com/originals/d3/83/57/d383575a560d2cdc413d5945ea608286.png")
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
