const Command = require("../../Base/Command");

class Bold extends Command {
  constructor(client) {
    super(client, {
      name: "bold",
      description: "Creates bold & slow audio.",
      aliases: ["lowpitch", "slow", "slowdown"],
      usage: ["bold"]
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
    queue.bold = !queue.bold;
    return message.channel.send(
      queue.bold
        ? "Bold effect enabled! [Available after this song]"
        : "Bold effect disabled! [Available after this song]"
    );
  }
}

module.exports = Bold;
