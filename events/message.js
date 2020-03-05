const Discord = require("discord.js");

module.exports = class {
    constructor(client) {
        this.client = client;
    }

    async run(message) {
        // return if not guild
        if (!message.guild || message.author.bot) return;

        // check for the guild
        if (!this.client.config.allowedGuilds.includes(message.guild.id)) return message.guild.leave();

        // check prefix
        const prefixes = this.client.db.fetch(`prefix_${message.guild.id}`) ? [this.client.db.fetch(`prefix_${message.guild.id}`), `<@${this.client.user.id}>`, `<@!${this.client.user.id}>`] : [">", `<@${this.client.user.id}>`, `<@!${this.client.user.id}>`];
        let prefix = false;
        for (const Prefix of prefixes) {
            if (message.content.startsWith(Prefix)) prefix = Prefix;
        }
        if (!prefix) return;
        this.client.prefix = prefix;

        // DevMode Check
        if (this.client.config.devMode && !this.client.admins.includes(message.author.id)) return message.channel.send("❌ | You can't use me on development mode.");

        // commands & args
        const args = message.content.slice(prefix.length).trim().split(" ");
        const command = args.shift().toLowerCase();
        const cmd = this.client.fetchCommand(command);
        if (!cmd) return;

        // command handler
        if (cmd.help.category === "Developer" && !this.client.admins.includes(message.author.id)) return;
        if (cmd.help.category === "Moderation" && !message.member.hasPermission("KICK_MEMBERS")) return message.channel.send("❌ | You don't have `KICK_MEMBERS` permission to perform this action.");
        if (cmd.help.category === "Configuration" && !message.member.hasPermission("ADMINISTRATOR")) return message.channel.send("❌ | You don't have `ADMINISTRATOR` permission to perform this action.");
        cmd.run(message, args, Discord);
    }
}