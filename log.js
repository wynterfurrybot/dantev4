// Logging javascript file

// Python can't log changes, but coffee can.

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});


client.on("messageDelete", (messageDelete) => {
  if (messageDelete.author.bot){return;}
  if(messageDelete.attachments)
  {
    var a = messageDelete.attachments;
    a.forEach(function (b)
  {
    messageDelete.content = messageDelete.content + " -- " + b.url;
  })
  }
  // send to local message channel
  var channel = messageDelete.guild.channels.find(channel => channel.name === "message_logs");

channel.send({embed: {
  color: 16726088,
  description: "A message sent by " + messageDelete.author.username + " was removed! \n\nContent: \n" + messageDelete.content ,
}});

});

client.on('messageUpdate', (oldMessage, newMessage) => {
  if (newMessage.author.bot){return;}
  if(newMessage.attachments)
  {
    var a = newMessage.attachments;
    a.forEach(function (b)
  {
    newMessage.content = newMessage.content + " -- " + b.url;
  })
  }
  var channel = newMessage.guild.channels.find(channel => channel.name === "message_logs");
  channel.send({embed: {
    color: 3447003,
    description: "A message sent by " + newMessage.author.username + " was edited! \n\nOld message: \n" + oldMessage.content + "\nNew message: \n" + newMessage.content,
  }});
});

client.on('channelCreate', channel => {
  var c = channel.guild.channels.find(c => c.name === "channel_logging");
  c.send({embed: {
    color: 3447003,
    description: "A new channel (" + channel.name + ") was created!",
  }});
});

client.on('channelDelete', channel => {
  var c = channel.guild.channels.find(c => c.name === "channel_logging");
  c.send({embed: {
    color: 16726088,
    description: "Channel (" + channel.name + ") was deleted!",
  }});
});

client.on('guildMemberAdd', member => {
  var channel = member.guild.channels.find(channel => channel.name === "user_logs");
  channel.send({embed: {
    color: 3447003,
    description: "A new member (" + member.user.username + ") has joined!",
  }});
});

client.on('guildMemberRemove', member => {
  var channel = member.guild.channels.find(channel => channel.name === "user_logs");
  channel.send({embed: {
    color: 16726088,
    description: "Member <@" + member.id + "> has left!",
  }});
});

client.on('guildBanAdd', (guild, member) => {
  var channel = guild.channels.find(channel => channel.name === "case_logs");
  channel.send({embed: {
    color: 16726088,
    description: "Member <@" + member.id + "> has been banned!",
  }});
});

client.on('guildBanRemove', (guild, member) => {
  var channel = guild.channels.find(channel => channel.name === "user_logs");
  channel.send({embed: {
    color: 16726088,
    description: "Member <@" + member.id + "> ban revoked",
  }});

  var channel = guild.channels.find(channel => channel.name === "case_logs");
  channel.send({embed: {
    color: 16726088,
    description: "Member <@" + member.id + "> ban revoked",
  }});
});

client.login('MyToken');
