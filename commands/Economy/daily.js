const Command = require("../../Base/Command");
const ms = require("parse-ms");

class Daily extends Command {
  constructor(client) {
    super(client, {
      name: "daily",
      aliases: [],
      usage: ["daily"],
      description: "Collect your daily WaZiCoins."
    });
  }

  async run(message, args, Discord) {
    let timeout = 86400000;
    let amount = Math.floor(Math.random() * 250) + 500;

    let daily = this.client.db.fetch(`daily_${message.author.id}`);

    if (daily !== null && timeout - (Date.now() - daily) > 0) {
      let time = ms(timeout - (Date.now() - daily));
      return message.channel.send(
        `:x: | Come back after **${time.hours}h ${time.minutes}m ${time.seconds}s**.`
      );
    } else {
      let embed = new Discord.MessageEmbed()
        .setAuthor("Daily", message.author.displayAvatarURL)
        .setColor(0x7289da)
        .setDescription(
          `You have claimed 💵**${amount}**. You can claim it again after a day.`
        );
      message.channel.send(embed);

      this.client.db.add(`money_${message.author.id}`, amount);
      this.client.db.set(`daily_${message.author.id}`, Date.now());
    }
  }
}

module.exports = Daily;
