// More to come, logging in JS due to python not supporting logging.

// Logging javascript file

// Python can't log changes, but coffee can.

const Discord = require('discord.js');
const client = new Discord.Client();

var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "user",
  password: "password",
  database: "dante"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
})

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('message', msg => {
// Log to new messages table

if(msg.attachments)
{
  var a = msg.attachments;
  a.forEach(function (b)
{
  msg.content = msg.content + " -- " + b.url;
})
}

con.query("INSERT INTO messages (id, content, guild_id, author) VALUES(?, ?, ?, ?)", [msg.id, msg.content, msg.guild.id, msg.author.id], async function(err, result, fields) {
console.log("1 record inserted");
// send to local message channel
});
});


client.on("messageDelete", (messageDelete) => {
  // Log to logging Channel Only

  if(msg.attachments)
  {
    var a = msg.attachments;
    a.forEach(function (b)
  {
    msg.content = msg.content + " -- " + b.url;
  })
  }
});

client.on('messageUpdate', (oldMessage, newMessage) => {
  if(newMessage.attachments)
  {
    var a = newMessage.attachments;
    a.forEach(function (b)
  {
    newMessage.content = newMessage.content + " -- " + b.url;
  })
  }
  con.query("INSERT INTO edithistory (id, oldcontent, newcontent) VALUES(?, ?, ?)", [oldMessage.id, oldMessage.content, newMessage.content], async function(err, result, fields) {
  console.log("1 record inserted");

  // send to local message channel
  });
});

client.on('channelCreate', channel => {
});

client.on('channelDelete', channel => {
});

client.on('channelDelete', channel => {
});

client.on('guildMemberAdd', member => {
});

client.on('guildMemberRemove', member => {
});

client.on('userUpdate', (oldmember, newmember) => {
});

client.on('messageReactionAdd', (reaction, usr) => {
});

client.on('messageReactionRemove', (reaction, usr) => {
});

client.on('guildMemberUpdate', (oldmember, newmember) => {
});

client.on('guildBanAdd', (guild, member) => {
});

client.on('guildBanRemove', (guild, member) => {
});

client.on("guildCreate", guild => {
});

client.on("guildDelete", guild => {
});

client.login('MyToken');
