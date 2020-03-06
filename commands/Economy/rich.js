const Command = require("../../Base/Command");

class Rich extends Command {
  constructor(client) {
    super(client, {
      name: "rich",
      aliases: ["ecolb"],
      usage: ["rich"],
      description: "Leaderboard? uwu"
    });
  }

  async run(message, args, Discord) {
    let data = this.client.db.all().filter(data => data.ID.startsWith("money_")).sort((a,b) => b.data - a.data);
    data.length = 12;
      let embed = new Discord.MessageEmbed()
        .setTitle("Leaderboard")
        .setColor("BLURPLE")
        .setThumbnail(message.guild.iconURL({dynamic: true}))
        .setFooter(message.author.tag, message.author.displayAvatarURL({dynamic: true}))
        .setTimestamp();
      data.forEach(d => {
        embed.addField(`${data.indexOf(d) + 1}. ` + (this.client.users.get(d.ID.split("_")[1]) ? this.client.users.get(d.ID.split("_")[1]).tag : "Unknown User#0000"), `Balance: ${d.data}\nBank: ${this.client.db.fetch(`bank_${d.ID.split("_")[1]}`) ? this.client.db.fetch(`bank_${d.ID.split("_")[1]}`) : 0}`, true)
      })
      return message.channel.send(embed);
    }
}

module.exports = Rich;
