const menu = require('./menu.js');
console.log('Done. Read menu.');

const talkedRecently = new Set();
var colors = require('colors');

console.log("Error".red);
console.log("Warning".yellow);
console.log("Log".cyan);
console.log("Success".green);

const Discord = require('discord.js');
const fc = new Discord.Client();

fc.on('ready', () => {
    console.log(`Logged in as ${fc.user.tag}!`.green);
    fc.user.setActivity(`Beta 4.0 | prefix = !`);
});

var regex = RegExp(/[^a-zA-Z\d\s:]/g);

fc.on('guildMemberAdd', member => {

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
	member.send("Welcome to The Floof Hotel! \n\nJust so you know, we operate a scrict no robot policy here! \n\nTo verify you're not one, please go to https://floofhotel.com/verify.php?id=" + member.id);
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
		if (role.id === "462042250612965386" || role.id === '634062572961923083')
		{
			hasmember = true;
		}

	})

	roles.forEach(function(role){
		if (role.id === "462042250612965386" && hasmember === false)
		{
			fc.channels.fetch("629056060803645453").then(channel => channel.send("<@" + newmem.id + ">, Welcome, welcome! We hope you enjoy your stay at The Floof Hotel!  *hands room card* \n\nYour room number is " + Math.floor(Math.random() * 5670) + "\n\nOn the desk is a free :cookie:, should you need us at any point, feel free to ping a member of staff or ask in <#629052614985777162> \n\nFeel free to tell us about you and your fursona in <#552957610899275776>"));

			fc.channels.fetch("629056060803645453").then(channel => channel.send("<@&463088144292511764> Please welcome the above user!"));

		}

    if(role.id === '634062572961923083' && hasmember === false)
    {
      	fc.channels.fetch("634065484052168715").then(channel => channel.send("Welcome <@" + newmem.id + "> to the resort! \n\nTo welcome you, we'd like to offer you a free :cookie:! \n\nWe hope you enjoy your stay here. \n\nWant to introduce yourself? <#634065279596363777> \nReady to chat? <#634060865750040588> \nWant to see the channels we offer? <#634080278222209034> \nGet some roles! > <#634070789326372884> / <#634071049905897505>"));
        fc.channels.fetch("634065484052168715").then(channel => channel.send("<@&635161004539641867> Please welcome the above user!"));

    }

	})

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

	if(msg.channel.id === "475003135220383744")
	{

		// On receive message, (Given string `msg`) from channel #awoo
if (!/^(\*|_)*awo+f?(!|\*|_)*( ?(:3|<3|owo|uwu))?( ?❤️)?(\*|_)*$/ui.test(msg.content)) {
msg.delete();
msg.author.send("No " + msg.content + ", only awoo!");
}
	}

	else{
		 var drinks = menu.get(msg, msg.content, msg.author.id, item => {
			 if(item === "Not a drink"){return;}
			 else{
			 msg.delete();
			 msg.channel.send("<@" + msg.author.id + "> , " + item);
			 }
		 })
	}


});


fc.login('MyToken');
