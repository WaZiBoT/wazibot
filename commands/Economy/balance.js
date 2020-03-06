const Command = require("../../Base/Command");

class Balance extends Command {
  constructor(client) {
    super(client, {
      name: "balance",
      aliases: ["bal"],
      usage: ["balance"],
      description: "Allows you to check your balance, what else?"
    });
  }

  async run(message, args, Discord) {
    let user = message.mentions.users.first() || this.client.users.get(args[0]) || message.author;
      let embed = new Discord.MessageEmbed()
        .setTitle("Balance Machine")
        .setThumbnail(user.displayAvatarURL({ dynamic: true }))
        .addField("Purse", (this.client.db.fetch(`money_${user.id}`) ? this.client.db.fetch(`money_${user.id}`) : 0) + " 💵")
        .addField("Bank", (this.client.db.fetch(`bank_${user.id}`) ? this.client.db.fetch(`bank_${user.id}`) : 0)+ " 💵")
        .setFooter(`Requested by ${message.author.tag}`, message.author.displayAvatarURL({ dynamic: true }))
        .setColor(0x7289DA)
      return message.channel.send(embed);
    }
}

module.exports = Balance;
