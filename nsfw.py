import discord
async def msg(message, x, p, self):
    msg = x

    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!
    if message.startswith(p + "yiff"):
        if not msg.channel.is_nsfw():
            embed = discord.Embed(title = "Not A NSFW channel!", description = "The channel you just ran the command in is not NSFW." , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed = embed)
            return
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Yiff!", description = "<@" + str(msg.author.id) + "> has yiffed <@" + str(member.id) + "> hard!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has gone to jack off"
                embed.set_thumbnail(url = "https://pbs.twimg.com/media/DOIOPZcX4AUraEw.jpg")
            else:
                embed.set_thumbnail(url = "https://ci.phncdn.com/videos/201812/04/195030881/original/(m=eaAaGwObaaaa)(mh=0KDlKJW31QShbuqU)14.jpg")
            await msg.channel.send(embed = embed)
