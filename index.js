const WaZiBoT = require("./Base/WaZiBoT");
const client = new WaZiBoT({
    fetchAllMembers: true
});
const fs = require("fs");
require("./handlers/Web.js");

// handle events
fs.readdir("./events/", (err, files) => {
    console.log(`Loading a total of ${files.length} events.`);
    files.forEach(file => {
        const eventName = file.split(".")[0];
        console.log(`Loading Event: ${eventName}`);
        const event = new (require(`./events/${file}`))(client);
        client.on(eventName, (...args) => event.run(...args));
        delete require.cache[require.resolve(`./events/${file}`)];
    });
});

// handle commands
fs.readdir("./commands/", (err, files) => {
    if (err) return console.error(err);
    files.forEach(dir => {
        fs.readdir(`./commands/${dir}/`, (err, cmd) => {
            cmd.forEach(file => {
                if (!file.endsWith(".js")) return;
                let Props = require(`./commands/${dir}/${file}`);
                let commandName = file.split(".")[0];
                console.log(`Loading Command: ${commandName}...`);
                let props = new Props(client);
                props.help.category = dir;
                props.location = `./commands/${dir}/${file}`;
                client.commands.set(props.help.name, props);
                props.help.aliases.forEach(alias => {
                    client.aliases.set(alias, props.help.name);
                });
            });
        });
    });
});

// counter
client.on("message", async (message) => {
  let channel = client.channels.cache.get("690456321643773962");
  if (!channel) return;
  if (message.channel.id !== channel.id) return;
  if (message.author.bot && message.author.id !== client.user.id) return message.delete();
  if (!message.author.bot && isNaN(message.content)) {
    message.delete();
    return message.reply("Messages in this channel must be a number.").then(m => m.delete({ timeout: 3000 }));
  };
  if (message.author.id === client.user.id) return;

  let num = parseInt(message.content);
  let parsed = client.db.fetch("counter");
  if (parsed.author.id === message.author.id) {
    message.delete();
    return message.reply("You can't count twice in a row.").then(m => m.delete({ timeout: 3000 }));
  };
  if (num !== parsed.value + 1) {
    message.delete();
    return message.reply(`Next number must be ${parsed.value + 1}`).then(m => m.delete({ timeout: 3000 }));
  };
  client.db.set(`counter`, { value: parsed.value + 1, author: message.author });
  channel.setTopic(`Next number: ${client.db.fetch(`counter`).value + 1}`);
});

client.run().then(() => {
  require("./handlers/Uploads")(client);
});;

String.prototype.toProperCase = function() {
  return this.replace(/([^\W_]+[^\s-]*) */g, function(txt) {
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
};

Array.prototype.random = function() {
  return this[Math.floor(Math.random() * this.length)];
};

Array.prototype.shuffle = function() {
  for (let i = this.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [this[i], this[j]] = [this[j], this[i]];
  }
  return this;
};

Array.prototype.insert = function(index, item) {
  this.splice(index, 0, item);
};

module.exports = client;
