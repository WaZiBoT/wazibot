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
        const image = await new DiscordCanvas.Welcome()
            .setUsername(member.user.username)
            .setDiscriminator(member.user.discriminator)
            .setMemberCount(member.guild.memberCount)
            .setGuildName("WAZIFERS")
            .setAvatar(member.user.displayAvatarURL({ dynamic: false, format: 'png', size: 1024 }))
            .setColor("border", "#355EF2")
            .setColor("username-box", "#355EF2")
            .setColor("discriminator-box", "#355EF2")
            .setColor("message-box", "#355EF2")
            .setColor("title", "#355EF2")
            .setColor("avatar", "#355EF2")
            .setText("message", "welcome to the {server}")
            .setBackground("https://cdn.glitch.com/6a8e40c8-fe0d-4099-99d2-02952070f31c%2Fe292d925-1e4f-4fe8-b460-a45a638d3234.image.png?v=1583548490710")
            .toAttachment();

        const attachment = new Discord.MessageAttachment(image.toBuffer(), "welcomer.png");
        return this.client.channels.get(this.client.config.greetingChannel).send(attachment);
    }
}
