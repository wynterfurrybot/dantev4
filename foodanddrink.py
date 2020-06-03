import discord
async def msg(message, x, p, self):
    msg = x

    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return
    #If not, we can execute commands, such as this simple ping!
    if message.startswith(p + "menu"):
        embed = discord.Embed(title = "Menu!", description = "**__Food__** \nCookie, Pineapple, Sandwich, Steak, Pizza, Muffin \n\n**__Alcohol__** \nWhiskey, Vodka, Martini, Beer, Rum, Pina Colada \n\n**__Non-alcoholic drinks__** \nCoke, Tea, Coffee" , color=0x00ff00)
        await msg.channel.send(embed = embed)

    if message.startswith(p + "cookie"):
        if not x.mentions:
            embed = discord.Embed(title = "Coooookiesssss!",color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your cookie! \n\nJust like the ones mama used to make"
            embed.set_thumbnail(url = "https://images-gmi-pmc.edge-generalmills.com/087d17eb-500e-4b26-abd1-4f9ffa96a2c6.jpg")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Coooookiesssss!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cookie!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your cookie! \n\nJust like the ones mama used to make"
            embed.set_thumbnail(url = "https://images-gmi-pmc.edge-generalmills.com/087d17eb-500e-4b26-abd1-4f9ffa96a2c6.jpg")
            await msg.channel.send(embed = embed)


    if message.startswith(p + "pineapple"):
        if not x.mentions:
            embed = discord.Embed(title = "Pineapple!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your pineapple slices!"
            embed.set_thumbnail(url = "https://www.organicfacts.net/wp-content/uploads/pineapplecalories.jpg")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Pineapple!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> some pineapple slices!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your pineapple slices!"
            embed.set_thumbnail(url = "https://www.organicfacts.net/wp-content/uploads/pineapplecalories.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "sandwich"):
        if not x.mentions:
            embed = discord.Embed(title = "Sandwich!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your Sandwich!"
            embed.set_thumbnail(url = "https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/egg-cress-club-sandwich_0.jpg")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Sandwich!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a sandwich!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your Sandwich!"
            embed.set_thumbnail(url = "https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/egg-cress-club-sandwich_0.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "steak"):
        if not x.mentions:
            embed = discord.Embed(title = "Steak!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your steak!"
            embed.set_thumbnail(url = "https://foremangrillrecipes.com/wp-content/uploads/2013/06/featured-ribeye-steak-foreman-grill.jpg")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Steak!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> some steak!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your steak!"
            embed.set_thumbnail(url = "https://foremangrillrecipes.com/wp-content/uploads/2013/06/featured-ribeye-steak-foreman-grill.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "pizza"):
        if not x.mentions:
            embed = discord.Embed(title = "Pizzzzzaaaaaa!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your pizza! \n\nCaution: hot"
            embed.set_thumbnail(url = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/08/02/16/istock-938742222.jpg")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Pizzzzzaaaaaa!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a box of pizza!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your pizza! \n\nCaution: hot"
            embed.set_thumbnail(url = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/08/02/16/istock-938742222.jpg")
            await msg.channel.send(embed = embed)

    if message.startswith(p + "muffin"):
        if not x.mentions:
            embed = discord.Embed(title = "I wanna die!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> It's muffin time! \n\n*gives you a muffin*"
            embed.set_thumbnail(url = "https://modworkshop.net/mydownloads/previews/preview_3168_1542481291_794f87346e5f426c4c45c7ab3a0711ec.png")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "I wanna die!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a muffin!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> It's muffin time! \n\n*gives you a muffin*"
            embed.set_thumbnail(url = "https://modworkshop.net/mydownloads/previews/preview_3168_1542481291_794f87346e5f426c4c45c7ab3a0711ec.png")
            await msg.channel.send(embed = embed)

    #Drinks:

    if message.startswith(p + "whiskey"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your whiskey! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of whiskey!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your whiskey! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "beer"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your beer! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a beer" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your beer! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "vodka"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your vodka! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a vodka" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your vodka! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "martini"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your martini! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a martini" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your martini! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)


    if message.startswith(p + "rum"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your rum! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of rum" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your rum! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "cola"):
        if not x.mentions:
            embed = discord.Embed(title = "Soft drink", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your coke!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Soft drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of coke" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your coke!"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "coke"):
        if not x.mentions:
            embed = discord.Embed(title = "Soft drink", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your coke!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Soft drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of coke" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your coke!"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "tea"):
        if not x.mentions:
            embed = discord.Embed(title = "Hot drink", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your tea!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hot drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cup of tea" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your tea!"
            await msg.channel.send(embed = embed)


    if message.startswith(p + "coffee"):
        if not x.mentions:
            embed = discord.Embed(title = "Hot drink", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your coffee!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hot drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cup of of coffee" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your coffee!"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "pinacolada"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.description = "<@" + str(msg.author.id) + "> here's your pina colada, don't get too drunk!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a pina colada!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your pina colada, don't get too drunk!"
            await msg.channel.send(embed = embed)
