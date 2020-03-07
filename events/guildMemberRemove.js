const DiscordCanvas = require("discord-canvas");
const Discord = require("discord.js");

module.exports = class {
    constructor(client) {
        this.client = client;
    }

    async run(member) {
        let total = member.guild.channels.get(this.client.config.serverStats.total);
        let humans = member.guild.channels.get(this.client.config.serverStats.humans);
        let bots = member.guild.channels.get(this.client.config.serverStats.bots);

        try {
            total.setName(`Total: ${member.guild.memberCount}`, "Stats Update");
            humans.setName(`Users: ${member.guild.members.filter(u => u.user.bot === false).size}`, "Stats Update");
            bots.setName(`Bots: ${member.guild.members.filter(u => u.user.bot === true).size}`, "Stats Update");
        } catch {
            console.log("ServerStats failed to update");
        }
        if (member.user.bot) return;
        const image = await new DiscordCanvas.Goodbye()
            .setUsername(member.user.username)
            .setDiscriminator(member.user.discriminator)
            .setMemberCount(member.guild.memberCount)
            .setGuildName("WAZIFERS")
            .setAvatar(member.user.displayAvatarURL({ dynamic: false, format: 'png', size: 1024 }))
            .setColor("border", "#FF0000")
            .setColor("username-box", "#FF0000")
            .setColor("discriminator-box", "#FF0000")
            .setColor("message-box", "#FF0000")
            .setColor("title", "#FF0000")
            .setColor("avatar", "#FF0000")
            .setText("message", "we will miss ya!")
            .setBackground("https://cdn.glitch.com/6a8e40c8-fe0d-4099-99d2-02952070f31c%2Ff6ee043f-2dd6-4408-8abf-21e955453d48.image.png?v=1583548160258")
            .toAttachment();

        const attachment = new Discord.MessageAttachment(image.toBuffer(), "leaver.png");
        this.client.channels.get(this.client.config.greetingChannel).send(attachment);
    }
}
