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

try{
  // send to local message channel
  var channel = messageDelete.guild.channels.find(channel => channel.name === "message_logs");

channel.send({embed: {
  color: 16726088,
  description: "A message sent by " + messageDelete.author.username + " was removed! \n\nContent: \n" + messageDelete.content + "\n\nChannel: <#" + messageDelete.channel.id + ">" ,
}});
}

catch(e){
  console.log(e)
}

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
  try{
  var channel = newMessage.guild.channels.find(channel => channel.name === "message_logs");
  channel.send({embed: {
    color: 3447003,
    description: "A message sent by " + newMessage.author.username + " was edited! \n\nOld message: \n" + oldMessage.content + "\nNew message: \n" + newMessage.content + "\n\nChannel: <#" + newMessage.channel.id + ">",
  }});
}
catch(e)
{
  console.log(e)
}
});

client.on('channelCreate', channel => {
  try{
  var c = channel.guild.channels.find(c => c.name === "channel_logging");
  c.send({embed: {
    color: 3447003,
    description: "A new channel (" + channel.name + ") was created!",
  }});
}
catch(e)
{
  console.log(e)
}
});

client.on('channelDelete', channel => {
  try{
  var c = channel.guild.channels.find(c => c.name === "channel_logging");
  c.send({embed: {
    color: 16726088,
    description: "Channel (" + channel.name + ") was deleted!",
  }});
}
catch(e){
  console.log(e)
}
});

client.on('guildMemberAdd', member => {
  try{
  var channel = member.guild.channels.find(channel => channel.name === "user_logs");
  channel.send({embed: {
    color: 3447003,
    description: "A new member (" + member.user.username + ") has joined!",
  }});
}
catch(e){
  console.log(e)
}
});

client.on('guildMemberRemove', member => {
  try{
  var channel = member.guild.channels.find(channel => channel.name === "user_logs");
  channel.send({embed: {
    color: 16726088,
    description: "Member <@" + member.id + "> ( " + member.user.username + " )" + " has left!",
  }});
}

catch(e){
  console.log(e)
}
});

client.on('guildBanAdd', (guild, member) => {
  try{
  var channel = guild.channels.find(channel => channel.name === "case_logs");
  channel.send({embed: {
    color: 16726088,
    description: "Member <@" + member.id + "> ( " +  member.user.username + " )" + " has been banned!",
  }});
}
catch(e)
{
  console.log(e)
}
});

client.on('guildBanRemove', (guild, member) => {
  try{
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
}
catch(e){
  console.log(e)
}
});

client.login('MyToken');
