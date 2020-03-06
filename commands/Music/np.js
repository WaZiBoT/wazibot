const Command = require("../../Base/Command");
let moment = require("moment");
require("moment-duration-format");

class Nowplaying extends Command {
  constructor(client) {
    super(client, {
      name: "np",
      description: "Shows now playing song.",
      aliases: ["nowplaying"],
      usage: ["np"]
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
      return message.channel.send(`❌ | You are not in my voice channel!`);

    let stream = queue.connection.dispatcher.streamTime;
    let total = queue.songs[0].duration2;
    let now = `${moment.duration(stream).format("HH[:]mm[:]ss[:]")}`;
    let full = `${moment.duration(total).format("HH[:]mm[:]ss[:]")}`;
    let q = queue.playing ? "🔊" : "🔈";
    const embed = new Discord.MessageEmbed()
      .setTitle("Now Playing!")
      .addField(
        `Song`,
        `**[${Discord.Util.escapeMarkdown(queue.songs[0].title)}](${
          queue.songs[0].url
        })**`
      )
      .setFooter(
        `${q} | ${
          now.length < 3 ? `00:${now}` : now
        } ${this.client.player.createBar(stream, total)} ${full}`
      )
      .setThumbnail(
        `https://img.youtube.com/vi/${queue.songs[0].id}/maxresdefault.jpg`
      )
      .setColor("#7289DA")
      .setAuthor(
        `${queue.songs[0].requestedBy.tag}`,
        queue.songs[0].requestedBy.displayAvatarURL({ dynamic: true })
      );
    message.channel.send(embed);
  }
}

module.exports = Nowplaying;
