import discord
async def msg(message, x, p, self):
    msg = x

    #Check if the message was sent by ourselves:
    if msg.author == self.user:
        print('Not a user message.')
        return

    cmd = message.split()
    validcommands = ["!menu", "!cookie", "!pineapple", "!sandwich", "!steak", "!pizza", "!muffin", "!whiskey", "!vodka", "!martini", "!beer", "!rum", "!pinacolada", "!coke", "!tea", "!coffee"]

    if not cmd[0].lower() in validcommands:
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
            embed.description = "<@" + str(msg.author.id) + "> has fed themselves pizza!"
            embed.set_thumbnail(url = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/08/02/16/istock-938742222.jpg")
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Pizzzzzaaaaaa!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a box of pizza!" , color=0x00ff00)
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has fed themselves pizza!"
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
            embed.set_thumbnail(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
            embed.description = "<@" + str(msg.author.id) + "> here's your whiskey! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of whiskey!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://cdn.britannica.com/71/192771-050-CEF9CEC3/Glass-scotch-whiskey-ice.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your whiskey! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "beer"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.set_thumbnail(url = "https://static.turbosquid.com/Preview/001184/092/MC/chinese-beer-barrel-3D_600.jpg")
            embed.description = "<@" + str(msg.author.id) + "> here's your beer! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a beer" , color=0x00ff00)
            embed.set_thumbnail(url = "https://static.turbosquid.com/Preview/001184/092/MC/chinese-beer-barrel-3D_600.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your beer! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "vodka"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.set_thumbnail(url = "https://www.solavia.co.uk/ekmps/shops/solavia2012/images/shot-vodka-glass-pack-of-6-35ml-163-1-p.jpg")
            embed.description = "<@" + str(msg.author.id) + "> has ordered some vodka to drown their sorrows."
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a vodka" , color=0x00ff00)
            embed.set_thumbnail(url = "https://www.solavia.co.uk/ekmps/shops/solavia2012/images/shot-vodka-glass-pack-of-6-35ml-163-1-p.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> has ordered some vodka to drown their sorrows."
            await msg.channel.send(embed = embed)

    if message.startswith(p + "martini"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.set_thumbnail(url = "https://www.liquor.com/thmb/SXyXRSEiNlSIWioGE8GOMb7arPM=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2018__09__05093330__dry-martini-720x720-recipe-8a80821c4ca944849690af8cda90cc03.jpg")
            embed.description = "<@" + str(msg.author.id) + "> here's your martini! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a martini" , color=0x00ff00)
            embed.set_thumbnail(url = "https://www.liquor.com/thmb/SXyXRSEiNlSIWioGE8GOMb7arPM=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2018__09__05093330__dry-martini-720x720-recipe-8a80821c4ca944849690af8cda90cc03.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your martini! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)


    if message.startswith(p + "rum"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.set_thumbnail(url = "https://shop.rammstein.de/img/original/katalog/1617/396/flasche-rum-null-2.jpg")
            embed.description = "<@" + str(msg.author.id) + "> here's your rum! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of rum" , color=0x00ff00)
            embed.set_thumbnail(url = "https://shop.rammstein.de/img/original/katalog/1617/396/flasche-rum-null-2.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your rum! \n\nDon't get too drunk"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "cola"):
        if not x.mentions:
            embed = discord.Embed(title = "Soft drink", color=0x00ff00)
            embed.set_thumbnail(url = "https://i.pinimg.com/originals/33/4d/a7/334da791a8e7df928905484fdab19262.jpg")
            embed.description = "<@" + str(msg.author.id) + "> chugs some coke!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Soft drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of coke" , color=0x00ff00)
            embed.set_thumbnail(url = "https://i.pinimg.com/originals/33/4d/a7/334da791a8e7df928905484fdab19262.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> chugs some coke!"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "coke"):
        if not x.mentions:
            embed = discord.Embed(title = "Soft drink", color=0x00ff00)
            embed.set_thumbnail(url = "https://i.pinimg.com/originals/33/4d/a7/334da791a8e7df928905484fdab19262.jpg")
            embed.description = "<@" + str(msg.author.id) + "> chugs some coke!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Soft drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a bottle of coke" , color=0x00ff00)
            embed.set_thumbnail(url = "https://i.pinimg.com/originals/33/4d/a7/334da791a8e7df928905484fdab19262.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> chugs some coke!"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "tea"):
        if not x.mentions:
            embed = discord.Embed(title = "Hot drink", color=0x00ff00)
            embed.set_thumbnail(url = "https://www.telegraph.co.uk/content/dam/health-fitness/2020/01/09/TELEMMGLPICT000169578515_trans%2B%2BbTl4D02iCM3NuMfK2RT0HTjsyN2j3JnAYXPi059mk8g.jpeg")
            embed.description = "<@" + str(msg.author.id) + "> here's your tea!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hot drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cup of tea" , color=0x00ff00)
            embed.set_thumbnail(url = "https://www.telegraph.co.uk/content/dam/health-fitness/2020/01/09/TELEMMGLPICT000169578515_trans%2B%2BbTl4D02iCM3NuMfK2RT0HTjsyN2j3JnAYXPi059mk8g.jpeg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your tea!"
            await msg.channel.send(embed = embed)


    if message.startswith(p + "coffee"):
        if not x.mentions:
            embed = discord.Embed(title = "Hot drink", color=0x00ff00)
            embed.set_thumbnail(url = "https://www.gannett-cdn.com/-mm-/b2b05a4ab25f4fca0316459e1c7404c537a89702/c=0-0-1365-768/local/-/media/2019/01/18/USATODAY/usatsports/gettyimages-500740897.jpg?width=660&height=372&fit=crop&format=pjpg&auto=webp")
            embed.description = "<@" + str(msg.author.id) + "> here's your coffee!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "Hot drink", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a cup of of coffee" , color=0x00ff00)
            embed.set_thumbnail(url = "https://www.gannett-cdn.com/-mm-/b2b05a4ab25f4fca0316459e1c7404c537a89702/c=0-0-1365-768/local/-/media/2019/01/18/USATODAY/usatsports/gettyimages-500740897.jpg?width=660&height=372&fit=crop&format=pjpg&auto=webp")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your coffee!"
            await msg.channel.send(embed = embed)

    if message.startswith(p + "pinacolada"):
        if not x.mentions:
            embed = discord.Embed(title = "It's time to get drunk!", color=0x00ff00)
            embed.set_thumbnail(url = "https://www.liquor.com/thmb/zPl7fCzXHeHD8uBo4z194OFRabA=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__02__13090826__pina-colada-720x720-recipe-253f1752769447f6998afd2b9469c24e.jpg")
            embed.description = "<@" + str(msg.author.id) + "> here's your pina colada, don't get too drunk!"
            await msg.channel.send(embed = embed)
        for member in x.mentions:
            print(member)
            embed = discord.Embed(title = "It's time to get drunk!", description = "<@" + str(msg.author.id) + "> has given <@" + str(member.id) + "> a pina colada!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://www.liquor.com/thmb/zPl7fCzXHeHD8uBo4z194OFRabA=/735x0/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__02__13090826__pina-colada-720x720-recipe-253f1752769447f6998afd2b9469c24e.jpg")
            if member.id == msg.author.id:
                embed.description = "<@" + str(msg.author.id) + "> here's your pina colada, don't get too drunk!"
            await msg.channel.send(embed = embed)
