const Command = require("../../Base/Command");

class Bassboost extends Command {
  constructor(client) {
    super(client, {
      name: "bassboost",
      description: "Bassboost the player.",
      aliases: [],
      usage: [
        "bassboost off",
        "bassboost low",
        "bassboost medium",
        "bassboost high",
        "bassboost hard"
      ]
    });
  }

  async run(message, args, Discord) {
    let queue = this.client.queue.get(message.guild.id);
    if (!queue) return message.channel.send("❌ | I'm not playing anything?");
    if (!message.member.voice.channel)
      return message.channel.send(`❌ | You're not in a voice channel!`);
    if (
      queue &&
      message.guild.me.voice.channel.id !== message.member.voice.channel.id
    )
      return message.channel.send(`❌ | You're not in my voice channel!`);
    let amt = args[0];
    if (!amt)
      return message.channel.send(
        `❌ | Valid options: \`off\`, \`low\`, \`medium\`, \`high\` & \`hard\`.`
      );
    amt = amt.toLowerCase();
    switch (amt) {
      case "off":
        queue.gain = 0;
        return message.channel.send(
          "✅ | Bassboost set to `off`. [Available from next song]."
        );
        break;
      case "low":
        queue.gain = 5;
        return message.channel.send(
          "✅ | Bassboost set to `low`. [Available from next song]."
        );
        break;
      case "medium":
        queue.gain = 10;
        return message.channel.send(
          "✅ | Bassboost set to `medium`. [Available from next song]."
        );
        break;
      case "high":
        queue.gain = 15;
        return message.channel.send(
          "✅ | Bassboost set to `high`. [Available from next song]."
        );
        break;
      case "hard":
        queue.gain = 20;
        return message.channel.send(
          "✅ | Bassboost set to `hard`. [Available from next song]."
        );
        break;
      default:
        return message.channel.send(
          `❌ | Valid options: \`off\`, \`low\`, \`medium\`, \`high\` & \`hard\`.`
        );
    }
  }
}

module.exports = Bassboost;
