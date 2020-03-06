const Command = require("../../Base/Command");
const ms = require("parse-ms");

class Search extends Command {
  constructor(client) {
    super(client, {
      name: "search",
      aliases: [],
      usage: ["search"],
      description: "Search something 👀."
    });
  }

  async run(message, args, Discord) {
    
    var givers = [
      "Purse",
      "Bed",
      "Bag",
      "Box",
      "Bank",
      "Street",
      "NASA"
    ];
    
    let timeout = 300000;
    let amount = Math.floor(Math.random() * 10) + 100;

    let search = this.client.db.fetch(`search_${message.author.id}`);

    if (search !== null && timeout - (Date.now() - search) > 0) {
      let time = ms(timeout - (Date.now() - search));
      return message.channel.send(
        `:x: | Come back after **${time.minutes}m ${time.seconds}s**.`
      );
    } else {
      this.client.db.set(`search_${message.author.id}`, Date.now());
      let event1 = Math.floor(Math.random() * 7);
      let event2 = Math.floor(Math.random() * 7);
      if (event1 === event2) return message.channel.send(`**${givers.random()}:** No money for you HAHAHAHAHHAHAHAHAHAHA.`);
      message.channel.send(`**${givers.random()}:** You found 💵**${amount}**.`);
      this.client.db.add(`money_${message.author.id}`, amount);
    }
  }
}

module.exports = Search;
