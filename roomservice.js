const talkedRecently = new Set();
var colors = require('colors');

console.log("Error".red);
console.log("Warning".yellow);
console.log("Log".cyan);
console.log("Success".green);

const { Client, MessageEmbed } = require('discord.js');
const fc = new Client();

var invites = {};

fc.on('ready', () => {
    console.log(`Logged in as ${fc.user.tag}!`.green);
    fc.user.setActivity(`Eating Pi | !help`);

    fc.guilds.forEach(g => {
    g.fetchInvites().then(guildInvites => {
      invites[g.id] = guildInvites;
})
})
});

var regex = RegExp(/[^a-zA-Z\d\s:]/g);

fc.on('guildMemberRemove', member => {
  if (member.guild.id === "667466143585402900"){

    fc.channels.fetch("667495189832794162").then(channel =>{
      channel.send(member.user.username + " has left, they will be missed")
    })
  }
})

fc.on('guildMemberAdd', member => {
  if(member.guild.id === "736969969404870688"){
    	member.send("Welcome to the elite server of european furries! \n\nJust so you know, we operate a scrict no robot policy here! \n\nTo verify you're not one, please go to https://verify.furrycentr.al/ef/ and log in with discord.");
  }
  if (member.guild.id === "667466143585402900"){

    fc.channels.fetch("667495189832794162").then(channel =>{
      channel.send("<@" + member.id + "> has joined the server!")
    })

    member.send("Hello " + member.user.username + " and welcome to Cuddle Club! Please answer these small questions and post them in the initiation (<#667495506251087902>) channel within the server! \n\nName:\nAge:\nPronouns:\nTimezone:\nA little bit about yourself:\nHow you found the server:\n\nOnce you fill this out please give staff 24 hours to review and approve you")

  }

  if (member.guild.id === "462041783438934036" || member.guild.id === "667466143585402900" || member.guild.id === "736969969404870688"){
    member.guild.fetchInvites().then(guildInvites => {
     try{
       const ei = invites[member.guild.id];

      invites[member.guild.id] = guildInvites;

       const invite = guildInvites.find(i => ei.get(i.code).uses < i.uses);

       const inviter = fc.users.get(invite.inviter.id);

       if(member.guild.id === "736969969404870688"){
         fc.channels.fetch("736981136164782171").then(channel =>{

         const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('New Joiner')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription(member.user.username + ' Joined using invite code ' + invite.code + ' made by <@' + invite.inviter.id + '> (' + inviter.username + ')');
       channel.send(embed);
     })
   }

       else if (member.guild.id === "667466143585402900"){
         fc.channels.fetch("713624679671136306").then(channel =>{

         const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('New Joiner')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription(member.user.username + ' Joined using invite code ' + invite.code + ' made by <@' + invite.inviter.id + '> (' + inviter.username + ')');
       channel.send(embed);
       })
       }

       else if (member.guild.id === "462041783438934036"){
            fc.channels.fetch("539917043886063636").then(channel =>{
              const embed = new MessageEmbed()
             // Set the title of the field
             .setTitle('New Joiner')
             // Set the color of the embed
             .setColor(0xff0000)
             // Set the main content of the embed
             .setDescription(member.user.username + ' Joined using invite code ' + invite.code + ' made by <@' + invite.inviter.id + '> (' + inviter.username + ')');
          channel.send(embed);

          })
        }
     }

     catch{
       if (member.guild.id === "667466143585402900"){
         fc.channels.fetch("713624679671136306").then(channel =>{

         const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('New Joiner')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription("I can't quite figure out how " + member.user.username + " joined the server. \n\nMaybe they used a temporary invite?")
       channel.send(embed);


       })
       }

       else if (member.guild.id === "736969969404870688"){
         fc.channels.fetch("736981136164782171").then(channel =>{

         const embed = new MessageEmbed()
        // Set the title of the field
        .setTitle('New Joiner')
        // Set the color of the embed
        .setColor(0xff0000)
        // Set the main content of the embed
        .setDescription("I can't quite figure out how " + member.user.username + " joined the server. \n\nMaybe they used a temporary invite?")
       channel.send(embed);


       })
       }

       else if (member.guild.id === "462041783438934036"){
            fc.channels.fetch("539917043886063636").then(channel =>{
              const embed = new MessageEmbed()
             // Set the title of the field
             .setTitle('New Joiner')
             // Set the color of the embed
             .setColor(0xff0000)
             // Set the main content of the embed
             .setDescription("I can't quite figure out how " + member.user.username + " joined the server. \n\nMaybe they used a temporary invite?")
          channel.send(embed);

          })
        }
     }

 })
}



	if(regex.test(member.user.username.match))
	{
		console.log("Username matched filter");
		try{
		console.log("Attempted change");

		if (member.guild.id === "462041783438934036"){
		fc.channels.fetch("462044318421745664").then(channel =>{
		channel.send("<@&462043912169586699> Please check the latest name for <@" + newmem.id + ">");
		})
		}

		else{
			fc.channels.fetch("634061513635790858").then(channel =>{
		channel.send("<@&634061152456015872> Please check the latest name for <@" + newmem.id + ">");
		})
		}
		}

		catch (err){
			console.log(err);
			if (member.guild.id === "462041783438934036"){
		fc.channels.fetch("462044318421745664").then(channel =>{
		channel.send("<@&462043912169586699> Please check the latest name for <@" + newmem.id + ">");
		})
		}

		else{
			fc.channels.fetch("634061513635790858").then(channel =>{
		channel.send("<@&634061152456015872> Please check the latest name for <@" + newmem.id + ">");
		})
		}
			newmem.setNickname("Please change");
		}
	}

  if(member.guild.id != "462041783438934036") return;
	member.send("Welcome to The Floof Hotel! \n\nJust so you know, we operate a scrict no robot policy here! \n\nTo verify you're not one, please go to https://verify.furrycentr.al/ and log in with discord.");
})

fc.on('guildMemberUpdate', (oldmem, newmem) => {

if(regex.test(newmem.user.username) && oldmem.user.username != newmem.user.username)
	{
		console.log("Username matched filter");
		try{
		console.log("Attempted change");
		if (member.guild.id === "462041783438934036"){
		fc.channels.fetch("462044318421745664").then(channel =>{
		channel.send("<@&462043912169586699> Please check the latest name for <@" + newmem.id + ">");
		})
		}

		else{
			fc.channels.fetch("634061513635790858").then(channel =>{
		channel.send("<@&634061152456015872> Please check the latest name for <@" + newmem.id + ">");
		})
		}
		}

		catch (err){
			console.log(err);
			if (member.guild.id === "462041783438934036"){
		fc.channels.fetch("462044318421745664").then(channel =>{
		channel.send("<@&462043912169586699> Please check the latest name for <@" + newmem.id + ">");
		})
		}

		else{
			fc.channels.fetch("634061513635790858").then(channel =>{
		channel.send("<@&634061152456015872> Please check the latest name for <@" + newmem.id + ">");
		})
		}

			newmem.setNickname("Please change");
		}
	}

	if(regex.test(newmem.nickname) && oldmem.nickname != newmem.nickname)
	{
		console.log("Username matched filter");
		try{
		console.log("Attempted change");
		if (member.guild.id === "462041783438934036"){
		fc.channels.fetch("462044318421745664").then(channel =>{
		channel.send("<@&462043912169586699> Please check the latest name for <@" + newmem.id + ">");
		})
		}

		else{
			fc.channels.fetch("634061513635790858").then(channel =>{
		channel.send("<@&634061152456015872> Please check the latest name for <@" + newmem.id + ">");
		})
		}
		}

		catch (err){
			console.log(err);
			if (member.guild.id === "462041783438934036"){
		fc.channels.fetch("462044318421745664").then(channel =>{
		channel.send("<@&462043912169586699> Please check the latest name for <@" + newmem.id + ">");
		})
		}

		else{
			fc.channels.fetch("634061513635790858").then(channel =>{
		channel.send("<@&634061152456015872> Please check the latest name for <@" + newmem.id + ">");
		})
		}

			newmem.setNickname("Please change");
		}
	}

	var roles = newmem.roles.array();
    var oldroles = oldmem.roles.array();
	var hasmember = false;

	oldroles.forEach(function(role){
		if (role.id === "462042250612965386" || role.id === '725462565852938301' || role.id === '667472170926080011' || role.id === "736971909362614362")
		{
			hasmember = true;
		}

	})

	roles.forEach(function(role){

    if (role.id === "736971909362614362" && hasmember === false)
    {
      fc.channels.fetch("736979363362373642").then(channel => channel.send("<a:wel:742119488366837780><a:come:742119500068946084>"));
      fc.channels.fetch("736979363362373642").then(channel => channel.send("Welcome <@" + newmem.id + "> to the most elite group of european furs! \n\nI hope you enjoy your stay here, and here's a free cookie to welcome you! :cookie:"));
    }

    if (role.id === "725462565852938301" && hasmember === false)
		{
      fc.channels.fetch("725476791858495508").then(channel => channel.send("<a:wel:742119488366837780><a:come:742119500068946084>"));
			fc.channels.fetch("725476791858495508").then(channel => channel.send("Welcome <@" + newmem.id + "> to the coolest club around! Club Floof! \n\nFeel free to go ahead and grab some roles in <#742103877582848173>!\n\nI hope you enjoy your stay here, and here's a free cookie to welcome you! :cookie: \n\n<@&736666911189893170> Please welcome the above user!"));

    }

		if (role.id === "462042250612965386" && hasmember === false)
		{
      fc.channels.fetch("629056060803645453").then(channel => channel.send("<a:wel:742119488366837780><a:come:742119500068946084>"));
      fc.channels.fetch("629056060803645453").then(channel => channel.send("<@" + newmem.id + ">, Welcome, welcome! We hope you enjoy your stay at The Floof Hotel!  *hands room card* \n\nYour room number is " + Math.floor(Math.random() * 5670) + "\n\nOn the desk is a free :cookie:, should you need us at any point, feel free to ping a member of staff! Should you have any feedback about anything, feel free to visit <#681616342733815825>! \n\nFeel free to tell us about you and your fursona in <#552957610899275776> \n\n<@&463088144292511764> Please welcome the above user!"));
		}

    if(role.id === '667472170926080011' && hasmember === false)
    {
        fc.channels.fetch("667466143585402903").then(channel => channel.send("<a:wel:742119488366837780><a:come:742119500068946084>"));
        fc.channels.fetch("667466143585402903").then(channel => channel.send("Welcome <@" + newmem.id + "> to cuddle club! \n\nPlease accept a free cookie, on me! :cookie:"));

    }

	})

})


fc.on('messageUpdate', (msg, newmsg) => {

  if (newmsg.content.includes("dark") && newmsg.content.includes('cute')){
    newmsg.delete()
  }

if(msg.channel.id === "717430439396245577" || msg.channel.id === "721808001098448896" || msg.channel.id === "717858360430428160")
	{

		// On receive message, (Given string `msg`) from channel #awoo
if (!/^(\*|_)*awo+f?(!|\*|_)*( ?(:3|<3|owo|uwu))?( ?❤️)?(\*|_)*$/ui.test(newmsg.content)) {
newmsg.delete();
newmsg.author.send("I see you.. No " + msg.content + ", only awoo!");
}
	}
})

fc.on('message', msg => {

	if(msg.channel.id === "462044347794456605" && msg.author.id === "155149108183695360")
	{
		msg.channel.send("<@&462043912169586699> Please check the latest dyno case log.");
	}

    if (msg.author.bot === true) return;




    if(msg.channel.id === "629075452723462154")
    {
      // Repost advertisement!
      msg.delete()
      fc.channels.fetch("629073904882810910").then(channel => channel.send("OP: <@" + msg.author.id + "> \n\n" + msg.content));
      msg.channel.send("<@" + msg.author.id + ">, I've reposted your advertisement to <#629073904882810910> - it shall be displayed for 3 days. \n\n<@&462043912169586699>")
    }

	if(msg.channel.id === "717430439396245577" || msg.channel.id === "721808001098448896" || msg.channel.id === "717858360430428160")

	{

		// On receive message, (Given string `msg`) from channel #awoo
if (!/^(\*|_)*awo+f?(!|\*|_)*( ?(:3|<3|owo|uwu))?( ?❤️)?(\*|_)*$/ui.test(msg.content)) {
msg.delete();
msg.author.send("No " + msg.content + ", only awoo!");
}
	}



});
fc.login('YourTokenHere');
