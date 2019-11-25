// More to come, logging in JS due to python not supporting logging.

// Logging javascript file

// Python can't log changes, but coffee can.

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

x.on("messageDelete", (messageDelete) => {
})

x.on('messageUpdate', (oldMessage, newMessage) => {
})

x.on('channelCreate', channel => {
})

x.on('channelDelete', channel => {
})

x.on('channelDelete', channel => {
})

x.on('guildMemberAdd', member => {
})

x.on('guildMemberRemove', member => {
})

x.on('userUpdate', (oldmember, newmember) => {
})

x.on('messageReactionAdd', (reaction, usr) => {
})

x.on('messageReactionRemove', (reaction, usr) => {
})

x.on('guildMemberUpdate', (oldmember, newmember) => {
})

x.on('guildBanAdd', (guild, member) => {
})

x.on('guildBanRemove', (guild, member) => {
})

x.on("guildCreate", guild => {
  })

x.on("guildDelete", guild => {
    })
    


});

client.login('MyToken');
