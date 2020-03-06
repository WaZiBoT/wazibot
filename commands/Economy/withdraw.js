const Command = require("../../Base/Command");

class Withdraw extends Command {
  constructor(client) {
    super(client, {
      name: "withdraw",
      aliases: ["with"],
      usage: ["withdraw <amount>"],
      description: "Increase ur balance maybe 👀"
    });
  }

  async run(message, args, Discord) {
    let amount = args[0];
    if (this.client.db.fetch(`bank_${message.author.id}`) === null || this.client.db.fetch(`bank_${message.author.id}`) <= 0) return message.reply("❌ | You are poor af");
    if (!amount) return message.channel.send("What r u trying to deposit lmao");
    if (typeof amount === "string" && amount.toLowerCase() === "all") amount = this.client.db.fetch(`bank_${message.author.id}`);
    if (isNaN(amount)) amount = 0;
    if (amount <= 0) return message.channel.send("Amount must be a number, greater than 0.");
    if (amount > this.client.db.fetch(`bank_${message.author.id}`)) return message.channel.send("Amount must be a number, less than your balance.");
    let added = this.client.db.add(`money_${message.author.id}`, amount);
    this.client.db.subtract(`bank_${message.author.id}`, amount);
    return message.channel.send(`Now you have 💵**${added}** on ur pocket!`);
  }
}

module.exports = Withdraw;
