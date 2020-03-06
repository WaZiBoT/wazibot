const Command = require("../../Base/Command");

class Remove extends Command {
  constructor(client) {
    super(client, {
      name: "remove",
      description: "Removes a song from the queue.",
      aliases: ["removesong"],
      usage: ["remove <song_index>"]
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
    let index = args[0];
    if (isNaN(index) || !index)
      return message.channel.send("❌ | Please provide song index to remove.");
    let song = queue.songs[parseInt(index)];
    if (!song) return message.channel.send("❌ | That Song was not found!");
    if (index <= 0)
      return message.channel.send(
        "❌ | You can't remove current song. Use skip command instead"
      );
    else delete queue.songs[parseInt(index) - 1];
    return message.channel.send(
      `✅ | Alright! I have removed **${song.title}** from the queue.`
    );
  }
}

module.exports = Remove;
