const Command = require("../../Base/Command");
const ms = require("parse-ms");

class Work extends Command {
  constructor(client) {
    super(client, {
      name: "work",
      aliases: [],
      usage: ["work"],
      description: "Work uwu."
    });
  }

  async run(message, args, Discord) {
    
    var jobs = [
      "Pornstar",
      "Dishwasher",
      "Memer",
      "Shit eater",
      "YouTuber",
      "Developer",
      "Musician",
      "Professional sleeper",
      "Teacher",
      "Scientist",
      "Baby maker",
      "Twitch Streamer",
      "Twitch Pornstar",
      "StickAnimator",
      "Strict Math Teacher",
      "Tik Toker"
    ];
    var givers = [
      "Zakktur",
      "Anion",
      "WASIF",
      "INEX",
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
      "RioGamer",
      "Potato",
      "WaZiBoT",
      "The ded Wazifo",
      "A random person",
      "Logokas",
      "Hamza",
      "Samza",
      "Spray",
      "Dick"
    ];
    
    let timeout = 2.7e+6;
    let amount = Math.floor(Math.random() * 200) + 700;

    let work = this.client.db.fetch(`work_${message.author.id}`);

    if (work !== null && timeout - (Date.now() - work) > 0) {
      let time = ms(timeout - (Date.now() - work));
      return message.channel.send(
        `:x: | Come back after **${time.minutes}m ${time.seconds}s**.`
      );
    } else {
      this.client.db.set(`work_${message.author.id}`, Date.now());
      let event1 = Math.floor(Math.random() * 7);
      let event2 = Math.floor(Math.random() * 7);
      if (event1 === event2) return message.channel.send(`**${givers.random()}:** Work well next time.`);
      message.channel.send(`You worked for **${givers.random()}** as **${jobs.random()}** and earned 💵**${amount}**.`);
      this.client.db.add(`money_${message.author.id}`, amount);
    }
  }
}

module.exports = Work;
