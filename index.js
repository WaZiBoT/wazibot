const WaZiBoT = require("./Base/WaZiBoT");
const client = new WaZiBoT({
    disableEveryone: true,
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

client.run();

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
