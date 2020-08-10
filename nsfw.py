import discord


async def msg(message, x, p, self):
    msg = x

    # Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    # If not, we can execute commands, such as this simple ping!

    cmd = message.split()
    validcommands = ["!yiff", "!breed", "!suck"]

    if not cmd[0].lower() in validcommands:
        return

    if message.startswith(p + "yiff"):
        if not msg.channel.is_nsfw():
            embed = discord.Embed(
                title="Not A NSFW channel!", description="The channel you just ran the command in is not NSFW.", color=0x00ff00)
            embed.set_thumbnail(
                url="https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed=embed)
            return
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title="H..harder daddy!", description="<@" + str(
                msg.author.id) + "> has yiffed <@" + str(member.id) + "> hard!", color=0x00ff00)
            if member.id == msg.author.id:
                embed.title = "Solo Scene!"
                embed.description = "<@" + \
                    str(msg.author.id) + "> has gone to jack off"
                embed.set_thumbnail(
                    url="https://pbs.twimg.com/media/DOIOPZcX4AUraEw.jpg")
            else:
                embed.set_thumbnail(
                    url="https://ci.phncdn.com/videos/201812/04/195030881/original/(m=eaAaGwObaaaa)(mh=0KDlKJW31QShbuqU)14.jpg")
            await msg.channel.send(embed=embed)

    if message.startswith(p + "breed"):
        if not msg.channel.is_nsfw():
            embed = discord.Embed(
                title="Not A NSFW channel!", description="The channel you just ran the command in is not NSFW.", color=0x00ff00)
            embed.set_thumbnail(
                url="https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed=embed)
            return
        for member in x.mentions:
            if member.id == msg.author.id:
                return
            print(member)
            embed = discord.Embed(title="GIVE ME YOUR CUBS!", description="<@" + str(
                msg.author.id) + "> has impregnated <@" + str(member.id) + ">!", color=0x00ff00)
            embed.set_thumbnail(
                url="https://us.rule34.xxx//images/364/3db9b8b409f5100aafc62f6352d31db1c60f3c64.png")
            await msg.channel.send(embed=embed)

    if message.startswith(p + "suck"):
        if not msg.channel.is_nsfw():
            embed = discord.Embed(
                title="Not A NSFW channel!", description="The channel you just ran the command in is not NSFW.", color=0x00ff00)
            embed.set_thumbnail(
                url="https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            await msg.author.send(embed=embed)
            return
        for member in x.mentions:
            if member.id == msg.author.id:
                return
            print(member)
            embed = discord.Embed(title="Spitters are quitters.", description="<@" + str(
                msg.author.id) + "> has sucked off <@" + str(member.id) + ">!", color=0x00ff00)
            embed.set_thumbnail(
                url="https://w1680.luscious.net/laise/342630/frrbq_22_01DBK73R7KYGJDX9X3D0972X8A.1680x0.jpg")
            await msg.channel.send(embed=embed)
