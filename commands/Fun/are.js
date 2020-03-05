const Command = require("../../Base/Command");

class Are extends Command {
  constructor(client) {
    super(client, {
      name: "are",
      description: "You are?",
      usage: ["are <text>"],
      aliases: ["iam", "im"]
    });
  }

  async run(message, args, Discord) {
    if (!args.join(" ")) return message.reply("You are what?");
    return message.reply(
      `You are ${Math.floor(Math.random() * 100)}% ${args.join(" ")}`
    );
  }
}

module.exports = Are;
