const Command = require("../../Base/Command");
const ms = require("parse-ms");

class Beg extends Command {
  constructor(client) {
    super(client, {
      name: "beg",
      aliases: [],
      usage: ["beg"],
      description: "Beg Beg Beg Beg."
    });
  }

  async run(message, args, Discord) {
    
    var givers = [
      "Zakktur",
      "Anion",
      "WASIF",
      "XENO",
      "Gay",
      "Shit",
      "Faggot",
      "Retard",
      "Kray",
      "IGP The Annoying Kid",
      "Shitro",
      "Osome",
      "PewDiePie",
      "Fortnite is retarded af",
      "Dickhead",
      "Northz",
      "Eggplant",
      "Peepee",
      "Hamza",
      "Samza",
      "Spray",
      "Dick",
      "Sex Master"
    ];
    
    let timeout = 120000;
    let amount = Math.floor(Math.random() * 1) + 70;

    let beg = this.client.db.fetch(`beg_${message.author.id}`);

    if (beg !== null && timeout - (Date.now() - beg) > 0) {
      let time = ms(timeout - (Date.now() - beg));
      return message.channel.send(
        `:x: | Come back after **${time.minutes}m ${time.seconds}s**.`
      );
    } else {
      this.client.db.set(`beg_${message.author.id}`, Date.now());
      let event1 = Math.floor(Math.random() * 7);
      let event2 = Math.floor(Math.random() * 7);
      if (event1 === event2) return message.channel.send(`**${givers.random()}:** Fuck off! No money for you.`);
      message.channel.send(givers.random() + ": Here's your money 💵**" + amount + "**.");
      this.client.db.add(`money_${message.author.id}`, amount);
    }
  }
}

module.exports = Beg;
