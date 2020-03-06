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
            .setColor("border", "#7289DA")
            .setColor("username-box", "#7289DA")
            .setColor("discriminator-box", "#7289DA")
            .setColor("message-box", "#7289DA")
            .setColor("title", "#7289DA")
            .setColor("avatar", "#7289DA")
            .setBackground("https://cdn.craftburg.net/stockage/img/discord/background.jpg")
            .toAttachment();

        const attachment = new Discord.MessageAttachment(image.toBuffer(), "welcomer.png");
        return this.client.channels.get(this.client.config.greetingChannel).send(attachment);
    }
}
